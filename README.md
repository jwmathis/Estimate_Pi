# Pi Estimator Web App
This is a simple web application that estimates the value of Pi using the Monte Carlo method. It provides a clear and interactive way to understand how this computational algorithm works. 

# How it Works
The application simulates random points within a square that encloses a perfect circle. The ratio of points that fall inside the circle to teh total number of points is used to approximate the value of Pi. The more points you generate, the m,ore accurate your estimate becomes.

The formula used for the estimation is:

$$
\pi \approx 4 \times \frac{\text{points in circle}}{\text{total points}}
$$

# Features
* Pi estimation: Calculates an estimate for Pi based on a user-defined number of points.
* Custom Precision: Allows the user to specify the number of decimal places to round the estimated value.
* Performance Tracking: Displas the total time taken to run the estimation


# Getting Started
To run this applicaiton, you'll need to have Python and the Flask framework installed.
1. **Install Flask:** Open your terminal or command prompt and run the following command to install Flask:
   ```
   pip install Flask
   ```
2. **Install Numpy:** Open your terminal or command prompt and run the following command to install Numpy:
   ```
   pip install Numpy
   ```
3. **Run the App:** Once Flask is installed, navigate to the project directory and run the main application file(e.g., estimate_pi.py) form your terminal:
   ```
   python estimate_pi.py
   ```
4. **Access the App:** This terminal will display a local address (usually http://127.0.0.1:5000). Open this address in your web browser to use the application.

# Technologies Used
  * **HTML5:** For the front-end structure of the web page
  * **Tailwind CSS:** For front-end styling and responsive design.
  * **Python:** For the back-end logic, including the Monte Carlo algorithm
  * **Flask:** A Python web framework used to serve the web application
