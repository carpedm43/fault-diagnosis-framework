from setuptools import setup
from setuptools import find_packages

setup(
    name="shrm",
    version="0.1.1",
    description='shrm',
    url='https://github.com/carpedm43/shrm.git',
    author='hyeonbaekong',
    author_email='carpedm43@gmail.com',
    license='MIT',
    python_requires='>=3',
    packages=find_packages(),
    package_data={
        "shrm": [
            'data/*'
        ]
    },
    zip_safe=False,
    install_requires=
    ["scipy==1.5.4",
     "numpy==1.19.4",
     "torch==1.7.0"]
)
