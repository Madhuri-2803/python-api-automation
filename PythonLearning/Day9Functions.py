#Functions are used when we need to run repetative tasks example to check status we can define a 
#a function and pass multiple values

#Function with parameter
def greet(name):
    print("Hello", name)

def add (a ,b):
    print(a+b)

def check_status(expected , actual):
    return expected == actual

def checkk_status(status_code):
    if status_code == 200 or status_code == 201:
        return "Pass"
    else: 
        return "Fail"

print(checkk_status(201))
