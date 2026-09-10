from app.services.student_service import StudentService


def test_create_student():
    service = StudentService()

    service.create_student(
        1,
        "Usha",
        25,
        "usha@gmail.com"
    )

    assert service.search_student(1)["name"] == "Usha"


def test_update_student():
    service = StudentService()

    service.create_student(
        1,
        "Usha",
        25,
        "usha@gmail.com"
    )

    service.update_student(
        1,
        "Usha Rani",
        26,
        "usharani@gmail.com"
    )

    student = service.search_student(1)

    assert student["name"] == "Usha Rani"
    assert student["age"] == 26


def test_delete_student():
    service = StudentService()

    service.create_student(
        1,
        "Usha",
        25,
        "usha@gmail.com"
    )

    service.delete_student(1)

    assert 1 not in service.students