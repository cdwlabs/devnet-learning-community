"""
import for the ipaddress module.
Testing the ipaddress module features.

Replace <EDIT_THIS> with the correct code.
"""

# the import ipaddress line may fail if you're running Python 2.x or Python versions below 3.3.
import ipaddress

# Note that the network and addresses are now ip_network and ip_address objects, which are input as strings.
network1 = ipaddress.ip_network("192.168.2.0/24")
address1 = ipaddress.ip_address("192.168.2.54")
address2 = ipaddress.ip_address("192.168.10.45")


# #xample ipaddress module features. Note the use of methods that belong to the new variables we defined.
def ipaddress_examples(host, network):
    """
    testing some basic ipaddress module features.
    You can find the details for attributes and methods used below in the standard library documentation:
    https://docs.python.org/3/library/ipaddress.html
    """
    print(
        f"""Network {network} is an IPv{network.version} network
  with {network.num_addresses} addresses, {network.broadcast_address} is the broadcast address.
  Is Global: {network.is_global}
  Is Link Local: {network.is_link_local}
  Is Private: {network.is_private}
  Is Multicast: {network.is_multicast}
  Is Loopback: {network.is_loopback}
  Is Reserved: {network.is_reserved}
  This network can be returned with default settings (prefix length): {network}, a netmask: {network.with_netmask},
  prefix length {network.with_prefixlen}, or hostmask (ACL style) {network.with_hostmask}"""
    )


# New function with defaults allocated. You can see the difference when called in the main() function.
def host_in_net(host, network):
    """
    Adding in real validation for if the IP address is in the network.
    This could be done with regular expressions, but the code would be more complex and hard to read.
    """
    if host in network:
        return (
            f"{host} is in network {network} and the broadcast address is <EDIT_THIS>"
        )
    else:
        return f"<EDIT_THIS>"  # Fix the return string. Any string formatting will work (%s, .format, or f-string).


def main():
    # Output of several ipaddress methods and attributes.
    ipaddress_examples(address1, network1)
    # host_in_net testing with real validation! That broadcast IP might need to be fixed though..
    print(host_in_net(address1, network1))
    # The return for this is broken above. It'll need to be fixed to show the correct output.
    print(host_in_net(address2, network1))


if __name__ == "__main__":
    main()
