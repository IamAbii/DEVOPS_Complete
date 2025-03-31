from flask import Flask
from flask_cors import CORS
import requests
import socket

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'Service is Healthy'

@app.route('/api/getJoke', methods=['GET'])
def send_request():
    joke = get_joke()
    return joke

def get_joke():
    # Fetch a programming joke from the JokeAPI
    response = requests.get("https://sv443.net/jokeapi/v2/joke/Programming?type=single")
    joke = response.json()
    
    if 'joke' not in joke:
        return "Oops! Couldn't fetch a joke at the moment. Please try again later. 😅"
    
    # Ensure the joke is properly formatted with a newline before the custom message
    return f"{joke['joke']} \n \n --->> **** Did I bring a smile on your face, Abhilash? If not, refresh for a new one by clicking on CLICK tab above. Go on, it's for free—don't be STINGY. LOL !!!! 😄 A smile is for free ****"

if __name__ == '__main__':
    # Get the server's IP address
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    
    # Run the app on the server's IP address and port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
