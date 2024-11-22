import os
from flask import Flask, request
from flask_cors import CORS
from .movies import movies_api

app = Flask(__name__)

# CORS Configuration: Allow specific origins for production
CORS(app, origins=["http://a1db91787e3d54a60b9d795d44e2dffc-1137869864.us-east-1.elb.amazonaws.com", "http://localhost:3000"])

# Register the blueprint for movie APIs
app.register_blueprint(movies_api)

# Health check route
@app.route('/health')
def health_check():
    return "OK", 200

# Request logging
@app.before_request
def log_request():
    app.logger.info(f"Request: {request.method} {request.path}")

# Start app
if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=int(os.getenv("FLASK_RUN_PORT", 5000)),
    )
