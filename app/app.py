from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

@app.route('/')
def home():
    #return 'Hello x, World!'
    uri='http://book-api.h8bpb6h5gtg2ecga.uksouth.azurecontainer.io/'
    response = requests.get(uri)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse JSON data from the response
        json_data = response.json()
        # Render a template with the JSON data
        return json_data
    else:
        # Return an error message if the request was not successful
        return f'Error: {response.status_code} - Unable to fetch data from API'



@app.route('/test')
def test():

    name = os.getenv('NAME')
    return f"Hello {name}"

if __name__ == '__main__':
    app.run(debug=True)
