from setuptools import setup, Extension
import numpy

module1 = Extension('_solver',
                    include_dirs = ['./include/armanpy/', numpy.get_include()],
                    libraries = ['m', 'z', 'armadillo'],
                    sources = ['solver.i', '../src_cpp/solver.cpp'],
                    swig_opts = ["-c++", "-Wall", "-I.", "-I./include/armanpy/"])

setup (name = 'package_solver',
       py_modules = ['solver'],
       version = '1.0',
       description = 'This package contains a solver for quatum physics differnetial equations',
       ext_modules = [module1])

