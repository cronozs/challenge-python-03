# Resolve the problem!!
import re

def run():
    
    with open('encoded.txt', 'r', encoding='utf-8') as f:
        encoded_message = f.read()
        message = re.findall('[a-z]', encoded_message)
        print(''.join(message))


if __name__ == '__main__':
    run()
