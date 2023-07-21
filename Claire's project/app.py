from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    # Retrieve form data
    id = request.form['id']
    surname = request.form['surname']
    dateofres = request.form['dateofres']
    time_start = request.form['time_start']
    time_end = request.form['time_end']
    # Establish a connection to the PostgreSQL database
    conn = psycopg2.connect(
        host="localhost",
        database="matteoreservation",
        user="postgres",
        password="kler",
        port = "5432"
    )
    # Create a cursor object to interact with the database
    cur = conn.cursor()
    # Construct and execute the SQL query
    query = "INSERT INTO reservationscheds (id, surname, dateofres, time_start, time_end) VALUES (%s, %s, %s, %s, %s);"
    cur.execute(query, (id, surname, dateofres, time_start, time_end))
    # Commit the changes and close the database connection
    conn.commit()
    cur.close()
    conn.close()
    # Provide feedback to the user
    return "Form submitted successfully!"

@app.route('/')
def index():
    return render_template('welcome-page.html')

@app.route('/templates/about.html')
def about():
    redirect('about.html')
    return render_template('about.html')

@app.route('/templates/birds-eye.html')
def birds_eye():
    redirect('birds-eye.html')
    return render_template('birds-eye.html')

@app.route('/templates/my-reservations.html')
def my_reservations():
    redirect('my-reservations.html')
    return render_template('my-reservations.html')

@app.route('/templates/reserve-table.html')
def reserve_table():
    redirect('reserve-table.html')
    return render_template('reserve-table.html')

@app.route('/templates/cancel-reservation.html')
def cancel_reservation():
    redirect('cancel-reservation.html')
    return render_template('cancel-reservation.html')

if __name__ == '__main__':
    app.run(debug = True)
