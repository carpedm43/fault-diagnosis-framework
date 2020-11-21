from setuptools import setup
from setuptools import find_packages

setup(
    name="shrm",
    version="0.0.4",
    description='shrm',
    url='https://github.com/carpedm43/shrm.git',
    author='hyeonbaekong',
    author_email='carpedm43@gmail.com',
    license='MIT',
    python_requires='>=3',
    packages=find_packages(),
    package_data={
        "shrm": [
            "data/B_7/*.mat",
            "data/B_14/*.mat",
            "data/B_21/*.mat",
            "data/I_7/*.mat",
            "data/I_14/*.mat",
            "data/I_21/*.mat",
            "data/O_7/*.mat",
            "data/O_14/*.mat",
            "data/O_21/*.mat",
            "data/N_0/*.mat"
        ]
    },
    zip_safe=False,
    install_requires=
    ["scipy==1.5.4",
     "numpy==1.19.4",
     "torch==1.7.0"]
)
