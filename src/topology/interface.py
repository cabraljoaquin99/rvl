# coding: utf-8
"""Módulo interface

Este módulo contiene la clase Interface.
La clase Interface representa una interfaz de red abstracta.

No debería instanciar un objeto de esta clase sino más bien de alguna
clase hija de ésta.

"""

import constants
import topology.topology_object as TO

class Interface(TO.TopologyObject):
    """
    Description:
        Representa una interfaz de red (Network Interface Card).
    """
    def __init__(self):
        pass

    def is_visible(self):
        return False

    def __repr(self):
        return "%s" % (self._name)