import os
import subprocess
import sys

import GooglePlayAdvancedSearch.tests.conftest as conftest


def getTestFolder():
	return os.path.dirname(os.path.abspath(__file__))


def startWebsite(test):
	g = conftest.websiteUrl()
	test(next(g))
	next(g)


def runScraper(args):
	if sys.platform == 'win32':
		mainArgs = ['python', 'Program.py']
	else:
		mainArgs = ['./Program.py']
	mainArgs.extend(args)
	if 'PYTHONIOENCODING' not in os.environ or os.environ['PYTHONIOENCODING'] != 'UTF8':
		os.environ['PYTHONIOENCODING'] = 'UTF8'
	return subprocess.run(mainArgs, cwd=os.path.join(getTestFolder(), '../scraper'))
