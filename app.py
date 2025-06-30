import os
from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, UTC


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=lambda: datetime.now(UTC))

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content) #type: ignore

        #attempt to add a new task
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')

        #if a new task couldn't be added
        except:
            return "There was a problem adding your task."

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_del = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_del)
        db.session.commit()
        return redirect('/')
    except:
        return "There was a problem deleting your task"

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "There was a problem updating your task"

    else:
        return render_template('update.html', task = task)

#checks if the app runs properly
@app.route("/health")
def health():
    return "OK", 200


if __name__ == "__main__":
    db_path = os.path.join(os.path.dirname(__file__), 'instance', 'test.db')
    if not os.path.exists(db_path):
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        with app.app_context():
            db.create_all()
            print("Database created.")

    app.run(host='0.0.0.0', debug=True)
