# print all integers from 0 to 150

for x in range(0, 151):
    print(x)

# print all the multiples of 5 from 5 to 1,000

for x in range(5, 1001, 5):
    print(x)

# print integers 1 to 100. if divisible by 5 print Coding if divisible by 10 print Dojo

for x in range(1, 101):
    if x % 10 == 0:
        print('Coding Dojo')
    elif x % 5 == 0:
        print('Coding')
    else:
        print(x)

# add odd integers from 0 to 500,000, and print the final sum

total = 0

for x in range(0, 500001):
    if(not (x % 2) == 0):
        total += x

print(total)

# print positive numbers starting at 2018, counting down by fours

for x in range(2018, 0, -4):
    print(x)

# set three variables: lowNum, highNum, mult. Starting at lowNum and going through
# highNum, print only the integers that are a multiple of mult. For example, if
# lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9

lowNum = 1
highNum = 100
mult = 3

for x in range(lowNum, highNum):
    if(x % mult == 0):
        print(x)
