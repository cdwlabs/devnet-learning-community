import json
import pathlib


def read_data(filename):
    # Read in some static JSON data
    # In the real world, you might have other functions to pull from an API 
    path = pathlib.Path.cwd() / filename
    with open(path, mode='r') as file_data:
        data = json.load(file_data)
    return(data)


def parse_wifi_channels(data):
    # Create a list of dictionaries containing valid channels and name
    chan_list = []
    for profile in data:
        channels = {}
        channels['two_four_ghz'] = profile['twoFourGhzSettings']['validAutoChannels']
        channels['five_ghz'] = profile['fiveGhzSettings']['validAutoChannels']
        channels['profile_name'] = profile['name']
        chan_list.append(channels)
    return(chan_list)


def print_two_four_ghz_chan(data):
    # Iterate through list printing name and channel for 2.4 GHz band
    all_channels = parse_wifi_channels(data)
    for profile in all_channels:
        print(f'Profile {profile["profile_name"]} has 2.4 GHz auto channels: {profile["two_four_ghz"]}')


def print_five_ghz_chan(data):
    # Iterate through list printing name and channel for 5 GHz band
    all_channels = parse_wifi_channels(data)
    for profile in all_channels:
        print(f'Profile {profile["profile_name"]} has 5 GHz auto channels: {profile["five_ghz"]}')


def parse_max_power(data):
    # Create a list of dictionaries containing max power levels and name
    power_list = []
    for profile in data:
        max_power = {}
        max_power['two_four_ghz'] = profile['twoFourGhzSettings']['maxPower']
        max_power['five_ghz'] = profile['twoFourGhzSettings']['maxPower']
        max_power['profile_name'] = profile['name']
        power_list.append(max_power)
    return(power_list)


def print_max_power(data):
    # Iterate through list printing name and max power for each band
    power_data = parse_max_power(data)
    for profile in power_data:
        print(f'Profile {profile["profile_name"]} has the 5.0 GHz max power at {profile["five_ghz"]} dBm')
        print(f'Profile {profile["profile_name"]} has the 2.4 GHz max power at {profile["two_four_ghz"]} dBm')


def main():
    # Using a python code pattern to execute as a script
    my_data = read_data('data.json')
    print_two_four_ghz_chan(my_data)
    print_five_ghz_chan(my_data)
    print_max_power(my_data)


if __name__ == "__main__":
    # Execute the script only when run but not when imported
    main()
