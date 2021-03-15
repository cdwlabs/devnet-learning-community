"""
Basic script for string formatting.

Replace <EDIT_THIS> with the correct code.
"""

network1 = "192.168.2.0/24"
address1 = "192.168.2.54"

# Simple concatentated string printing...
print(address1 + " is in network " + network1 + ".")

# That works, but what if we try a different address? Create a new IP address for the next test.
address2 = <EDIT_THIS> #Any IP will work. Since they're not validated (yet) any string would work.

print(f"{address2} is in network {network1}.")

# OK, how about doing this with a list of IP addresses?
ip_list = [address1, address2]
for ip in ip_list:
    # printing in the loop is the same as printing outside of it. Just need the right variables.
    print(f"<EDIT_THIS> is in the network {network1}.")
