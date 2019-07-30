import os
import webbrowser
from flask import Flask, render_template, redirect, request, session, flash
import subprocess
from subprocess import Popen, PIPE

app = Flask(__name__)    

# HOME
@app.route('/')          
def index():
    return render_template("index.html")

# OPEN MAIL & CALENDAR
@app.route("/mailCalendar")
def openMailCalendar():
    subprocess.Popen("/Applications/Mail.app/Contents/MacOS/Mail") 
    subprocess.Popen("/Applications/Calendar.app/Contents/MacOS/Calendar")
    return redirect("/")

# OPEN MAIL & CALENDAR
@app.route("/google")
def openBrowserGoogle():
    webbrowser.open("https://google.com")
    return redirect("/")

# OPEN TOUCH ID
@app.route('/touchId')
def openTouchId():
    subprocess.Popen("/Applications/System Preferences.app/Contents/MacOS/System Preferences")
    return redirect("/")


if __name__=="__main__":   
    app.run(debug=True)    