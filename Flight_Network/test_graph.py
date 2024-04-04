import pytest
import json
import hashlib
from skeleton_graph import *


def get_hash(object):
    h = hashlib.sha256(json.dumps(object, sort_keys=True).encode())
    return (h.hexdigest())


def test_create_flight_network():
    flight_net = create_flight_network('flight_network.csv', 1)
    assert get_hash(
        flight_net) == "25437fbf39bd31f1a82552520801866d1d9be75064a9d722ddc6a8f2bf6a0c5b"
    flight_net = create_flight_network('flight_network.csv', 2)
    assert get_hash(
        flight_net) == "0d461badf591a7287d668bb7b4c7cb90aa0214fd58a8d488c4881b4adf9a39b0"


def test_flight_connection():
    G = create_flight_network('flight_network.csv', 1)

    # Test case 1
    f = get_flight_connections(G, "Dubai", 'o')
    assert get_hash(
        f) == "b5d0417e2053a535e2d90cfecd5b97ac96426d82fcf2be1b3303ea84e6bc0a57"
    fnum = get_number_of_flight_connections(G, "Dubai", 'o')
    assert get_hash(
        fnum) == "e629fa6598d732768f7c726b4b621285f9c3b85303900aa912017db7617d8bdb"

    # Test case 2
    f = get_flight_connections(G, "Sao Paulo", 'o')
    assert get_hash(
        f) == "8a7d421348bf480ed237be9120e7ba31163d8098f0a5d6e235717dff709c5a0d"
    fnum = get_number_of_flight_connections(G, "Sao Paulo", 'o')
    assert get_hash(
        fnum) == "d4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35"

    # Test case 3
    f = get_flight_connections(G, "London", 'o')
    assert get_hash(
        f) == "44810ce3aee71592fd7686eef9a098d42c706effa5310ca78edf4aa265530bec"
    fnum = get_number_of_flight_connections(G, "London", 'o')
    assert get_hash(
        fnum) == "d4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35"

    # Test case 4
    f = get_flight_connections(G, "Detroit", 'o')
    assert get_hash(
        f) == "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945"
    fnum = get_number_of_flight_connections(G, "Detroit", 'o')
    assert get_hash(
        fnum) == "5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9"

    # Test case 5
    f = get_flight_connections(G, "Seattle", 'i')
    assert get_hash(
        f) == "9313a452841b82427b33ca05964558ff9ae3fd012cfee98f81e4b6d2a363572d"
    fnum = get_number_of_flight_connections(G, "Seattle", 'i')
    assert get_hash(
        fnum) == "4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce"

    # Test case 6
    f = get_flight_connections(G, "Dubai", 'i')
    assert get_hash(
        f) == "08982c4a99f1205fb781b2df34460e7839fd5a9c7ac834149baf40482eadbbbd"
    fnum = get_number_of_flight_connections(G, "Dubai", 'i')
    assert get_hash(
        fnum) == "e629fa6598d732768f7c726b4b621285f9c3b85303900aa912017db7617d8bdb"

    # Test case 7
    f = get_flight_connections(G, "Toronto", 'i')
    assert get_hash(
        f) == "148e112f2143f4d0a9a5e69c61a004d8f561b3626c93b291d7efdf1cd6041aca"
    fnum = get_number_of_flight_connections(G, "Toronto", 'i')
    assert get_hash(
        fnum) == "4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a"

    # Test case 8
    f = get_flight_connections(G, "Karachi", 'i')
    assert get_hash(
        f) == "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945"
    fnum = get_number_of_flight_connections(G, "Karachi", 'i')
    assert get_hash(
        fnum) == "5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9"


