from datetime import datetime
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@localhost/test_flash01'
    return app


mainApp = create_app()
db = SQLAlchemy(mainApp)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return '<Task %r>' % self.id


@mainApp.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'issue en tu cara'
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)


@mainApp.route('/delete/<int:id_key>')
def delete(id_key):
    task_to_delete = Todo.query.get_or_404(id_key)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return ' no delete'


@mainApp.route('/update/<int:id_key>', methods=['GET', 'POST'])
def update(id_key):
    task = Todo.query.get_or_404(id_key)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'pete en tu actu'
    else:
        return render_template("update.html", task=task)


if __name__ == "__main__":
    mainApp.run(debug=True)
