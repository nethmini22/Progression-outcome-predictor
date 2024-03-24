# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1998755     IIT ID : 20220034
# Date: 15/04/2023

#Define variables
PASS=0 #creating variable to store pass credits
DEFER=0 #creating variable to store defer credits
FAIL=0 #creating variable to store fail credits
total=0 #creating variable to add pass, defer and fail credits

progress=0 #creating variable to the count of progress
moduleTrailer=0 #creating variable to the count of module trailers
exclude=0 #creating variable to the count of exclude
retriever=0 #creating variable to the count of retrivers

main_list=[] #creating a list to append all the details 
i = [] #creating a list to access nested list

print(">>>>>>>>>>>>>>>>>>>>Welcome to the University of Westminster<<<<<<<<<<<<<<<<<<<<<<<<< ")
#getting the choice from the user
def choice():
    global choice
    try:
        choice=int(input('\nfor student press 1,for staff press 2:'))
        inputs()
    except:
        print('Invalid choice')
        choice()
        
#asking for credits
def inputs():
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
        
#cheking total
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
    global choice
    if choice == 2:
        user=input('''\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:''')
        if (user=='y'):
            inputs()
        elif (user=='q'):
            quit
            Histogram()
        else:
            Continue()
    elif choice == 1:
        quit
    else:
        print('Enter a valid option')
        choice()

#check progression
def progression():
    global main_list
    global progress, retriever, exclude, moduleTrailer
    global PASS,DEFER,FAIL
    if PASS == 120:
        print('\nProgress')
        progress=progress+1
        main_list.append(["progress:",PASS,DEFER,FAIL])
    elif PASS==100:
        print('\nProgress (module trailer)')
        moduleTrailer=moduleTrailer+1
        main_list.append(["module trailer:",PASS,DEFER,FAIL])
    elif FAIL>=80:
        print('\nExclude')
        exclude=exclude+1
        main_list.append(["Exclude:",PASS,DEFER,FAIL])
    else:
        print('\nDo not progress-module retriever')
        retriever=retriever+1
        main_list.append(["module retriever:",PASS,DEFER,FAIL])
    Continue()
    
#PART 2
def List():
    global main_list
    for i in main_list:
        print(*i)
    text_file()

#display histogram
def Histogram():
    global progress, retriever, exclude, moduleTrailer
    print('\nHistogram''\nprogress',progress,':','*'*progress,"\ntailer", moduleTrailer, ":", "*" * moduleTrailer,"\nRetriever",retriever, ":", "*" * retriever, "\nExcluded", exclude, ":", "*" * exclude)
    totalOutcomes=progress+moduleTrailer+exclude+retriever
    print(totalOutcomes,'outcomes in total.\n')
    List()
    
#part 3
def text_file():
    global main_list
    print("\nData Stored in file named Credict_file")       # Reference : www.w3schools.com
    file = open("Credict_file",'w')
    for i in main_list:
        file.write(str(i[0])+str(i[1])+" "+str(i[2])+" "+str(i[3])+"\n")
    file.close()

    file = open("Credict_file",'r')
    print(file.read())
choice()