def test_flight_details():
    G1 = create_flight_network('flight_network.csv', 1)
    G2 = create_flight_network('flight_network.csv', 2)

    # Test case 1
    dur = get_flight_details(G1, "Dubai", "Seattle")
    assert get_hash(
        dur) == "52efd2aad05d27e3eac3665b82f2bffa6da52351ce871c1c28e4ba69b40ea3e6"

    dist = get_flight_details(G2, "Dubai", "Seattle")
    assert get_hash(
        dist) == "7078c7f8564ee0300ee371c8511553483f3465110b7b962bd63822b541aa8892"

    # Test case 2
    dur = get_flight_details(G1, "Sao Paulo", "Lima")
    assert get_hash(
        dur) == "377adeb4cd4096adc7ca64b533938cffc6294a9b3534f883b2336a26252cda9a"

    dist = get_flight_details(G2, "Sao Paulo", "Lima")
    assert get_hash(
        dist) == "fa66df2f99cec3fe2cb72c2286083c4cbf0897f9697d0a63f142a46138610a86"

    # Test case 3
    dur = get_flight_details(G1, "London", "Mexico City")
    assert get_hash(
        dur) == "35c71bd7eaf4607047bb7c186d17251942204229b897e033923b13dc8ce2d109"

    dist = get_flight_details(G2, "London", "Mexico City")
    assert get_hash(
        dist) == "c4b606ff15bd9b86c37e4fbccf8b5f7e57890c6f675e7a250538e297b4c1303e"

    # Test case 4
    dur = get_flight_details(G1, "Karachi", "Dubai")
    assert get_hash(
        dur) == "74234e98afe7498fb5daf1f36ac2d78acc339464f950703b8c019892f982b90b"

    dist = get_flight_details(G2, "Karachi", "Dubai")
    assert get_hash(
        dist) == "74234e98afe7498fb5daf1f36ac2d78acc339464f950703b8c019892f982b90b"

    # Test case 5
    dur = get_flight_details(G1, "Detroit", "Denver")
    assert get_hash(
        dur) == "74234e98afe7498fb5daf1f36ac2d78acc339464f950703b8c019892f982b90b"

    dist = get_flight_details(G2, "Detroit", "Denver")
    assert get_hash(
        dist) == "74234e98afe7498fb5daf1f36ac2d78acc339464f950703b8c019892f982b90b"

    # Test case 6
    dur = get_flight_details(G1, "Seattle", "Detroit")
    assert get_hash(
        dur) == "1bad6b8cf97131fceab8543e81f7757195fbb1d36b376ee994ad1cf17699c464"

    dist = get_flight_details(G2, "Seattle", "Detroit")
    assert get_hash(
        dist) == "1bad6b8cf97131fceab8543e81f7757195fbb1d36b376ee994ad1cf17699c464"

    # Test case 7
    dur = get_flight_details(G1, "Dubai", "Calgary")
    assert get_hash(
        dur) == "1bad6b8cf97131fceab8543e81f7757195fbb1d36b376ee994ad1cf17699c464"

    dist = get_flight_details(G2, "Dubai", "Calgary")
    assert get_hash(
        dist) == "1bad6b8cf97131fceab8543e81f7757195fbb1d36b376ee994ad1cf17699c464"

    # Test case 8
    dur = get_flight_details(G1, "Toronto", "Montreal")
    assert get_hash(
        dur) == "1bad6b8cf97131fceab8543e81f7757195fbb1d36b376ee994ad1cf17699c464"

    dist = get_flight_details(G2, "Toronto", "Montreal")
    assert get_hash(
        dist) == "1bad6b8cf97131fceab8543e81f7757195fbb1d36b376ee994ad1cf17699c464"


