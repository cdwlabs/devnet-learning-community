def test_parse_wifi_channels(test_data):
    expected = [{'two_four_ghz': [1, 11], 'five_ghz': [36, 40, 153, 157, 161, 165], 'profile_name': 'Fake Data'}]
    assert example.parse_wifi_channels(test_data) == expected
