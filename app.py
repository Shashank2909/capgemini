from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route('/',methods=['Post'])
def bmi():
    data = request.get_json()
    height = data['height']
    weight = data['weight']
    b = (weight/(height**2))* 10**4
    return jsonify({"body mass index":b})

@app.route('/virat',methods=['Post'])
def virat():
    return "world cup nahi jeet sakta vro....Biwi ke isharo pe G*nd matkani hai toh bolo"


