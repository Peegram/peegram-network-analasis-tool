from setuptools import setup, find_packages

setup(
    name="pos-netpulse",
    version="1.0.0",
    author="Peegram",
    description="pOS NetPulse: Terminal Network Analysis Tool",
    packages=find_packages(),
    install_requires=[
        "scapy",
    ],
    entry_points={
        'console_scripts': [
            'netpulse=main:main',
        ],
    },
    python_requires='>=3.6',
)
