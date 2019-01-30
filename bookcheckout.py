'''This module allows the user to checkout a book from the library. The user
Enters the book ID that he wants to checkout and his student ID. The module
first checks if the student ID is valid using the check_student_id function.
If it is valid it checks if the book exists and if the book is available usnig
the functions check_book_existance and check_book_available. If all inputs are
valid it allows the user to check it out, returns an appropiate message and
updates the database and logfile text files to indicate that the user has the book.
If one of the fields entered is not valid it will return an appropiate errormessage.

This module contains the functions: check_student_id, check_book_existance,
check_book_available, checkout_book, modify_database, modify_logfile.

Module created by: Jose Narvaez Paliza
Date of creation: 11/12/2018'''


import datetime
import booksearch
import bookweed

now = datetime.datetime.now()
current_month = now.month #current month using datetime module
current_month=str(current_month)
current_year= now.year #current year using datatime module
current_year=str(current_year)

database_name="database.txt" #global variable
logfile_name="logfile.txt" #global variable

def check_student_id(student_id):
    '''This function checks if the student ID entered is valid i.e if it was 4 digits
        and is an integer. It uses an exception handler to determine if the ID entered
        is a 4 digit number. This function does not check if the entered ID type is an
        integer, it checks if the string is a number by changing the type into int type.
        If the ID is valid it returns True if it is not valid it returns False.

       student_id is entered by the user, it is their own student ID (string)'''
    
    while True:
        try:
            try_error=int(student_id) # used to trigger ValueError
            student_id = str(student_id)
            if len(student_id) != 4: #different than 4 digits
                return False
            else:
                return True

        except ValueError:
            return False


def check_book_existance(book_id):
    '''If the book entered by the user is in the library it returns a True value,
        otherwise returns False. It uses the function read_database from search module
        to read through the database.

        book_id is entered by the user, it is the book ID of the desired book (string)'''

    library = booksearch.read_database(database_name)
    
    for book in library:
        id_of_book=book[0]
        if id_of_book == book_id: 
            return True #the book exists
    
    return False #the book doesn't exists

def check_book_available(book_id):
    '''If the book entered is available it will return a True value, otherwise False.
        It uses the function read_database from search module to read through the database.

        book_id is entered by the user using the GUI, it is the book ID of the desired book (string)'''
    
    library = booksearch.read_database(database_name)

    for book in library:
        id_of_book = book[0]
        student_id = book[3]
        if id_of_book == book_id and  student_id != '0': #if the student id is 0 it means no one has it
            return False #the book is on loan
    
    return True #the book is free if it exists

        
def checkout_book(student_id, book_id):
    '''This function allows the user to checkout a book. It first checks if student ID is valid
        and if the book is available and it exists. If al criteria is true it will allow the
        user to checkout the book, it will modify the database and logfile files and will
        return an appropiate message. If any of the criteria is false then it will not allow
        the user to checkout the book and will return an error message. 
   
        student_ID is entered by the user and it's their own student ID (string)
        book_ID is entered by the user and it's the book they want to checkout (string)'''
    
    library = booksearch.read_database(database_name)
    
    #true or false values
    check_student= check_student_id(student_id) 
    book_available= check_book_available(book_id) 
    book_existance = check_book_existance(book_id) 

    if student_id=='':
        return ("Please enter your ID")

    elif book_id=='':
        return ("Please enter the book ID")
    
    elif check_student == False:
        return ("That is not a valid student ID")
    
    elif book_existance==False: #book doesn't exist
        return ("This book does not exist")

    elif book_existance and book_available: #book exits and available
                    
        modify_database(student_id, book_id)

        modify_logfile(student_id,book_id)

        return ("You have withdrawn the book")
    
    else: #book is not available
        return ("This book is not available")

    
def modify_database(student_id, book_id):
    '''This function is used to modify the database txt file by changing the status of the book.
        It will change the student ID field from '0' to the number the student enters. This function
        asks for the student ID and book ID. 
        
        student_id is the ID of the student wanting to checkout the book (string)
        book_id is the ID of the book the student wants to checkout (string)'''

    library = booksearch.read_database(database_name)
        
    database=open(database_name, "w") #open database txt file to modify it
        
    for line in library:
        id_of_book = line[0] 
        title= line[1]
        author=line[2]
        student = line[3] 
        if id_of_book == book_id:                               
            student=student_id #rewrites student ID field to the one entered
            database.write(id_of_book+':'+title+':'+author+':'+student+'\n')
        else:#writes book as it was
            database.write(id_of_book+':'+title+':'+author+':'+student+'\n') 
    database.close()
    
def modify_logfile(student_id, book_id):
    '''This function is used to modify the logfile by changing the date of checkout or return.
        It uses the module datetime to get the current date. It also modifies the loan status.
        
        student_id is the ID of the student wanting to checkout the book (string)
        book_id is the ID of the book the student wants to checkout/return (string)'''

    logfile_load=bookweed.read_logfile(logfile_name)

    logfile=open(logfile_name,"w")

    for book in logfile_load:
        id_of_book= book[0]
        title = book[1]
        author = book[2]
        student= book[3]
        month=book[4]
        year=book[5]
        
        if id_of_book == book_id: #modifies the line of the book
            month=current_month 
            year=current_year 
            student=student_id 
            logfile.write(id_of_book+':'+title+':'+author+':'+student+':'+month+':'+year+'\n')
        else: #writes line as it was
            logfile.write(id_of_book+':'+title+':'+author+':'+student+':'+month+':'+year+'\n') 
    logfile.close()
        
if __name__=='__main__':
    ## valid
    #student enters his id number
    print ("------------------------------------------------------------")
    print ("Student enters valid student ID number------\n")
    student_id='1234'
    print ("Student ID: " + student_id + '\n')
    

    #student enters book id number
    print ("Student enters valid book Id----- \n")
    book_id='2'
    print ("Book ID: " + book_id + '\n')
    

    #checkout
    checkout=checkout_book(student_id,book_id)
    print ("Message----- \n")
    print (checkout)

    ##not valid student ID
     #student enters his id number
    print ("------------------------------------------------------------")
    print ("Student enters not valid student ID number----\n")
    student_id='abcd'
    print ("Student ID: " + student_id + '\n')
    

    #student enters book id number
    print ("Student enters valid book Id----- \n")
    book_id='2'
    print ("Book ID: " + book_id + '\n')
    

    #checkout
    checkout=checkout_book(student_id,book_id)
    print ("Message----- \n")
    print (checkout)

    ##not valid book ID
    #student enters his id number
    print ("------------------------------------------------------------")
    print ("Student enters valid student ID number------\n")
    student_id='1234'
    print ("Student ID: " + student_id + '\n')
    

    #student enters book id number
    print ("Student enters not valid book Id----- \n")
    book_id='223'
    print ("Book ID: " + book_id + '\n')
    

    #checkout
    checkout=checkout_book(student_id,book_id)
    print ("Message----- \n")
    print (checkout)


    ##book on loan
    #student enters his id number
    print ("------------------------------------------------------------")
    print ("Student enters valid student ID number------\n")
    student_id='1234'
    print ("Student ID: " + student_id + '\n')
    
    
    #student enters book id number
    print ("Student enters not available book Id----- \n")
    book_id='2'
    print ("Book ID: " + book_id + '\n')
    

    #checkout
    checkout=checkout_book(student_id,book_id)
    print ("Message----- \n")
    print (checkout)

 