def test_add_flight():
    # Testing for creating new flights between existing cities
    # Test Case 1
    G1 = create_flight_network('flight_network.csv', 1)
    G2 = create_flight_network('flight_network.csv', 2)
    add_flight(G1, "Dubai", "Vancouver", 950)
    assert get_hash(
        G1) == "f6160d7df43075b895d85101d5e44d373610b6fd5b7fc0fa44d93c0b6c5fe60d"
    add_flight(G2, "Dubai", "Vancouver", 7333)
    assert get_hash(
        G2) == "2e855502cb36460d40a66d2680abefe75bc3e1cc3d7433ac51fb3c43bf36aaf3"

    # Test Case 2
    G1 = create_flight_network('flight_network.csv', 1)
    G2 = create_flight_network('flight_network.csv', 2)
    add_flight(G1, "Toronto", "Los Angeles", 330)
    assert get_hash(
        G1) == "887f5e47e7cc5582862ada7d70713ca4963852ab16171552083d68d06304238d"
    add_flight(G2, "Toronto", "Los Angeles", 2183)
    assert get_hash(
        G2) == "f2be6a33787e61db120e8ae8812c90079e324abcd3d10d570505415543cbb82a"

    # Test Case 3
    G1 = create_flight_network('flight_network.csv', 1)
    G2 = create_flight_network('flight_network.csv', 2)
    add_flight(G1, "London", "Boston", 475)
    assert get_hash(
        G1) == "f6065a03dbab679892cbe6ec8ca595adfc9148a2684101256963059be3bf2218"
    add_flight(G2, "London", "Boston", 3274)
    assert get_hash(
        G2) == "1b27b8bc0c0df2556883a1c6cc30bbad247b14b32cf9467cef08ed2d99f43cab"

    # Test Case 4
    G1 = create_flight_network('flight_network.csv', 1)
    G2 = create_flight_network('flight_network.csv', 2)
    add_flight(G1, "Sao Paulo", "Rio de Janeiro", 65)
    assert get_hash(
        G1) == "d4b85825bb25fd7637d0cea29c713ba0f809d4a49133a37ffedd90ba7026c309"
    add_flight(G2, "Sao Paulo", "Rio de Janeiro", 210)
    assert get_hash(
        G2) == "34d14c34d68fe8f168a033c8a0f5d9d5b4570283e0516c487afa6aa70ca14f23"

    # Testing for the cases when origin city is not in the network
    # Test Case 1
    G1 = create_flight_network('flight_network.csv', 1)
    G2 = create_flight_network('flight_network.csv', 2)
    add_flight(G1, "Mumbai", "Dubai", 200)
    assert get_hash(
        G1) == "25437fbf39bd31f1a82552520801866d1d9be75064a9d722ddc6a8f2bf6a0c5b"
    add_flight(G2, "Mumbai", "Dubai", 1202)
    assert get_hash(
        G2) == "0d461badf591a7287d668bb7b4c7cb90aa0214fd58a8d488c4881b4adf9a39b0"

    # Test Case 2
    G1 = create_flight_network('flight_network.csv', 1)
    G2 = create_flight_network('flight_network.csv', 2)
    add_flight(G1, "Detroit", "Orlando", 165)
    assert get_hash(
        G1) == "25437fbf39bd31f1a82552520801866d1d9be75064a9d722ddc6a8f2bf6a0c5b"
    add_flight(G2, "Detroit", "Orlando", 964)
    assert get_hash(
        G2) == "0d461badf591a7287d668bb7b4c7cb90aa0214fd58a8d488c4881b4adf9a39b0"

    # Test Case 3
    G1 = create_flight_network('flight_network.csv', 1)
    G2 = create_flight_network('flight_network.csv', 2)
    add_flight(G1, "San Diego", "Miami", 285)
    assert get_hash(
        G1) == "25437fbf39bd31f1a82552520801866d1d9be75064a9d722ddc6a8f2bf6a0c5b"
    add_flight(G2, "San Diego", "Miami", 2275)
    assert get_hash(
        G2) == "0d461badf591a7287d668bb7b4c7cb90aa0214fd58a8d488c4881b4adf9a39b0"

    # Testing for the cases when destination city is not in the network
    # Test Case 1
    G1 = create_flight_network('flight_network.csv', 1)
    G2 = create_flight_network('flight_network.csv', 2)
    add_flight(G1, "Seattle", "Phoenix", 170)
    assert get_hash(
        G1) == "25437fbf39bd31f1a82552520801866d1d9be75064a9d722ddc6a8f2bf6a0c5b"
    add_flight(G2, "Seattle", "Phoenix", 1113)
    assert get_hash(
        G2) == "0d461badf591a7287d668bb7b4c7cb90aa0214fd58a8d488c4881b4adf9a39b0"

    # Test Case 2
    G1 = create_flight_network('flight_network.csv', 1)
    G2 = create_flight_network('flight_network.csv', 2)
    add_flight(G1, "Dubai", "Karachi", 115)
    assert get_hash(
        G1) == "25437fbf39bd31f1a82552520801866d1d9be75064a9d722ddc6a8f2bf6a0c5b"
    add_flight(G2, "Dubai", "Karachi", 742)
    assert get_hash(
        G2) == "0d461badf591a7287d668bb7b4c7cb90aa0214fd58a8d488c4881b4adf9a39b0"

    # Test Case 3
    G1 = create_flight_network('flight_network.csv', 1)
    G2 = create_flight_network('flight_network.csv', 2)
    add_flight(G1, "Lima", "Cancun", 335)
    assert get_hash(
        G1) == "25437fbf39bd31f1a82552520801866d1d9be75064a9d722ddc6a8f2bf6a0c5b"
    add_flight(G2, "Lima", "Cancun", 2391)
    assert get_hash(
        G2) == "0d461badf591a7287d668bb7b4c7cb90aa0214fd58a8d488c4881b4adf9a39b0"

    # Testing for updating weights in existing flights
    # Test Case 1
    G1 = create_flight_network('flight_network.csv', 1)
    G2 = create_flight_network('flight_network.csv', 2)
    add_flight(G1, "Toronto", "Calgary", 275)
    assert get_hash(
        G1) == "b19dca59eee14c25ca5f024662eb2bb7af784db2591fd88d1ea45f12810d6983"
    add_flight(G2, "Jamaica", "Dallas", 1550)
    assert get_hash(
        G2) == "5a8b87b5a779debbf5c86aa84c284a1cc74b2e4a123fcc171d1e422161074481"

    # Test Case 2
    G1 = create_flight_network('flight_network.csv', 1)
    G2 = create_flight_network('flight_network.csv', 2)
    add_flight(G1, "Rio de Janeiro", "Buenos Aires", 195)
    assert get_hash(
        G1) == "0d2669efb45c939ddcfade5fbe7aaaad47e2f67d006e46c762684d8c08056f1a"
    add_flight(G2, "Washington", "Kansas", 955)
    assert get_hash(
        G2) == "88470e29a69888152b4b0978990546fec7f6130703c4008ab0b920515ac91be9"

    # Test Case 3
    G1 = create_flight_network('flight_network.csv', 1)
    G2 = create_flight_network('flight_network.csv', 2)
    add_flight(G1, "Caracas", "Mexico City", 305)
    assert get_hash(
        G1) == "d5e537921cbbac69b8b612a90a104341ff27677a953b32a2bda46fdf9b56ae7d"
    add_flight(G2, "Barcelona", "Mexico City", 5930)
    assert get_hash(
        G2) == "51af477944b032bb4104009389f2b5f3d1b6941f151d0a625990ac6ea0867e12"

    # Test Case 4
    G1 = create_flight_network('flight_network.csv', 1)
    G2 = create_flight_network('flight_network.csv', 2)
    add_flight(G1, "Dubai", "Seattle", 890)
    assert get_hash(
        G1) == "2066aa659b10728c8a5dff440740fac6697cba18911b90e55cd60affb673e3a7"
    add_flight(G2, "Dubai", "Seattle", 7405)
    assert get_hash(
        G2) == "4c7df7807ac185e07c5bd00c180948cd3aa1730409be8ae8a1dcd47ab57d723e"


