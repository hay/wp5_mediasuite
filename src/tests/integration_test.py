import os
import sys
from flask import Flask
import requests
import json

"""
uses pytest
"""

#only needed if you run this module from command line
parts =  os.path.realpath(__file__).split('/')
myModules = '/'.join(parts[0:len(parts) -2])
if myModules not in sys.path:
	sys.path.append(myModules)

class TestSearchAPI:

	"""<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><
	<><><><><><><><><><><><> SETUP & TEARDOWN <><><><><><><><><><><>
	<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><"""

	def setup(self):
		self.strictMode = True
		self.app = Flask(__name__)
		self.app.config.from_object('settings.Config')

		#TODO think of a way to dynamically obtain test data
		self.collectionId = 'nisv-catalogue-aggr'

	def teardown(self):
		pass

	"""----------------------------- TEST MEDIASUITE -------------------"""

	"""
    def test_server_response_and_content_ok(self):
        response = requests.get(self.hostUrl)
        assert response.status_code == 200
        assert "<html>" in response.text

    def test_invalid_urls(self):
        response = requests.get(self.hostUrl + "/doesnotexist/")
        assert response.status_code == 404
    """


	"""----------------------------- TEST SEARCH API -------------------"""

	def test_search_api_config(self):
		assert 'SEARCH_API' in self.app.config

	def test_search_api_isalive(self):
		resp = requests.get(
			'%s/ping' % (self.app.config['SEARCH_API'][0:len('/api/v1.1') * -1])
		)
		assert resp.status_code == 200
		assert resp.text == 'pong'


	def test_collection_stats(self):
		resp = requests.post(
			'%s/collections/show_stats/%s?cid=%s&at=%s' % (
				self.app.config['SEARCH_API'],
				self.collectionId,
				self.app.config['CLIENT_ID'],
				self.app.config['TOKEN']
			)
		)
		assert resp.status_code == 200
		try:
			stats = json.loads(resp.text)
			self.__validateCollectionStats(stats)
		except Exception as error:
			assert False

	def __validateCollectionStats(self, stats):
		assert 'collection_annotation_indices' in stats
		assert 'collection_statistics' in stats
		if self.strictMode:
			assert 'timestamp' in stats
			assert 'service' in stats
			assert 'query' in stats

	"""----------------------------- TEST ANNOTATION API -------------------"""

	def test_annotation_api_config(self):
		assert 'ANNOTATION_API' in self.app.config

	def test_annotation_api_isalive(self):
		resp = requests.get(
			'%s/ping' % (self.app.config['ANNOTATION_API'][0:len('/api') * -1])
		)
		assert resp.status_code == 200
		assert resp.text == 'pong'

	"""----------------------------- TEST WORKSPACE API -------------------"""

	def test_workspace_api_config(self):
		assert 'USER_SPACE_API' in self.app.config

	def test_workspace_api_isalive(self):
		resp = requests.get(
			'%s/ping' % (self.app.config['USER_SPACE_API'][0:len('/api/v0.1') * -1])
		)
		assert resp.status_code == 200
		assert resp.text == 'pong'

