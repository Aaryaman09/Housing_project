from flask import Flask

app = Flask(__name__)

@app.route("/",methods=['GET','Post'])
def index():
    return 'Hello'

if __name__=='__main__':
    app.run(debug=True)