#exercise 8
#count from one number to another. User selects starting and ending number

#ask user for input for first number and second number. convert to integer. store values in variable
n = int(input('Please select a starting number: '))
m = int(input('Please select an ending number: '))

#loop through numbers and print result

while n <= m:
    print(n)
    n += 1
