from flask import Flask,flash,url_for,redirect,render_template,request
from flask_cors import cross_origin
from SKBIS import SKBIS
app=Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

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
    return render_template('Results copy.html',results=results,Num=len(results))

@app.after_request
def add_header(response):
    response.cache_control.no_store = True
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response
if __name__=='__main__':
    app.run(port=5000,debug=True)