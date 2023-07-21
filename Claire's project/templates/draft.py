from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__, template_folder='.')

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
        password="kler"
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
    return render_template('form.html')

if __name__ == '__main__':
    app.run(port=5000)
