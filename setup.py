from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Meu primeiro pacote em Python'
LONG_DESCRIPTION = 'Meu primeiro pacote em Python com uma descrição um pouco mais longa'

# Setting up
setup(
        name="stupid_simple_imgpro", 
        version=VERSION,
        author="Otavio Pereira Cardoso",
        author_email="otavio.pc@proton.me",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[],
        
        keywords=['python', 'image processing', 'simple'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)