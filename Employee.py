class Employee:
    def __init__(self):
        print("Employee created")
    def __del__(self):
        print("Destructor called!")
def Create_Obj():
    print("Making Objects")
    obj = Employee()
    print("Function End")
    return obj
print("Calling Create_Obj() function")
obj = Create_Obj()
print("Program End...")