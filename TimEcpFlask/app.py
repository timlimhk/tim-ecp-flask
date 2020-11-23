#coding: utf-8
"""
ECP Test

Author: Tim Lim 

"""
from flask import Flask, jsonify, g, request, make_response
import os

# added for strcuture request logs
import datetime
import time
import logging
from rfc3339 import rfc3339



# Extract the required environment variables
# Guarantee minimum setting for this app to run
log_level = os.environ.get('log_level',"INFO")
service_port = os.environ.get('service_port',5000)
git_commit_sha = os.environ.get('git_commit_sha',"undefined")
version = os.environ.get('version',"undefined")


# default logging is WARN, set to desired level for more logs output
logging.basicConfig(level=log_level)

# Disable Flask console logs for show structured data 
# for /info request only
log = logging.getLogger('werkzeug')
log.disabled = True

infos = dict([
            ('Service_name',"tim-ecp"),
            ('version',version),
            ('git_commit_sha',git_commit_sha),
            ('environment',dict([
                                ('service_port',service_port),
                                ('log_level',log_level)
                                ])
            )        
        ])



# create_app wrapps the other functions to set up the project
def create_app(config=None, testing=False, cli=False):
    """
    Application factory, used to create application
    """

    app = Flask(__name__, static_folder=None)

    # To display JSON output unsorted
    app.config['JSON_SORT_KEYS'] = False

    @app.before_request
    def start_timer():
       g.start = time.time()

    # Define after request logging for get /info request only
    @app.after_request
    def log_request(response):
       if (
           request.path != "/info"
       ):
           return response

       now = time.time()
       duration = round(now - g.start, 6)  # to the microsecond
       ip_address = request.headers.get("X-Forwarded-For", request.remote_addr)
       host = request.host.split(":", 1)[0]
       params = dict(request.args)
       dt = datetime.datetime.fromtimestamp(now)
       timestamp = rfc3339(dt, utc=False)
       request_id = request.headers.get("X-Request-ID", "")

       log_params = {
           "time": timestamp,
           "method": request.method,
           "path": request.path,
           "status": response.status_code,
           "duration": duration,
           "ip": ip_address,
           "host": host,
           "params": params,
           "request_id": request_id,
       }
       app.logger.info(log_params)
       return response

    @app.route("/")
    def root():
       response = make_response('<!DOCTYPE html>\
       <html><body><h1>My ECP testing site</h1>\
       <h2>Supported endpoint:</h2><li>/info.</li>\
       </body></html>')
       return response

    # Info ENDPOINT created for ANZ ECP code test
    # output display in JSON format 

    @app.route("/info")
    def info():
       return jsonify (infos)
     
    @app.route('/<page_name>')
    def other_page(page_name):
       response = make_response('<!DOCTYPE html>\
       <html><body><h1>My ECP testing site</h1>\
       <p>The page named %s does not exist.</p></body></html>'\
       % page_name, 404)
       return response

    return app

def main():
   app=create_app()
   app.logger.info('App Started!')
   app.run(debug=False,host='0.0.0.0',port=service_port)

if __name__ == '__main__':
   main() 
