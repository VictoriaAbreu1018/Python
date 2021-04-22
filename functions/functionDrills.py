'''
For this assignment you should read the task, then below the task do what it asks you to do.
For tasks with return statements, you can test out if you are correct by putting in some parameters
and printing what is returned outside of the function.

EXAMPLE TASK:
'''
#EX) Define a function that has two parameters. Make the function add the two
#numbers together and return the result.
def add_two_numbers(num1, num2):
    sumOfTwoNumbers = num1 + num2
    return sumOfTwoNumbers

'''
END OF EXAMPLE
'''

'''
START HERE
'''


#1) Define a function that has two int parameters. Make the function subtract 
#the first parameter minus the second one. Then, return the result. Now call 
#the function.
#Print what the function returns.
def twoandone (two, one):
    difference = two - one
    return difference 

diff = twoandone(2, 1)
print(diff)


#2) Define a function that has one parameter. Make the function divide the 
#parameter by 2, multiply it by 77, and then add 10,000. Return the result.
#Now call the function.
#Print what the function returns.
def multipels (eighty):
    equ = eighty / 2 * 77 + 10,000
    return equ

solution = multipels(80)
print(solution)


#3) Define a function that has two int parameters. Make the function check if 
#two numbers are equal. If they are equal, return true. If they are not equal, 
#return false. Now call the function.
#Print what the function returns.
def checkity (uno, dos):
    if(uno == dos):
        return "True"
    else:
        return "False"
    
ans = checkity(40, 40)
print(ans)


#4) Define a function that has two int parameters. Make the function
#check which parameter is bigger, and return the bigger parameter. 
#If they are the same, it should just return either parameter. Now call the 
#function.
#Print what the function returns.
def aaaron (tres, oui):
    if(tres > oui):
        return tres
    elif(tres < oui):
        return oui
    else:
        return tres
    
big = aaaron(333, 47)
print(big)


#5) Define a function that has two string parameters. Make the function
#add the two strings together. And then return the combined string. Now call 
#the function.
#Print what the function returns.
def abscat (so, rude):
    bruh = so + rude
    return bruh

ray = abscat("dry", "land")
print(ray)


#6) Define a function that has three int parameters. If the first number is 
#equal to the second OR the third number, return true. Else, return false. Now 
#call the function.
#Print what the function returns.
def threesacrowd (why, I, cry):
    if(why == I or why == cry):
        return "True"
    else:
        return "False"

car = threesacrowd(36, 478, 111)
print(car) 


#7) Define a function that prints your name. It should have no parameters and 
#shouldn't return anything. Now call the function.

def myname( ):
    print("Victoria")

call = myname()
print(call)

#8) Define a function that has one string parameter. The string should be a
#color. If that string is equal to your favorite color, it prints "That's my 
#favorite color!". If it is not, it prints "That is not my favorite color. 
#Try again.". It shouldn't return anything. Now call the function.
def colorss (string):
    if( string == "burnt orange"):
        print("that's my favorite color!")
    else:
        print("that is not my favorite color")
        
color = colorss("dark chestnut")
print(color)
        


#9) Define a function that has one int parameter. The int should be 
#positive. If the number is not equal to zero, the function runs a loop that
#decrements the parameter by 1 and prints it each time. Now call the function.

def looptiloops (quatro):
    x = 186
    while(x >0 and x != 0):
        print(x)
        x -= 1

int = looptiloops(186)
print(int)