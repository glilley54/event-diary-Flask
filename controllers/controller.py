from flask import render_template, request
from app import app
from models.event_list import events
from models.event import Event


@app.route('/')
def index():
    return render_template('index.html', title = "Diary", events = events)