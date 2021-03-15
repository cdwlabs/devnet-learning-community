"""
Working with lists in functions.

Replace <EDIT_THIS> with the correct code.
"""

# the import ipaddress line may fail if you're running Python 2.x or Python versions below 3.3.
import ipaddress

# Note that the network and addresses are now ip_network and ip_address objects.
network1 = ipaddress.ip_network("192.168.2.0/24")
address1 = ipaddress.ip_address("192.168.2.54")
address2 = ipaddress.ip_address("192.168.10.45")
# Now we'll have a list of IP addresses to use.
address_list = [address1, address2]


# We'll be reusing our new host_in_net check with the lists.
def host_in_net(host, network):
    """
    Adding in real validation for if the IP address is in the network.
    This could be done with regular expressions, but the code would be more complex and hard to read.
    """
    if host in network:
        return f"{host} is in network {network}."
    else:
        return f"The address {host} isn't in network {network}."


# how do we handle a list of IPs?
def check_host_list(ip_list, network):
    """
    Functions can call other functions.
    For loops can be used to process iterables (list, dictionaries, tuples, etc.)
    We'll print the responses as they come back.
    """
    for host in ip_list:
        print(host_in_net(<EDIT_THIS>, network))


# What if we want to do somehting more useful than print the data?
def return_host_list(ip_list, network):
    """
    You may also want to return the data back to the main() fucntion.
    We'll save the responses and return them when called.
    """
    # Used to collect responses from each for loop interation.
    host_status = []
    for host in ip_list:
        current_host = host_in_net(host, network)
        # Append adds the new result to the exisintg host_status list.
        host_status.append(<EDIT_THIS>)
    return host_status


def main():
    check_host_list(address_list, network1)
    print(return_host_list(address_list, network1))
    # Hmmm... that's not great. Dumping the whole list is hard to read. How about we make that more readable.
    for list_item in return_host_list(address_list, network1):
        print(list_item)
    # A more advanced version of printing a list would use a feature called a list comprehension.
    # https://realpython.com/list-comprehension-python/
    # This has the beneift of being a single line and being very easy to read.
    [print(list_item) for list_item in return_host_list(address_list, network1)]


if __name__ == "__main__":
    main()
