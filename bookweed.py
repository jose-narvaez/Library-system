'''This module allows the user to remove a book from the library for ever.
The user can request a suggestion of which book to remove from the library.
The book suggested will be the book that has not been checked out for the longest
time. It will only suggest a book that is not on loan. In other words, it suggests
the book that has not been used for the longest amount of time. It calculates the time
by the number of months, and it ignores the number of days. If two books have not been checked
out for the same amount of time it will suggest the first one that appears in the library.
This module removes a book from the library by asking the user to enter the book ID he
of the book he wants to remove. It checks if the book exists and if it is not on loan.
If both conditions are true, the database and logfile will be modified by deleting the book.
It will return an appropiate message saying if the removal was a succes or not.

This module contains the functions: read_logfile, suggest_book and remove_book

Module created by: Jose Narvaez Paliza
Creation Date: 11/12/2018'''

import datetime
import booksearch
import bookcheckout
import bookreturn


now = datetime.datetime.now()
current_month = now.month
current_month=int(current_month) #global variable
current_year= now.year
current_year=int(current_year) #global variable

logfile_name="logfile.txt" #global variable
database_name="database.txt" #global variable

def read_logfile(name_logfile):
    '''This function reads the logfile text file. It return list_logs which is a list of
        books with their corresponding checked out/return date. Each book is contained within a list. e.g
        ['1', 'To kill a mockingbird', 'Harper Lee', '0','7','2018'] each element is a string and the fourth
        and fifht element represent a month and a year.''' 
    
    logfile=open(name_logfile,'r')

    list_logs=[] #list of books

    for line in logfile:     
        line= line.strip()
        line= line.split(':')#txt file uses : to separate fields
        list_logs.append(line)
    logfile.close()
     
    return list_logs 
        


def suggest_book():
    '''This function is used to suggest which book needs to be removed from the library.
        From all the book that are not on loan, it returns the book which has not been
        checked out for the longest amount of time. It uses months to compare times.'''

    logfile_load=read_logfile(logfile_name)
    
    time_list=[] #list with total times

    #calculating total time that a book has not been checked out for (for each book)
    for book in logfile_load:
        student = book[3]
        if student=='0':  #book not on loan
            year= book[5]
            year=int(year) #in order to make arithmetic operations
            
            month=book[4]
            month=int(month) #in order to make arithmetic operations

            year_difference=current_year-year
            years_to_months=year_difference*12 
            
            #absolute value of difference of months
            month_difference=(max(month, current_month))-(min(month, current_month))
            
            total_time=years_to_months+month_difference #total time it hasn't been checked out for
            time_list.append(total_time)

            if max(time_list) ==total_time: #if the total_time is the max
                suggestion_list=[] #deletes list
                suggestion_list.append(book) #append the total_time

    suggestion=suggestion_list[0] #only contains the max value
            
    book_id=suggestion[0] 
    title = suggestion[1]
    author = suggestion[2]
    student_id = suggestion[3]
    new_month = suggestion[4]
    new_year = suggestion[5]
    
    fields='Book ID'+20*' '+ 'Title' + 18*' '+ 'Author'+14*' '+ 'Date' +'\n'#display
    return (fields+book_id+ 15*' '+ title+ 10*' '+author+ 9*' '+new_month+'/'+new_year)
            
def remove_book(book_id):
    '''This function allows the user to remove any chosen book from the library if the
        book is not on loan. If the book is on loan it will return an error message,
        it also checks that the book exists.If the book exists and it is not on loan it
        will remove the book from both the logfile and database text files and will return
        a message saying the removal has been succesfull.

        book_id is the book the user wants to remove (string)'''

    library=booksearch.read_database(database_name)
    logfile_load=read_logfile(logfile_name)
    
    #true or false values
    book_exists = bookcheckout.check_book_existance(book_id)
    book_available= bookcheckout.check_book_available(book_id)


    if book_id=='': #empty input
        return ("Please enter a book ID")
    
        
    elif book_exists==True and book_available==True: #it exists and is not on loan

        #modifies logfile by deleting the book
        logfile=open(logfile_name,'w')
        for book in logfile_load:
            if book[0]!=book_id: #rewrites all other lines as they were
                logfile.write(book[0]+':'+book[1]+':'+book[2]+':'+book[3]+':'+book[4]+':'+book[5]+'\n')               
        logfile.close()

        #modifies database by deleting the book
        database=open(database_name, 'w')
        for book in library:
            if book[0]!=book_id:#rewrites all other lines as they were
                database.write(book[0]+':'+book[1]+':'+book[2]+':'+book[3]+'\n') 
        database.close()

        return ("You have removed the book")

    elif book_exists==False:

        return ("That book doesn't exists")

    else:
        return ("That book is on loan")


if __name__=='__main__':

    

    print ("----------------------------------------------------------")
    print ("User asks for book suggestion----------------\n")

    suggestion =suggest_book()
    print (suggestion + '\n')

    print ("----------------------------------------------------------")
    print ("User enters on loan book to be removed-------\n")

    id_book='1'
    print ("Book ID: " + id_book + '\n')

    removal= remove_book(id_book)
    
    print ("Message----------------\n")

    print (removal)

    print ("----------------------------------------------------------")
    print ("User enters on valid book to be removed-------\n")

    id_book='20'
    print ("Book ID: " + id_book + '\n')

    removal= remove_book(id_book)
    
    print ("Message----------------\n")

    print (removal)

        

        

        
        
        

        

    

    
