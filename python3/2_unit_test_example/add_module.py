!/usr/bin/env python3

test_endpoint = "http://test.com"

def test_varaibles():
    if test_endpoint != "http://test.com":
        raise("\nIncorrect value used", test_endpoint)
    else:
        print("\nTests passed")

def add(x, y):
    result = x + y
    return result
    print(result)

if __name__ == "__main__":
    test_varaibles()
    add(1, 5)
