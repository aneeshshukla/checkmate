from flask import Flask, render_template, jsonify
import required.perf as perf
import logging
import os, sys

app = Flask(__name__)

# Disable the werkzeug logger
logging.getLogger('werkzeug').disabled = True

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/update_metrics')
def update_metrics():
    return jsonify(perf.collect_metrics())

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=51234)
