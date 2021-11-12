from flask import Flask, jsonify, request
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)

class BMI(Resource):
    def post(self):
        data = request.get_json()
        height = data['height']
        weight = data['weight']
        bmi = (weight/(height**2))* 10**4
        if bmi < 18.4:
            status = 'Underweight!'
        elif bmi >= 18.4 and bmi <=24.9:
            status = 'Normal'
        else:
            status = 'Overweight!'

        return jsonify({"Body mass index" : bmi, "msg" : status})

api.add_resource(BMI,'/')

if __name__ == '__main__':
    app.run(debug=True, port=5000)