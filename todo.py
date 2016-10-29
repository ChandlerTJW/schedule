from flask import Blueprint
from flask import render_template
from flask import request
from flask import abort
from flask import redirect
from flask import url_for

from models import Todo


main = Blueprint('todo', __name__)


@main.route('/')
def index():
    todos = Todo.query.all()
    return render_template('index.html', ts=todos)


@main.route('/todo/add', methods=['POST'])
def add():
    form =request.form
    t = Todo(form)
    if t.valid():
        t.save()
        return redirect(url_for('.index'))
    else:
        abort(400)


@main.route('/todo/delete/<int:todo_id>')
def delete(todo_id):
    t = Todo.query.get(todo_id)
    print('debug delete', t)
    t.delete()
    return redirect(url_for('.index'))


@main.route('/todo/edit/<int:todo_id>')
def edit(todo_id):
    t = Todo.query.get(todo_id)
    return render_template('todo_edit.html', todo=t)


@main.route('/todo/update/<int:todo_id>', methods=['POST'])
def update(todo_id):
    t = Todo.query.get(todo_id)
    task = request.form.get('task', '')
    print('debug update', task)
    if len(task) > 0:
        t.task = task
        t.save()
    return redirect(url_for('.index'))
