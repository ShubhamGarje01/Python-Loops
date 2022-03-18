for i in range(1, 5, 1):
    for j in range(1, 5, 1):
        print("# ", end = "")
    print("")
###########################################
for i in range(5): #or by putting 4 here we can pass i+1 in for loop of J
    for j in range(i): #i is row and i is column, we want row no = col no.
        print("# ", end = "")
    print("")
###########################################
print("\n")
for i in range(5): # or we can put put range in reverse(5, 1, -1) and onliy i in j loop
    for j in range(4 - i):
        print("# ", end = "")
    print("")
