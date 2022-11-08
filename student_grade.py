
#A simple program demonstrating the use of dictionaries
#Asks the user for a student's name and their grade and prints it out in dictionary form

import time
#importing time allows us to work with something called sleep which lets us manipulate that program to display
#certain outputs at certain time intervals


#First we start with an empty dictionary that will be filled later
students = {}

#Then we need to make sure the program runs as long a the 'q' button is not pressed
while True:
    #ask for the name of the student
    res = input("Please give me the name of the student(q to quit): ")

    #if the 'q' button is pressed
    if res == "q":
        print("quitting...")
        time.sleep(2) #Delay output for 2 seconds
        print("...quitting...")
        time.sleep(3) #Delay output for 3 seconds
        print("Bye!")
        break #exits the program if the 'q' button on the keyboard is pressed
    else:
        #Add the input of "res" to the "keys" part of the dictionary called "students"
        students['Student'] = res

        #Ask for the grade of the student
        res_grade = input("Please give me their grade: ")


        #Assigns the input of  "res_grades" to the "values" part of the dictionary called "students"
        students["Grade"] = res_grade

        #Finally, it prints student's name and their grade
        print("Here is your student and their grade ${}".format(students))

