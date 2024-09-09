from tkinter import *
from PyMultiDictionary import MultiDictionary


dictionary = MultiDictionary()
root = Tk()
root.title("Dictionary")
root.geometry("1250x750")


def dict():
    '''
    This function is used to get the meaning, synonym and antonym of the word
    '''
    meaning.config(text=dictionary.meaning('en', word.get())[1])
    synonym.config(text=dictionary.synonym('en', word.get()))
    antonym.config(text=dictionary.antonym('en', word.get()))