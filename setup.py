from setuptools import setup, find_packages

VERSION = '0.0.2' 
DESCRIPTION = 'Debugging Functions and Decorators useful within any project'
LONG_DESCRIPTION = 'Libary of often useful functions that are collected to be maintained here.'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="generichelpermodule", 
        version=VERSION,
        author="Tabea Röthemeyer",
        author_email="tabea.roethemeyer@gruppe.ai",
        scripts=[],
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[
               'matplotlib',
               'seaborn',
               'numpy'], 
        url="",
        
        keywords=['python', 'debugging'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: Microsoft :: Windows",
        ]
)
