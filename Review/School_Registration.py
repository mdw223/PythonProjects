class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def set_age(self, age):
        self.age = age
    
    def set_grade(self, grade):
        self.grade = grade

class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.classes = []

    def get_name(self):
        return self.name

    def get_classes(self):
        return str(self.classes)
    
    def get_students(self):
        return self.students

    def add_student_to_school(self, student):
        if student not in self.students:
            self.students.append(student)

    def add_class_to_school(self, Class):
        if Class not in self.classes:
            self.classes.append(Class)

    def get_class(self, class_name):
        for c in self.classes:
            if c.name == class_name:
                return c
        return None
    
    def get_student(self, student_name):
        for s in self.students:
            if s.name == student_name:
                return s
        return None
    
    def remove_student(self, student_name):
        try:
            self.students.remove(self.get_student(student_name))
            return True
        except:
            return False
    
    def remove_class(self, class_name):
        try:
            self.classes.remove(self.get_class(class_name))
            return True
        except:
            return False
    
class Class:
    def __init__(self, name):
        self.students = []
        self.name = name

    def add_to_class(self, student):
        if student not in self.students:
            self.students.append(student)

    def get_student(self, student_name):
        for s in self.students:
            if s.name == student_name:
                return s
        return None
    
    def remove_student(self, student_name):
        try:
            self.students.remove(self.get_student(student_name))
            return True
        except:
            return False    
        
    def class_size(self):
        return len(self.students)
    
    def get_roll(self):
        return str(self.students)
    
    def get_name(self):
        return self.name
    
school_1 = School("South Garner High")
list_of_classes = ['Math', 'Science', 'Gym', "Art", 'English']
for c in list_of_classes:
    school_1.add_class_to_school(c)
print(f'Welcome to {school_1.get_name()}.\nThe number of classes here is {str(len(school_1.classes))}')
print(f'They are: {school_1.get_classes()}')
students = [Student('Adam', 16, 10), Student('Brian', 17, 11), Student('Maddie', 17, 11), Student('Blake', 18, 12),
            Student('Fisher', 15, 9), Student('Simon', 15, 10), Student('Luke', 15, 10), Student('Kimberly', 15, 10), Student('David', 16, 11), Student('Ralph', 18, 12)]
for s in students:
    school_1.add_student_to_school(s)
print(f'Here are the number of students attending the school: {len(school_1.get_students())}')

loop = True
while loop:
    user = input("Would you like to be principal? (Yes/No): ")
    if user == "Yes":
        print(f"Enter a command to run...") # TODO add more code here 
        break
    elif user == "No":
        loop = False
        




