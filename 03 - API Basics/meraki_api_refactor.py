import requests
from pprint import pprint


def create_meraki_request(method, endpoint, headers, payload):
    # Create the request to send to the Meraki API
    url = f"https://api.meraki.com/api/v1/{endpoint}"
    headers = {"X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0", **headers}
    response = requests.request(method, url, headers=headers, data=payload)
    return response


def print_output(title, data):
    # Create a repeatable print format
    print(title)
    print("-" * 12)
    pprint(data)
    print("-" * 12 + "\n")


def create_org():
    # Example of a POST method to creat an organization in the Meraki Dashboard
    payload = '{"name": "DevNet Tset Org"}'
    headers = {"Content-Type": "application/json"}
    response = create_meraki_request("POST", "organizations", headers, payload)
    org_data = response.json()
    print_output("Creating Organization", org_data)
    return org_data["id"]


def list_org(org_id):
    # List the org just created via a GET method request
    endpoint = f"organizations/{org_id}"
    payload = {}
    headers = {}
    response = create_meraki_request("GET", endpoint, headers, payload)

    if response.status_code == 200:
        org_data = response.json()
        print_output("Show Created  Organization", org_data)
    else:
        print("Organization not found")


def update_org(org_id):
    # Change the name of the org via the PUT method
    endpoint = f"organizations/{org_id}"
    payload = '{"name": "DevNet Test Org"\n}'
    headers = {"Content-Type": "application/json"}
    response = create_meraki_request("PUT", endpoint, headers, payload)
    org_data = response.json()
    print_output("Show Updated  Organization", org_data)


def delete_org(org_id):
    # Remove the org via a DELETE method call
    endpoint = f"organizations/{org_id}"
    payload = {}
    headers = {}
    response = create_meraki_request("DELETE", endpoint, headers, payload)
    if response.status_code == 204:
        print("-" * 12)
        print(f"Organization {org_id} deleted")
        print("-" * 12 + "\n")
    else:
        print("Org Deletion unsuccessful")


def main():
    # Create the org and store the ID in a variable
    org_id = create_org()
    # List Orgs with the Org ID returned from creating it
    list_org(org_id)
    # Update the org name
    update_org(org_id)
    # Delete the org
    delete_org(org_id)
    # Check to see if the org exists after deletion.
    list_org(org_id)


if __name__ == "__main__":
    main()