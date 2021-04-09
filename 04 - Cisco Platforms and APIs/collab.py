# ---------------------------------------------------------#
# Application:	04-Intro to Cisco Platforms and APIs
# Module:		collab.py
# Author:		CDW
# Summary:
# 	Example code to highlight collab APIs:
#     * CUCM
#     * CCX
#     * Webex
#
# Pre-requisites:
#  pip install requests
#  pip install beautifulsoup4
#  pip install lxml
#
# AXL Reference:
#  https://developer.cisco.com/docs/axl-schema-reference/
#
# CCX Resources (Agents/Supervisors) Reference:
#  https://developer.cisco.com/docs/contact-center-express/#!get-list-of-resources/get-list-of-resources
#
# Webex Messages Reference:
#  https://developer.webex.com/docs/api/v1/messages
# --------------------------------------------------------#
import os                         # Get Environment variables
import json                       # JSON Parsing
import requests                   # HTTP Client
import urllib3                    # URL functions
from base64 import b64encode      # Basic Authentication encoding
from bs4 import BeautifulSoup     # SOAP response processsing
from cards import webex_card

cucm_version = '12.5'
cucm_host = 'hq-cucm-pub.abc.inc'
ccx_host = 'hq-uccx.abc.inc'
# CDW & Cisco DevNet Customer Discussion room
webex_room_id = 'Y2lzY29zcGFyazovL3VzL1JPT00vZDQ1MDRiZjAtN2RjYS0xMWViLWFjMmYtZjk3OGM5NzVkM2Ix'

# Environment Variables
cucm_user = os.getenv('CUCM_USER')                # CUCM Admin User Id
cucm_password = os.getenv('CUCM_PASSWORD')        # CUCM Admin User Password
ccx_user = os.getenv('CCX_USER')                  # CCX Admin User Id
ccx_password = os.getenv('CCX_PASSWORD')          # CCX Admin User Password
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')          # Webex API Access Token

# Suppress Insecure request warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def cucm_get_device(device_name):
    """
    Sends a POST request to CUCM using SOAP
     Retrieves device owner
    """
    result = False
    user_data = {}
    try:
        url = f"https://{cucm_host}:8443/axl/"
        cm_auth = b64encode(bytes(f"{cucm_user}:{cucm_password}", 'utf-8')).decode("ascii")
        # Set Basic Authorization in the header
        headers = {
            'Authorization': f'Basic {cm_auth}',
            'Content-Type': 'text/xml',
            'SOAPAction': f'CUCM:DB ver={cucm_version}'
        }
        # Payload creates the body of the request
        payload = '''
            <soapenv:Envelope xmlns:soapenv='http://schemas.xmlsoap.org/soap/envelope/' xmlns:ns='http://www.cisco.com/AXL/API/''' + cucm_version + ''''>
                <soapenv:Header/>
                <soapenv:Body>
                    <ns:getPhone sequence="1">
                        <name>''' + device_name + '''</name>
                    </ns:getPhone>
                </soapenv:Body>
            </soapenv:Envelope>
        '''

        # Send the POST and get a response back in XML
        response = requests.request("POST", url, headers=headers, data=payload, verify=False)

        # Check the response code
        if response.status_code == 200:
            # Use Beautiful Soup to parse the SOAP Response
            soup = BeautifulSoup(response.text, 'xml')
            description = soup.find('description').text
            user = soup.find('ownerUserName').text
            model = soup.find('model').text
            pattern = soup.find('pattern').text
            print(f"Found device '{device_name}' with description '{description}', model '{model}', extension '{pattern}', and owner user id '{user}'")
            user_data = {'device_name': device_name, 'description': description, 'model': model, 'extension': pattern, 'user_id': user}
            result = True
        else:
            print(f"Response Status:{response.status_code}:{get_response_status(response.status_code)}")

    except Exception as ex:
        print(f"Error in cucm_get_device: {str(ex)}")

    finally:
        return result, user_data


def ccx_get_agent(user_id):
    """
    Sends a GET request to CCX to retrieve agent information
    """
    result = False
    agent_data = {}
    try:
        url = f"https://{ccx_host}/adminapi/resource"
        ccx_auth = b64encode(bytes(f"{ccx_user}:{ccx_password}", 'utf-8')).decode("ascii")
        # Set Basic Authorization in the header
        headers = {
            'Authorization': f'Basic {ccx_auth}',
            'Accept': 'application/json'
        }
        # Payload creates the body of the request
        payload = None

        # Send the GET and read the response in JSON
        response = requests.request("GET", url, headers=headers, data=payload, verify=False)
        if response.status_code == 200:
            json_data = json.loads(response.text)
            for r in json_data['resource']:
                if user_id.lower() == r['userID']:
                    print(f"Found agent {r['firstName']} {r['lastName']}")
                    agent_data = {'first_name': r['firstName'], 'last_name': r['lastName'],
                                  'skill_group': r['skillMap']['skillCompetency'][0]['skillNameUriPair']['@name'],
                                  'team_name': r['team']['@name']}
            result = True
        else:
            print(f"Response Status:{response.status_code}:{get_response_status(response.status_code)}")

    except Exception as ex:
        print(f"Error in ccx_get_agent: {str(ex)}")

    finally:
        return result, agent_data


def webex_send_message(phone, agent):
    """
    Send a message to a Webex room
    """
    try:
        url = "https://webexapis.com/v1/messages"
        webex_payload = webex_card.get_webex_card(webex_room_id, phone, agent)

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {ACCESS_TOKEN}'
        }
        response = requests.request("POST", url, headers=headers, data=webex_payload)
        if response.status_code == 200:
            print("Successfully sent message to Webex room")
        else:
            print(f"Response Status:{response.status_code}:{get_response_status(response.status_code)}")

    except Exception as ex:
        print(f"Error in webex_send_message: {str(ex)}")

    finally:
        return True


def get_response_status(status_code):
    if status_code == 400:
        return 'Bad Request'
    elif status_code == 401:
        return 'Unauthorized'
    elif status_code == 403:
        return 'Forbidden'
    elif status_code == 404:
        return 'Not Found'
    elif status_code == 405:
        return 'Method Not Allowed'
    elif status_code == 429:
        return 'Too Many Requests'
    elif status_code == 500:
        return 'Internal Server Error'
    elif status_code == 503:
        return 'Service Unavailable'
    else:
        return 'Unknown Status'


if __name__ == '__main__':
    # Get the CUCM phone information
    result, phone_data = cucm_get_device('SEP003C4A832B09')
    if result:
        print('Successfully retrieved CUCM device')

        # Get the Agent information for the device
        result, agent_data = ccx_get_agent(phone_data['user_id'])

        if result:
            print('Successfully retrieved Agent information')
            # Send to Webex room
            webex_send_message(phone_data, agent_data)
