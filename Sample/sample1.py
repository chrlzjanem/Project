import tkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector
from mysql.connector import Error


root = Tk()
root.title("Add Info")

try:
    # Establish a database connection
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',  # Add your MySQL password here if needed
        port='3306',
        database='dbl'
    )

    if connection.is_connected():
        c = connection.cursor()

        bkg = "#636e72"
        
        frame = tk.Frame(root, bg=bkg)

        label_firstname = tk.Label(frame, text="First Name: ", font=('verdana',12), bg=bkg)
        entry_firstname = tk.Entry(frame, font=('verdana',12))

        label_lastname = tk.Label(frame, text="Last Name: ", font=('verdana',12), bg=bkg)
        entry_lastname = tk.Entry(frame, font=('verdana',12))

        label_email = tk.Label(frame, text="Email: ", font=('verdana',12), bg=bkg)
        entry_email = tk.Entry(frame, font=('verdana',12))

        label_age = tk.Label(frame, text="Age: ", font=('verdana',12), bg=bkg)
        entry_age = tk.Entry(frame, font=('verdana',12))

        label_address = tk.Label(frame, text="Address: ", font=('verdana',12), bg=bkg)
        entry_address = tk.Entry(frame, font=('verdana',12))

        label_contactnumber = tk.Label(frame, text="Contact Number: ", font=('verdana',12), bg=bkg)
        entry_contactnumber = tk.Entry(frame, font=('verdana',12))

        def insertData():
            firstname = entry_firstname.get()
            lastname = entry_lastname.get()
            email = entry_email.get()
            age = entry_age.get()
            address = entry_address.get()
            contactnumber = entry_contactnumber.get()

            if not (firstname and lastname and email and age, address, contactnumber):
                print("All fields must be filled!")
                return

            try:
                insert_query = """
                INSERT INTO tblinfo (firstname, lastname, email, age, address, contactnumber) 
                VALUES (%s, %s, %s, %s, %s, %s)
                """
                vals = (firstname, lastname, email, age, address, contactnumber)
                c.execute(insert_query, vals)
                connection.commit()
                print("Data inserted successfully")
            except Error as e:
                print(f"Error inserting data: {e}")

        button_insert = tk.Button(frame, text="ADD", fg="White",  font=('verdana',14), bg='Black',
                                  command=insertData)

        label_firstname.grid(row=0, column=0)
        entry_firstname.grid(row=0, column=1, pady=10, padx=10)

        label_lastname.grid(row=1, column=0)
        entry_lastname.grid(row=1, column=1, pady=10, padx=10)

        label_email.grid(row=2, column=0, sticky='e')
        entry_email.grid(row=2, column=1, pady=10, padx=10)

        label_age.grid(row=3, column=0, sticky='e')
        entry_age.grid(row=3, column=1, pady=10, padx=10)

        label_address.grid(row=4, column=0, sticky='e')
        entry_address.grid(row=4, column=1, pady=10, padx=10)

        label_contactnumber.grid(row=5, column=0, sticky='e')
        entry_contactnumber.grid(row=5, column=1, pady=10, padx=10)

        button_insert.grid(row=6, column=0, columnspan=2, pady=10, padx=10, sticky='nsew')

        frame.grid(row=0, column=0)

except Error as e:
    print(f"Error connecting to MySQL: {e}")
finally:
    root.mainloop()

    # Close the connection when the app is closed
    if connection.is_connected():
        c.close()
        connection.close()
        print("MySQL connection closed")
