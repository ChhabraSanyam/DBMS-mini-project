-- Drop tables if they exist to start fresh during development
DROP TABLE IF EXISTS Students;
DROP TABLE IF EXISTS Buses;
DROP TABLE IF EXISTS Route_Stops;
DROP TABLE IF EXISTS Bus_Stops;
DROP TABLE IF EXISTS Routes;

-- 1. Routes Table
CREATE TABLE Routes (
    Route_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Route_Name TEXT NOT NULL
);

-- 2. Bus_Stops Table
CREATE TABLE Bus_Stops (
    Stop_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Stop_Name TEXT NOT NULL,
    Location_Landmark TEXT
);

-- 3. Route_Stops (Junction Table for Many-to-Many relationship)
CREATE TABLE Route_Stops (
    Route_ID INTEGER,
    Stop_ID INTEGER,
    Stop_Sequence INTEGER NOT NULL,
    Estimated_Arrival_Time TEXT,
    PRIMARY KEY (Route_ID, Stop_ID),
    FOREIGN KEY (Route_ID) REFERENCES Routes(Route_ID) ON DELETE CASCADE,
    FOREIGN KEY (Stop_ID) REFERENCES Bus_Stops(Stop_ID) ON DELETE CASCADE
);

-- 4. Buses Table
CREATE TABLE Buses (
    Bus_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Registration_Number TEXT NOT NULL UNIQUE,
    Capacity INTEGER NOT NULL,
    Route_ID INTEGER,
    FOREIGN KEY (Route_ID) REFERENCES Routes(Route_ID) ON DELETE SET NULL
);

-- 5. Students Table
CREATE TABLE Students (
    Student_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Grade TEXT,
    Stop_ID INTEGER,
    FOREIGN KEY (Stop_ID) REFERENCES Bus_Stops(Stop_ID) ON DELETE SET NULL
);
