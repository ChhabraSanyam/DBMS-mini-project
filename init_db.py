import sqlite3

def init_db():
    connection = sqlite3.connect('transport.db')
    
    with open('schema.sql') as f:
        connection.executescript(f.read())
        
    cur = connection.cursor()
    
    # Insert Routes
    cur.execute("INSERT INTO Routes (Route_Name) VALUES (?)", ('Route A (North)',))
    cur.execute("INSERT INTO Routes (Route_Name) VALUES (?)", ('Route B (South)',))
    cur.execute("INSERT INTO Routes (Route_Name) VALUES (?)", ('Route C (Central Express)',))
    
    # Insert Bus Stops
    cur.execute("INSERT INTO Bus_Stops (Stop_Name, Location_Landmark) VALUES (?, ?)", ('Main Gate', 'School Entrance'))
    cur.execute("INSERT INTO Bus_Stops (Stop_Name, Location_Landmark) VALUES (?, ?)", ('Green Park', 'Near Public Library'))
    cur.execute("INSERT INTO Bus_Stops (Stop_Name, Location_Landmark) VALUES (?, ?)", ('City Center', 'Metro Station Exit 2'))
    cur.execute("INSERT INTO Bus_Stops (Stop_Name, Location_Landmark) VALUES (?, ?)", ('Oak Street', 'Corner Bakery'))
    cur.execute("INSERT INTO Bus_Stops (Stop_Name, Location_Landmark) VALUES (?, ?)", ('Riverside', 'Boat Club'))
    
    # Insert Many-to-Many Relationships (Route_Stops)
    # Route A: Main Gate (1), Green Park (2), City Center (3)
    cur.execute("INSERT INTO Route_Stops (Route_ID, Stop_ID, Stop_Sequence, Estimated_Arrival_Time) VALUES (?, ?, ?, ?)", (1, 1, 1, '07:00 AM'))
    cur.execute("INSERT INTO Route_Stops (Route_ID, Stop_ID, Stop_Sequence, Estimated_Arrival_Time) VALUES (?, ?, ?, ?)", (1, 2, 2, '07:15 AM'))
    cur.execute("INSERT INTO Route_Stops (Route_ID, Stop_ID, Stop_Sequence, Estimated_Arrival_Time) VALUES (?, ?, ?, ?)", (1, 3, 3, '07:30 AM'))
    
    # Route B: Main Gate (1), Oak Street (2), Riverside (3)
    cur.execute("INSERT INTO Route_Stops (Route_ID, Stop_ID, Stop_Sequence, Estimated_Arrival_Time) VALUES (?, ?, ?, ?)", (2, 1, 1, '07:00 AM'))
    cur.execute("INSERT INTO Route_Stops (Route_ID, Stop_ID, Stop_Sequence, Estimated_Arrival_Time) VALUES (?, ?, ?, ?)", (2, 4, 2, '07:20 AM'))
    cur.execute("INSERT INTO Route_Stops (Route_ID, Stop_ID, Stop_Sequence, Estimated_Arrival_Time) VALUES (?, ?, ?, ?)", (2, 5, 3, '07:45 AM'))

    # Route C (Demonstrating overlap): City Center (1), Oak Street (2), Main Gate (3)
    # This shows City Center and Oak Street are shared between routes
    cur.execute("INSERT INTO Route_Stops (Route_ID, Stop_ID, Stop_Sequence, Estimated_Arrival_Time) VALUES (?, ?, ?, ?)", (3, 3, 1, '08:00 AM'))
    cur.execute("INSERT INTO Route_Stops (Route_ID, Stop_ID, Stop_Sequence, Estimated_Arrival_Time) VALUES (?, ?, ?, ?)", (3, 4, 2, '08:15 AM'))
    cur.execute("INSERT INTO Route_Stops (Route_ID, Stop_ID, Stop_Sequence, Estimated_Arrival_Time) VALUES (?, ?, ?, ?)", (3, 1, 3, '08:30 AM'))
    
    # Insert Buses
    cur.execute("INSERT INTO Buses (Registration_Number, Capacity, Route_ID) VALUES (?, ?, ?)", ('BUS-001', 40, 1))
    cur.execute("INSERT INTO Buses (Registration_Number, Capacity, Route_ID) VALUES (?, ?, ?)", ('BUS-002', 40, 2))
    cur.execute("INSERT INTO Buses (Registration_Number, Capacity, Route_ID) VALUES (?, ?, ?)", ('BUS-003', 30, 3))
    
    # Insert Students
    cur.execute("INSERT INTO Students (Name, Grade, Stop_ID) VALUES (?, ?, ?)", ('Alice Johnson', '10th', 2))
    cur.execute("INSERT INTO Students (Name, Grade, Stop_ID) VALUES (?, ?, ?)", ('Bob Smith', '8th', 3))
    cur.execute("INSERT INTO Students (Name, Grade, Stop_ID) VALUES (?, ?, ?)", ('Charlie Brown', '12th', 4))
    cur.execute("INSERT INTO Students (Name, Grade, Stop_ID) VALUES (?, ?, ?)", ('Daisy Miller', '9th', 5))
    
    connection.commit()
    connection.close()
    print("Database initialized successfully with sample data.")

if __name__ == '__main__':
    init_db()
