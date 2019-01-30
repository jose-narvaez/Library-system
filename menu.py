'''This module is used to develop a GUI using the module tkinter. It uses the modules
booksearch, bookcheckout, bookreturn and bookweed for its functionality. This GUI
allows the user to perform all functionalities of the different modules, the user can
search for a book, checkout a book, return it, and remove a book from the library.

Created by: Jose Narvaez Paliza
Creation date: 11/12/2018'''


from tkinter import *

import booksearch
import bookcheckout
import bookreturn
import bookweed


###functions to get entries


def get_title_entry():
    '''This function is used to get the title of the book that the user wants to search. It then uses that entry
        when calling the function search_book from the booksearch module. It stores the available books
        in a variable and then creates a text widget from tkinter module and writes the available books
        into the text widget. This function is called when the search book button is clicked.'''

    book = (entry_book.get())
    books_display=booksearch.search_book(book) #stores available books in variable
    
    books_txt=Text(search_frame, height = 4, width= 50, font=("helvetica",14)) #creates text widget   
    books_txt.grid(row=6, column=1,columnspan=4, pady=20)
    books_txt.config(state=NORMAL)
    books_txt.delete(1.0,END)
    books_txt.insert(CURRENT, books_display) #it writes the books in widget
    scrl = Scrollbar(search_frame, command=books_txt.yview) #creates scrollbar
    books_txt.config(yscrollcommand = scrl.set)
    scrl.grid(row=6, column =6, sticky='ns')
    books_txt.config(state=DISABLED)
    
def get_IDs():
    '''This function is used to get the student ID entry and the book ID entry of the book that the student
        wants to checkout. It then calls the function checkout_book from the bookcheckout module and stores
        a message on a variable. It then writes the message into a label which is displayed
        in the GUI. This function is called when the button checkout book is clicked.'''
    
    student_id= (entry_studentID.get())
    book_id=(entry_bookID.get())
    checkout_message = bookcheckout.checkout_book(student_id,book_id)
    checkout_msg_lbl.configure(text=checkout_message) #writes message into label

def get_book_return():
    '''This function is used to get the book ID that the student wants to return. It then calls the function
        return_book from the bookreturn module and stores the appropiate message in a variable. It writes the
        message in a label so it can be displayed in the GUI. This function is called when the button
        return book is clicked.'''
    book_id_r=(entry_return_bookID.get())
    return_message= bookreturn.return_book(book_id_r)
    return_msg_lbl.configure(text=return_message) #writes message into label

def get_suggestion():
    '''This function is used to call the suggest_book function from the bookweed module. It stores the suggested
        book in a variable and then writes it in the suggestion label so it can be displayed in GUI. This
        function is called when the button suggest book is clicked.'''
    suggestion_return=bookweed.suggest_book()
    suggestion_lbl.configure(text=suggestion_return)#writes message into label 

def get_remove():
    '''This function is used to get the book Id that the user wants to remove from the library. It calls
        for the function remove_book from the bookweed module and stores the appropiate message in a variable.
        It writes the message into the message label so it can be displayed in the GUI. This function is called
        when the button remove book is clicked.'''
    book_id_remove=(entry_remove_bookID.get())
    remove_message= bookweed.remove_book(book_id_remove)
    remove_msg_lbl.configure(text=remove_message) #writes message into label

###functions to activate frames
    
def search_frame():
    '''This function is used to show the search frame and to hide the rest of the frames. It is activated
        when the button search is clicked.'''
    checkout_frame.grid_remove()
    return_frame.grid_remove()
    weed_frame.grid_remove()

    search_frame.grid(row=2, column= 0, columnspan=4)

def checkout_frame():
    '''This function is used to show the checkout frame and to hide the rest of the frames. It is activated
        when the button checkout is clicked.'''
    search_frame.grid_remove()
    return_frame.grid_remove()
    weed_frame.grid_remove()

    checkout_frame.grid(row=2, column=0, columnspan=4)

def return_frame():
    '''This function is used to show the return frame and to hide the rest of the frames. It is activated
        when the button return is clicked. '''
    search_frame.grid_remove()
    checkout_frame.grid_remove()
    weed_frame.grid_remove()

    return_frame.grid(row=2, column=0, columnspan=4)

def weed_frame():
    '''This function is used to show the bookweed frame and to hide the rest of the frames. It is activated
        when the button remove is clicked. '''
    search_frame.grid_remove()
    checkout_frame.grid_remove()
    return_frame.grid_remove()
    
    weed_frame.grid(row=2, column=0, columnspan=4)