def test_add_airport():
    # Testing for creating new airports in different cities for graph with durations
    # Test Case 1
    G1 = create_flight_network('flight_network.csv', 1)
    add_airport(G1, "Karachi", "Dubai", 115)
    assert get_hash(
        G1) == "41bc62a3c2464555fdc0a580b000aec5b3a18e447714355f4ad9ebd84b9b6318"

    # Test Case 2
    G1 = create_flight_network('flight_network.csv', 1)
    add_airport(G1, "Detroit", "Toronto", 75)
    assert get_hash(
        G1) == "484e4ebe722a362c39d6cf96fcd7319079fb602877a70e5f2db7c3bd8bcd1130"

    # Test Case 3
    G1 = create_flight_network('flight_network.csv', 1)
    add_airport(G1, "San Diego", "Los Angeles", 65)
    assert get_hash(
        G1) == "3ab6181324f3eb56fba98a9376aae5cdd394dee53cdd5e99b7dae7db39362e82"

    # Test Case 4
    G1 = create_flight_network('flight_network.csv', 1)
    add_airport(G1, "Santiago", "Rio de Janeiro", 250)
    assert get_hash(
        G1) == "ca7eae19fa366ef54fbad0ab16f498ed4b2238319e2eec6d046e4a7d80212b4a"

    # Testing for cases when airport already exists in that city for graph with durations
    # Test Case 1
    G1 = create_flight_network('flight_network.csv', 1)
    add_airport(G1, "Toronto", "Calgary", 275)
    assert get_hash(
        G1) == "25437fbf39bd31f1a82552520801866d1d9be75064a9d722ddc6a8f2bf6a0c5b"

    # Test Case 2
    G1 = create_flight_network('flight_network.csv', 1)
    add_airport(G1, "Rio de Janeiro", "Buenos Aires", 195)
    assert get_hash(
        G1) == "25437fbf39bd31f1a82552520801866d1d9be75064a9d722ddc6a8f2bf6a0c5b"

    # Test Case 3
    G1 = create_flight_network('flight_network.csv', 1)
    add_airport(G1, "Caracas", "Mexico City", 305)
    assert get_hash(
        G1) == "25437fbf39bd31f1a82552520801866d1d9be75064a9d722ddc6a8f2bf6a0c5b"

    # Testing for creating new airports in different cities for graph with distances
    # Test Case 1
    G2 = create_flight_network('flight_network.csv', 2)
    add_airport(G2, "Mumbai", "Dubai", 1202)
    assert get_hash(
        G2) == "ce54c5adfc74aa1cd6848c69125b34ee97365a740b86d52b215d90fa697113ed"

    # Test Case 2
    G2 = create_flight_network('flight_network.csv', 2)
    add_airport(G2, "Detroit", "Orlando", 964)
    assert get_hash(
        G2) == "5d34dcd23e7c771b3b75535a0fbc29f169c21bacd44133d7694d052646cf8a45"

    # Test Case 3
    G2 = create_flight_network('flight_network.csv', 2)
    add_airport(G2, "San Diego", "Miami", 2275)
    assert get_hash(
        G2) == "85037654f269e690a027977477f24bb87d0881e7ca8ecab35926d4232b0bf65b"

    # Test Case 4
    G2 = create_flight_network('flight_network.csv', 2)
    add_airport(G2, "Phoenix", "Seattle", 1113)
    assert get_hash(
        G2) == "afdc6e91fb4631ec20c4675f32b266cf2daae292171a079e834da4560d1b278e"

    # Testing for cases when airport already exists in that city for graph with distances
    # Test Case 1
    G2 = create_flight_network('flight_network.csv', 2)
    add_airport(G2, "Jamaica", "Dallas", 1550)
    assert get_hash(
        G2) == "0d461badf591a7287d668bb7b4c7cb90aa0214fd58a8d488c4881b4adf9a39b0"

    # Test Case 2
    G2 = create_flight_network('flight_network.csv', 2)
    add_airport(G2, "Washington", "Kansas", 955)
    assert get_hash(
        G2) == "0d461badf591a7287d668bb7b4c7cb90aa0214fd58a8d488c4881b4adf9a39b0"

    # Test Case 3
    G2 = create_flight_network('flight_network.csv', 2)
    add_airport(G2, "Barcelona", "Mexico City", 5930)
    assert get_hash(
        G2) == "0d461badf591a7287d668bb7b4c7cb90aa0214fd58a8d488c4881b4adf9a39b0"


