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

@stories_bp.route('/frozen2')
@login_required
def frozen2():
   return render_template('/stories/frozen_part_2.html')

@stories_bp.route('/noot')
@login_required
def no_ot():
   return render_template('/stories/no_ot.html')

@stories_bp.route('/bobbygone')
@login_required
def bobby_gone():
   return render_template('/stories/bobby_gone.html')