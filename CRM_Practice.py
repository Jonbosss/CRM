import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import mysql.connector


root = tk.Tk()
root.title('CRM')
root.geometry('400x400')

# Connect to mySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Letmeinnow1875!",
)

# Check to see if connection to MySQL was created
# print(mydb)

# Create a cursor and Initialize it
my_cursor = mydb.cursor()

# Create database


root.mainloop()
