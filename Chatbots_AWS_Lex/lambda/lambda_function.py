import json

def lambda_handler(event, context):
    intent_name = event["currentIntent"]["name"]
    
    if intent_name == "GreetingIntent":
        response = "Hi there! How can I assist you?"
    elif intent_name == "HelpIntent":
        response = "Sure, I can help. Please provide more details."
    else:
        response = "Sorry, I didn't understand that. Could you rephrase?"

    return {
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {"contentType": "PlainText", "content": response}
        }
    }
