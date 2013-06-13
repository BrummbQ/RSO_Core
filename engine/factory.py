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


class Factory:

    def __init__(self):
        pass

    def create_object(self, data, object_type, schema):
        attributes = dict()
        for tag in schema:
            if tag in data:
                attributes[tag] = data[tag]

        new_object = type(object_type, (object,), attributes)
        return new_object