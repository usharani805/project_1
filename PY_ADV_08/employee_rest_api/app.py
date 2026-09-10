from flask import Flask, request, jsonify
from db import get_db_connection
import logging

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Employee REST API is running"
    })


# GET all employees
@app.route("/employees", methods=["GET"])
def get_employees():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT employee_id, employee_name, email,
                   department, salary, department_id
            FROM employees
            ORDER BY employee_id;
        """)

        rows = cursor.fetchall()

        employees = []

        for row in rows:
            employees.append({
                "employee_id": row[0],
                "employee_name": row[1],
                "email": row[2],
                "department": row[3],
                "salary": row[4],
                "department_id": row[5]
            })

        cursor.close()
        conn.close()

        logging.info("Fetched all employees")

        return jsonify(employees), 200

    except Exception as e:
        logging.error(f"Error fetching employees: {e}")

        return jsonify({
            "error": "Unable to fetch employees"
        }), 500


# GET employee by ID
@app.route("/employees/<int:employee_id>", methods=["GET"])
def get_employee(employee_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT employee_id, employee_name, email,
                   department, salary, department_id
            FROM employees
            WHERE employee_id = %s;
        """, (employee_id,))

        row = cursor.fetchone()

        cursor.close()
        conn.close()

        if row is None:
            return jsonify({
                "error": "Employee not found"
            }), 404

        employee = {
            "employee_id": row[0],
            "employee_name": row[1],
            "email": row[2],
            "department": row[3],
            "salary": row[4],
            "department_id": row[5]
        }

        logging.info(f"Fetched employee {employee_id}")

        return jsonify(employee), 200

    except Exception as e:
        logging.error(f"Error fetching employee: {e}")

        return jsonify({
            "error": "Unable to fetch employee"
        }), 500


# POST employee
@app.route("/employees", methods=["POST"])
def create_employee():
    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "error": "JSON request body is required"
            }), 400

        required_fields = [
            "employee_name",
            "email",
            "department",
            "salary",
            "department_id"
        ]

        for field in required_fields:
            if field not in data:
                return jsonify({
                    "error": f"{field} is required"
                }), 400

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO employees
            (employee_name, email, department, salary, department_id)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING employee_id, employee_name, email,
                      department, salary, department_id;
        """, (
            data["employee_name"],
            data["email"],
            data["department"],
            data["salary"],
            data["department_id"]
        ))

        row = cursor.fetchone()
        conn.commit()

        cursor.close()
        conn.close()

        employee = {
            "employee_id": row[0],
            "employee_name": row[1],
            "email": row[2],
            "department": row[3],
            "salary": row[4],
            "department_id": row[5]
        }

        logging.info("Employee created successfully")

        return jsonify(employee), 201

    except Exception as e:
        logging.error(f"Error creating employee: {e}")

        return jsonify({
            "error": "Unable to create employee"
        }), 500


# PUT employee
@app.route("/employees/<int:employee_id>", methods=["PUT"])
def update_employee(employee_id):
    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "error": "JSON request body is required"
            }), 400

        allowed_fields = [
            "employee_name",
            "email",
            "department",
            "salary",
            "department_id"
        ]

        invalid_fields = [
            field for field in data
            if field not in allowed_fields
        ]

        if invalid_fields:
            return jsonify({
                "error": f"Invalid fields: {invalid_fields}"
            }), 400

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE employees
            SET employee_name = %s,
                email = %s,
                department = %s,
                salary = %s,
                department_id = %s
            WHERE employee_id = %s
            RETURNING employee_id, employee_name, email,
                      department, salary, department_id;
        """, (
            data.get("employee_name"),
            data.get("email"),
            data.get("department"),
            data.get("salary"),
            data.get("department_id"),
            employee_id
        ))

        row = cursor.fetchone()

        if row is None:
            conn.rollback()
            cursor.close()
            conn.close()

            return jsonify({
                "error": "Employee not found"
            }), 404

        conn.commit()

        cursor.close()
        conn.close()

        employee = {
            "employee_id": row[0],
            "employee_name": row[1],
            "email": row[2],
            "department": row[3],
            "salary": row[4],
            "department_id": row[5]
        }

        logging.info(f"Employee {employee_id} updated successfully")

        return jsonify(employee), 200

    except Exception as e:
        logging.error(f"Error updating employee: {e}")

        return jsonify({
            "error": "Unable to update employee"
        }), 500


# DELETE employee
@app.route("/employees/<int:employee_id>", methods=["DELETE"])
def delete_employee(employee_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM employees
            WHERE employee_id = %s
            RETURNING employee_id;
        """, (employee_id,))

        row = cursor.fetchone()

        if row is None:
            conn.rollback()
            cursor.close()
            conn.close()

            return jsonify({
                "error": "Employee not found"
            }), 404

        conn.commit()

        cursor.close()
        conn.close()

        logging.info(f"Employee {employee_id} deleted successfully")

        return jsonify({
            "message": "Employee deleted successfully"
        }), 200

    except Exception as e:
        logging.error(f"Error deleting employee: {e}")

        return jsonify({
            "error": "Unable to delete employee"
        }), 500


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "error": "Endpoint not found"
    }), 404


@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({
        "error": "Internal server error"
    }), 500


if __name__ == "__main__":
    app.run(debug=True)