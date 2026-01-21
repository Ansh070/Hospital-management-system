# Import necessary modules from the Flask library
# Flask: The main class for creating the application.
# render_template: To render HTML templates.
# request: To handle incoming data (forms, etc.).
# redirect, url_for: To navigate between pages.
from flask import Flask, render_template, request, redirect, url_for

# Initialize the Flask application
# __name__ helps Flask determine the root path for the application
app = Flask(__name__)

# --- Routes ---
# Routes define the URLs that users can visit on the website.

@app.route("/")
def home():
    """
    The Home Page Route.
    Triggered when the user visits the root URL ('/').
    Returns the 'home.html' template.
    """
    return render_template("home.html")

@app.route("/admin_dashboard")
def admin_dashboard():
    """
    Admin Dashboard Route.
    Renders the dashboard specifically designed for administrators.
    """
    return render_template("admin_dashboard.html")

@app.route("/doctor_dashboard")
def doctor_dashboard():
    """
    Doctor Dashboard Route.
    Renders the dashboard for doctors to view appointments and patients.
    """
    return render_template("doctor_dashboard.html")

@app.route("/patient_dashboard")
def patient_dashboard():
    """
    Patient Dashboard Route.
    Renders the dashboard for patients to view health stats and history.
    """
    return render_template("patient_dashboard.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Login Route.
    Handles both displaying the login form (GET) and processing the login (POST).
    """
    # Check if the form has been submitted (POST request)
    if request.method == "POST":
        # Get data from the form fields
        email = request.form["email"]
        password = request.form["password"]

        # For now, just print the data to the console (Terminal)
        print("Login attempt:", email, password)

        # After successful login, redirect the user to the home page
        return redirect(url_for("home"))

    # If it's a GET request (loading the page), show the login form
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Registration Route.
    Handles user registration logic.
    """
    if request.method == "POST":
        # Retrieve form data
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        print("Register:", name, email, password)

        # After registration, redirect to the login page
        return redirect(url_for("login"))

    return render_template("register.html")

# --- Main Block ---
# This ensures the server only runs if the script is executed directly (not imported)
if __name__ == "__main__":
    # Run the app in debug mode. 
    # Debug mode auto-reloads the server when you make code changes and provides error logs.
    app.run(debug=True)
