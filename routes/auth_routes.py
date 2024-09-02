from flask import Blueprint, render_template, request, redirect, url_for, flash

# Create a Blueprint for authentication routes
auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Replace this with real authentication logic
        if username == "admin" and password == "password":
            flash("Login successful!", "success")
            return redirect(url_for("main.index"))
        else:
            flash("Invalid username or password", "danger")

    return render_template("login.html")

@auth_bp.route("/logout")
def logout():
    # Implement logout logic
    flash("You have been logged out.", "info")
    return redirect(url_for("main.index"))
