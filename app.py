
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>CI/CD Pipeline Using Jenkins</h1>
    <p>Flask application deployed successfully!</p>
    <p>Technologies: GitHub, Jenkins, Docker and AWS EC2</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
