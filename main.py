import argparse

from validator_for_postcodes import parse_postcode


def main():
    parser = argparse.ArgumentParser(prog='postcode')
    parser.add_argument('--country', help='Country', default="uk")
    parser.add_argument('--postcode', help='Postcode')
    args = parser.parse_args()

    parse_postcode(postcode=args.postcode, country=args.country)


if __name__ == '__main__':
    main()
