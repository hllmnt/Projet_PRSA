from setuptools import setup, Extension

module1 = Extension('_solver',
                    sources = ['solver.i',
                               '../src_cpp/solver.cpp'],
                    swig_opts = ["-c++"])

setup (name = 'package_test',
       py_modules = ['solver'],
       version = '1.0',
       description = 'This is a solver package',
       ext_modules = [module1])