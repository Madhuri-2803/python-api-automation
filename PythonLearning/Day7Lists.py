# Lists index starts with Zero
#To add items to lists we use append

L= ["Hyd" , "Vzg" , "Vzm"]
print(L[1])

N = [1,2,3,4,5]
for i in N:
    print(i)

T = ["Login" , "Search" , "Logout"]
for t in T:
    print("Running test :" , t)

T.append("Payment")

#-------------------------------------------------------------------------------------

# to replace an item in list
#test_cases[1] = "Product Search"
#to remove an item test_case.remove
#number of /length of : len(test_cases)

T = ["Login" , "Search" , "Logout"]
T[1] = "Checkout"
T.remove("Logout")
T.append("Payment")
print(T)
print("TotalNumberofitems:" , len(T))


