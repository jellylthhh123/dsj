from flask import Flask  , render_template
app = Flask(__name__)

@app.route('/index.html')
def index():  # put application's code here
    return render_template('index.html')

@app.route('/Words Cloud.html')
def about(): #put application's code here
    return render_template('Words Cloud.html')

@app.route('/timeline.html')
def contact():
    return render_template('timeline.html')


@app.route('/topicc.html', endpoint="topicc")
def contact():
    return render_template('topicc.html')

@app.route('/hot topicc.html', endpoint="hot topicc")
def contact():
    return render_template('hot topicc.html')

@app.route('/emotion.html', endpoint="emotion")
def contact():
    return render_template('emotion.html')

@app.route('/net.html', endpoint="net")
def socialnet():
    return render_template('net.html')

@app.route('/text.html', endpoint="text")
def text():
    return render_template('text.html')


















