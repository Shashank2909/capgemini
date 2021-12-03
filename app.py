from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route('/',methods=['Post'])
def bmi():
    data = request.get_json()
    height = data['height']
    weight = data['weight']
    b = (weight/(height**2))* 10**4
    return jsonify({"body mass index":b})


