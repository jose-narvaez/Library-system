'''This module is used to search for a certain book in a given database which
is a text file. In order to search for a book, the user needs to enter the
name of the book as a string using the search_book function. It will return a
string containing all books that match the name. If there is no book with that
name in the library, it will return an appropiate error meessage.

This module contains the functions: read_database and search_book

Created by: Jose Narvaez Paliza
Creation Date: 11/12/2018'''


database_name="database.txt" #global variable
    
def read_database(name_database):
    '''This functions reads the database text file and it returns a list named list_books
        which contains all the books in the database. Each book is contained within a list
        e.g ['1', 'To kill a mockingbird', 'Harper Lee', '0'] where the first element is
        the book ID, the second the name of the book, then the name of the author and last
        the ID of the student who has the book or 0 if no one has it. Every element is a string.
        For this function to work, the fielsds of each book in the database text file need
        to be separated with colons.

        name_database is the name of a file e.g "database.txt" (string)'''
    
    database=open(name_database, "r")
    list_books= [] #list to store all books 
    for line in database: #every book is in one line in the txt file
        line= line.strip()
        line= line.split(':') #txt file uses : to separate fields
        list_books.append(line)
    database.close()
     
    return list_books 
    

def search_book(book_name):
    '''This function allows the user to search for a certain book using the book name.
        It returns a string variable that contains all books with that name if it founds
        any book, otherwise it returns an appropiate error message. It uses the function
        read_database to get the books from the database and the global variable database_name.

        book_name is the name of the book entered by the user (string)'''
    
    library = read_database(database_name)
    book_name = book_name.strip()
    book_name = book_name.lower() # user can type with lower or uppercase
    available_books_list=[] #list to store the books with the same name as the name entered

    for book in library:
        title=book[1]
        title=title.lower() # converts book title to lowercase to compare it easier
        if title == book_name:
            available_books_list.append(book)

    if book_name=='':
        return ("Please enter a book")        
           
    elif available_books_list == []: #no book found
        return ("No book with that name")
    
    else: #books were found
        existing_books=7*' '+'Book ID'+ 3*' '+ 10*' '+'Title'+ 18*' '+\
                        'Author'+ 12*' '+'Student'+'\n' #field names
    
        for book in available_books_list: #loops through list adding the books to the existing_books variable
            
            existing_books= existing_books+ 15*' '+ book[0] + 5*' '+book[1] +\
                            5*' '+ book[2] + 5*' ' +book[3]+'  '+ '\n'
              
        return existing_books
    
    
if __name__=="__main__":

       
    
    print ("-------------User enters an existing book title-----------\n")
    title= 'to kill a mockingbird'
    print ('Title: ' + title +'\n')
    books=search_book(title)
    print ("Search result-----\n")
    print (books)

    print ("-------------User enters a not existing book title-----------\n")
    title= 'Harry Potter'
    print ('Title: ' + title +'\n')
    books=search_book(title)
    print ("Search result-----\n")
    print (books)
    
    





       



    


    


        
            

    

    
    



    
    


