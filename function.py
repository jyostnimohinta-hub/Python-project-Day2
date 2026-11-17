#function
#function is a block of code which is used to perform a specific task
#function without return type and without parameter
def greet():
    print("Welcome")
greet()
#function without return type and with parameter
def greeting(message):
    print(message)
greeting("Hello, how are you?")
#funnction with return type and with parameter
def cal(a,b):
    return a+b, a*b
total,mul=cal(10,20)
print("Total:", total)
print("Product:", mul)

#default parameter
def greeting(name="Guest"):
    print("Hello,", name)
greeting("Jyostni")
greeting()

#keyword argument
def student(name, age,city):
    print( name,age,city)
student(age=20, name="Jyostni", city="Bangalore")