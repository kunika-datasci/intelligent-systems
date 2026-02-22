text =""" Data Science is a growing field in 2026 that uses data to solve real problems. 
A model learns from 1000+ records and improves accuracy step by step. 
Sometimes errors like @noise or #missing values affect the result. 
Good preprocessing helps remove 50% of issues before training. Tools like Python, SQL, and ML@Models are widely used today. 
Strong logic, practice, and consistency lead to SUCCESS!"""

import mysql.connector 
import re

def connector(db = None):
   mySQL = mysql.connector.connect(
      host = "localhost",
      user = "root",
      password = "root",
      database = db
   )
   return mySQL


def ac (file= None):
    import os
    if os.path.exists(f"{file}"):
       with open(file,"r") as f:
         content = f.read()
         print(content)
    else:
        all_char = {"digit":digit,"caps":caps,"special_ch":special_ch,"space":space,"repeated_word":repeated_word}
        with open (file,"w") as f:
            for key,value in all_char.items():
             f.writelines(f"{key}:{value}\n")
        print("done")

while True:
    choice = input("""
    #==========================================
    print("press 1 for all digits : ")
    print("press 2 for all caps :")
    print("press 3 special_character: ")
    print("press 4 for all number of spaces :")
    print("press 5 all for repeated word: ")
    #===========================================
    """
    )
    if choice == "1":
       digit = re.findall(r"\d+",text)
       file = input("Enter your file name:")
       ac(file)
    if choice == "2":
       caps = re.findall(r"[A-Z]",text)
       file = input("Enter your file name:")
       ac(file)
    if choice == "3":
     special_ch = re.findall(r"[^a-zA-Z0-9\s]",text)
     file = input("Enter your file name:")
     ac(file)
    if choice == "4":
       space = len(re.findall(r" ",text))
       file = input("Enter your file name:")
       ac(file)
    if choice == "5":
       repeated_word = len(re.findall(r"is",text))
       file = input("Enter your file name:")
       ac(file)
    if choice == "0":
       print("prrogram closed")
       break





       