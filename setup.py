from setuptools import setup
import premierleaguedata as pld

long_description = open('README.md', encoding='utf8').read()

setup(
    name = 'premierleaguedata',
    version = pld.__version__,
    author = pld.__author__,
    author_email = 'ghuron@usp.br',
    packages = ['premierleaguedata'],
    description = 'An unofficial Premier League API client.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url = 'https://github.com/ghurone/premier-league-data',
    project_urls = {
        'Source Code': 'https://github.com/ghurone/premier-league-data',
    },
    install_requires=['requests>=2.26.0'],
    license = 'MIT',
    keywords = 'premier league api',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ]
)