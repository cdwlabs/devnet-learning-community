#
# Adaptive Card for Webex
# Schema Explorer:
#  https://adaptivecards.io/explorer/
# 
def get_webex_card(room_id, phone_info, agent_info):
    payload = None
    try:
        user_name = agent_info['first_name'] + ' ' + agent_info['last_name']
        agent_id = phone_info['user_id']
        phone_model = phone_info['model']
        extension = phone_info['extension']
        skill_group = agent_info['skill_group']
        team_name = agent_info['team_name']
        payload = '{ \
            "roomId": "' + room_id + '", \
            "markdown": "**Error Rendering Card!**", \
            "attachments": [ \
                { \
                    "contentType": "application/vnd.microsoft.card.adaptive", \
                    "content": { \
                        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json", \
                        "type": "AdaptiveCard", \
                        "version": "1.1", \
                        "body": [ \
                            { \
                                "type": "ColumnSet", \
                                "columns": [ \
                                    { \
                                        "type": "Column", \
                                        "width": 2, \
                                        "items": [ \
                                            { \
                                                "type": "TextBlock", \
                                                "text": "New User Verification", \
                                                "weight": "bolder", \
                                                "size": "medium" \
                                            }, \
                                            { \
                                                "type": "TextBlock", \
                                                "text": "Hello!  We have added ' + user_name + ' to the Contact Center.", \
                                                "isSubtle": true, \
                                                "wrap": true \
                                            }, \
                                            { \
                                                "type": "TextBlock", \
                                                "text": "Please review the information below and select verify if the configuration is correct.  Thank you!", \
                                                "isSubtle": true, \
                                                "wrap": true, \
                                                "size": "small" \
                                            }, \
                                            { \
                                                "type": "TextBlock", \
                                                "text": "---", \
                                                "wrap": false \
                                            } \
                                        ] \
                                    }, \
                                    { \
                                        "type": "Column", \
                                        "width": 1, \
                                        "items": [ \
                                            { \
                                                "type": "Image", \
                                                "url": "https://www.marketbeat.com/logos/cdw-corporation-logo.jpg", \
                                                "size": "auto" \
                                            } \
                                        ] \
                                    } \
                                ] \
                            }, \
                            { \
                                "type": "ColumnSet", \
                                "columns": [ \
                                    { \
                                        "type": "Column", \
                                        "width": 30, \
                                        "items": [ \
                                            { \
                                                "type": "TextBlock", \
                                                "text": "Agent Id:", \
                                                "weight": "bolder" \
                                            }, \
                                            { \
                                                "type": "TextBlock", \
                                                "text": "Phone Model:", \
                                                "weight": "bolder", \
                                                "spacing": "Small" \
                                            }, \
                                            { \
                                                "type": "TextBlock", \
                                                "text": "Extension:", \
                                                "weight": "bolder", \
                                                "spacing": "Small" \
                                            }, \
                                            { \
                                                "type": "TextBlock", \
                                                "text": "Skill Group(s):", \
                                                "weight": "bolder", \
                                                "spacing": "Small" \
                                            }, \
                                            { \
                                                "type": "TextBlock", \
                                                "text": "Team:", \
                                                "weight": "bolder", \
                                                "spacing": "Small" \
                                            } \
                                        ] \
                                    }, \
                                    { \
                                        "type": "Column", \
                                        "width": 55, \
                                        "items": [ \
                                            { \
                                                "type": "TextBlock", \
                                                "text": "' + agent_id + '", \
                                                "spacing": "Small", \
                                                "color": "Light" \
                                            }, \
                                            { \
                                                "type": "TextBlock", \
                                                "text": "' + phone_model + '", \
                                                "spacing": "Small", \
                                                "color": "Light" \
                                            }, \
                                            { \
                                                "type": "TextBlock", \
                                                "text": "' + extension + '", \
                                                "spacing": "Small", \
                                                "color": "Light" \
                                            }, \
                                            { \
                                                "type": "TextBlock", \
                                                "text": "' + skill_group + '", \
                                                "spacing": "Small", \
                                                "color": "Light" \
                                            }, \
                                            { \
                                                "type": "TextBlock", \
                                                "text": "' + team_name + '", \
                                                "spacing": "Small", \
                                                "color": "Light" \
                                            } \
                                        ] \
                                    } \
                                ], \
                                "spacing": "Padding", \
                                "horizontalAlignment": "Center" \
                            } \
                        ], \
                        "actions": [ \
                            { \
                                "type": "Action.Submit", \
                                "title": "  Verify  " \
                            }, \
                            { \
                                "type": "Action.Submit", \
                                "title": "Needs Modified" \
                            } \
                        ] \
                    } \
                } \
            ] \
        }'

    except Exception as ex:
        print(f"Error in get_webex_card: {str(ex)}")

    finally:
        return payload
