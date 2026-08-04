from flask import Blueprint, render_template
from blueprints.auth import login_required


stories_bp = Blueprint('stories',__name__,url_prefix='/stories')

@stories_bp.route("/frozen")
@login_required
def frozen_in_time():
   return render_template("stories/frozen_in_time.html")

@stories_bp.route("/strike")
def strike_booth():
   return render_template("stories/strike_booth.html")

@stories_bp.route("/std")
@login_required
def std():
   return render_template('/stories/short_term_disability.html')