# Premier League Scores Web App

A web application for displaying Premier League scores, designed to run on OpenShift.

## Installation

Follow these steps to set up the application:

1. Install the required packages:
   sudo yum install -y python3 git

2. Clone the repository:
   git clone https://github.com/mritsurgeon/premier-league-scores-webapp.git

3. Navigate to the project directory:
   cd premier-league-scores-webapp

4. Install Python dependencies:
   pip3 install -r requirements.txt

5. Run the application:
   python3 app.py

6. Access the application:
   - Create a route to your VM in OpenShift
   - Access the application at http://<vm-ip>:5000

## Notes

- Ensure that you have the necessary permissions to install packages and create routes in your OpenShift environment.
- The application runs on port 5000 by default. Adjust your firewall settings if needed.
- For production deployment, consider using a WSGI server like Gunicorn instead of the built-in Flask development server.
