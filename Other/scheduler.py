import calendar
from tkinter import *
from tkcalendar import *

root = Tk()
root.title('Schedule')

cal = Calendar(root, selectmode="day", year=2022, month=3, day=8)
cal.pack(pady=20)

def grab_date():
  label1.config(text=cal.get_date())

button1 = Button(root, text="Get date", command="grab_date")
button1.pack(pady=20)

label1 = Label(root, text="")
label1.pack(pady=20)

class Event:
  def __init__(self, title, date, time, duration, reminder):
    self.title = title
    self.date = date
    self.time = time
    self.duration = duration
    self.reminder = reminder
    # Repeats
    # Location
    # List of people
    # Color
    # Attachment

  def display(self):
    print(self.title)
    print(self.date + ", " + self.time)
    print(str(self.duration) + " hour(s)")
    print("Has a reminder: " + str(self.reminder))

  def get_title(self):
    return self.title
  def get_date(self):
    return self.date
  def get_time(self):
    return self.time
  def get_duration(self):
    return self.duration
  def get_reminder(self):
    return self.reminder

  def set_title(self, title):
    self.title = title
  def set_date(self, date):
    self.date = date
  def set_time(self, time):
    self.time = time
  def set_duration(self, duration):
    self.duration = duration
  def set_reminder(self, reminder):
    self.reminder = reminder

event1 = Event("Dinner", "January 4", "6pm", 1, True)
event1.display()

print("Hello World")

# input_title = input("Enter an event title: ")
# input_date = input("Enter an event date: ")
# input_time = input("Enter an event time: ")
# input_duration = input("Event duration in hours: ")
# input_reminder = input("Do you want a reminder: ")
# event2 = Event(input_title, input_date, input_time, input_duration, input_reminder)
# event2.display()

# print(calendar.prcal(2022))