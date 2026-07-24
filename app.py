from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def home():
   return render_template("home.html")

@app.route("/frozen")
def frozen_in_time():
   return render_template("frozen_in_time.html")

@app.route("/romance-rumor")
def workplace_romance_rumor():
    return render_template("workplace-romance-rumor.html")

@app.route("/receiving-clutter")
def receiving_floor_clutter():
    return render_template("receiving-floor-clutter.html")

@app.route("/overtime")
def mandatory_overtime_debate():
    return render_template("mandatory-overtime-debate.html")

@app.route("/loss-prevention")
def loss_prevention_reminders():
    return render_template("loss-prevention-reminders.html")

@app.route("/shift-rotation")
def new_shift_rotation():
    return render_template("new-shift-rotation.html")

@app.route("/vaughan-traffic")
def vaughan_council_traffic():
    return render_template("vaughan-council-traffic.html")

@app.route("/fridge-standoff")
def fridge_standoff():
    return render_template("fridge-standoff.html")

@app.route("/whiteboard-dispute")
def whiteboard_schedule_dispute():
    return render_template("whiteboard-schedule-dispute.html")

@app.route("/parking-layout")
def parking_layout_fallout():
    return render_template("parking-layout-fallout.html")

@app.route("/fifth-wing")
def fifth_automated_wing():
    return render_template("fifth-automated-wing.html")

@app.route("/bay-9-hum")
def bay_9_hum():
    return render_template("bay-9-hum.html")

@app.route("/quietest-corner")
def quietest_corner():
    return render_template("quietest-corner.html")

@app.route("/staff-entrance")
def staff_entrance_redesign():
    return render_template("staff-entrance-redesign.html")

@app.route("/exec-visit")
def regional_exec_visit():
    return render_template("regional-exec-visit.html")

@app.route("/truck-livery")
def unusual_truck_livery():
    return render_template("unusual-truck-livery.html")

@app.route("/badge-colour")
def mystery_badge_colour():
    return render_template("mystery-badge-colour.html")

@app.route("/merch")
def merch():
    return render_template("merch.html")