def test_secondary_flight():
    G = create_flight_network('flight_network.csv', 1)
    # Testing for valid cities
    # Test case 1
    fll = get_secondary_flights(G, "Dubai")
    assert get_hash(
        fll) == "ce4af28792996d4e7a3379b93f38db618de4dff0afe58d27026c07100bda6d73"

    # Test case 2
    fll = get_secondary_flights(G, "Sao Paulo")
    assert get_hash(
        fll) == "b5d0417e2053a535e2d90cfecd5b97ac96426d82fcf2be1b3303ea84e6bc0a57"

    # Test case 3
    fll = get_secondary_flights(G, "London")
    assert get_hash(
        fll) == "e88f34159d4f1587195bef60dbe7da0e05b4bbbff5ab09681ea10d8431092421"

    # Test case 4
    fll = get_secondary_flights(G, "Seattle")
    assert get_hash(
        fll) == "802e6c0ed78d955dbd239945293861dac3ef654a390ea05e9033b1e988349031"

    # Testing for cities that do not exist in the network
    # Test case 1
    fll = get_secondary_flights(G, "Karachi")
    assert get_hash(
        fll) == "74234e98afe7498fb5daf1f36ac2d78acc339464f950703b8c019892f982b90b"

    # Test case 2
    fll = get_secondary_flights(G, "Detroit")
    assert get_hash(
        fll) == "74234e98afe7498fb5daf1f36ac2d78acc339464f950703b8c019892f982b90b"

    # Test case 3
    fll = get_secondary_flights(G, "Cancun")
    assert get_hash(
        fll) == "74234e98afe7498fb5daf1f36ac2d78acc339464f950703b8c019892f982b90b"

    # Test case 4
    fll = get_secondary_flights(G, "Winnipeg")
    assert get_hash(
        fll) == "74234e98afe7498fb5daf1f36ac2d78acc339464f950703b8c019892f982b90b"


def test_common_airpot():
    G = create_flight_network('flight_network.csv', 1)
    # Test Case 1
    c = counting_common_airports(G, "Dubai", "Seattle")
    assert get_hash(
        c) == "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b"

    # Test Case 2
    c = counting_common_airports(G, "Sao Paulo", "Rio de Janeiro")
    assert get_hash(
        c) == "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b"

    # Test Case 3
    c = counting_common_airports(G, "London", "Jamaica")
    assert get_hash(
        c) == "5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9"

    # Test Case 4
    c = counting_common_airports(G, "Boston", "Chicago")
    assert get_hash(
        c) == "d4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35"

    # Test Case 5
    c = counting_common_airports(G, "Dubai", "Dubai")
    assert get_hash(
        c) == "e629fa6598d732768f7c726b4b621285f9c3b85303900aa912017db7617d8bdb"


