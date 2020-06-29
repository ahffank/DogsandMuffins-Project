# -*- coding: utf-8 -*-
"""Flask API.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15_fAuBHLsDNLfEJxJ4SW4xhrxmRbAR8p
"""

#!pip install flask_cors
#pip install fastai


from flask import Flask,render_template,request,url_for,jsonify 
from fastai.basic_train import load_learner
from fastai.vision import open_image
from flask_cors import CORS,cross_origin
app = Flask(__name__)
#CORS(app, support_credentials=True)

@app.route("/")
def homepage():
	return render_template("index.html")
#!pwd

#from google.colab import drive
#drive.mount('/content/drive')

#!pip install "torch==1.4" "torchvision==0.5.0"

#Path('drive/My Drive/test')
# load the learner
#learn = load_learner(path='./Model', file='trained_model.pkl')
#classes = learn.data.classes
 

#def predict_single(img_file):
#    'function to take image and return prediction'
#    prediction = learn.predict(open_image(img_file))
#    probs_list = prediction[2].numpy()
#    return(probs_list)
#    return {
#        'category': classes[prediction[1].item()],
#        'probs': {c: round(float(probs_list[i]), 5) for (i, c) in enumerate(classes)}
#    }


@app.route("/",methods=['POST']) 
def predict():
    if request.method == 'POST':
 	#my_prediction = predict_single(request.files['image'])
        return render_template('results.html',prediction = [0.01],comment = "asd")
  
# route for prediction
#@app.route('/predict', methods=['POST'])
#def predict():
    
#	if request.method == 'POST': 
#		my_prediction = predict_single(request.files['image'])
#	return render_template('results.html',prediction = my_prediction,comment = "Ahffan")

    #return jsonify(predict_single(request.files['image']))

if __name__ == '__main__':
	app.run(debug=True)
