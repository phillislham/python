# project/main.py
from flask import Flask, request, make_response, redirect, render_template, session
from flask_bootstrap import Bootstrap


app = Flask(__name__)

bootstrap = Bootstrap(app)

# con esto se cifra la info de la cookie
# esto habria que cambiarlo a un hash más seguro, para el ejemplo nos vale
app.config["SECRET_KEY"] = "super secreto"


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html",error=error)

@app.errorhandler(500)
def not_found(error):
    return render_template("500.html",error=error)

@app.route("/")
def index():
    user_ip = request.remote_addr
    response = make_response(redirect("/hello"))
    # response.set_cookie("user_ip",user_ip+" :) ")
    session["user_ip"] = user_ip
    return response

todos = ["Comprar cafe","Enviar solicitud","Entregar video"]

@app.route("/hello")
def hello():
    # userip = request.cookies.get("user_ip")
    user_ip = session.get("user_ip")
    context = {
        "user_ip":user_ip,
        "todos":todos
    }
    # spread operator
    return render_template("hello.html",**context)