from flask import Flask, render_template, request, session, redirect, flash, jsonify
import pymongo
import os
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from chatbot import chatbot

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.static_folder = 'static'


MONGO_URI = "mongodb+srv://vitinternstudent:YnO3X6dkSIGezvGS@cluster0.7phru.mongodb.net"

client = pymongo.MongoClient(MONGO_URI)
db = client["register"]  
users_collection = db["users"]  

@app.route('/')
def login():
    return render_template("login.html")

@app.route("/index")
def home():
    if 'id' in session:
        return render_template('index.html')
    else:
        return redirect('/')


@app.route('/register')
def about():
    return render_template('register.html')

@app.route('/forgot')
def forgot():
    return render_template('forgot.html')


@app.route("/login_validation", methods=['POST'])
def login_validation():
    email = request.form.get('email')
    password = request.form.get('password')

    
    user = users_collection.find_one({"email": email})

    if user and check_password_hash(user["password"], password):  
        session['id'] = str(user["_id"])  
        flash('You were successfully logged in')
        return redirect('/index')
    else:
        flash('Invalid credentials !!!')
        return redirect('/')


@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form.get('name')
    email = request.form.get('uemail')
    password = request.form.get('upassword')

   
    if users_collection.find_one({"email": email}):
        flash("Email already registered! Try logging in.")
        return redirect('/register')

    new_user = {"name": name, "email": email, "password": password}
    users_collection.insert_one(new_user)
    
    flash('You have successfully registered!')
    return redirect('/')


@app.route('/reset_password', methods=['POST'])
def reset_password():
    data = request.form

    email = data.get('uemail')
    new_password = data.get('upassword')

    if not email or not new_password:
        return jsonify({"error": "Email and Password are required"}), 400


    user = users_collection.find_one({"email": email})
    if not user:
        return jsonify({"error": "User not found"}), 404

   
    hashed_password = generate_password_hash(new_password)

  
    users_collection.update_one({"email": email}, {"$set": {"password": hashed_password}})

    flash('Password updated successfully. Please login with your new password.')
    return redirect('/')

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')  
    return str(chatbot.get_response(userText))


@app.route('/logout')
def logout():
    session.pop('id', None)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
