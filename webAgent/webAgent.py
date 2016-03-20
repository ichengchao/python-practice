from flask import Flask
import os
import logging
from logging import Formatter

__author__ = 'charles'

app = Flask(__name__)


# logging setting
userHome = os.path.expanduser('~/')
logHandler = logging.FileHandler(userHome + 'logs/webAgent.log')
logHandler.setLevel(logging.INFO)
logHandler.setFormatter(Formatter(
    '%(asctime)s %(levelname)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'
))
app.logger.addHandler(logHandler)
app.logger.setLevel(logging.INFO)


@app.route('/deploy')
def deploy_tomcat():
    deploy_cmd = userHome + 'myscript/tomcat-springrun.sh'
    result = os.system(deploy_cmd)
    app.logger.info('excute cmd:' + deploy_cmd)
    app.logger.info(result)
    return 'delpoy success'


@app.route('/test')
def test():
    app.logger.info('test')
    return "test success"


@app.route('/uptime')
def uptime():
    uptime_result = os.popen('uptime')
    line_list = uptime_result.readlines()
    result = ''
    for line in line_list:
        result += line
    return result


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8888, debug=True)
