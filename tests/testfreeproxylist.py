import unittest
from proxyscraper.scrapers.freeproxylist import FreeProxyListScraper


class TestFreeProxyList(unittest.TestCase):

    def test_get_proxy_list(self):
        scraper = FreeProxyListScraper()
        proxies = scraper.get_proxy_list()
        [print(p) for p in proxies]


if __name__ == "__main__":
    unittest.main()
