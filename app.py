"""Flask App Project."""

from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def index():
    """Return homepage."""
#    json_data = {'Hello': 'World!'}
    #return jsonify(json_data)
    return "มิ้น 21 4/1"

if __name__ == '__main__':
    app.run()
