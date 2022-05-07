from flask import Flask,render_template,request
import pickle

file = open('campusplacementpredictor.pkl', 'rb')
gb = pickle.load(file)
file.close()

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result',methods=["POST"])
def result():
    if request.method == 'POST':
        mydict = request.form
        crt = int(mydict['crt'])
        branch = int(mydict['branch'])
        gender = int(mydict['gender'])
        gradex = float(mydict['ssc'])
        inter = int(mydict['inter'])
        hs = float(mydict['hs'])
        ug = float(mydict['b.tech'])
        backlogs = int(mydict['backlogs'])
        inputfeatures = [[crt, branch, gender, gradex, inter, hs, ug, backlogs]]
        # predicting the class either 0 or 1
        predictedclass = gb.predict(inputfeatures)

        # predicting the probability

        #predictedprob = gb.predict_proba(inputfeatures)

        #print(predictedclass, predictedprob[0][0])

        if predictedclass[0] == 1:
            proba = predictedprob[0][1]

        else:
            proba = predictedprob[0][0]

        print(predictedclass, proba * 100)

        placemap = {1: 'Will be Placed', 0: 'Better Luck Next Time :('}
        predictedclasssend = placemap[predictedclass[0]]

        if predictedclass[0] == 1:
            return render_template('show.html', predictedclasssend=predictedclasssend, placed=True)

        else:
            return render_template('show.html', predictedclasssend=predictedclasssend)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
