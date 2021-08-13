from flask import Flask

app = Flask(__name__)


@app.route('/')
def hi():
    return 'hi world again!!!'

@app.route('/about')
def about():
    return 'About!'



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0') 
     

