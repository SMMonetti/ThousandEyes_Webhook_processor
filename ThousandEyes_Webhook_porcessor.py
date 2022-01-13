# Main script. Processor with waitress server listening for Thousandeyes Webhooks
# Sergio Monetti - smonetti@cisco.com 
#!/usr/bin/env python3

from flask import Flask,request,json
from waitress import serve
import alert_parser, slack_messenger

# Retrieve customer-specific parameters from template file
f = open('Configuration_template.json')
data = json.load(f)
f.close

channel = data["slack"]["channel"]
username = data["slack"]["username"]
icon_url = data["slack"]["icon_url"]
token = data["slack"]["token"]
port  = data["Webhook server"]["port"]
alertURLsubFolder = data["Webhook server"]["alertURLsubFolder"]

# Flask app definition and Webhook processor
app = Flask(__name__)

@app.route(alertURLsubFolder, methods=['POST'])
def alert():
    data = request.json

    message = alert_parser.formatAlertMessage(data)
    slack_messenger.sendMessage(channel, message, username, icon_url, token)
    
    return data

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=port)
