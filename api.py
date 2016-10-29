from flask import Blueprint
from flask import render_template
from flask import request
from flask import abort
from flask import redirect
from flask import url_for

from models import Todo


main = Blueprint('api', __name__)


@main.route('/todo/add', methods=['POST'])
def add():
    form =request.form
    t = Todo(form)
    if t.valid():
        t.save()
        return t.json()


@main.route('/todo/delete/<int:todo_id>', methods=['POST'])
def delete(todo_id):
    t = Todo.query.get(todo_id)
    t.delete()
    return t.json()


@main.route('/todo/update/<int:todo_id>', methods=['POST'])
def update(todo_id):
    t = Todo.query.get(todo_id)
    task = request.form.get('task', '')
    if len(task) > 0:
        t.task = task
        t.save()
    return t.json()
