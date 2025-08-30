from flask import Flask, render_template, request
import random
import math
import time
import numpy as np

# Initialize Flask Application
app = Flask(__name__)

def estimate_pi(num_points, decimal_places):
    """
    Estimates the value of Pi using the Monte Carlo method
    Pi is the ratio of the circumference and diameter of the circle.

    :param decimal_places:
    :param num_points:
    :return float: An estimate of the value of Pi:
    """
    # points_in_circle = 0
    # total_points = 0
    # for i in range(0, num_points):
    #     # Generate random point
    #     x = random.random()
    #     y = random.random()
    #     total_points += 1 # Increment total points
    #
    #     distance = math.sqrt(x*x + y*y) # Calculate distance point is from center of the circle
    #
    #     if distance < 1:
    #         points_in_circle += 1
    points_in_circle = 0

    # Chunk size that is a power of 10 to reduce chance of memory allocation errors
    chunk_size = 1000000

    for _ in range(num_points // chunk_size):
        # Generate an array of random points with numpy
        points = np.random.rand(chunk_size, 2)
        # Calculate squared distance of each point from the origin
        distance_squared = np.sum(points**2, axis=1)
        # Count number of points that fall within the circle
        points_in_circle += np.sum(distance_squared <= 1)

    # Handle remaining points in a final chunk
    remaining_points = num_points % chunk_size
    if remaining_points > 0:
        points = np.random.rand(num_points, 2)
        distance_squared = np.sum(points ** 2, axis=1)
        points_in_circle += np.sum(distance_squared <= 1)

    # Count total number of points
    total_points = num_points

    # Calculate estimated value of pi
    if total_points > 0:
        pi = (4 * points_in_circle) / total_points
        formatted_pi = round(pi, decimal_places)
        return formatted_pi
    else:
        return 0

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
    decimal_places = 0
    calculation_time = 0

    # Check if form was submitted via a POST
    if request.method == 'POST':
        try:
            # Get number of points from the HTML form
            num_points_str = request.form['num_points']
            num_points = int(num_points_str)

            # Get number of deicmal places from the HTML form
            decimal_places_str = request.form['decimal_places']
            decimal_places = int(decimal_places_str)

            # Run simulation and get Pi estimation
            if num_points > 0:
                # Get start time before calculation
                start_time = time.time()
                pi_estimate = estimate_pi(num_points, decimal_places)
                # Get end time after calculation
                end_time = time.time()

                # Calculate total time to perform calculation
                calculation_time = round((end_time - start_time), 3)

        except (ValueError, KeyError):
            # Error handling when input is not a valid number
            pi_estimate = "Invalid input. Enter a positive whole number."
            num_points = "N/A"
            decimal_places = "N/A"
            calculation_time = "N/A"

    # Render HTML template using results
    return render_template('index.html', pi_estimate=pi_estimate, num_points=num_points, decimal_places=decimal_places, calculation_time=calculation_time)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)
