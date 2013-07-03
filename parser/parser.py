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
            "return_flight", "flight_class", "baggage"]
        self.article_schema = ["name", "tags", "regular_price", "action_price"]
        self.tags_schema = ["target_property", "positive", "negative"]
        self.flight_schema = ["departure", "arrival", "departure_time",
            "arrival_time", "remaining_time"]
        self.city_schema = ["temperature", "type"]

    def parse_customers(self, customer_file):
        return self.parse_json_file(customer_file, "Customer", "customers",
            self.customer_schema)

    def parse_articles(self, article_file):
        return self.parse_json_file(article_file, "Article", "articles",
            self.article_schema)

    def parse_tags(self, tag_file):
        return self.parse_json_file(tag_file, "Tag", "tags", self.tags_schema)

    def parse_flights(self, flight_file):
        return self.parse_json_file(flight_file, "Flight", "flights",
            self.flight_schema)

    def parse_cities(self, city_file):
        return self.parse_json_file(city_file, "City", "cities",
            self.city_schema)

    def parse_json_file(self, jfile, datatype, group, schema):
        with open(jfile, 'r') as f:
            objects = dict()
            json_data = f.read()
            json_decoded = json.loads(json_data)
            for obj in json_decoded[group]:
                new_obj = self.factory.create_object(
                    json_decoded[group][obj],
                    datatype, schema)
                objects[obj] = new_obj
            return objects