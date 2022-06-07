import sqlite3
from staff_class import Staff
from area_class import Area

conn = sqlite3.connect('Staff.db')
c = conn.cursor()

staff_list = []
area_list = []

def add_staff():
    number_of_staff = int(input("How many staff members are there? "))
    for i in range(number_of_staff):
        staff_id = int(input("Enter the staff ID: "))
        first_name = input("Enter the first name of the staff member: ")
        last_name = input("Enter the last name of the staff member: ")
        area = input("Enter the area of the staff member: ")
        staff_list.append(Staff(staff_id,first_name, last_name, area))

def add_area():
    number_of_areas = int(input("How many areas are there? "))
    for i in range(number_of_areas):
        name = input("Enter the name of the area: ")
        staff_id = int(input("Enter the ID of staff member alocated : "))
        area_list.append(Area(name, staff_id))

add_staff()
add_area()

for person in staff_list:
    c.execute("""INSERT INTO Staff VALUES(?, ?, ?, ?)""",
            (person.staff_id, person.first_name, person.last_name, person.area))

for area in area_list:
    c.execute("""INSERT INTO Areas VALUES(?, ?)""",
            (area.name, area.staff_id))

conn.commit()
conn.close()