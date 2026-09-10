# Practice *args and **kwargs

def student_details(*subjects, **details):
    print("Subjects:", subjects)
    print("Student details:", details)


student_details(
    "Python",
    "SQL",
    "HTML",
    name="John",
    age=25
)