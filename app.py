from flask import Flask, render_template, jsonify
import required.perf as perf

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/update_metrics')
def update_metrics():
    return jsonify(perf.collect_metrics())

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=51234)
