# Program #3 & #4: Phone Directory Program
# Programmer: Mai Lillie
# Date: 12/7/24

import sqlite3

# Set-Up
connection = sqlite3.connect("directory.db")
cursor = connection.cursor()

# Creates and fills the database
cursor.execute("create table directory (person_name text, phone_number text)")
phone_directory_list = [
    ("Mai Lillie", "612-500-5455"),
    ("Astarion Vampire", "656-457-6466")
]
cursor.executemany("insert into directory values (?,?)", phone_directory_list)

# Allows the user to pick what they wish to do
action = input("Would you like to read, update, or delete a row?: ")

# Allows the user to find a certain number
if action == "Read":
    person = input("Whose number would you like to find?: ")
    cursor.execute("select * from directory where person_name=:n", {"n": person})
    directory_search = cursor.fetchall()
    print(directory_search)

# Allows the user to change a number
elif action == "Update":
    person = input("Whose number would you like to change?: ")
    new_number = input("What is their new number?: ")
    cursor.execute("SELECT person_name From directory WHERE person_name = ?", (person,))
    cursor.execute("UPDATE directory SET phone_number = ? WHERE person_name = ?", (new_number, person))

    # Prints the new number and person
    cursor.execute("select * from directory where person_name=:n", {"n": person})
    directory_search = cursor.fetchall()
    print(directory_search)

# Allows the user to delete an item from the list
elif action == "Delete":
    person = input("Whose number would you like to delete?: ")
    cursor.execute("SELECT person_name From directory WHERE person_name = ?", (person,))
    cursor.execute("DELETE From directory WHERE person_name = ?", (person,))

    # Prints a confirmation statement
    print("Congrats, your person was wiped from the database!")

# Prints the information in the database
print("")
print("This is the database to prove that it was really changed.")
for row in cursor.execute("select * from directory"):
    print(row)

# Closes out the database
connection.close
