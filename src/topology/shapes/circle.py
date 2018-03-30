# coding: utf-8
"""Módulo circle

Contiene a la clase circle.

"""

import topology.shape as shape


class Circle(shape.Shape):

    def __init__(self):
        pass

    def get_tool_name(self):
        return "Círculo"

    def is_tool(self):
        return True

    def get_url_icon(self):
        return "resources/img/circle-icon.png"

    def get_subtype(self):
        return "Circle"

    def __repr__(self):
        return "Circle"

    def __copy__(self):
        circle = Circle()
        return circle
