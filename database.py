import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect("students.db")

# Create a cursor
cursor = connection.cursor()

# Create students table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    marks INTEGER NOT NULL,
    age INTEGER
)
""")

# Insert sample student records
students = [
    ("Rahul", "CSE", 85, 21),
    ("Priya", "AIML", 92, 20),
    ("Arjun", "CSE", 76, 22),
    ("Sneha", "AIML", 88, 21),
    ("Kiran", "ECE", 79, 20),
    ("Divya", "AIML", 95, 22),
]

cursor.executemany("""
INSERT INTO students (name, department, marks, age)
VALUES (?, ?, ?, ?)
""", students)

# Save changes
connection.commit()

# Close connection
connection.close()

print("Database and student table created successfully!")
