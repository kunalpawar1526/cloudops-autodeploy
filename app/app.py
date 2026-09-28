from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>CloudOps AutoDeploy</title>
        </head>
        <body>
            <h1> CloudOps AutoDeploy</h1>
            <h2>Application is running!</h2>

            <p><strong>Environment:</strong> Development</p>
            <p><strong>Platform:</strong> AWS</p>
            <p><strong>Container:</strong> Docker</p>
            <p><strong>CI/CD:</strong> GitHub Actions</p>

            <a href="/health">Health Check</a>
        </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "cloudops-autodeploy"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
