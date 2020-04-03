#exercise 10
#print NxN square of *. Prompt user for value of N.

#prompts user for value of N. Turns that value into an integer
N = int(input('How big is the square? '))
counter = 0
star = '' 

while counter < N:
    star += '*'   
    counter += 1  
    
counter = 1
while counter <= N:    #repeat first while loop for N lines
    print(star)
    counter += 1




