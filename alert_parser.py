# Module for parsing json dictionary from webhook and formating values into string messages ready for being sent to slack.
# Sergio Monetti - smonetti@cisco.com 

def parseAgentsFromAlert(jsonAgents):
    agents = ""
    for agent in jsonAgents:
        agents += "\n• " + agent["agentName"] + " - " + agent["metricsAtStart"]
    return agents

def formatAlertMessage(jsonAlert):
    message = ""

    # Relevant fields for all alerts.
    eventType = jsonAlert["eventType"]
    alertName = jsonAlert["alert"]["ruleName"]
    alertStart = jsonAlert["alert"]["dateStartZoned"]
    
    # Verify the type of event to format data accordingly for the message.
    if (eventType == "ALERT_NOTIFICATION_CLEAR"):
        alertEnd = jsonAlert["alert"]["dateEndZoned"]
        
        message = f"Alert: '{alertName}' has been cleared.\n\nAlert start: {alertStart}\nAlert end: {alertEnd}"
                  
    elif (eventType == "ALERT_NOTIFICATION_TRIGGER"):
        alertType = jsonAlert["alert"]["type"]
        alertPermalink = jsonAlert["alert"]["permalink"]

        # Verify the type of alert. Currently script is considered for detailed Network alerts.
        # This section is scalable as more detailed alerts can be configured as needed using a switch-like structure.
        if (alertType == "Network"):
            alertAgents = parseAgentsFromAlert(jsonAlert["alert"]["agents"])
            alertRule = jsonAlert["alert"]["ruleExpression"]

            message = f"Alert: '{alertName}' has been triggered.\n\nAlert start: {alertStart}\nRule configured for alert: {alertRule}\nAgents reporting alert: {alertAgents}\n\nDetailed alert: \n<{alertPermalink}>"

        # Generic alert trigger
        else:
            message = f"Alert: '{alertName}' has been triggered.\nAlert start: {alertStart}\n\nDetailed alert: \n<{alertPermalink}>"

    return message
