class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def get_avg(self):
        sum = 0
        for mark in self.marks:
            sum += mark
        avg = sum / len(self.marks)
        print(f"hi {self.name} your average is",avg)

s1 = Student("adarsh", [11,12,13,13])
s1.get_avg()

s1.name = "aditya"
s1.marks = [1,2,3,4,5]
s1.get_avg()

# overwrite variable while calling obj