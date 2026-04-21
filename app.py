import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('transport.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    route_count = conn.execute('SELECT COUNT(*) FROM Routes').fetchone()[0]
    bus_count = conn.execute('SELECT COUNT(*) FROM Buses').fetchone()[0]
    student_count = conn.execute('SELECT COUNT(*) FROM Students').fetchone()[0]
    conn.close()
    return render_template('index.html', route_count=route_count, bus_count=bus_count, student_count=student_count)

@app.route('/routes')
def routes():
    conn = get_db_connection()
    routes = conn.execute('SELECT * FROM Routes').fetchall()
    conn.close()
    return render_template('routes.html', routes=routes)

@app.route('/route/<int:route_id>')
def route_details(route_id):
    conn = get_db_connection()
    route = conn.execute('SELECT * FROM Routes WHERE Route_ID = ?', (route_id,)).fetchone()
    # M:N Query: Get all stops for a specific route
    stops = conn.execute('''
        SELECT s.Stop_ID, s.Stop_Name, s.Location_Landmark, rs.Stop_Sequence, rs.Estimated_Arrival_Time
        FROM Bus_Stops s
        JOIN Route_Stops rs ON s.Stop_ID = rs.Stop_ID
        WHERE rs.Route_ID = ?
        ORDER BY rs.Stop_Sequence
    ''', (route_id,)).fetchall()
    conn.close()
    return render_template('route_details.html', route=route, stops=stops)

@app.route('/stops')
def stops():
    conn = get_db_connection()
    stops = conn.execute('SELECT * FROM Bus_Stops').fetchall()
    conn.close()
    return render_template('stops.html', stops=stops)

@app.route('/stop/<int:stop_id>')
def stop_details(stop_id):
    conn = get_db_connection()
    stop = conn.execute('SELECT * FROM Bus_Stops WHERE Stop_ID = ?', (stop_id,)).fetchone()
    # M:N Query: Get all routes that pass through a specific stop
    routes = conn.execute('''
        SELECT r.Route_ID, r.Route_Name, rs.Stop_Sequence, rs.Estimated_Arrival_Time
        FROM Routes r
        JOIN Route_Stops rs ON r.Route_ID = rs.Route_ID
        WHERE rs.Stop_ID = ?
    ''', (stop_id,)).fetchall()
    
    # Get students at this stop
    students = conn.execute('SELECT * FROM Students WHERE Stop_ID = ?', (stop_id,)).fetchall()
    conn.close()
    return render_template('stop_details.html', stop=stop, routes=routes, students=students)

@app.route('/students', methods=['GET', 'POST'])
def students():
    conn = get_db_connection()
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        stop_id = request.form['stop_id']
        conn.execute('INSERT INTO Students (Name, Grade, Stop_ID) VALUES (?, ?, ?)', (name, grade, stop_id))
        conn.commit()
        conn.close()
        return redirect(url_for('students'))
    
    students = conn.execute('''
        SELECT s.*, b.Stop_Name 
        FROM Students s 
        LEFT JOIN Bus_Stops b ON s.Stop_ID = b.Stop_ID
    ''').fetchall()
    stops = conn.execute('SELECT * FROM Bus_Stops').fetchall()
    conn.close()
    return render_template('students.html', students=students, stops=stops)

if __name__ == '__main__':
    app.run(debug=True)
