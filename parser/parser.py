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

import json

from engine.factory import Factory


class Parser:

    def __init__(self):
        self.factory = Factory()
        self.customer_schema = ["name", "gender", "age", "address", "flight",
            "return_flight"]
        self.article_schema = ["name", "tags", "regular_price", "action_price",
            "limit_time", "limit_number"]
        self.tags_schema = ["target_property", "positive", "negative"]

    def parse_customers(self, customer_file):
        with open(customer_file, 'r') as f:
            customers = dict()
            json_data = f.read()
            json_decoded = json.loads(json_data)
            for customer in json_decoded["customers"]:
                new_customer = self.factory.create_object(
                    json_decoded["customers"][customer]["Customer"],
                    "Customer", self.customer_schema)
                customers[customer] = new_customer
            return customers

    def parse_articles(self, articles_file):
        with open(articles_file, 'r') as f:
            articles = dict()
            json_data = f.read()
            json_decoded = json.loads(json_data)
            for article in json_decoded["articles"]:
                new_article = self.factory.create_object(
                    json_decoded["articles"][article]["Article"],
                    "Article", self.article_schema)
                articles[article] = new_article
            return articles

    def parse_tags(self, tag_file):
        with open(tag_file, 'r') as f:
            tags = dict()
            json_data = f.read()
            json_decoded = json.loads(json_data)
            for tag in json_decoded["tags"]:
                new_tag = self.factory.create_object(
                    json_decoded["tags"][tag],
                    "Tag", self.tags_schema)
                tags[tag] = new_tag
            return tags
