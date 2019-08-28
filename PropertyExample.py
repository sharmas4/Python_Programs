##################################################################
print("################### Example 1")
class Student1:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.gotmarks = self.name + " obtained " + self.marks + " marks"

st1 = Student1("John", "25")
print("name: ",st1.name)
print("marks: ",st1.marks)
print("gotmarks: ",st1.gotmarks)
st1.name = "Kate"
print("Updated gotmarks: ",st1.gotmarks)     ## gotmarks is not updated


##################################################################
print("################### Example 2")

class Student2:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def gotmarks(self):
        return self.name + " obtained " + self.marks + " marks"

st2 = Student2("Alice", "75")
print("name: ",st2.name)
print("marks: ",st2.marks)
print("gotmarks: ",st2.gotmarks())  
st2.name = "Kate"
print("Updated gotmarks: ",st2.gotmarks())     ## gotmarks is not updated

## () to be put at every place where gotmarks have been called earlier, which
# is not desirable. To avoid this, we use property


##################################################################
print("################### Example 3")

class Student3:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @property
    def gotmarks(self):
        return self.name + " obtained " + self.marks + " marks"

    @gotmarks.setter
    def gotmarks(self, sentence):
        split = sentence.split()
        self.name = split[0]
        self.marks = split[2]

st3 = Student3("Alice", "80")
print("name: ",st3.name)
print("marks: ",st3.marks)
print("gotmarks: ",st3.gotmarks)  
st3.name = "Kate"
print("Updated gotmarks: ",st3.gotmarks)     ## gotmarks is not updated
st3.gotmarks = "Rick obtained 100 marks"    ## this statement would cause
# AttributeError if @gotmarks.setter method is not defined
print("Updatd name: ", st3.name)
print("Updated marks: ", st3.marks)
        

        

    

