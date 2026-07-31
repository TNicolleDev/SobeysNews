from flask import Blueprint, render_template

merch_bp = Blueprint('merch',__name__, url_prefix='/merch')

@merch_bp.route("/plushies")
def plushies():
    return render_template("merch/plushies.html")


@merch_bp.route("/hats")
def hats():
    return render_template("merch/hats.html")

@merch_bp.route("/tshirts")
def tshirts():
    return render_template("merch/tshirts.html")

@merch_bp.route("/accessories")
def accessories():
    return render_template("merch/accessories.html")