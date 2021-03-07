# aPyThing Exercise 1
# ===============EASY=================
 
# Question 1
 
"""
test_string = "welcome introduction to python"
# split by spaces
string_list = test_string.split(" ")
print(string_list[3:])
"""
 
# Question 1 (Alternate Ans)
"""
exerciseString = "welcome introduction to python"
# .split(" ") means i split the string by space into a list
answerString = exerciseString.split(" ")
# why [3] is because the word python is at the 3rd index of the list, [-1] works too
answerString = answerString[3]
print(answerString)
"""
 
# Question 2
# convert str input to int
"""
x = int(input("x: "))
y = int(input("y: "))
value = (x + y) - (x * y)
print(value)
"""
 
# ## Question 2 (Alternate Ans)
"""
# dont forget, input("...") gives you a string, need to typecast to an integer
firstInput = int(input("Enter 1st Number:"))
secondInput = int(input("Enter 2nd Number:"))
outputAns = (firstInput + secondInput) - (firstInput * secondInput)
print(outputAns)
"""
 
# Question 3
 
"""
num = int(input("num: "))
cube_root = num ** 0.5
if cube_root ** 2 == num:
    print(True)
else:
    print(False)
"""
 
# ## Question 3 (Alternate Ans)
"""
# same as question 2, type cast.
userInputted = int(input("Enter Number:"))
checkSq = userInputted ** 0.5
if (checkSq % 1 == 0):
    print("Perfect Square")
else:
    print("Not a perfect square")
"""
 
# Question 4
 
"""
input_string = input("string: ")
reverse_string = ""
for i in range(len(input_string)):
    reverse_string += input_string[-1-i]
print(reverse_string)
"""
 
# ## Question 4 (Alternate Ans)
"""
userInputted = input("Enter Number to be reversed:")
# You do not need to reverse the integer, you can instead treat is as
# a string and reverse the string. [::-1] slices the input (rmb string is a list)
# and reverse it.
reverseInput = userInputted[::-1]
print("The number reversed is:",reverseInput)
"""
 
# ===============INTERMEDIATE=================
 
# Question 1
 
"""
output_list = []
 
# # when using in range(x,y) it takes x to (y - 1)
for i in range(1900, 2000):
    if i % 7 == 0 and i % 5 != 0:
        output_list.append(i)
print(output_list)
"""
 
# Question 2
 
"""
n = 8
outputDict = {}
 
# why 1 to n+1? refer to Intermediate q1 explaination
for i in range(1,n+1):
    # storing i as a key, and i*i as a value.
    # Always remember Key:Value
    outputDict[i] = i*i
 
print(outputDict)
"""
 
# Question 3
 
"""
test_string = "vGcnX1tikVEwgAWGE39y"
num_letters = 0
num_digits = 0
for i in test_string:
    if i.isdigit():
        num_digits += 1
    elif i.isalpha():
        num_letters += 1
 
print("There are {} letters and {} digits".format(num_letters, num_digits))
"""
 
## Question 3 (Alternate Ans)
"""
exerciseString = "vGcnX1tikVEwgAWGE39y"
totalDigits = 0
totalLetter = 0
 
# A string is a list
for i in exerciseString:
    # if i is a digit, it adds 1 to the digit counter
    # ELSE, it must be a letter so add 1 to the letter counter
    if (i.isdigit()):
        totalDigits += 1
    else:
        totalLetter += 1
 
print("There are", totalLetter, "letters and",totalDigits,"digits")
"""
 
# Question 4
"""
test_string = "wyyj5vwgdlvqwsajbremwdfq35bvbc"
output_dict = {}
for i in test_string:
    if i not in output_dict:
        output_dict[i] = 1
    else:
        output_dict[i] += 1
 
print(output_dict)
"""
 
# ===============ADVANCE=================
 
# Question 1
 
"""
for i in range(1,6):
    output_string = ""
    for j in range(i):
        output_string += str(i) + " "
    print(output_string)
"""
 
## Question 1 (Alternate Ans)
"""
# First get the number 1,2,3,4,5
for i in range(1,6):
    # Initialize an empty string PER loop
    output = ""
    # Having a loop eg 1 > 1,2 > 1,2,3 > 1,2,3,4 etc
    for j in range(i):
        # Use typecast from int to string and why 'i' is because 
        # you would want the primary first loop 
        output += str(i) + " "
    print(output)
"""
 
# Question 2
 
"""
output_list = [i, i]
i = output_list[1]
while i < 50:
    next_sequence = i + output_list[len(output_list)-1]
    output_list.append(i + 1)
    i = next_sequence
 
print(output_list)
"""
 
# Question 3
 
"""
sample_input = [2,7,11,15]
target = 9
lengthOfList = len(sample_input)
outputList = []
 
# Enumerate makes the for loop like this:
# eg. aList = [2,4,6,8,10]
# for i,j in enumerate(aList) gives you (0,2) (1,4) (2,6) (3,8) ...
# so esentially its (index, value)
# so using the var i (for the very first loop gives you 0) is the current index
# while using the var j (for the very first loop gives you 2) is the current value
 
for i,j in enumerate(sample_input):
    remainder_list = sample_input[i+1:lengthOfList]
    possibleAns = target - j
    if(possibleAns in remainder_list):
        outputList.append(j)
        outputList.append(possibleAns)
 
print(outputList)
"""
 
# Question 4
 
'''
sample_input = [1, 2, 3]
final_list = []
n = len(sample_input)
i = 0
while i < n:
    # check empty
    if not final_list:
        final_list.append([sample_input[i]])
    else:
        temp_list = []
        for j in final_list:
            for k in range(0, i+1):
                # copy list
                e = j[:]
                # insert into position k
                e.insert(k, sample_input[i])
                temp_list.append(e)
        final_list = temp_list
    i += 1
print(final_list)
'''
