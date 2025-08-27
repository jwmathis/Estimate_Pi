from flask import Flask, render_template, request
import random
import math

# Initialize Flask Application
app = Flask(__name__)

"""Core Functions"""
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
    return pi

# Define the route for the home page
@app.route('/', methods=['GET', 'POST'])

def main():
    """
    Main function
    :return:
    """
    while True:
        try:
            num_decimal_places = int(input("Enter the number of decimal places you would like to use: "))
            if num_decimal_places == 0:
                break
            elif num_decimal_places >= 5:
                num_points = 1000000000
            else:
                num_points = 10**(num_decimal_places + 2)

            print(f"\Running Monte Carlo simulation for {num_points} points.")

            pi_approximation = estimate_pi(num_points)

            formatted_pi = round(pi_apporximation, num_decimal_places)

            print(f"\Pi calculated is approximately {pi_approximation}")
            print(f"\Pi is approximately {formatted_pi}")
            break

        except ValueError:
            print("Please enter a number greater than 0")

if __name__ == "__main__":
    main()
