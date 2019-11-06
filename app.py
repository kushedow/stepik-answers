from flask import Flask
import requests

app = Flask(__name__)     

@app.route('/')          

def hello():

  r = requests.get( < url >)

  return 'Hello, World!'   

app.run('0.0.0.0',8000)     