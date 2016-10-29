from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import time
import json
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'

app.secret_key = 'secret key'
db = SQLAlchemy(app)


def current_time():
    format = '%Y/%m/%d %H:%M:%S'
    value = time.localtime(int(time.time()))
    dt = time.strftime(format, value)
    return dt


class ModelHelper(object):
    def __repr__(self):
        classname = self.__class__.__name__
        properties = ['{}: ({})'.format(k, v) for k, v in self.__dict__.items()]
        s = '\n'.join(properties)
        return '< {}\n{} \n>\n'.format(classname, s)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Todo(ModelHelper, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String())
    created_time = db.Column(db.Integer, default=0)

    def __init__(self, form):
        self.task = form.get('task', '')
        self.created_time = current_time()

    def valid(self):
        return len(self.task) > 0

    def json(self):
        d = dict(
            id=self.id,
            task=self.task,
            created_time=self.created_time,
        )
        return json.dumps(d, ensure_ascii=False)

if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    print('rebuild database')