from flask import Flask
from housing.logger import logging

app = Flask(__name__)

@app.route("/",methods=['GET','Post'])
def index():
    logging.info("we are testing logging")
    return 'Hello'

if __name__=='__main__':
    app.run(debug=True)