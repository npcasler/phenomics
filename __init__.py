"""
/***************************************************************************
Name                 : HTP Geoprocessor
Description          : Tools for geoprocessing field-based HTP data
Date                 : 22/Mar/12 
copyright            : (C) 2012 by Dr. Kelly Thorp, USDA-ARS
email                : kelly.thorp@ars.usda.gov 
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

def classFactory(iface): 
    # load CroppingSystemDDS class from file CroppingSystemDDS
    from HTPGeoprocessor import HTPGeoprocessor 
    return HTPGeoprocessor(iface)