from flask import Flask
from flask import render_template
import socket
import random
import os
import argparse

app = Flask(__name__)

color_codes = {
    "red": "#e74c3c",
    "green": "#16a085",
    "blue": "#2980b9",
    "blue2": "#30336b",
    "pink": "#be2edd",
    "darkblue": "#130f40"
}

color = os.environ.get('APP_COLOR') or random.choice(["red","green","blue","blue2","darkblue","pink"])

@app.route("/")
def main():
    #return 'Hello'
    print(args.color)
    return render_template('hello.html', name=socket.gethostname(), color=color_codes[args.color])

@app.route('/color/<new_color>')
def new_color(new_color):
    return render_template('hello.html', name=socket.gethostname(), color=color_codes[new_color])

@app.route('/read_file')
def read_file():
    f = open("/data/testfile.txt")
    contents = f.read()
    return render_template('hello.html', name=socket.gethostname(), contents=contents, color=color_codes[args.color])

if __name__ == "__main__":
    # Check for Command Line Parameters for color
    parser = argparse.ArgumentParser()
    parser.add_argument('--color', required=False, default='blue')
    args = parser.parse_args()
    
    print("ArgParse color=" + args.color)
    
    # Run Flask Application
    app.run(host="0.0.0.0", port=8080)
