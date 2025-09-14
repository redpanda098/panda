
class student:
    def __init__(self,name,hobby,age,country):  #constructor
        self.name = name
        self.hobby = hobby
        self.age = age
        self.country = country

    def speak(self):
        print(f"{self.name} is speaking.")

    def read(self):
        print(f"{self.name} is reading")

    def details(self):
        print(f"{self.name} is {self.age} years old, and she is from {self.country}.she likes {self.hobby}.")

#creating dog object
student1 = student("alice","dancing",20,"USA")
student1.speak()
student1.read()
student1.details()
student2 = student("sejal","singing",19,"india")
student2.speak()
student2.read()
student2.details()