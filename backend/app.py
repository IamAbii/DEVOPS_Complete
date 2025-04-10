from flask import Flask, jsonify
from flask_cors import CORS
import requests
import socket
import os

# Initialize Flask app
app = Flask(__name__)

# IMPORTANT: Configure CORS to allow requests from anywhere
# This is critical for option 1 where frontend and backend are on different domains
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def index():
    return 'Service is Healthy'

@app.route('/api/getJoke', methods=['GET'])
def send_request():
    joke = get_joke()
    # UPDATED: Return as JSON so frontend can parse it easily
    return jsonify({"joke": joke})

def get_joke():
    try:
        # Fetch a programming joke from the JokeAPI
        response = requests.get("https://sv443.net/jokeapi/v2/joke/Programming?type=single")
        joke_data = response.json()
        
        if 'joke' not in joke_data:
            return "Oops! Couldn't fetch a joke at the moment. Please try again later. 😅"
        
        # Ensure the joke is properly formatted with a newline before the custom message
        return f"{joke_data['joke']} \n \n --->> **** Did I bring a smile on your face, Abhilash? If not, refresh for a new one by clicking on CLICK tab above. Go on, it's for free—don't be STINGY. LOL !!!! 😄 A smile is for free ****"
    except Exception as e:
        app.logger.error(f"Error fetching joke: {str(e)}")
        return "Sorry, an error occurred while fetching your joke. Please try again later!"

# ADDED: Test endpoint for debugging connectivity
@app.route('/api/test', methods=['GET'])
def test():
    return jsonify({
        "status": "success",
        "message": "Backend is accessible!",
        "cors": "enabled"
    })

if __name__ == '__main__':
    # Get the server's IP address
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    
    print(f"Starting server on {ip_address}:5000")
    
    # Run the app on the server's IP address and port 5000
    # Note: In production, this will be replaced by gunicorn command
    app.run(host='0.0.0.0', port=5000, debug=False)
