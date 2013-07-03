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


class Engine:

    def __init__(self, customer_catalog, article_catalog, tag_catalog,
            flight_catalog, city_catalog):
        self.customer_catalog = customer_catalog
        self.article_catalog = article_catalog
        self.tag_catalog = tag_catalog
        self.flight_catalog = flight_catalog
        self.city_catalog = city_catalog

    def applicable_tags_customer(self, customer):
        tags = []
        for tag in self.tag_catalog:
            tagobj = self.tag_catalog[tag]
            tp = tagobj.target_property
            prop = self.get_property(customer, tp)
            if prop:
                if tagobj.positive[0] in '><':
                    try:
                        val = int(tagobj.positive[1:])
                        if not eval(str(prop) + tagobj.positive[0] + str(val)):
                            continue
                    except ValueError:
                        print('valerr', val)
                elif prop != tagobj.positive:
                    continue

                tags.append(tag)

        return tags

    def articlerating_customer(self, cid):
        customer = self.customer_catalog[cid]
        ctags = self.applicable_tags_customer(customer)
        customer.tags = ctags

        customer.article_rating = dict()
        for aid in self.article_catalog:
            customer.article_rating[aid] = len(set(customer.tags).intersection(
                set(self.article_catalog[aid].tags)))
            customer.article_rating[aid] -= len(set(
                self.article_catalog[aid].tags).difference(set(customer.tags)))

        return customer.article_rating

    def get_property(self, target, property_string):
        property_list = property_string.split('/')
        return self.resolve_property(target, 0, property_list)

    def resolve_property(self, target, index, property_list):
        prop = property_list[index]
        if not hasattr(target, prop):
            return None
        attr = getattr(target, prop)
        next_target = target
        if prop in ['flight', 'return_flight']:
            if attr in self.flight_catalog:
                next_target = self.flight_catalog[attr]
        elif prop in ['departure', 'arrival']:
            if attr in self.city_catalog:
                next_target = self.city_catalog[attr]
        if len(property_list) > index + 1:
            return self.resolve_property(next_target, index + 1, property_list)
        else:
            return attr