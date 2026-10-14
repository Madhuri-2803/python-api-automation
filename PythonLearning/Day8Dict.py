test_Case ={
    "name" : "Login" ,
    "status" : "Pass",
    "browser" : "Chrome"
}
print(test_Case["browser"])
test_Case["status"] = "Fail"
# to add new key and value to dictionary
test_Case["device"] = "Android"
print(test_Case)
