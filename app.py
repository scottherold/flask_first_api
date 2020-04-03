from flask import Flask

# __name__ gives each file a unique name
app = Flask(__name__)


# ===== HTTP requests =====
@app.route('/') # root URL
def home():
    return "Hello, world!"


# ==== Port =====
app.run(port=5000)