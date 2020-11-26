from flask import Flask,flash,url_for,redirect,render_template,request
from flask_cors import cross_origin

from SKBIS import SKBIS
app=Flask(__name__)

@app.route('/')
@cross_origin()
def Index():
    return render_template('Index.html')

@app.route('/results',methods=['POST'])
@cross_origin()
def Results():
    searchString=request.form['searchString']
    Imagescrapper=SKBIS(searchString=searchString)
    results=Imagescrapper.mainExecution()
    return render_template('Results copy.html',results=results)


if __name__=='__main__':
    app.run(port=5000,debug=True)