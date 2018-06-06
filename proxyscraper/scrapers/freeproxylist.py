from proxyscraper.scrapers.basescraper import BaseScraper


class FreeProxyListScraper(BaseScraper):

    def __init__(self):
        """
        Note: May need to rethink BaseScraper as parsing may become more difficult with current setup.
            ie. more page manipulation may be involved.
        """
        name = 'FreeProxyList'
        url = 'https://free-proxy-list.net/'
        options = {}
        super().__init__(name, url, options)

    def scrape(self):
        pass
