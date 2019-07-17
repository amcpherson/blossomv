import os
import sys
import tarfile
import urllib.request
from setuptools import setup, find_packages, Extension


external_dir = os.path.abspath('src/external')

blossom5_url = 'http://pub.ist.ac.at/~vnk/software/blossom5-v2.04.src.tar.gz'
blossom5_tar_gz = os.path.join(external_dir, 'blossom5-v2.04.src.tar.gz')
blossom5_dir = os.path.join(external_dir, 'blossom5-v2.04.src')
blossom5_bin = os.path.join(blossom5_dir, 'blossom5')

if not os.path.exists(blossom5_tar_gz):
    urllib.request.urlretrieve(blossom5_url, blossom5_tar_gz)

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

with open("README.md", "r") as fh:
    long_description = fh.read()

if not os.path.exists('blossomv/blossomv.cpp'):
    ext = '.pyx'
    use_cython = True

else:
    ext = '.cpp'
    use_cython = False

extensions = [
    Extension(
        name='blossomv.blossomv',
        sources=['blossomv/blossomv' + ext] + blossom_source,
        include_dirs=[blossom_directory],
        libraries=libraries,
    ),
]

if use_cython:
    from Cython.Build import cythonize
    extensions = cythonize(extensions)

setup(
    name='blossomv',
    version='v2.04_r2',
    author="Andrew McPherson",
    author_email="andrew.mcpherson@gmail.com",
    description="A wrapper for the BlossomV code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amcpherson/blossomv",
    packages=find_packages(),
    ext_modules=extensions,
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
