# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1998755     IIT ID : 20220034
# Date: 19/04/2023

user_dict={} #creating the dictionary
studentIdList = [] #creating a list to append the student ID's
studentID = 0 # creating variable

#getting the inputs for credits and validating
def inputs():
    global p,q,r,s
    global PASS,DEFER,FAIL
    try:
        PASS=int(input('\nPlease enter your credits  as pass:'))
        if PASS not in range(0, 121, 20):
            print('Out of range')
            inputs()
        else:
            DEFER=int(input('Please enter your credits  as defer:'))
            if DEFER not in range(0, 121, 20):
                print('Out of range')
                inputs()
            else:
                FAIL=int(input('Please enter your credits  as fail:'))
                if DEFER not in range(0, 121, 20):
                    print('Out of range')
                    inputs()
                else:
                    total()
                                   
    except ValueError:
        print('\nInteger required')
        inputs()

#Adding the total of the credits
def total():
    global PASS,DEFER,FAIL
    total=PASS+DEFER+FAIL
    if (total==120):
        progression()
    else:
        print('\nTotal incorrect')
        inputs()
        

#to continue
def Continue():
    global user_dict, studentIdList
    user=input('''\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:''')
    if (user=='y'):
        stuId()
    elif (user=='q'):
            for k, v in user_dict.items():
                print(k, "\t:", *v)
            quit()
    else:
            Continue()

#check progression
def progression():   # Reference : www.w3schools.com
    global user_dict, studentID
    global PASS,DEFER,FAIL

    if PASS == 120:
        print('\nProgress')
        user_dict [studentID] = [("progress-",PASS,DEFER,FAIL)] #Updating the dictionary , 
    elif PASS==100:
        print('\nProgress (module trailer)')
        user_dict [studentID] = [("Progress (module trailer)-",PASS,DEFER,FAIL)] #Updating the dictionary
    elif FAIL>=80:
        print('\nExclude')
        user_dict [studentID] = [("Exclude-",PASS,DEFER,FAIL)] #Updating the dictionary
    else:
        print('\nDo not progress-module retriever')
        user_dict [studentID] = [("Do not progress-module retriever -",PASS,DEFER,FAIL)] #Updating the dictionary
    Continue()

#Getting the student ID
def stuId():
    global studentIdList,studentID
    while True:
        studentID = input('Enter the student ID:')
        if studentID not in studentIdList:
            studentIdList.append(studentID)
            inputs()
        else:
            print("\nStudent ID already entered! \nplease enter another ID\n")
            continue  

#to print the display
def startUp():
    print("---------Dictionary - Part 4---------\n")
    stuId()

startUp()
    
    
    
