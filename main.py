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

    conn = psycopg2.connect(dbname=os.getenv("DB_NAME"), user=os.getenv("DB_USER"), password=os.getenv("DB_PASSWORD"), host=os.getenv("DB_HOST"), port=os.getenv("DB_PORT"))
    cur = conn.cursor()

    cur.execute("UPDATE students SET name =%s, addrss=%s, age=%s,number=%s WHERE id=%s ",(name, address, age, number, id))
   
    conn.commit()
    conn.close()

update_data()