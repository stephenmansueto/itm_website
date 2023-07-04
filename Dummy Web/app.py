from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200), nullable = False)
    completed = db.Column(db.Integer, default = 0)
    time_from = db.Column(db.DateTime, default =0)
    time_to = db.Column(db.DateTime, default = 0)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/templates/room_c.html', methods =['POST', 'GET'])
def room_c():

    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/templates/room_c.html')
        
        except:
            return "There was an issue adding your task"

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('room_c.html', tasks=tasks)

@app.route('/templates/room_d.html')
def room_d():
    redirect('/templates/room_d.html')
    return render_template('room_d.html')

@app.route('/templates/C1.html')
def C1():
    redirect('/C1.html')
    return render_template('C1.html')

@app.route('/templates/C2.html')
def C2():
    redirect('C2.html')
    return render_template('C2.html')

@app.route('/templates/C3.html')
def C3():
    redirect('/C3.html')
    return render_template('C3.html')

@app.route('/templates/C4.html')
def C4():
    redirect('/C4.html')
    return render_template('C4.html')

@app.route('/templates/C5.html')
def C5():
    redirect('/C5.html')
    return render_template('C5.html')

@app.route('/templates/C6.html')
def C6():
    redirect('/C6.html')
    return render_template('C6.html')

@app.route('/templates/C7.html')
def C7():
    redirect('/C7.html')
    return render_template('C7.html')

@app.route('/templates/C8.html')
def C8():
    redirect('/C8.html')
    return render_template('C8.html')

@app.route('/templates/C9.html')
def C9():
    redirect('/C9.html')
    return render_template('C9.html')

@app.route('/templates/C10.html')
def C10():
    redirect('/C10.html')
    return render_template('C10.html')

@app.route('/templates/C11.html')
def C11():
    redirect('/C11.html')
    return render_template('C11.html')

@app.route('/templates/C12.html')
def C12():
    redirect('/C12.html')
    return render_template('C12.html')

@app.route('/templates/C13.html')
def C13():
    redirect('/C13.html')
    return render_template('C13.html')

@app.route('/templates/C14.html')
def C14():
    redirect('/C14.html')
    return render_template('C14.html')

@app.route('/templates/C15.html')
def C15():
    redirect('/C15.html')
    return render_template('C15.html')

@app.route('/templates/D1.html')
def D1():
    redirect('/D1.html')
    return render_template('D1.html')

@app.route('/templates/D2.html')
def D2():
    redirect('/D2.html')
    return render_template('D2.html')

@app.route('/templates/D3.html')
def D3():
    redirect('/D3.html')
    return render_template('D3.html')

@app.route('/templates/D4.html')
def D4():
    redirect('/D4.html')
    return render_template('D4.html')

@app.route('/templates/D5.html')
def D5():
    redirect('/D5.html')
    return render_template('D5.html')

@app.route('/templates/D6.html')
def D6():
    redirect('/D6.html')
    return render_template('D6.html')

@app.route('/templates/D7.html')
def D7():
    redirect('/D7.html')
    return render_template('D7.html')

@app.route('/templates/D8.html')
def D8():
    redirect('/D8.html')
    return render_template('D8.html')

@app.route('/templates/D9.html')
def D9():
    redirect('/D9.html')
    return render_template('D9.html')

@app.route('/templates/D10.html')
def D10():
    redirect('/D10.html')
    return render_template('D10.html')

@app.route('/templates/D11.html')
def D11():
    redirect('/D11.html')
    return render_template('D11.html')

@app.route('/templates/D12.html')
def D12():
    redirect('/D12.html')
    return render_template('D12.html')

@app.route('/templates/D13.html')
def D13():
    redirect('/D13.html')
    return render_template('D13.html')

if __name__ == "__main__":
    app.run(debug = True)