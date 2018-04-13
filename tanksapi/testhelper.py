from django.contrib.auth.models import User


def make_user(username="testuser", password="testpassword") -> User:
    """
    Make a user and store it into the database. No LOGIN is performed

    :param username: Optional, provide a username
    :param password: Optional, provide a password
    :return: The user object
    """
    user = User(
        username=username,
        is_active=True
    )
    user.set_password(password)
    user.save()
    return user


def login_client(client) -> User:
    """
    Creates a user, and performs a login with the user.
    :param client: The client that will be logged in. Can be used for both Django and Rest Framework
    :return: The user object
    """
    username = "testuser"
    password = "testpassword"
    user = make_user(username, password)
    client.login(username=username, password=password)
    return user


def raw_data():
    return {"name": "Swamp", "thumbnail_url": "https://i.imgur.com/NWQ0mVE.png",
            "terrain": '[{"id":0,"type":"water","center":{"x":1234.423076923077,"y":525.2307692307693},"points":[{'
                       '"x":1191,"y":168},{"x":1160,"y":170},{"x":1122,"y":173},{"x":1083,"y":178},{"x":1054,'
                       '"y":184},{"x":1029,"y":191},{"x":1006,"y":200},{"x":982,"y":213},{"x":961,"y":226},{"x":941,'
                       '"y":242},{"x":918,"y":260},{"x":894,"y":281},{"x":872,"y":302},{"x":853,"y":325},{"x":839,'
                       '"y":349},{"x":829,"y":377},{"x":822,"y":413},{"x":820,"y":446},{"x":821,"y":481},{"x":825,'
                       '"y":518},{"x":833,"y":555},{"x":843,"y":588},{"x":852,"y":619},{"x":859,"y":649},{"x":867,'
                       '"y":675},{"x":878,"y":698},{"x":892,"y":719},{"x":913,"y":741},{"x":938,"y":763},{"x":966,'
                       '"y":784},{"x":993,"y":799},{"x":1030,"y":820},{"x":1067,"y":836},{"x":1106,"y":853},'
                       '{"x":1145,"y":866},{"x":1176,"y":874},{"x":1205,"y":878},{"x":1234,"y":883},{"x":1259,'
                       '"y":884},{"x":1283,"y":882},{"x":1307,"y":879},{"x":1325,"y":873},{"x":1344,"y":865},'
                       '{"x":1362,"y":854},{"x":1386,"y":844},{"x":1413,"y":835},{"x":1440,"y":824},{"x":1465,'
                       '"y":813},{"x":1486,"y":800},{"x":1505,"y":785},{"x":1524,"y":768},{"x":1539,"y":751},'
                       '{"x":1555,"y":731},{"x":1572,"y":710},{"x":1586,"y":685},{"x":1597,"y":662},{"x":1610,'
                       '"y":640},{"x":1623,"y":619},{"x":1638,"y":596},{"x":1651,"y":572},{"x":1648,"y":409},'
                       '{"x":1636,"y":383},{"x":1628,"y":366},{"x":1619,"y":350},{"x":1608,"y":335},{"x":1592,'
                       '"y":318},{"x":1571,"y":299},{"x":1545,"y":276},{"x":1517,"y":257},{"x":1490,"y":238},'
                       '{"x":1464,"y":224},{"x":1440,"y":212},{"x":1420,"y":204},{"x":1404,"y":199},{"x":1388,'
                       '"y":193},{"x":1366,"y":185},{"x":1344,"y":179},{"x":1316,"y":172}]}]'}
