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


Label(root, text="Dictionary", font=("Arial 20 bold"), fg="Green").pack(pady=10)

frame = Frame(root)
'''
This frame is used to take the input from the user
'''
Label(frame, text="Enter Word", font=("Arial 15 bold")).pack(side=LEFT)
word = Entry(frame, font=("Arial 15 bold"))
word.pack()
frame.pack(pady=10)

frame1 = Frame(root)
'''
This frame is used to display the meaning of the word
'''
Label(frame1, text="Meaning: ", font=("Arial 14 bold")).pack(side=LEFT)
meaning = Label(frame1, text="", font=("Arial 14"),wraplength=1000)
meaning.pack()
frame1.pack(pady=15)

frame2 = Frame(root)
'''
This frame is used to display the synonym of the word
'''
Label(frame2, text="Synonym: ", font=("Arial 14 bold")).pack(side=LEFT)
synonym = Label(frame2, text="", font=("Arial 14"),wraplength=1000)
synonym.pack()
frame2.pack(pady=15)

frame3 = Frame(root)
'''
This frame is used to display the antonym of the word
'''
Label(frame3, text="Antonym: ", font=("Arial 14 bold")).pack(side=LEFT)
antonym = Label(frame3, text="", font=("Arial 14"),wraplength=1000)
antonym.pack()
frame3.pack(pady=15)

Button(root, text="Submit", font=("Arial 15 bold"), command=dict).pack()
root.mainloop()