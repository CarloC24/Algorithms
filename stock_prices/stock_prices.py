#!/usr/bin/python

import argparse


def find_max_profit(prices):
    minPrice = prices[0]
    maxProfit = 0
    for price in prices:
        minPrice = min(minPrice, price)
        compare_profit = minPrice - price
        maxProfit = max(compare_profit, maxProfit)
    return maxProfit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
