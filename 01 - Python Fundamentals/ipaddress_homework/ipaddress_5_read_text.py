"""
Working with text files and IP addresses.
We'll be reusing much fo the code from the previous example and just adding files instead of a defined lists.

Replace <EDIT_THIS> with the correct code.
"""

# the import ipaddress line may fail if you're running Python 2.x or Python versions below 3.3.
import ipaddress


# Open the IP address list
with open("ipaddress_hosts.txt", mode="r") as ip_file:
    IP_ADDRESSES = []
    for line in ip_file:
        # strip the newline character from the end
        line = line.strip()
        # Make the line an IP address
        line = ipaddress.ip_address(line)
        # Append properly formatted line to list
        IP_ADDRESSES.append(line)


# Open IP network list
with open("ipaddress_nets.txt", mode="r") as net_file:
    IP_NETWORKS = []
    for line in net_file:
        # strip the newline character from the end
        line = <EDIT_THIS>
        # Make the line an IP address
        line = <EDIT_THIS>
        # Append properly formatted line to list
        <EDIT_THIS>
    # Functionally identical list comprehension that would replace the for loop:
    # [IP_NETWORKS.append(ipaddress.ip_network(line.strip())) for line in net_file]
    # Can be dense to read, but you can see how the loop is collapsed into this one-liner.


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


# What if we want to do somehting more useful than print the data?
def return_host_list(ip_list, network):
    """
    You may also want to return the data back to the main() fucntion.
    We'll save the responses and return them when called.
    """
    # Used to collect responses from each for loop interation.
    host_status = []
    for host in ip_list:
        # Append adds the new result to the exisintg host_status list.
        host_status.append(host_in_net(host, network))
    return host_status


def main():
    # Calling a list item directly by position in list:
    print(return_host_list(IP_ADDRESSES, IP_NETWORKS[0]))
    # Hmmm... that's not great. Dumping the whole list is hard to read. How about we make that more readable.
    for list_item in return_host_list(IP_ADDRESSES, IP_NETWORKS[1]):
        print(list_item)
    # A more advanced version of printing a list would use a feature called a list comprehension.
    # https://realpython.com/list-comprehension-python/
    # This has the beneift of being a single line and being very easy to read.
    # [print(list_item) for list_item in return_host_list(IP_ADDRESSES, IP_NETWORKS[0])]


if __name__ == "__main__":
    main()
