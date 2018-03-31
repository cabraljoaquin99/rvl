# coding: utf-8
"""Módulo device.

Este módulo contiene todos los dispositivos que se pueden insertar en la
topología.

Esta clase es la padre de todos los dispositivos que se van a crear.

"""

import constants
import topology.topology_object as TO
from lib.canvas import ObjectCanvas


class Device(TO.TopologyObject):
    """
    Description:
        Esta clase representa un dispositivo donde cada uno posee una cantidad
        limitada de interfaces. La cantidad de interfaces se puede cambiar,
        para ello existen algunas restricciones que se detallan en el método
        set_count_nics.
    """
    def __init__(self, interfaces_amount = 3):
        """
        """
        self._interfaces = []  # Network cards
        self._interfaces_amount = interfaces_amount  # Number of interfaces
        self.MAX_INTERFACES = 16  # Maximum number of interfaces

        # self._name = name
        # self._set_host_name(name)
        # self._configuration = configuration
        # self._type = constants.TYPE_DEVICE
        # self._conections = []  # List<Connection>
        # self._interfaces = []
        # self._configure()

    def add_interface(self, interface):
        if len(self._interfaces) >= self._interfaces_amount:
            raise ValueError("Se intentó insertar una interfaz y no hay lugar")
        self._interfaces.append(interface)

    def get_interface(self, i):
        """
        Description:
            Retorna la i-ésima interfaz.
        
        Returns:
            Retorna None en caso que el índice pasado no esté en el intervalo
            válido.
        """
        if i < 0 or i >= len(self._interfaces):
            return None
        return self._interfaces[i]

    def get_interfaces_amount(self):
        return self._interfaces_amount

    def set_interfaces_amount(self, number):
        """
        Description:
            Establece la cantidad de interfaces.
        """
        if number <= 0 or number > self._interfaces_amount:
            raise ValueError("Cantidad incorrecta de interfaces")
        self._interfaces_amount = number

    def __repr__(self):
        return self._name

    def get_configuration(self):
        return self._configuration

    def get_count_nics(self):
        return self._count_nics

    def get_host_name(self):
        return self._host_name

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_position(self):
        return 0

    def get_subtype(self):
        return ""

    def get_type(self):
        return self._type

    def set_count_nics(self, cantidad_nics_nueva, forzar=False):
        pass

    def set_id(self, id):
        self._id = id

    def set_name(self, name):
        self._name = name
        self._set_host_name(host_name)


class CanvasDevice(ObjectCanvas):
    """

    """
    def __init__(self, url_image, etiqueta):
        super().__init__()
        # cr = cairo.Context()
        # Se necesita el conext de cairo para obtener los text_extents de la etiqueta.
        # (x, y, width, height, dx, dy) = cr.text_extents(etiqueta)
        # print((x, y, width, height, dx, dy))
        import cairo
        self.url_image = url_image
        self.image = cairo.ImageSurface.create_from_png(self.url_image)
        self.set_width(self.image.get_width())
        self.set_height(self.image.get_height())
        self.expandable = False

        self.etiqueta = etiqueta
        self.cr = None
        self.text_image_distance = 0

    def draw(self, w, cr):
        (x, y, text_width, text_height, dx, dy) = cr.text_extents(self.etiqueta)
        if self.cr is None:
            self.cr = cr
            image_width = self.get_width()
            self.set_width(max(image_width, text_width))
            self.set_height(self.get_height() + text_height)
            if text_width > image_width:
                self.text_image_distance = (text_width - image_width) / 2
                self.set_x(self.get_x() - self.text_image_distance)
        cr.save()
        cr.translate(self.get_x(), self.get_y() + self.get_height())
        cr.move_to(self.get_width() / 2 - text_width / 2, 0)
        cr.set_font_size(10)
        cr.show_text(self.etiqueta)
        cr.restore()

        cr.set_source_surface(self.image, self.get_x() + self.text_image_distance, self.get_y())
        cr.paint()
        #cr.stroke()

