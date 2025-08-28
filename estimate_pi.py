from flask import Flask, render_template, request
import random
import math

# Initialize Flask Application
app = Flask(__name__)

# Core Functions to estimate Pi
def count_decimal_places(number):
    """
    Counts the number of decimal places in a number.
    :param number:
    :return:
    """
    s = str(number) # Convert number to a string
    if '.' in s: # Find the decimal point
        return len(s.split('.')[-1]) # return the number of digits after decimal point
    else:
        return 0

def estimate_pi(num_points):
    """
    Estimates the value of Pi using the Monte Carlo method
    Pi is the ratio of the circumference and diameter of the circle.

    :param num_points:
    :return float: An estimate of the value of Pi:
    """
    pointsInCircle = 0
    totalPoints = 0
    for i in range(0, num_points):
        # Generate random point
        x = random.random()
        y = random.random()
        totalPoints += 1 # Increment total points

        distance = math.sqrt(x*x + y*y) # Calculate distance point is from center of the circle

        if distance < 1:
            pointsInCircle += 1

    pi = (4 * pointsInCircle) / totalPoints
    formatted_pi = round(pi, 3)
    return pi

# Define the route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Handles requests to the /index route.
    On GET request, it shows the form.
    On POST request, it calculates Pi and displays results
    """

    pi_estimate = 0
    num_points = 0

    # Check if form was submitted via a POST
    if request.method == 'POST':
        try:
            # Get number of points from the HTML form
            num_points_str = request.form['num_points']
            num_points = int(num_points_str)

            # Run simulation and get Pi estimation
            if num_points > 0:
                pi_estimate = estimate_pi(num_points)

        except (ValueError, KeyError):
            # Error handling when input is not a valid number
            pi_estimate = "Invalid input. Enter a positive whole number."
            num_points = "N/A"

    # Render HTML template using results
    return render_template('index.html', pi_estimate=pi_estimate, num_points=num_points)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)
