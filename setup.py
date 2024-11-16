from setuptools import setup, find_packages

VERSION = '0.0.a' 
DESCRIPTION = 'Um simples Pacote de Processamento de Imagens'
LONG_DESCRIPTION = 'Um pacote que contém funções básicas para processamento de imagens'

# Setting up
setup(
        name="simple_imgpro", 
        version=VERSION,
        author="Otavio Pereira Cardoso",
        author_email="otavio.pc@proton.me",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['numpy>=2.0.0'],  # Only package dependencies here
        python_requires='>=3.6',  # Python version compatibility specified here
        keywords=['python', 'image processing', 'simple'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.11",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)