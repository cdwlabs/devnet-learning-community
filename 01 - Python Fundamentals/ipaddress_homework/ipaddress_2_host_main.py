"""
Adding in:
Proper script formatting with a main() function and __name__
Consructing a function for our previous example
Reviewing various options for function construction.

Replace <EDIT_THIS> with the correct code.
"""

network1 = "192.168.2.0/24"
address1 = "192.168.2.54"
address2 = "192.168.10.45"


def ip_in_net(host, network):
    """
    Basic function to print the same output as the basic example in the ip_1_output.py file.
    This is a docstring and they're a best practice for functions, as they tell you what the function SHOULD do.
    """
    print(f"{host} is in network {network}.")


def ip_in_net_return(host, network):
    """
    Improved function that returns data instead of printing to the screen.
    This configuration makes passing data from a function into the main function easy.
    The function is called differently if you want the data on the console though. You can see this in main() below.
    """
    return f"{host} is in network {network}."


# New function with defaults allocated. You can see the difference when called in the main() function.
def ip_in_net_defaults(host=address1, network=network1):
    """
    This function has defaults, so the host and network are now optional. You can see the difference when it's called in main() below.
    Hard-coding defaults is great if a function will generally have one behavior, but you want to overrie it sometimes.
    """
    return f"<EDIT_THIS>"  # Fix the return string. Any string formatting will work (%s, .format, or f-string).


def main():
    ip_in_net(address1, network1)
    print(ip_in_net_return(<EDIT_THIS>, <EDIT_THIS>))
    print(ip_in_net_defaults())


if __name__ == "__main__":
    main()
