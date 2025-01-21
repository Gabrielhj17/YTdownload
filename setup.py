from setuptools import setup, find_packages

setup(
    name="ytdownload",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "yt-dlp>=2024.3.10"
    ],
    entry_points={
        'console_scripts': [
            'ytdownload=ytdownload.ytdownload:main'  # Adjust if your main function has a different name
        ],
    },
)