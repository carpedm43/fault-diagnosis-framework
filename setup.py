from setuptools import setup

setup(
    name="shrm",
    version="0.0.2",
    description='shrm',
    install_requires=["numpy", "scipy", "torch"],
    author='hyeonbaekong',
    author_email='carpedm43@gmail.com',
    license='MIT',
    python_requires='>=3',
    packages=["shrm"],
    package_data={
        "shrm": [
            "data/*"
        ]
    },
    zip_safe=False,

)
