# Create a Python program that displays the name of three students (Student 1, Student 2, and Student 3) and their term grades
# Create a class name Person and attributes - std1, std2, std3, pre,mid,fin
# Compute the average of each term grade using Grade() method
# Information about student's grades must be hidden from others
class Person:
    def __init__(self, std1, std2, std3, pre, mid, fin):
        self.__std1 = std1
        self.__std2 = std2
        self.__std3 = std3
        self.__pre = pre
        self.__mid = mid
        self.__fin = fin

    def grade(self):
        std_avg = sum([self.__pre, self.__mid, self.__fin]) / 3
        print(self.__std1,"average grade is:",std_avg)


std1 = Person("Student 1", "", "", 90, 93, 74)
std1.grade()

std2 = Person("Student 2", "", "", 89, 98, 78)
std2.grade()

std3 = Person("Student 3", "", "", 76, 75, 87)
std3.grade()