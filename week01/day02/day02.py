#Typecasting in Python = the process of converting a variable from one data type to another data type.
#                       str() int() float() bool() are the built-in functions used for typecasting in Python.
import math
name = input("Enter your name: ") # Where you can input your name and it will be stored in the variable name as a string data type.
is_name = True  #Where you can set the variable is_name as True or False. If you set it as True then it will return True and if you set it as False then it will return False.

# __name__= bool(name) #Typecasting str to bool


#So the next Question is how can we show like if the User doesnt input any name then it will return False but it will not show the name as False. 
#It will be an Please enter your name.

if  name == "":
    print("Please enter your name.")
else:
    print("Hello", name , "!")









#age = bool(age) #Typecasting int to bool
# gpa = bool(gpa) #Typecasting float to bool
# is_student = bool(is_student) #Typecasting bool to bool
#gpa = int(gpa) #Typecasting float to int
#print(gpa) #Output 1 what will be the output of this code? its shown 1st is 1 because when we convert float to int, 
#                    it will remove the decimal part and return only the integer part.   


#gpa = int (math.floor (gpa + 0.4))

#print(gpa) #Output 2 what will be the output of this code? its shown 2nd is 2 because when we convert float to int,
#                    it will remove the decimal part and return only the integer part. but here we are using math.floor() function to round the float value to
#                    the nearest integer. so 1.3 + 0.5 = 1.8 and math.floor(1.8) = 1 and then int(1) = 1. so the final output is 1. 

#                    But if we use math.floor(gpa + 0.5) then it will round the float value to the nearest integer. so 1.5 + 0.5 = 2.0 and math.floor(2.0) = 2 and then int(2) = 2. so the final output is 2.
#                    So we need to readjust or recalculate the value of gpa to get the correct output. 

#gpa = round (gpa) #Typecasting float to int with some adjustment to get the correct output. but here we are using round() function to round the float value to the nearest integer. so 1.5 will be rounded to 2.0 and then int(2.0) = 2. so the final output is 2.
#print (gpa) 


# Converting a integer into an string using str() function

# age = str(age) #Typecasting int to str
# gpa = str(gpa) #Typecasting float to str
# is_student = str(is_student) #Typecasting bool to str
# print(type(age)) #Output <class 'str'> what will be the output of this code? its shown
# print(type(gpa))
# print(type(is_student))

#OUTPUT 4 This time i try to convert the string into a boolean value using bool() function. The bool() function returns True if the string is not empty and 
# False if the string is empty. It will be used on some input type where you can ask the user to enter some input and if the user enters some input then 
# it will return True and if the user does not enter any input then it will return False.
