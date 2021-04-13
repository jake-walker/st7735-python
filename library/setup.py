from setuptools import setup, find_packages


classifiers = ['Development Status :: 4 - Beta',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: System :: Hardware']

setup(name='ST7735',
      version='0.0.5',
      description='Library to control an ST7735 168x80 TFT LCD display.',
      long_description=open('README.rst').read() + '\n' + open('CHANGELOG.txt').read(),
      license='MIT',
      author='Jake Walker',
      author_email='hi@jakew.me',
      classifiers=classifiers,
      url='https://github.com/jake-walker/st7735-python/',
      packages=find_packages(),
      install_requires=['spidev>=3.4'])
