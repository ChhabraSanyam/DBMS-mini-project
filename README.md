# DBMS Mini Project Report: School Transport Route Database

**Domain:** School Transport Management  
**Focus:** Many-to-Many Routing Relations  
**Student Name:** Sanyam Chhabra  
**Group:** 4I7  

---

## 1. Introduction
The School Transport Route Database is designed to manage buses, routes, stops, and students effectively. The core challenge addressed in this project is the **Many-to-Many relationship** between Routes and Bus Stops:
*   A single **Route** consists of multiple **Bus Stops**.
*   A single **Bus Stop** can be a part of multiple **Routes** (e.g., a central hub or the school main gate).

## 2. Objectives
*   To design a normalized relational database schema.
*   To implement and resolve Many-to-Many (M:N) relationships using junction tables.
*   To provide a web-based interface for easy data visualization and management.

## 3. Entity-Relationship

*   **Entities:**
    *   **Student:** (Student_ID, Name, Grade)
    *   **Route:** (Route_ID, Route_Name)
    *   **Bus_Stop:** (Stop_ID, Stop_Name, Landmark)
    *   **Bus:** (Bus_ID, Registration_No, Capacity)
*   **Relationships:**
    *   **Student boards at Bus_Stop:** Many-to-One (N:1)
    *   **Bus assigned to Route:** Many-to-One (N:1) - *assuming one bus per route*
    *   **Route includes Bus_Stop:** Many-to-Many (M:N) -> Resolved via **Route_Stops** table.

## 4. Data Dictionary

| Table | Column | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- | :--- |
| **Routes** | `Route_ID` | INTEGER | PK, Auto-inc | Unique identifier for a route |
| **Routes** | `Route_Name` | TEXT | NOT NULL | Name of the route (e.g., North-1) |
| **Bus_Stops** | `Stop_ID` | INTEGER | PK, Auto-inc | Unique identifier for a bus stop |
| **Bus_Stops** | `Stop_Name` | TEXT | NOT NULL | Name of the physical stop |
| **Bus_Stops** | `Location_Landmark`| TEXT | | Nearby landmark for identification |
| **Route_Stops**| `Route_ID` | INTEGER | FK, Comp. PK | Link to Routes table |
| **Route_Stops**| `Stop_ID` | INTEGER | FK, Comp. PK | Link to Bus_Stops table |
| **Route_Stops**| `Stop_Sequence` | INTEGER | NOT NULL | Order of the stop in the route |
| **Route_Stops**| `Estimated_Arrival_Time`| TEXT | | Arrival time for that specific stop |
| **Buses** | `Bus_ID` | INTEGER | PK, Auto-inc | Unique identifier for a bus |
| **Buses** | `Registration_Number`| TEXT | UNIQUE, NOT NULL | Vehicle registration plate |
| **Buses** | `Route_ID` | INTEGER | FK | The route this bus is assigned to |
| **Students** | `Student_ID` | INTEGER | PK, Auto-inc | Unique identifier for a student |
| **Students** | `Name` | TEXT | NOT NULL | Full name of the student |
| **Students** | `Stop_ID` | INTEGER | FK | The stop where the student boards |

## 5. Relational Schema & Normalization
The database is designed in **Third Normal Form (3NF)**:

*   **1st Normal Form (1NF):** All attributes are atomic (single-valued), and there are no repeating groups of columns. Each record is unique via its Primary Key.
*   **2nd Normal Form (2NF):** It is in 1NF, and all non-key attributes are fully functionally dependent on the primary key. In the `Route_Stops` junction table, the sequence and arrival time depend on the combination of both `Route_ID` and `Stop_ID` (Composite Primary Key).
*   **3rd Normal Form (3NF):** It is in 2NF, and there are no transitive dependencies. For example, student details like `Name` depend only on `Student_ID`, not on `Stop_ID`. Similarly, stop landmarks depend only on `Stop_ID`.

## 6. Implementation Details
*   **Database:** SQLite
*   **Backend:** Python (Flask)
*   **Frontend:** HTML/CSS

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

## 7. Conclusion
The project successfully demonstrates the handling of complex routing logic in a school environment. By using a junction table (`Route_Stops`), we efficiently managed overlapping routes and stop sequences, ensuring data integrity and reducing redundancy.
