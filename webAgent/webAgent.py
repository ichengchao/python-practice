from flask import Flask
import os
import logging
from logging import Formatter

__author__ = 'charles'

app = Flask(__name__)

userHome = os.path.expanduser('~/')
logHandler = logging.FileHandler(userHome + 'logs/webAgent.log')
logHandler.setLevel(logging.INFO)
logHandler.setFormatter(Formatter(
    '%(asctime)s %(levelname)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'
))
app.logger.addHandler(logHandler)
app.logger.setLevel(logging.INFO)


@app.route('/')
def hello():
    result = os.system(userHome + 'myscript.sh')
    app.logger.info(result)
    return "result:test1234123"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8888, debug=True)