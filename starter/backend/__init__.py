import os
from flask import Flask
from flask_cors import CORS

from .movies import movies_api

app = Flask(__name__)
CORS(app, origins="http://a1db91787e3d54a60b9d795d44e2dffc-1137869864.us-east-1.elb.amazonaws.com")
app.register_blueprint(movies_api)

# Start app
if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=int(os.getenv("FLASK_RUN_PORT", 5000)),
    )
