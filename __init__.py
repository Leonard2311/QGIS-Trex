# -*- coding: utf-8 -*-
"""
/***************************************************************************
 TreeExtractor
                                 A QGIS plugin
 This plugin extracts the position coordinates of the trees on a specified area
                             -------------------
        begin                : 2015-12-12
        copyright            : (C) 2015 by Leonard Stanescu
        email                : leonardstanescu@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load TreeExtractor class from file TreeExtractor.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .tree_extractor import TreeExtractor
    return TreeExtractor(iface)
