from distutils.core import setup
import py2exe

setup(
	console=['imagescraper.py'],
	options = {
		'py2exe': {
			'packages': ['BeautifulSoup','requests','urllib','os']
		}
	}
	)