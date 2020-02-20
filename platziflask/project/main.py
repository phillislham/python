# project/main.py
from flask import request, make_response, redirect, render_template, session, redirect, url_for, flash
from flask_login import login_required, current_user
import unittest 
from pprint import pprint

from app.services.firestore import get_users, get_todos, put_todo, delete_todo, update_todo

# from folder-app import __init__.py.def create_app
from app import create_app
from app.forms.forms import TodoForm, DeleteTodoForm, UpdateTodoForm

app = create_app()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/todo-list",methods=["GET","POST"])
@login_required
def todo_list():
    user_ip = session.get("user_ip")
    username = current_user.id
    todoform = TodoForm()
    deleteform = DeleteTodoForm()
    updateform = UpdateTodoForm()

    context = {
        "user_ip":user_ip,
        "todos":get_todos(userid=username),
        "username":username,
        "todoform":todoform,
        "deleteform":deleteform,
        "updateform": updateform
    }

    if todoform.validate_on_submit():
        put_todo(userid=username,description=todoform.description.data)
        flash("tu tarea se creó con éxito")
        return redirect(url_for("todo-list"))
  
    # spread operator
    return render_template("todo-list.html",**context)

@app.route("/todos/delete/<todoid>",methods=["POST"])
def delete(todoid):
    userid = current_user.id
    delete_todo(userid=userid,todoid=todoid)
    return redirect(url_for("todo-list"))

@app.route("/todos/update/<todoid>/<int:done>",methods=["POST"])
def update(todoid, done):
    userid = current_user.id
    update_todo(userid=userid,todoid=todoid,done=done)
    return redirect(url_for("todo-list"))

@app.errorhandler(404)
def not_found(error):
    return render_template("404.html",error=error)

@app.errorhandler(500)
def not_found(error):
    return render_template("500.html",error=error)

# se llamara con: flask test
@app.cli.command()
def test():
    import werkzeug
    werkzeug.cached_property = werkzeug.utils.cached_property
    # todo lo que este en la carpeta de project/test se ejecutara
    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner().run(tests)