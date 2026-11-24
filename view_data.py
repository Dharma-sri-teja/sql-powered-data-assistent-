import sqlite3

# Connect to database
connection = sqlite3.connect("students.db")

# Create cursor
cursor = connection.cursor()

# Retrieve all student records
cursor.execute("SELECT * FROM students")

# Fetch records
records = cursor.fetchall()

# Display records
print("STUDENT DATABASE")
print("-" * 50)
for record in records:
    print(record)

# Close connection
connection.close()
