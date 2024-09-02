from routes import create_app  # Import the create_app function from the car_rental package

# Create the app instance using the factory function
app = create_app()

# Check if the script is executed directly (i.e., not imported as a module)
if __name__ == "__main__":
    # Run the Flask app in debug mode for development purposes
    app.run(debug=True)
