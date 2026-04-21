# DBMS Mini Project Report: School Transport Route Database

**Domain:** School Transport Management  
**Focus:** Many-to-Many Routing Relations  
**Student Name:** [Your Name]  
**Class:** B.Tech IT 2nd Year  

---

## 1. Introduction
The School Transport Route Database is designed to manage buses, routes, stops, and students effectively. The core challenge addressed in this project is the **Many-to-Many relationship** between Routes and Bus Stops:
*   A single **Route** consists of multiple **Bus Stops**.
*   A single **Bus Stop** can be a part of multiple **Routes** (e.g., a central hub or the school main gate).

## 2. Objectives
*   To design a normalized relational database schema.
*   To implement and resolve Many-to-Many (M:N) relationships using junction tables.
*   To provide a web-based interface for easy data visualization and management.

## 3. Entity-Relationship (ER) Diagram
*(Note: You can use tools like Draw.io or Lucidchart to draw this based on the description below)*

*   **Entities:**
    *   **Student:** (Student_ID, Name, Grade)
    *   **Route:** (Route_ID, Route_Name)
    *   **Bus_Stop:** (Stop_ID, Stop_Name, Landmark)
    *   **Bus:** (Bus_ID, Registration_No, Capacity)
*   **Relationships:**
    *   **Student boards at Bus_Stop:** Many-to-One (N:1)
    *   **Bus assigned to Route:** Many-to-One (N:1) - *assuming one bus per route*
    *   **Route includes Bus_Stop:** Many-to-Many (M:N) -> Resolved via **Route_Stops** table.

## 4. Relational Schema & Normalization
The database is designed in **Third Normal Form (3NF)**:
1.  **1NF:** All attributes are atomic; no repeating groups.
2.  **2NF:** All non-key attributes are fully functional dependent on the primary key.
3.  **3NF:** There are no transitive dependencies (e.g., Student depends on Stop, but Stop details are in a separate table).

### Tables:
*   `Routes` (`Route_ID`, `Route_Name`)
*   `Bus_Stops` (`Stop_ID`, `Stop_Name`, `Location_Landmark`)
*   `Route_Stops` (`Route_ID`, `Stop_ID`, `Stop_Sequence`, `Estimated_Arrival_Time`)
*   `Buses` (`Bus_ID`, `Registration_Number`, `Capacity`, `Route_ID`)
*   `Students` (`Student_ID`, `Name`, `Grade`, `Stop_ID`)

## 5. Implementation Details
*   **Database:** SQLite
*   **Backend:** Python (Flask)
*   **Frontend:** HTML/CSS (Jinja2)

### Key SQL Queries (M:N Highlight):
**Find all stops for a specific route:**
```sql
SELECT s.Stop_Name, rs.Stop_Sequence, rs.Estimated_Arrival_Time
FROM Bus_Stops s
JOIN Route_Stops rs ON s.Stop_ID = rs.Stop_ID
WHERE rs.Route_ID = [ROUTE_ID]
ORDER BY rs.Stop_Sequence;
```

**Find all routes passing through a specific stop:**
```sql
SELECT r.Route_Name, rs.Stop_Sequence
FROM Routes r
JOIN Route_Stops rs ON r.Route_ID = rs.Route_ID
WHERE rs.Stop_ID = [STOP_ID];
```

## 6. Conclusion
The project successfully demonstrates the handling of complex routing logic in a school environment. By using a junction table (`Route_Stops`), we efficiently managed overlapping routes and stop sequences, ensuring data integrity and reducing redundancy.
