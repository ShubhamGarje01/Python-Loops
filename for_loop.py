x = [00, 12, 34, 56, 78, 90] #list
print("using normal print:- ",x)
print("using for loop:-")
for i in x:
    print("\t",i)

z = 'shubham' #string
print("using normal print:- ",z)
print("using for loop:-")
for i in z:
    print("\t",i)

for i in [11, 69.69, 'sam', 'names']: #insted of variable define list on spot
    print("\t", i)

for i in range(1, 11, 2): #or we can give (11)too ##printing 1 to 10 using range
    print(i)

for i in range(11, 1, -2): #-1 for reversing, -2 for skipping one digit
    print(i)

#print 1 to 20 number and skip all number which are divisible by 3:
print("print 1 to 20 number which are divisible by 3")
for i in range(1, 21, 3):
    print(i)
#and
print("print 1 to 20 number and skip all number which are divisible by 3")
for i in range(1, 20):
    if i%3 != 0:
        print(i)