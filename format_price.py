import re
import argparse


def parse_price():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p',
        '--price',
        required=True
    )
    return parser.parse_args().price


def format_price(price):
    try:
        float_price = round(float(str(price)), 2)
    except(ValueError, TypeError):
        return None
    if float_price.is_integer():
        pretty_price = '{:,.0f}'.format(float_price).replace(',', ' ')
    else:
        formatable_price = '{:,.2f}'.format(float_price)
        pretty_price = formatable_price.replace(',', ' ').replace('.', ',')
    return pretty_price


def main():
    input_price = parse_price()
    print("Введеная цена: {}\nОтформатированая цена: {}".format(
        input_price,
        format_price(input_price)
    ))

if __name__ == '__main__':
    main()
