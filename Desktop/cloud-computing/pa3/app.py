from flask import Flask, jsonify, request
app = Flask(__name__)

temp = 75
setpt = 70

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/ThermsAreUs/api/v1.0/current-temp', methods=['GET'])
def get_temp():
    return jsonify({'current_temp': temp})

@app.route('/ThermsAreUs/api/v1.0/current-setpoint', methods=['GET'])
def get_setpoint():
    return jsonify({'current_setpoint': setpt})

@app.route('/ThermsAreUs/api/v1.0/current-setpoint', methods=['PUT'])
def update_setpoint():
    global setpt
    setpt = request.json['newsetpt']
    return jsonify({'new_setpoint': setpt})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
