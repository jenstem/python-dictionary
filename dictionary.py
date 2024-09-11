from tkinter import *
from PyMultiDictionary import MultiDictionary


dictionary = MultiDictionary()
root = Tk()
root.title("Dictionary")
root.geometry("1250x750")


def dict():
    '''
    This function is used to set the text for the meaning, synonym and antonym of the word
    '''
    meaning.config(text=dictionary.meaning('en', word.get())[1])
    synonym.config(text=dictionary.synonym('en', word.get()))
    antonym.config(text=dictionary.antonym('en', word.get()))


Label(root, text="Dictionary", font=("Arial 28 bold"), fg="SpringGreen4").pack(pady=10)

frame = Frame(root)
'''
This frame is used to take the input from the user
'''
Label(frame, text="Enter Word:", font=("Arial 20 bold")).pack(side=LEFT)
word = Entry(frame, font=("Arial 20 bold"))
word.pack()
frame.pack(pady=10)
Button(root, text="Submit", font=("Arial 18 bold"), command=dict).place(x=800, y=73)

frame1 = Frame(root)
'''
This frame is used to display the meaning of the word
'''
Label(frame1, text="Meaning: ", font=("Arial 18 bold")).pack(side=TOP)
meaning = Label(frame1, text="", font=("Arial 18"),wraplength=600)
meaning.pack()
frame1.pack(pady=15)

frame2 = Frame(root)
'''
This frame is used to display the synonym of the word
'''
Label(frame2, text="Synonym: ", font=("Arial 18 bold")).pack(side=TOP)
synonym = Label(frame2, text="", font=("Arial 18"),wraplength=600)
synonym.pack()
frame2.pack(pady=15)

frame3 = Frame(root)
'''
This frame is used to display the antonym of the word
'''
Label(frame3, text="Antonym: ", font=("Arial 18 bold")).pack(side=TOP)
antonym = Label(frame3, text="", font=("Arial 18"),wraplength=600)
antonym.pack()
frame3.pack(pady=15)

root.mainloop()