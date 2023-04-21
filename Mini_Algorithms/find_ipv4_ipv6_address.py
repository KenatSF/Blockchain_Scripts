




def isIPV4(address):
    parts = address.split('.')
    if len(parts) != 4:
        return False

    for part in parts:
        try:
            value = int(part)
            if value < 0 or value > 255:
                return False
        except ValueError:
            return False
    return True

def isIPV6(address):
    parts = address.split(':')
    if len(parts) != 8:
        return False

    for part in parts:
        try:
            value = int(part, 16)
            if value < 0 or value > 65535:
                return False
        except ValueError:
            return False
    return True


def checkIPAddress(address):
    if isIPV4(address):
        return 'IPv4'
    elif isIPV6(address):
        return 'IPv6'
    else:
        return 'Neither'


def main():

    ipv4Address = '192.10.24.2'
    ipv6Address = '2001:0db8:85a3:0000:0000:8a2e:0370:7334'

    answer1 = checkIPAddress(ipv4Address)
    print(answer1)
    answer2 = checkIPAddress(ipv6Address)
    print(answer2)


if __name__ == "__main__":
    main()