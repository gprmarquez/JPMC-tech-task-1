import unittest
from client import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (
                quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (
                quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

    """ ------------ Add more unit tests ------------ """

    def test_getRatio_priceBZero(self):
        prices = [{'price_a': 117.1, 'price_b': 116.915}, {
            'price_a': 115.7, 'price_b': 0}, {'price_a': 116.91, 'price_b': 114.65}]

        for price in prices:
            try:
                print price['price_a'] / price['price_b']
            except ZeroDivisionError:
                print "ZeroDivisionError: price_b cannot be 0"

    def test_getRatio_priceAZero(self):
        price_a = 0
        price_b = 90.77
        self.assertEqual (getRatio(price_a, price_b), 0)

    def test_getRatio_greaterThan1(self):
        price_a = 110.31
        price_b = 102.78
        self.assertGreater (getRatio(price_a, price_b), 1)

    def test_getRatio_LessThan1(self):
        price_a = 121.65
        price_b = 133.53
        self.assertLess (getRatio(price_a, price_b), 0)

    def test_getRatio_exactlyOne(self):
        price_a = 323.64
        price_b = 323.64
        self.assertEqual (getRatio(price_a, price_b), 1)


if __name__ == '__main__':
    unittest.main()
