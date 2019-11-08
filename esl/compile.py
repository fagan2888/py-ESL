from Cython.Distutils import build_ext

from setuptools import setup
from setuptools import Extension

setup(
    name='trade',
    ext_modules=[
        Extension('trade', ['trade.pyx']),
    ],
    cmdclass={'build_ext': build_ext}
)
