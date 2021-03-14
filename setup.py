from setuptools import setup
from biketrauma import __version__ as current_version

setup(
  name='biketrauma',
  version=current_version,
  description='Visualization of a bicycle accident db',
  url='git@github.com:mohamedfattouhy/packaging_tutorial.git',
  author='mohamedfattouhy',
  author_email='m.fattouhy@hotmail.com',
  license='MIT',
  packages=['biketrauma','biketrauma.io', 'biketrauma.preprocess', 'biketrauma.vis'],
  zip_safe=False
)