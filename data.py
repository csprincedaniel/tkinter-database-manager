import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()



def create_table():
    conn = psycopg2.connect(dbname=os.getenv("DB_NAME"), user=os.getenv("DB_USER"), password=os.getenv("DB_PASSWORD"), host=os.getenv("DB_HOST"), port=os.getenv("DB_PORT"))
    cur = conn.cursor()
    cur.execute("CREATE TABLE students(id serial primary key, name text, addrss text, age int, number text);")
    print("Student table created")
    conn.commit()

    conn.close()


def insert_data():
    #accept data from user
    name = input("Enter name: ")
    address = input("Enter address: ")
    age = input("Enter age: ")
    number = input("Enter number: ")
    conn = psycopg2.connect(dbname=os.getenv("DB_NAME"), user=os.getenv("DB_USER"), password=os.getenv("DB_PASSWORD"), host=os.getenv("DB_HOST"), port=os.getenv("DB_PORT"))
    cur = conn.cursor()
    cur.execute("INSERT into students(name, addrss, age, number) values(%s, %s, %s, %s)",(name, address, age, number))
    print("Data added to student table")
    conn.commit()
    conn.close()
    

#insert_data()

def update_data():
    conn = psycopg2.connect(dbname=os.getenv("DB_NAME"), user=os.getenv("DB_USER"), password=os.getenv("DB_PASSWORD"), host=os.getenv("DB_HOST"), port=os.getenv("DB_PORT"))
    cur = conn.cursor()

    id = input("Enter id of the student to be updated")
    fields = {
        "1":("name", "Enter the new name"),
        "2":("addrss", "Enter the new address"),
        "3":("name", "Enter the new name"),
        "4":("number", "Enter the new number"),
    }
    print("Which field would you like to update?")
    for key in fields:
        print(f"{key}:{fields[key][0]}")

    field_choice = input("Enter the number of the field you want to update:")

    if field_choice in fields:
        field_name, prompt = fields[field_choice]
        newvalue = input(prompt)
        sql = f"UPDATE STUDENTS set {field_name} = %s WHERE id= %s"
        cur.execute(sql, (newvalue, id))
        print(f"{field_name} updated successfully")
    else:
        print("This is an invalid choice")
    
    conn.commit()
    conn.close()

def delete_data():
    id = input("Enter ID of student you want to delete")
    conn = psycopg2.connect(dbname=os.getenv("DB_NAME"), user=os.getenv("DB_USER"), password=os.getenv("DB_PASSWORD"), host=os.getenv("DB_HOST"), port=os.getenv("DB_PORT"))
    cur = conn.cursor()

    cur.execute("SELECT * FROM students WHERE id=%s", (id))
    student = cur.fetchone()

    if student:
        print(f"Student to be deleted: ID {student[0]}, Name: {student[1]}, Address: {student[3]}, Number: {student[4]}")
        choice = input("Are you sure you want to delete the student? (yes/no)")
        if choice.lower() == "yes":
            cur.execute("DELETE FROM students WHERE id=%s", (id))
            print("Student record deleted")
        else:
            print("Deletion cancelled")
    else:
        print("Student not found")

    conn.commit()
    conn.close()

def read_data():
    conn = psycopg2.connect(dbname=os.getenv("DB_NAME"), user=os.getenv("DB_USER"), password=os.getenv("DB_PASSWORD"), host=os.getenv("DB_HOST"), port=os.getenv("DB_PORT"))
    cur = conn.cursor()

    cur.execute("SELECT * FROM students")

    students = cur.fetchall()

    for student in students:
        print(f"Student to be deleted: ID {student[0]}, Name: {student[1]}, Address: {student[3]}, Number: {student[4]}")


while True:
    print("\nWelcome to the student database management system.")
    print("1. Create Table")
    print("2. Insert Data")
    print("3. Read Data")
    print("4. Update Data")
    print("5. Delete Data")
    print("6. Exit")

    choice = input("Enter choic (1-6)")
    if choice == '1':
        create_table()
    elif choice=='2':
        insert_data()
    elif choice=='3':
        read_data()
    elif choice == '4':
        update_data()
    elif choice == '5':
        delete_data
    elif choice == '6':
        break
    else:
        print("Invalid choice, please enter a number between 0 and 6")
        