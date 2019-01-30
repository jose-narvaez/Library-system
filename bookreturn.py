'''This module allows the user to return a book. The user needs to enter the book ID
of the book he wants to return. It checks if the book exists and if it is on loan.
If both criteria are true then it returns the book to the library and modifies
the database and logfile accordingly. It returns an appropiate message if
the book was returned or an error message otherwise.

This module contains the function: return_book

Module created by: Jose Narvaez Paliza
Creation date: 11/12/2018
'''
import booksearch
import bookcheckout
import bookweed
        
def return_book(book_id):
    '''This function allows the user to return book if the book ID entered is valid.
        the book ID is valid this function will modify the database text file so that
        the returned book is now available to checkout. If the user has returned the
        book succesfully the function will return a message saying so, if not it will
        return an error message.

        book_id is the book ID that the user wants to return (String) '''

    book_existance= bookcheckout.check_book_existance(book_id)
    book_available= bookcheckout.check_book_available(book_id)

    if book_id=='':
        return ("Please enter the book ID")

    elif book_existance==True and book_available==False: #book ID valid and can be returned

        student_id= '0'    
        bookcheckout.modify_database(student_id, book_id)
        bookcheckout.modify_logfile(student_id, book_id)

        return ("You have returned the book")

    elif book_existance==False:
        return ("This book does not exist")

    else:
        return ("This book is currently available")

    

if __name__=='__main__':

    ##valid
    #student enters book ID to return
    print ("-------------------------------------------------------------")
    print ("Student enters valid book ID to return------ \n")
    book_id='10'
    print ("Book ID: " + book_id + '\n')

    #return
    book_to_return=return_book(book_id)
    print ("Message-----------\n")
    print (book_to_return)

    ##not valid ID
    #student enters book ID to return
    print ("-------------------------------------------------------------")
    print ("Student enters not valid book ID to return----- \n")
    book_id='432'
    print ("Book ID: " + book_id + '\n')

    #return
    book_to_return=return_book(book_id)
    print ("Message------------\n")
    print (book_to_return)

    ##book on available
    #student enters book ID to return
    print ("-------------------------------------------------------------")
    print ("Student enters available book ID to return----- \n")
    book_id='5'
    print ("Book ID: " + book_id + '\n')

    #return
    book_to_return=return_book(book_id)
    print ("Message----------------------------------- \n")
    print (book_to_return)

    

    
            
    
            
            

            

    


            
    
