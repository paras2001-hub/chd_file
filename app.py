from flask import Flask,request,jsonify
import pickle
from flask_restful import reqparse

app = Flask(__name__)

@app.route('/')
def hello():
	return 'Up and running'

@app.route('/predict',methods = ['POST'])
def predict():
	with open('HeartDiseasePred_model','rb') as w:
		imp_model = pickle.load(w)
	json = request.get_json()
	lst = list(json[0].values())
	print(lst)
	prediction=imp_model.predict([lst])
	print("here:",prediction)
	if(prediction[0]==1):
		res = 'High Ten year C.H.D. risk'
	else:
		res = 'Minimal Ten year C.H.D. risk'
	return jsonify({'prediction': res})

if __name__=='__main__':
	#app.run(host='192.168.0.100', port='8000', debug=True)
	app.run(host='0.0.0.0',)