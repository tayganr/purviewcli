import os
import unittest
from purviewcli.client import _search

class TestSearch(unittest.TestCase):
    PURVIEW_NAME = None

    def test_query(self):
        args = {
            '--keywords': '*',
            '--limit': None,
            '--offset': None,
            '--filterFile': None,
            '--facets-file': None,
            '--purviewName': self.PURVIEW_NAME
        }
        search = _search.Search()
        data = search.searchQuery(args)
        self.assertGreaterEqual(data['@search.count'],0)

if __name__ == "__main__":
    os.environ.get('PURVIEW_NAME', TestSearch.PURVIEW_NAME)
    unittest.main()