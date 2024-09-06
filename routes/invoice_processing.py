from flask import Blueprint, render_template

invoice_processing = Blueprint('invoice_processing', __name__)

@invoice_processing.route("/invoice")
def invoice():
    return render_template("invoice.html")