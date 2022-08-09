import time
import sys


print('launched the simplest task!')
try:
    values = sys.argv[1:]
    print('0th', sys.argv[0])
    print(values)
except IndexError:
    print('No arguments provided')
    values = list(range(100))

if __name__ == '__main__':

    for counter in values:
        print('counting: ', counter)
        time.sleep(2)

