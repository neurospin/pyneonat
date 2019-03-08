# coding: utf-8
##########################################################################
# NSAp - Copyright (C) CEA, 2019
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html
# for details.
##########################################################################

# Module current version
version_major = 0
version_minor = 0
version_micro = 1

# Expected by setup.py: string of form "X.Y.Z"
__version__ = "{0}.{1}.{2}".format(version_major, version_minor, version_micro)

# Expected by setup.py: the status of the project
CLASSIFIERS = ["Development Status :: 1 - Planning",
               "Environment :: Console",
               "Operating System :: OS Independent",
               "Programming Language :: Python",
               "Topic :: Scientific/Engineering"]

# Project descriptions
description = """
pyneonat: 
"""
SUMMARY = """
.. container:: summary-carousel

    pycaravel is a Python module for 
"""
long_description = """
=========
pyneonat
=========

"""

# Main setup parameters
NAME = "pyneonat"
ORGANISATION = "CEA"
MAINTAINER = "Antoine Grigis"
MAINTAINER_EMAIL = "antoine.grigis@cea.fr"
DESCRIPTION = description
LONG_DESCRIPTION = long_description
EXTRANAME = "NeuroSpin webPage"
EXTRAURL = "http://joliot.cea.fr/drf/joliot/Pages/Entites_de_recherche/NeuroSpin.aspx"
URL = "https://github.com/neurospin/pyneonat"
DOWNLOAD_URL = "https://github.com/neurospin/pyneonat"
LICENSE = "CeCILL-B"
CLASSIFIERS = CLASSIFIERS
AUTHOR = """
Antoine Grigis <antoine.grigis@cea.fr>
"""
AUTHOR_EMAIL = "antoine.grigis@cea.fr"
PLATFORMS = "Linux,OSX"
ISRELEASE = True
VERSION = __version__
PROVIDES = ["pyneonat"]
REQUIRES = [
    "pandas>=0.19.2",
    "nibabel>=2.3.1"
]
EXTRA_REQUIRES = {}
