import example
import pytest

@pytest.fixture
def test_data():
    data = [
        {
            "name": "Fake Data",
            "twoFourGhzSettings": {
                "maxPower": 14,
                "minPower": 5,
                "minBitrate": 11,
                "validAutoChannels": [ 1, 11 ]
            },
            "fiveGhzSettings": {
                "maxPower": 11,
                "minPower": 9,
                "minBitrate": 12,
                "validAutoChannels": [
                    36,
                    40,
                    153,
                    157,
                    161,
                    165
                ],
                "channelWidth": "auto"
            }
        }
    ]
    return(data)


def test_print_two_four_ghz_chan(capsys, test_data):
    expected = 'Profile Fake Data has 2.4 GHz auto channels: [1, 11]\n'
    example.print_two_four_ghz_chan(test_data)
    captured = capsys.readouterr()
    assert expected == captured.out


def test_parse_max_power(test_data):
    expected = [{'two_four_ghz': 14, 'five_ghz': 11, 'profile_name': 'Fake Data'}]
    assert example.parse_max_power(test_data) == expected