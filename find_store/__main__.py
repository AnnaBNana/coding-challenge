import sys
import argparse

from .addressmodule import Address

# from .addressmodule import Address

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--address")
    args = parser.parse_args()
    
    # Address.distance_to(args.address)
    # print(args.address)

if __name__ == '__main__':
    main()