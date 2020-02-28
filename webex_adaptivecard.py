#!/usr/bin/env python
import requests
import json
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
WEBEX_BOT_TOKEN ='WEBEX_TOKEN'
WEBEX_API_URL = 'https://api.ciscospark.com/v1/'
TO_PERSON_EMAIL = 'RECIPIENT_EMAIL'

def send_webex_api(type, api_type, data): #post/get/put, messages/rooms, data
    r = requests.request(type, WEBEX_API_URL + api_type, data=data,
                    headers={'Authorization': 'Bearer ' +  WEBEX_BOT_TOKEN,
                    'Content-Type': "application/json"})
    return r

def webex_card_example():
    card = {
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
        "type": "AdaptiveCard",
        "version": "1.0",
        "body": [
            {
                "type": "TextBlock",
                "text": "Publish Adaptive Card schema",
                "weight": "bolder",
                "size": "medium"
            },
            {
                "type": "ColumnSet",
                "columns": [
                    {
                        "type": "Column",
                        "width": "auto",
                        "items": [
                            {
                                "type": "Image",
                                "url": "https://pbs.twimg.com/profile_images/3647943215/d7f12830b3c17a5a9e4afcc370e3a37e_400x400.jpeg",
                                "size": "small",
                                "style": "person"
                            }
                        ]
                    },
                    {
                        "type": "Column",
                        "width": "stretch",
                        "items": [
                            {
                                "type": "TextBlock",
                                "text": "Matt Hidinger",
                                "weight": "bolder",
                                "wrap": True
                            },
                            {
                                "type": "TextBlock",
                                "spacing": "none",
                                "text": "Created {{DATE(2017-02-14T06:08:39Z, SHORT)}}",
                                "isSubtle": True,
                                "wrap": True
                            }
                        ]
                    }
                ]
            },
            {
                "type": "TextBlock",
                "text": "Now that we have defined the main rules and features of the format, we need to produce a schema and publish it to GitHub. The schema will be the starting point of our reference documentation.",
                "wrap": True
            },
            {
                "type": "FactSet",
                "facts": [
                    {
                        "title": "Board:",
                        "value": "Adaptive Card"
                    },
                    {
                        "title": "List:",
                        "value": "Backlog"
                    },
                    {
                        "title": "Assigned to:",
                        "value": "Matt Hidinger"
                    },
                    {
                        "title": "Due date:",
                        "value": "Not set"
                    }
                ]
            }
        ],
        "actions": [
            {
                "type": "Action.ShowCard",
                "title": "Set due date",
                "card": {
                    "type": "AdaptiveCard",
                    "body": [
                        {
                            "type": "Input.Date",
                            "id": "dueDate"
                        }
                    ],
                    "actions": [
                        {
                            "type": "Action.Submit",
                            "title": "OK"
                        }
                    ]
                }
            },
            {
                "type": "Action.ShowCard",
                "title": "Comment",
                "card": {
                    "type": "AdaptiveCard",
                    "body": [
                        {
                            "type": "Input.Text",
                            "id": "comment",
                            "isMultiline": True,
                            "placeholder": "Enter your comment"
                        }
                    ],
                    "actions": [
                        {
                            "type": "Action.Submit",
                            "title": "OK"
                        }
                    ]
                }
            }
        ]
    }
    return card

def main(): 
    # default data payload
    data = {
        "markdown": "Hi, This Python script is an example of Adaptive Cards in Webex",
        "toPersonEmail": TO_PERSON_EMAIL,
    }

    # Create attachment
    attachment = {
        "attachments": [{
            "contentType": "application/vnd.microsoft.card.adaptive",
            "content": webex_card_example()
        }]
    }

    # update the payload with the attachment adaptive card
    data.update(attachment)

    #send the request to the webex server. Adaptive cards need to be json dumped otherwise it will cause a 400 error.
    my_api = send_webex_api ('post', 'messages', json.dumps(data))
    logging.info (f"Server Response: {my_api.status_code}")

if __name__ == '__main__':
    main()