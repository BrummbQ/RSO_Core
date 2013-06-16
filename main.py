#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Copyright 2013  Gregor Tätzner gregor@freenet.de

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License as
published by the Free Software Foundation; either version 2 of
the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import sys

from parser.parser import Parser
from engine.engine import Engine

from operator import itemgetter


format_width = 15


def print_customers(customers, schema):
    print("Available Customers: \n=========")
    for customer in customers:
        print('{:<{format_width}}{} {}'.format('id', ':', customer,
            format_width=format_width))
        print_type(customers[customer], schema)


def print_type(datatype, schema):
    for tag in schema:
        print('{:<{format_width}}{} {}'.format(tag, ':',
            str(getattr(datatype, tag, "None")), format_width=format_width))
    print("=========")


def dialog_customer(customers, customer_schema):
    custid = input('\nSelect customer [id]: ')
    if custid not in customers:
        print('Invalid customer id!')
        dialog_customer(customers, customer_schema)
    else:
        print("\nSelected customer: ")
        print_type(customers[custid], customer_schema)
        return custid


def show_best_articles(article_rating, article_catalog, schema):
    print('\nMatching articles for customer (in descending order):')
    sorted_article_list(article_rating, article_catalog, schema)


def sorted_article_list(articledict, article_catalog, schema):
    slist = sorted(articledict.items(), key=itemgetter(1),
        reverse=True)
    for a in slist:
        article = article_catalog.get(a[0])
        if article:
            print_type(article, schema)


def main():
    parser = Parser()
    cities = parser.parse_cities('data/city.json')
    flights = parser.parse_flights('data/flight.json')
    customers = parser.parse_customers('data/customer.json')
    articles = parser.parse_articles('data/article.json')
    tags = parser.parse_tags('data/tags.json')

    engine = Engine(customers, articles, tags, flights, cities)

    print_customers(customers, parser.customer_schema)
    cid = dialog_customer(customers, parser.customer_schema)

    ar = engine.articlerating_customer(cid)
    show_best_articles(ar, articles, parser.article_schema)

    return True


if __name__ == '__main__':
    status = main()
    sys.exit(status)
