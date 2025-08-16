import sqlite3

# 1
conn = sqlite3.connect("homework.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS Roster")
cursor.execute("""
CREATE TABLE Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")

# 2
roster_data = [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
]

cursor.executemany("INSERT INTO Roster VALUES (?, ?, ?)", roster_data)

# 3
cursor.execute("""
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax'
""")

# 4
cursor.execute("""
SELECT Name, Age
FROM Roster
WHERE Species = 'Bajoran'
""")

results = cursor.fetchall()
print("Bajoran bo‘lganlar:")
for row in results:
    print(row)

conn.commit()
conn.close()
