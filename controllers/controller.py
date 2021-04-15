from flask import render_template, request
from app import app
from models.event_list import events, add_new_event
from models.event import Event


@app.route('/')
def index():
    return render_template('index.html', title = "Diary", events = events)

@app.route('/', methods = ['POST'])
def add_event():
    new_name = request.form['event_name']
    new_date = request.form['date']
    new_guests = request.form['guests']
    new_room = request.form['room']
    new_description = request.form['description']
    new_recurring = False
    if 'recurring' in request.form:
        new_recurring = True
    new_event = Event(new_name, new_date, new_guests, new_room, new_description, new_recurring)
    add_new_event(new_event)

    return render_template('index.html', title="Diary", events=events)
