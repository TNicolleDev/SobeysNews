from flask import Blueprint, render_template


stories_bp = Blueprint('stories',__name__,url_prefix='/stories')

@stories_bp.route("/frozen")
def frozen_in_time():
   return render_template("stories/frozen_in_time.html")

@stories_bp.route("/strike")
def strike_booth():
   return render_template("stories/strike_booth.html")