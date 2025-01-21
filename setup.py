from setuptools import setup, find_packages

setup(
    name="ytdownload",
    version="1.1.0",
    packages=find_packages(),
    install_requires=[
        "yt-dlp>=2024.1.15"
    ],
    entry_points={
        'console_scripts': [
            'ytdownload=ytdownload.ytdownload:main'
        ],
    },
    python_requires='>=3.11'
)