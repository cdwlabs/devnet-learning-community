import ipaddress


network1 = "192.4.2.0/24"
address1 = "192.168.2.45"
address2 = "192.4.2.54"
address_list = [
    "192.168.0.1",
    "172.16.55.2",
    "224.56.12.4",
    "192.4.2.54",
    "23.61.164.67",
]


def host_in_net(host=address1, net=network1):
    if ipaddress.IPv4Address(host) in ipaddress.IPv4Network(net):
        return f"The host {host} is in network {net}"
    else:
        return f"The host {host} doesn't belong in the network {net}"


def main():
    host = input("Enter a host name:  ")
    network = input("Enter a network with mask:  ")
    print(host_in_net(host, network))


if __name__ == "__main__":
    main()
