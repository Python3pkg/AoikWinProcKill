import os
from setuptools import find_packages
from setuptools import setup

setup(
    name='AoikWinProcKill',

    version='0.1.0',

    description="""Kill Windows processes by matching their full command line with regular expression.""",
    
    long_description="""`Documentation on Github 
<https://github.com/AoiKuiyuyou/AoikWinProcKill>`_""",

    url='https://github.com/AoiKuiyuyou/AoikWinProcKill',

    author='Aoi.Kuiyuyou',
    
    author_email='aoi.kuiyuyou@google.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='Kill Windows process command line regular expression',

    install_requires=[
        #'pywin32',
        ## pywin32 cannot be installed via PyPI so do not list it here.
    ],
      
    package_dir={'':'src'},
    
    packages=find_packages('src'),

    entry_points={
        'console_scripts': [
            'aoikwpk=aoikwinprockill.aoikwpk:main',
        ],
    },
)
