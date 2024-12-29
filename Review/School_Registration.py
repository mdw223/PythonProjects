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
        return str(self.students)

    def add_student_to_school(self, student):
        self.students.append(student)

    def add_class_to_school(self, class_name):
        self.classes.append(class_name)

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
print('The number of classes at', school_1.get_name(), "is", str(len(school_1.classes)))
print(f'Here are the classes they offer: {school_1.get_classes()}')
students = ['Adam', 'Brian', 'Maddie', 'Blake', 'Fisher', 'Simon', 'Luke', 'Kimberly', 'David', 'Ralph']
for s in students:
    school_1.add_student_to_school(s)
print(f'Here are the students attending the school: {school_1.get_students()}')


