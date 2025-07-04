# coding=utf-8
"""
Setup for AISE4025
"""

from setuptools import setup, find_packages
import versioneer

# Get the long description
with open('README.rst') as f:
    long_description = f.read()

setup(
    name='AISE4025',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='AISE4025: Computer Assisted Interventions course',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/cheneuwo/UWO_AISE_4025_FW25',
    author='Elvis Chen',
    author_email='chene@robarts.ca',
    license='BSD-3 license',
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',


        'License :: OSI Approved :: BSD License',


        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',

        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
    ],

    keywords='medical imaging',

    packages=find_packages(
        exclude=[
            'doc',
            'tests',
        ]
    ),

    install_requires=[
        'six>=1.10',
        'numpy>=1.11',
        'scipy',
        'ipykernel',
        'jupyter',
        'nbsphinx',
        'matplotlib',
        'opencv-contrib-python',
        'scikit-surgerycore',
        'scikit-surgeryvtk',
        'scikit-surgerynditracker',
        'scikit-surgeryarucotracker',
        'scikit-surgerypclcpp',
        'scikit-surgeryopencvcpp',
        'scikit-surgeryfred',
        'scikit-surgerybard',
        'scikit-surgerycalibration'
    ],

    entry_points={
        'console_scripts': [
            'aise4025_manual_registration=aise4025.ui.aise4025_manual_registration_command_line:main',
            'aise4025_registration=aise4025.ui.aise4025_register_command_line:main',
            'aise4025_quadview=aise4025.ui.aise4025_quadview_command_line:main',
            'aise4025_grab_pointer=aise4025.ui.aise4025_grab_pointer_command_line:main',
            'aise4025_template_calibration=aise4025.ui.aise4025_template_calibration_command_line:main',
            'aise4025_pivot_calib=aise4025.ui.aise4025_pivot_calib_command_line:main'
        ],
    },
)