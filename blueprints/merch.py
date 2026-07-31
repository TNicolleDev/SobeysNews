from flask import Blueprint, render_template

merch_bp = Blueprint('merch',__name__, url_prefix='/merch')

@merch_bp.route("/plushies")
def plushies():
    return render_template("merch/plushies.html")


@merch_bp.route("/hats")
def hats():
    return render_template("merch/hats.html")