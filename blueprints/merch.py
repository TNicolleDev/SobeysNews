from flask import Blueprint, render_template

merch_bp = Blueprint('merch',__name__, url_prefix='/merch')

@merch_bp.route("/merch")
def merch():
    return render_template("merch/merch.html")