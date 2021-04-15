from models.event import *

event1 = Event('Football', 'Apr 15th', 6, 'Pub', 'Watch football with friends.', True)
event2 = Event('Party', 'Apr 16th', 20, 'Living Room', '30th Birthday Party', False)
events = [event1, event2]

def add_new_event(event):
    events.append(event)