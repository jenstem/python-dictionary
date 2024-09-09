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
Label(frame, text="Enter Word", font=("Arial 15 bold")).pack(side=LEFT)
word = Entry(frame, font=("Arial 15 bold"))
word.pack()
frame.pack(pady=10)