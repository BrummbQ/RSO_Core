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

    def __init__(self, customer_catalog, article_catalog, tag_catalog):
        self.customer_catalog = customer_catalog
        self.article_catalog = article_catalog
        self.tag_catalog = tag_catalog

    def articlelist_customer(self, customer):
        pass

    def get_property(self, target, property_string):
        property_list = property_string.split('/')
        self.resolve_property(target, 0, property_list)

    def resolve_property(self, target, index, property_list):
        attr = getattr(target, property_list[index])
        if len(property_list) > index:
            self.resolve_property(attr, index + 1, property_list)
        else:
            print("found property " + attr)