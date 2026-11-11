from flask import Flask


app = Flask(__name__)
@app.route('/')
def hello():
    return 'Hey there'

#changing url processors
## when u run the code on your local host,then on the url add '/greet/lily'output expected is hello lily.The name can be changed as desired
@app.route('/greet/<name>')
def greet(name):
    return f'hello {name}'

@app.route('/sum/<int:number1>/<int:number2>')
def add(number1,number2):
    return f'{number1}+{number2} = {number1+number2}'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=555 ,debug=True)
    ##During deployment ensure debug is false
