
print('---------------- Problem 1 ----------------')
for i in range(151):
    print(i)

print('---------------- Problem 2 ----------------')
for i in range(5,1001,5):
    print(i)
print('---------------- Problem 3 ----------------')
for i in range(1,101):
    if i % 10 == 0:
        print('Coding Dojo')
    elif i % 5 == 0:
        print('Coding')
    else:
        print(i)
print('---------------- Problem 4 ----------------')
sum = 0
for i in range(500001):
    if i % 2 == 1:
        sum += i
print(sum)
print('---------------- Problem 5 ----------------')
for i in range(2018, 0, -4):
    if i >=0:
        print(i)
print('---------------- Problem 6 ----------------')
lowNum = 2
highNum = 9
multi = 3
for i in range(lowNum,highNum):

    if i % multi == 0:
        print(i)