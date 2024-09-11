from flask import jsonify, request, Flask

app = Flask(__name__)

app.route('/app', methods=['GET'])
def hello():
	return 'hello' + 'world'

if __name__=="main":
	app.run(debug=True)