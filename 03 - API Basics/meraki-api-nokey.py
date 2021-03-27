import requests
import creds
from pprint import pprint


def create_org(apikey):
    # Example of a POST method to creat an organization in the Meraki Dashboard
    url = "https://api.meraki.com/api/v1/organizations"

    payload = '{"name": "DevNet Tset Org"}'
    headers = {"X-Cisco-Meraki-API-Key": f"{apikey}", "Content-Type": "application/json"}

    response = requests.request("POST", url, headers=headers, data=payload)

    org_data = response.json()

    print("Creating Organization")
    print("-" * 12)
    pprint(org_data)
    print("-" * 12 + "\n")
    return org_data["id"]


def list_org(org_id, apikey):
    # List the org just created via a GET method request
    url = f"https://api.meraki.com/api/v1/organizations/{org_id}"

    payload = {}
    headers = {"X-Cisco-Meraki-API-Key": f"{apikey}"}

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        org_data = response.json()

        print("Show Created Organization")
        print("-" * 12)
        pprint(org_data)
        print("-" * 12 + "\n")
    else:
        print("Organization not found")


def update_org(org_id, apikey):
    # Change the name of the org via the PUT method
    url = f"https://api.meraki.com/api/v1/organizations/{org_id}"

    payload = '{"name": "DevNet Test Org"\n}'
    headers = {"X-Cisco-Meraki-API-Key": f"{apikey}", "Content-Type": "application/json"}

    response = requests.request("PUT", url, headers=headers, data=payload)

    org_data = response.json()

    print("Show Updated Organization")
    print("-" * 12)
    pprint(org_data)
    print("-" * 12 + "\n")


def delete_org(org_id, apikey):
    # Remove the org via a DELETE method call
    url = f"https://api.meraki.com/api/v1/organizations/{org_id}"

    payload = {}
    headers = {"X-Cisco-Meraki-API-Key": f"{apikey}"}

    response = requests.request("DELETE", url, headers=headers, data=payload)

    if response.status_code == 204:
        print("-" * 12)
        print(f"Organization {org_id} deleted")
        print("-" * 12 + "\n")
    else:
        print("Org Deletion unsuccessful")


def main():
    apikey = creds.apiKey

    # Create the org and store the ID in a variable
    org_id = create_org(apikey)

    # List Orgs with the Org ID returned from creating it
    list_org(org_id, apikey)

    # Update the org name
    update_org(org_id, apikey)

    # Delete the org
    delete_org(org_id, apikey)

    # Check to see if the org exists after deletion.
    list_org(org_id, apikey)


if __name__ == "__main__":
    main()
