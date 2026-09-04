from flask import Flask, request, jsonify
from services import (
    create_employee,
    update_employee,
    delete_employee,
    search_employee,
    list_employees
)
from validation import validate_employee

app = Flask(__name__)


@app.route("/employees", methods=["POST"])
def add_employee():
    data = request.json

    error = validate_employee(data)

    if error:
        return jsonify({"error": error}), 400

    create_employee(
        data["id"],
        data["name"],
        data["department"],
        data["salary"]
    )

    return jsonify({"message": "Employee created successfully"}), 201


@app.route("/employees", methods=["GET"])
def get_employees():
    employees = list_employees()

    employee_list = []

    for employee in employees:
        employee_list.append({
            "id": employee[0],
            "name": employee[1],
            "department": employee[2],
            "salary": employee[3]
        })

    return jsonify(employee_list), 200


@app.route("/employees/<int:employee_id>", methods=["GET"])
def get_employee(employee_id):
    employee = search_employee(employee_id)

    if employee is None:
        return jsonify({"error": "Employee not found"}), 404

    return jsonify({
        "id": employee[0],
        "name": employee[1],
        "department": employee[2],
        "salary": employee[3]
    }), 200


@app.route("/employees/<int:employee_id>", methods=["PUT"])
def edit_employee(employee_id):
    data = request.json

    error = validate_employee({
        "id": employee_id,
        **data
    })

    if error:
        return jsonify({"error": error}), 400

    update_employee(
        employee_id,
        data["name"],
        data["department"],
        data["salary"]
    )

    return jsonify({"message": "Employee updated successfully"}), 200


@app.route("/employees/<int:employee_id>", methods=["DELETE"])
def remove_employee(employee_id):
    delete_employee(employee_id)

    return jsonify({"message": "Employee deleted successfully"}), 200


if __name__ == "__main__":
    app.run(debug=True)