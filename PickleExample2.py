import pickle


class Employee:
    organization = "XYZ"

    def __init__(self, name):
        self.name = name
        # self.dept = "TRnD"

    def getOrg(self):
        return self.organization

    def __str__(self):
        return "Employee Name:{0}  and\t Employee Org: {1} and \t".format(self.name, self.organization)

    def getDept(self):
        return self.dept


if __name__ == "__main__":
    obj = Employee("Swati")
    obj.organization = "ABC"
    obj.salary = 200000000

    file = open("PickleTest.pkl", 'wb')
    pickle.dump(obj, file)
    file.close()

    file_read = open("PickleTest.pkl", "rb")
    unPickledObj = pickle.load(file_read)
    file_read.close()

    print("Organization:", unPickledObj.organization)
    print("Name:", unPickledObj.name)
    print("Salary:", unPickledObj.salary)

    ### If you unpickle in another file, u need to import the class, whose obj are
    # to be unpickled, as well

    """
    When working with your own classes, you must ensure that the class being pickled
    appears in the namespace of the process reading the pickle. Only the data for
    the instance is pickled, not the class definition. The class name is used to
    find the constructor to create the new object when unpickling. 
    """
    import io

    out_string = io.BytesIO()
    pickle.dump(Employee, out_string)
    out_string.flush()

    print("----------------- Pickling a Class Object -----------------")

    in_string = io.BytesIO(out_string.getvalue())
    newEmployee = pickle.load(in_string)
    objNew = newEmployee("Vaibhav")
    objNew.salary = 100000000
    print("New Object: ", objNew)
    print("New employee's orgaization: ", objNew.organization)

    """
    To pickle/unpickle an unpicklable object, you need to define __getstate__() and
    __setstate__() methods.
    For example:
    anotherInstance = MyClass(1, 2, open('three', 'w'))  #file object is included
    In such a case, to pickle anotherInstance, you need to define __getstate__ and
    __setstate__ in the class MyClass.

    """

    #### shelve example   ## linked with ShelveExample.py
    import shelve

    db = shelve.open("ShelveDB4Employee")
    db["Employee 1"] = obj
    db.close()

