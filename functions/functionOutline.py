'''
This outline will help solidify concepts from the Functions lesson.
Fill in this outline as the instructor goes through the lesson.
'''

#1) Make a function that has two boolean parameters. If both booleans are
#true, return true. Else, return false. Then, call the function.
#Print what the function returns.

def booleanvars (booone , bootwo):
    if(booone == bootwo):
        return "True"
    else:
        return "False"
lean = booleanvars(2, 3)
print(lean)
#2) Make a function that takes one int parameter: gallons. Convert gallons
#to cups (do this by multiplying gallons by 16). Then return cups. Then,
#call the function.
#Print what the function returns.
def galsandcups (gallons):
    cups = gallons * 16
    return cups

galls = galsandcups(5)
print(galls)


#3) Make a function of any any kind with a common SYNTAX error. Then, call the
#function.
#Print what the function returns.
def oneandtwo ony,twy):
    sum = ony + twy
    return sum

num = oneandtwo(1, 2)
print(num)
