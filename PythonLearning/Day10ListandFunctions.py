status_code = [200 , 404 , 201 , 500 ]
def check_status (status_code):
    if status_code == 200 or status_code == 201:
        return "Pass"
    else:
        return "Fail"

for i in status_code:
    print( i , check_status(i))

#ASSERT (This works only when the condition is true , if condition is false python raise an assertion error)
a = 200
b = 200

assert a==b
print("Pass")

c=200
d =201

assert c!= d
print("Fail")