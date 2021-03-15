"""
Working with text files and IP addresses.
Open a list of IP adddresses and a list of networks and write out which networks the IP addresses belong.

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
        line = line.strip()
        # Make the line an IP address
        line = ipaddress.ip_network(line)
        # Append properly formatted line to list
        IP_NETWORKS.append(line)


# We'll be reusing our new host_in_net check with the lists with a minor change. We won't return anything if there's no match.
def host_in_net(host, network):
    """
    Adding in real validation for if the IP address is in the network.
    This could be done with regular expressions, but the code would be more complex and hard to read.
    """
    if host in network:
        return f"{host} is in network {network}."
    else:
        # pass does nothing.
        pass


# What if we want to do somehting more useful than print the data?
def return_host_list(ip_list, network):
    """
    You may also want to return the data back to the main() fucntion.
    We'll save the responses and return them when called.
    """
    # Used to collect responses from each for loop interation.
    host_status = []
    for host in ip_list:
        # Append adds the new result to the exisintg host_status list, dropping "None" values.
        if host_in_net(host, network) != None:
            host_status.append(host_in_net(host, network))
    return host_status


def hosts_in_networks(ip_list, net_list):
    """
    Interation of networks and hosts to find the full list ofr host to network matches.
    """
    net_status = []
    for network in net_list:
        net_status.append(return_host_list(ip_list, network))
    # sum used to collapse the nested lists into a flat list.
    return sum(net_status, [])


def main():
    # since return_host_list doesn't support a list of networks we selected the sixth network from the list.
    for list_item in return_host_list(IP_ADDRESSES, IP_NETWORKS[5]):
        print(f"From return_host_list - {list_item}")

    # The new function has no limitations and returns all the matches.
    for list_item in hosts_in_networks(IP_ADDRESSES, IP_NETWORKS):
        print(f"From hosts_in_networks - {list_item}")

    # Write a file with the console information. More information on file wirtes can be found here:
    # https://realpython.com/read-write-files-python/
    with open("ipaddress_host_nets.txt", "w") as host_output:
        for list_item in hosts_in_networks(IP_ADDRESSES, IP_NETWORKS):
            # Note that the newline needs be be inserted on write.
            host_output.write(f"{<EDIT_THIS>}\n")


if __name__ == "__main__":
    main()
