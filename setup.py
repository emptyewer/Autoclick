# -*- coding: utf-8 -*-
"""
First build the extension using

python setup.py build_ext --inplace

then...

py2app/py2exe build script for Fytt2.

Will automatically ensure that all build prerequisites are available
via ez_setup

Usage (Mac OS X):
   python setup.py py2app -O2

Usage (Windows):
   python setup.py py2exe

Usage (Linux):
pyinstaller -y -F fytt2.py -n Fytt -i Icon.ico (use dev version 2.1-dev from https://github.com/pyinstaller/pyinstaller)
"""
import os
import sys
if sys.platform == 'darwin':
    from distutils.core import setup
    import py2app
elif sys.platform == 'win32':
    from setuptools import setup
    import py2exe

# from distutils.extension import Extension
# from Cython.Distutils import build_ext
# import numpy as np

# ext_modules = [Extension("functions", ["functions.pyx"])]
#
# setup(
#   name='Test',
#   cmdclass={'build_ext': build_ext},
#   include_dirs=[np.get_include()],
#   ext_modules=ext_modules,
# )

APP = ['autoclick.py']
# DATA_FILES = [('images', ['fytt-icon.png']), ('db', ['fytt2_db.sqlite3'])]
DATA_FILES = []
OPTIONS = {'argv_emulation': False,
           'iconfile' : 'Icon.icns',
           'plist': {'CFBundleGetInfoString': 'Autoclick: Automated mouse clicks',
                     'CFBundleIdentifier': 'murkymadolin',
                     'CFBundleShortVersionString': '1.0',
                     'CFBundleName': 'Autoclick',
                     'CFBundleVersion': '10',
                     'NSHumanReadableCopyright': '(c) 2015 Murky Madolin'},
            'includes': ['sip', 'time', 'PyQt4', 'PyQt4.QtCore', 'PyQt4.QtGui', 'sys', 'autopy', 'threading'],
           }


sys.setrecursionlimit(100000)

if sys.platform == 'darwin':
  setup(
    app=APP,
    name='Autoclick',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    author='Murky Mandolin',
    author_email='murkymandolin@gmail.com',
  )
elif sys.platform == 'win32':
  setup(
    windows=[{"script":'autoclick.py',
               "icon_resources": [(1, "Icon.ico")],
               "dest_base":"Autoclick"
            }],
    options={"py2exe":{"includes" :['sip', 'time', 'PyQt4', 'PyQt4.QtCore', 'PyQt4.QtGui', 'sys', 'autopy', 'threading'],
                       "optimize": 2}}
  )