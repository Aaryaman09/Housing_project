from flask import Flask
import sys
from housing.logger import logging
from housing.exception import HousingException

app = Flask(__name__)

@app.route("/",methods=['GET','Post'])
def index():
    try: 
        raise Exception("we are testing custom exception")
    except Exception as e:
        housing = HousingException(e,sys)
        logging.info(housing.error_message)
        logging.info("We are testing logging module")    
    logging.info("we are testing logging")
    return 'Hello this is update'

if __name__=='__main__':
    app.run(debug=True)