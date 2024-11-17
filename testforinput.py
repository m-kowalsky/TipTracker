import os
from datetime import datetime

now = datetime.now()
today = now.strftime('%Y/%m/%d')
month = now.strftime('%B')


folder_path = "/Users/michaelkowalsky/Desktop/Test folder for PP1"

# filename = input("What is the name of the file? ")
complete_path = os.path.join(folder_path, month + "_tips" + ".txt")
# complete_path = os.path.join(folder_path, filename + ".txt")
name = input("What is your name? ")


file1 = open(complete_path, "a")

file1.write(today + "\n\n\n")
file1.write(name + "\n\n\n")
file1.close()


