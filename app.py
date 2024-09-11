from flask import Flask, render_template

# Initialize Flask app and specify the path to the templates folder
app = Flask(__name__)

# Configuration settings
app.config['SECRET_KEY'] = 'SUPERSECRETKEY'  # Change this to a secure random key

# Routes
@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/auth")
def auth():
    return render_template("auth.html")

@app.route("/invoice")
def invoice():
    return render_template("invoice.html")

# Check if the script is executed directly (i.e., not imported as a module)
if __name__ == "__main__":
    # Run the Flask app in debug mode for development purposes
    app.run(debug=True)
