import os
import sys
import tarfile
import urllib
from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize


external_dir = os.path.abspath('src/external')

blossom5_url = 'http://pub.ist.ac.at/~vnk/software/blossom5-v2.04.src.tar.gz'
blossom5_tar_gz = os.path.join(external_dir, 'blossom5-v2.04.src.tar.gz')
blossom5_dir = os.path.join(external_dir, 'blossom5-v2.04.src')
blossom5_bin = os.path.join(blossom5_dir, 'blossom5')

if not os.path.exists(blossom5_tar_gz):
    urllib.urlretrieve(blossom5_url, blossom5_tar_gz)

if not os.path.exists(os.path.join(blossom5_dir, 'README.TXT')):
    tar = tarfile.open(blossom5_tar_gz)
    tar.extractall(path=external_dir)
    tar.close()

blossom_directory = 'src/external/blossom5-v2.04.src/'

blossom_source = [
    'PMduals.cpp',
    'PMexpand.cpp',
    'PMinit.cpp',
    'PMinterface.cpp',
    'PMmain.cpp',
    'PMrepair.cpp',
    'PMshrink.cpp',
    'MinCost/MinCost.cpp',
]

blossom_source = [os.path.join(blossom_directory, filename) for filename in blossom_source]

libraries = []
if 'linux' in sys.platform:
    libraries.append('rt')

extensions = [
    Extension(
        name='blossomv.blossomv',
        sources=['blossomv/blossomv.pyx'] + blossom_source,
        include_dirs=[blossom_directory],
        libraries=libraries,
    ),
]

setup(
    name='blossomv',
    version='v2.04',
    packages=find_packages(),
    description='Python wrapper for the Blossom V algorithm',
    author='Andrew McPherson',
    author_email='andrew.mcpherson@gmail.com',
    url='http://bitbucket.org/dranew/blossomv',
    ext_modules=cythonize(extensions),
)
