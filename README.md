# ThousandEyes Webhook processor

ThousandEyes Webhook processor is a simple ThousandEyes webhook integration that will format and forward relevant alert messages to a Slack channel.

## Installation
You can use pip to install the following package dependencies:
flask, waitress, slack_sdk

## Slack configuration
In order to make this integration work you will also need to create a basic slack app and add it to the channel you will be using, this can be done on the following link:
https://api.slack.com/apps

Additionally you will need to add the following OAuth permissions to the Bot Token Scopes under OAuth & Permissions
- chat:write
- chat:write.customize

## Usage

The Configuration Template has default values for almost everything, so those can be used. The only value you will need to get is the Bot User OAuth Token which can be found under the OAuth and Permissions section of your app configuration. Other values can be modified if needed.

On ThousandEyes you need to configure the notification Webhook using the URL of the server hosting this script. Example using template default value for URL subfolder: https://myServerURL/alert

Once those configurations are ready, run the main script that will run the server and processor "ThousandEyes_Webhook_processor.py"

Note:
In case you want to run this for local testing and don't have a domain name redirecting to your PC, ngrok or any other tunneling service can be used. Example on Windows:
C:\Users\Downloads\ngrok-stable-windows-amd64> ngrok.exe http 8080 --region=us
