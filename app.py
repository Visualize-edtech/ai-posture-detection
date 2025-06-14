from flask import Flask, render_template
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # We'll create this HTML file next

if __name__ == '__main__':
    app.run()
