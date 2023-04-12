from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    result = ''
    return render_template('index.html',**locals())

@app.route('/predict',methods=['POST','GET'])

def predict():
    AVG_EAR = float(request.form['AVG_EAR'])
    mouth_ratio = float(request.form['mouth_ratio'])
    if(mouth_ratio>17):Yawn=1
    else : Yawn=0
    if(AVG_EAR<0.25):
        Eye_class=0
    else:
        Eye_class=1
    result = model.predict([[AVG_EAR, mouth_ratio, Yawn, Eye_class]])[0]
    return render_template('index.html', **locals())


if __name__ == '__main__':
    app.run(debug=True)