def test_remove_flight():
    # Testing for removing existing flights between cities
    # Test case 1
    G1 = create_flight_network('flight_network.csv', 1)
    G2 = create_flight_network('flight_network.csv', 2)
    remove_flight(G1, "Dubai", "Seattle")
    remove_flight(G2, "Dubai", "Seattle")
    assert get_hash(
        G1) == "ff91b80c37c467fe002bea24ef3b5823fb47b7db0d538db369e80b8c8084d8b3"
    assert get_hash(
        G2) == "ede372af35310f42e0aa8ba2bee3ee154b5523fcb997bcb04eac5bb79d8c890a"

    # Test case 2
    G1 = create_flight_network('flight_network.csv', 1)
    G2 = create_flight_network('flight_network.csv', 2)
    remove_flight(G1, "London", "Dubai")
    remove_flight(G2, "London", "Dubai")
    assert get_hash(
        G1) == "7d259b75763edb598dd03d637a5b2819aa53aec1f552ed8e4cdcc8ca8524282d"
    assert get_hash(
        G2) == "f4724531e0957f4defc256afd0085e95972e2e78ae325c69b2a781a57bb36ba2"

    # Test case 3
    G1 = create_flight_network('flight_network.csv', 1)
    G2 = create_flight_network('flight_network.csv', 2)
    remove_flight(G1, "Rio de Janeiro", "Buenos Aires")
    remove_flight(G2, "Rio de Janeiro", "Buenos Aires")
    assert get_hash(
        G1) == "d40cab9fac8ae1ebd16d76e6fd7ec92acc698e2b20406c90f901b8608e74b271"
    assert get_hash(
        G2) == "60c114d7b57ac0267274992fa17724411e89e0374a368b56ad3dec892ed7e9d2"

    # Test case 4
    G1 = create_flight_network('flight_network.csv', 1)
    G2 = create_flight_network('flight_network.csv', 2)
    remove_flight(G1, "Mexico City", "Caracas")
    remove_flight(G2, "Mexico City", "Caracas")
    assert get_hash(
        G1) == "922ed6d69d3d5ca0589518189588ce49755fb9c8c120d838d0fe2cdbbb4441f8"
    assert get_hash(
        G2) == "633335a8be090f046f46d62a7d3b2e71c492f6bb87d25390ae3980db47283816"

    # Test case 5
    G1 = create_flight_network('flight_network.csv', 1)
    G2 = create_flight_network('flight_network.csv', 2)
    remove_flight(G1, "Jamaica", "Dallas")
    remove_flight(G2, "Jamaica", "Dallas")
    assert get_hash(
        G1) == "60fc0e64238f2250142aa7c7bc8fdc873de826b513be2f6bcc05bab53b89b0be"
    assert get_hash(
        G2) == "a1cc7eef1c50b7cad8ea8ff327143b04f2a9da0ee3c42653f5bc0a4f7c6bf558"

    # Test case 6
    G1 = create_flight_network('flight_network.csv', 1)
    G2 = create_flight_network('flight_network.csv', 2)
    remove_flight(G1, "Barcelona", "Mexico City")
    remove_flight(G2, "Barcelona", "Mexico City")
    assert get_hash(
        G1) == "e35951c4dc2ae2cc51a415e90dd403ba7fbc86cf48393e7f4003f0af04953973"
    assert get_hash(
        G2) == "59ac179a2175cf4b91b0096d19cf4a5595f7c810075a1fa3739956eeae745047"

    # Testing for the cases when origin city is not in the network
    # Test case 1
    G1 = create_flight_network('flight_network.csv', 1)
    G2 = create_flight_network('flight_network.csv', 2)
    remove_flight(G1, "Mumbai", "Dubai")
    remove_flight(G2, "Mumbai", "Dubai")
    assert get_hash(
        G1) == "25437fbf39bd31f1a82552520801866d1d9be75064a9d722ddc6a8f2bf6a0c5b"
    assert get_hash(
        G2) == "0d461badf591a7287d668bb7b4c7cb90aa0214fd58a8d488c4881b4adf9a39b0"

    # Test case 2
    G1 = create_flight_network('flight_network.csv', 1)
    G2 = create_flight_network('flight_network.csv', 2)
    remove_flight(G1, "Detroit", "Orlando")
    remove_flight(G2, "Detroit", "Orlando")
    assert get_hash(
        G1) == "25437fbf39bd31f1a82552520801866d1d9be75064a9d722ddc6a8f2bf6a0c5b"
    assert get_hash(
        G2) == "0d461badf591a7287d668bb7b4c7cb90aa0214fd58a8d488c4881b4adf9a39b0"

    # Test case 3
    G1 = create_flight_network('flight_network.csv', 1)
    G2 = create_flight_network('flight_network.csv', 2)
    remove_flight(G1, "San Diego", "Miami")
    remove_flight(G2, "San Diego", "Miami")
    assert get_hash(
        G1) == "25437fbf39bd31f1a82552520801866d1d9be75064a9d722ddc6a8f2bf6a0c5b"
    assert get_hash(
        G2) == "0d461badf591a7287d668bb7b4c7cb90aa0214fd58a8d488c4881b4adf9a39b0"

    # Testing for the cases when destination city is not in the network
    # Test case 1
    G1 = create_flight_network('flight_network.csv', 1)
    G2 = create_flight_network('flight_network.csv', 2)
    remove_flight(G1, "Seattle", "Phoenix")
    remove_flight(G2, "Seattle", "Phoenix")
    assert get_hash(
        G1) == "25437fbf39bd31f1a82552520801866d1d9be75064a9d722ddc6a8f2bf6a0c5b"
    assert get_hash(
        G2) == "0d461badf591a7287d668bb7b4c7cb90aa0214fd58a8d488c4881b4adf9a39b0"

    # Test case 2
    G1 = create_flight_network('flight_network.csv', 1)
    G2 = create_flight_network('flight_network.csv', 2)
    remove_flight(G1, "Dubai", "Karachi")
    remove_flight(G2, "Dubai", "Karachi")
    assert get_hash(
        G1) == "25437fbf39bd31f1a82552520801866d1d9be75064a9d722ddc6a8f2bf6a0c5b"
    assert get_hash(
        G2) == "0d461badf591a7287d668bb7b4c7cb90aa0214fd58a8d488c4881b4adf9a39b0"

    # Test case 3
    G1 = create_flight_network('flight_network.csv', 1)
    G2 = create_flight_network('flight_network.csv', 2)
    remove_flight(G1, "Lima", "Cancun")
    remove_flight(G2, "Lima", "Cancun")
    assert get_hash(
        G1) == "25437fbf39bd31f1a82552520801866d1d9be75064a9d722ddc6a8f2bf6a0c5b"
    assert get_hash(
        G2) == "0d461badf591a7287d668bb7b4c7cb90aa0214fd58a8d488c4881b4adf9a39b0"


