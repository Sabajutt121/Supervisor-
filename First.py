class Supervisor:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.students = []

    def assign_student(self, student):
        self.students.append(student)
        print(f"{student.name} has been assigned to {self.name}.")

    def review_progress(self, student):
        print(f"{self.name} is reviewing the progress of {student.name}.")

    def provide_feedback(self, student, feedback):
        print(f"{self.name} provides feedback to {student.name}: {feedback}")

# Example usage:
supervisor1 = Supervisor("Dr. Smith", "email@domain.com")
student1 = Student("Alice")
student2 = Student("Bob")

supervisor1.assign_student(student1)
supervisor1.assign_student(student2)

supervisor1.review_progress(student1)
supervisor1.provide_feedback(student1, "Good work on literature review.")
