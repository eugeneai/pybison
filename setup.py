"""
Builds bison python module
"""

from __future__ import absolute_import
from __future__ import print_function
version = '0.1'

from setuptools import setup
from setuptools import Extension
from Cython.Distutils import build_ext
from setuptools import find_packages

import sys

if sys.platform == 'win32':
    print('No windows support at this time. PyBison won\'t work for you :(')
    libs = []
    extra_link_args = []
    bison2pyscript = 'utils/bison2py.py'
    bisondynlibModule = 'src/c/bisondynlib-win32.c'
elif sys.platform.startswith('linux'):
    libs = ['dl']
    extra_link_args = []
    bison2pyscript = 'utils/bison2py'
    bisondynlibModule = 'src/c/bisondynlib-linux.c'
elif sys.platform.startswith('darwin'):
    libs = ['dl']
    extra_link_args = []
    bison2pyscript = 'utils/bison2py'
    bisondynlibModule = 'src/c/bisondynlib-linux.c'
    from distutils import sysconfig
    vars = sysconfig.get_config_vars()
    vars['LDSHARED'] = vars['LDSHARED'].replace('-bundle', '-dynamiclib')
else:
    print('Sorry, your platform is presently unsupported.')
    sys.exit(1)

setup(
        name='bison',
        version=version,
        description='Python bindings for bison/flex parser engine',
        author='David McNab <david@freenet.org.nz>',
        url='http://www.freenet.org.nz/python/pybison',
        ext_modules=[
            Extension('bison_', [
                    'src/pyrex/bison_.pyx',
                    'src/c/bison_callback.c',
                    bisondynlibModule],
                libraries=libs,
                extra_compile_args=['-Wall', '-Wextra'],
               # extra_compile_args=['/Od','/Zi','-D__builtin_expect(a,b)=(a)'], extra_link_args=extra_link_args,
                )
            ],
        #packages=find_packages(),
        packages=['bison'],
        package_dir={'': 'src'},
        #py_modules=['node', 'xmlifier', 'convert'],
        cmdclass={'build_ext': build_ext},
        scripts=[bison2pyscript],
        install_requires=[
            "cython",
            "six"
        ],
        )