def test_remove_airport():
    # Testing for removing existing airports
    # Test case 1
    G1 = create_flight_network('flight_network.csv', 1)
    G2 = create_flight_network('flight_network.csv', 2)
    remove_airport(G1, "Boston")
    remove_airport(G2, "Boston")
    assert get_hash(
        G1) == "40bea640fe6cc47ea6b0efbf642d1fd914deee22a8c8d01207d1743885d65479"
    assert get_hash(
        G2) == "ba3a9eace71539adda0ca4e45c306e57e58b8cfda803d7e792e7cad685775819"

    # Test case 2
    G1 = create_flight_network('flight_network.csv', 1)
    G2 = create_flight_network('flight_network.csv', 2)
    remove_airport(G1, "Toronto")
    remove_airport(G2, "Toronto")
    assert get_hash(
        G1) == "72d32d4f029b32910788bb3d03a39a2f585073c7a8fe28703d6a0f8e9d22859c"
    assert get_hash(
        G2) == "db36131db1c4d3f1e91f4e089fbed9227f9f721d13fdd15ecf405cc0da827714"

    # Test case 3
    G1 = create_flight_network('flight_network.csv', 1)
    G2 = create_flight_network('flight_network.csv', 2)
    remove_airport(G1, "Rio de Janeiro")
    remove_airport(G2, "Rio de Janeiro")
    assert get_hash(
        G1) == "b7a0ed59a9591e1e86aa59999a15c57fa4578e39643bbb220a86d0148ee756b2"
    assert get_hash(
        G2) == "180b37a287bd1f9827611e78900e71237e81cefb395a2c63b48fb5ef6890735d"

    # Test case 4
    G1 = create_flight_network('flight_network.csv', 1)
    G2 = create_flight_network('flight_network.csv', 2)
    remove_airport(G1, "Buenos Aires")
    remove_airport(G2, "Buenos Aires")
    assert get_hash(
        G1) == "0933ff84429920528e32923b230236b17963ae85bae156c8554ed9e69b529d35"
    assert get_hash(
        G2) == "99915cfef6d17fef5c8bad0e13c7192eb8e06b610bdb56d4e37f141d82911e0f"

    # Test case 5
    G1 = create_flight_network('flight_network.csv', 1)
    G2 = create_flight_network('flight_network.csv', 2)
    remove_airport(G1, "Caracas")
    remove_airport(G2, "Caracas")
    assert get_hash(
        G1) == "e05e6e68f16229b5733de7b2d946f1e6f4a1b21da838461454b0bb787b3a12b7"
    assert get_hash(
        G2) == "57b3a68b0ba52c613bec3bf11073bb85273544741c1b62de90eb30f338f21811"

    # Testing for the cases when city is not in the network
    # Test case 1
    G1 = create_flight_network('flight_network.csv', 1)
    G2 = create_flight_network('flight_network.csv', 2)
    remove_airport(G1, "Mumbai")
    remove_airport(G2, "Mumbai")
    assert get_hash(
        G1) == "25437fbf39bd31f1a82552520801866d1d9be75064a9d722ddc6a8f2bf6a0c5b"
    assert get_hash(
        G2) == "0d461badf591a7287d668bb7b4c7cb90aa0214fd58a8d488c4881b4adf9a39b0"

    # Test case 2
    G1 = create_flight_network('flight_network.csv', 1)
    G2 = create_flight_network('flight_network.csv', 2)
    remove_airport(G1, "Detroit")
    remove_airport(G2, "Detroit")
    assert get_hash(
        G1) == "25437fbf39bd31f1a82552520801866d1d9be75064a9d722ddc6a8f2bf6a0c5b"
    assert get_hash(
        G2) == "0d461badf591a7287d668bb7b4c7cb90aa0214fd58a8d488c4881b4adf9a39b0"

    # Test case 3
    G1 = create_flight_network('flight_network.csv', 1)
    G2 = create_flight_network('flight_network.csv', 2)
    remove_airport(G1, "San Diego")
    remove_airport(G2, "San Diego")
    assert get_hash(
        G1) == "25437fbf39bd31f1a82552520801866d1d9be75064a9d722ddc6a8f2bf6a0c5b"
    assert get_hash(
        G2) == "0d461badf591a7287d668bb7b4c7cb90aa0214fd58a8d488c4881b4adf9a39b0"


