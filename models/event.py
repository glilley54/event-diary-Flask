class Event():

    def __init__(self, event_name, date, guests, room, description, recurring):
        self.event_name = event_name
        self.date = date
        self.guests = guests
        self.room = room
        self.description = description
        self.recurring = recurring
