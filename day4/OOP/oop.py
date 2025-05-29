class Student:
    def __init__(self, name , house ):
        self.name = name
        self.house = house
        if house in ["pasig", "rizal" , "laguna"]:
            self.house = house
        else:
            raise ValueError("You are banned from this school.")
    
    def get_student(self):
        return self.name

def main():
    try:
        student = get_student()
        # student1 = Student("kenneth" , "Pasig")
        # student3 = Student("ralp" , "recto")

        print(f"{student.name} from {student.house}")
        print(student.get_student(), 'hey')
    except ValueError as err:
        print(err)
   
    # print(f"{student1.name} from {student1.house}")
    # print(f"{student3.name} from {student3.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name , house)
    return student


if __name__ == "__main__":
    main()


