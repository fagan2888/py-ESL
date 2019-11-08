import os
try:
    from setuptools import setup
    from setuptools import Extension
except ImportError:
    from distutils.core import setup
    from distutils.extension import Extension
try:
    from Cython.Distutils import build_ext
except ImportError:
    from distutils.command.build_ext import build_ext
from distutils.errors import CCompilerError, DistutilsExecError, \
    DistutilsPlatformError


class TXEntension(build_ext):
    # This class allows C extension building to fail.
    def run(self):
        try:
            build_ext.run(self)
        except DistutilsPlatformError:
            raise Exception("BuildFailed")

    def build_extension(self, ext):
        try:
            build_ext.build_extension(self, ext)
        except (CCompilerError, DistutilsExecError, DistutilsPlatformError):
            pass  # raise BuildFailed()


cmdclass = {}
ext_modules = []

install_requires = ['numpy']


try:
    ext_modules += [
        Extension("esl.trade", ["esl/trade.pyx"]),
    ]
    cmdclass.update({'build_ext': TXEntension})
except ImportError:
    ext_modules += [
        Extension("abcEconomics.trade", ["abcEconomics/trade.c"]),
        Extension("abcEconomics.logger.online_variance", ["abcEconomics/logger/online_variance.c"]),
    ]

version = '0.1'

setup(name='ESL',
      version=version,
      package_dir={'esl': 'esl',
                   },
      packages=['esl'],
      install_requires=install_requires,
      include_package_data=True,
      ext_modules=ext_modules,
      cmdclass=cmdclass)
