from flask import Flask, render_template
import pymongo

app = Flask(__name__)


client = pymongo.MongoClient("mongodb+srv://puteri:12345put@clusters.otuvw.mongodb.net/systemuser?retryWrites=true&w=majority")
db = client.systemuser

#Routes
from user import routes

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')