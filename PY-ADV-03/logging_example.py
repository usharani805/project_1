import logging

# Configure logging
logging.basicConfig(
    filename="application.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Start of program
logging.info("Program started")

print("Student Management System")

# Simulate student operations
student_name = "John"

logging.info("Student added: %s", student_name)
print("Student added:", student_name)

# Simulate a warning
age = 15

if age < 18:
    logging.warning("Student is under 18")
    print("Warning: Student is under 18")

# Simulate an error
try:
    result = 10 / 0
except ZeroDivisionError:
    logging.error("Cannot divide by zero")
    print("Error: Cannot divide by zero")

logging.info("Program finished")

print("Program finished")