def test_find_all_routes():
    G = create_flight_network('flight_network.csv', 1)

    # Testing for valid cases
    # Test case 1
    routes = find_all_routes(G, "Dubai", "Seattle")
    print(routes)
    assert get_hash(
        routes) == "806cc56793af72bbfd4cd6ce0c0d0a6b0219f1226b0616918d6fd1588b174474"

    # Test case 2
    routes = find_all_routes(G, "Sao Paulo", "Rio de Janeiro")
    print(routes)
    assert get_hash(
        routes) == "4a78db8c4ddc37102fa08dc35bf5a3ac66a152e4821f940b5a2c01703610c0ee"

    # Test case 3
    routes = find_all_routes(G, "London", "Jamaica")
    print(routes)
    assert get_hash(
        routes) == "7b44ff073d30c4447e0a75f311cf4296cb1269c7f17019e246914411d599289e"

    # Test case 4
    routes = find_all_routes(G, "Boston", "Chicago")
    print(routes)
    assert get_hash(
        routes) == "2ad0a8ac5b7f1745e1c52fff20e577c7d2385cbb1b7d02c787f13ac87408c5db"

    # Test case 5
    routes = find_all_routes(G, "Dubai", "Dubai")
    print(routes)
    assert get_hash(
        routes) == "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945"

    # Testing for the cases when origin city is not in the network
    # Test case 1
    routes = find_all_routes(G, "Mumbai", "Dubai")
    print(routes)
    assert get_hash(
        routes) == "74234e98afe7498fb5daf1f36ac2d78acc339464f950703b8c019892f982b90b"

    # Test case 2
    routes = find_all_routes(G, "Detroit", "Orlando")
    print(routes)
    assert get_hash(
        routes) == "74234e98afe7498fb5daf1f36ac2d78acc339464f950703b8c019892f982b90b"

    # Test case 3
    routes = find_all_routes(G, "San Diego", "Miami")
    print(routes)
    assert get_hash(
        routes) == "74234e98afe7498fb5daf1f36ac2d78acc339464f950703b8c019892f982b90b"

    # Testing for the cases when destination city is not in the network
    # Test case 1
    routes = find_all_routes(G, "Seattle", "Phoenix")
    print(routes)
    assert get_hash(
        routes) == "74234e98afe7498fb5daf1f36ac2d78acc339464f950703b8c019892f982b90b"

    # Test case 2
    routes = find_all_routes(G, "Dubai", "Karachi")
    print(routes)
    assert get_hash(
        routes) == "74234e98afe7498fb5daf1f36ac2d78acc339464f950703b8c019892f982b90b"

    # Test case 3
    routes = find_all_routes(G, "Lima", "Cancun")
    print(routes)
    assert get_hash(
        routes) == "74234e98afe7498fb5daf1f36ac2d78acc339464f950703b8c019892f982b90b"


def test_layovers():
    G = create_flight_network('flight_network.csv', 1)

    # Testing for valid cases
    # Test case 1
    assert get_hash(find_number_of_layovers(G, "Dubai", "Seattle")
                    ) == "268aebbb0bb20abd1a959c9f0f6299785add2e7c33e709b93489134246003109"

    # Test case 2
    assert get_hash(find_number_of_layovers(G, "Sao Paulo", "Rio de Janeiro")
                    ) == "080a9ed428559ef602668b4c00f114f1a11c3f6b02a435f0bdc154578e4d7f22"

    # Test case 3
    assert get_hash(find_number_of_layovers(G, "London", "Jamaica")
                    ) == "2d2b1c3992e04e1469b96b426a1504d50e277cfe274887bc764152d00b86edfb"

    # Test case 4
    assert get_hash(find_number_of_layovers(G, "Boston", "Chicago")
                    ) == "a76df89fc83ee038244d65e41f69837b3ecc7a89e6b059ce85b920b1bf9d2360"

    # Test case 5
    assert get_hash(find_number_of_layovers(G, "Dubai", "Dubai")
                    ) == "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945"

    # Testing for the cases when origin city is not in the network
    # Test case 1
    assert get_hash(find_number_of_layovers(G, "Mumbai", "Dubai")
                    ) == "74234e98afe7498fb5daf1f36ac2d78acc339464f950703b8c019892f982b90b"

    # Test case 2
    assert get_hash(find_number_of_layovers(G, "Detroit", "Orlando")
                    ) == "74234e98afe7498fb5daf1f36ac2d78acc339464f950703b8c019892f982b90b"

    # Test case 3
    assert get_hash(find_number_of_layovers(G, "San Diego", "Miami")
                    ) == "74234e98afe7498fb5daf1f36ac2d78acc339464f950703b8c019892f982b90b"

    # Testing for the cases when destination city is not in the network
    # Test case 1
    assert get_hash(find_number_of_layovers(G, "Seattle", "Phoenix")
                    ) == "74234e98afe7498fb5daf1f36ac2d78acc339464f950703b8c019892f982b90b"

    # Test case 2
    assert get_hash(find_number_of_layovers(G, "Dubai", "Karachi")
                    ) == "74234e98afe7498fb5daf1f36ac2d78acc339464f950703b8c019892f982b90b"

    # Test case 3
    assert get_hash(find_number_of_layovers(G, "Lima", "Cancun")
                    ) == "74234e98afe7498fb5daf1f36ac2d78acc339464f950703b8c019892f982b90b"