### window    
window = Tk()
window.title("Library")
window.geometry('650x400')

#title
title_lbl =Label(window, text='WELCOME TO THE LIBRARY!', font=("helvetica",24))
title_lbl.grid(row=0, column=0,columnspan=5,pady=15)


#buttons to activate frames

search=Button(window, text="Search Book", command=search_frame)
search.grid(row=1,column=0, padx=10)

checkout=Button(window, text="Checkout Book", command=checkout_frame)
checkout.grid(row=1,column=1, padx=10)

return_b=Button(window, text="Return Book", command=return_frame)
return_b.grid(row=1,column=2, padx=10)

weed=Button(window, text="Remove Book", command=weed_frame)
weed.grid(row=1,column=3, padx=10)


#search frame

search_frame = Frame(window)

a=Label(search_frame, text='')
a.grid(row=6, column = 2)

lbl_Section1=Label(search_frame, text='Search book:', font=("helvetica",16)) 
lbl_Section1.grid(row=3, column= 0, pady=20)
    
lbl_book=Label(search_frame, text = 'Book name', font=("helvetica",16))
lbl_book.grid(row=4, column=1)

entry_book = Entry(search_frame)
entry_book.grid(row=4, column=2)

btn_search=Button(search_frame, text = 'Search', command = get_title_entry)
btn_search.grid(row=5, column = 2, pady=10)



#checkout frame

checkout_frame = Frame(window)

lbl_Section2 = Label(checkout_frame, text='Checkout book:', font=("helvetica",16))
lbl_Section2.grid(row=6, column=0, pady=20)

lbl_studentID=Label(checkout_frame, text = 'Student ID', font=("helvetica",16))
lbl_studentID.grid(row=7, column=1)

entry_studentID = Entry(checkout_frame)
entry_studentID.grid(row=7,column =2)

lbl_bookID=Label(checkout_frame, text = 'Book ID', font=("helvetica",16))
lbl_bookID.grid(row=8, column=1)

entry_bookID = Entry(checkout_frame)
entry_bookID.grid(row=8,column=2)

btn_checkout = Button(checkout_frame, text = 'Checkout', command = get_IDs)
btn_checkout.grid(row=9, column=2, columnspan=2, pady=2)

checkout_msg_lbl = Label(checkout_frame,text='', font=("helvetica",16))
checkout_msg_lbl.grid(row=10, column= 2, columnspan=3)

#return frame

return_frame=Frame(window)

lbl_Section3 = Label(return_frame, text='Return book:', font=("helvetica",16))
lbl_Section3.grid(row=11, column=0, pady=20)

lbl_bookID_return=Label(return_frame, text = 'Book ID', font=("helvetica",16))
lbl_bookID_return.grid(row=12, column=1)

entry_return_bookID=Entry(return_frame)
entry_return_bookID.grid(row=12, column=2)

btn_return = Button(return_frame, text='Return', command = get_book_return)
btn_return.grid(row=13, column= 2, columnspan=2, pady=5)

return_msg_lbl = Label(return_frame,text='', font=("helvetica",16))
return_msg_lbl.grid(row=14, column=2, columnspan=3)

#Bookweed frame

weed_frame=Frame(window)

lblSection4=Label(weed_frame,text='Book removal:', font=("helvetica",16))
lblSection4.grid(row=15, column=0, pady=20)

btn_suggest=Button(weed_frame,text="Suggest Book", command=get_suggestion)
btn_suggest.grid(row=16,column=2, columnspan=2, pady=2)

suggestion_lbl=Label(weed_frame,text='', font=("helvetica",14))
suggestion_lbl.grid(row=17, column=1, columnspan=5, pady=10)

entry_remove_bookID=Entry(weed_frame)
entry_remove_bookID.grid(row=18,column=2)

remove_book_lbl=Label(weed_frame, text="Book ID", font=("helvetica",16))
remove_book_lbl.grid(row=18, column=1)

btn_remove=Button(weed_frame, text="Remove", command=get_remove)
btn_remove.grid(row=19, column =2, columnspan=2, pady=2)

remove_msg_lbl=Label(weed_frame, text='', font=("helvetica",16))
remove_msg_lbl.grid(row=20, column=2, columnspan=3)

window.mainloop()





