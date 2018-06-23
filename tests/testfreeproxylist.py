from proxyscraper.scrapers.freeproxylist import FreeProxyListScraper

# Temp implementation
# A lot of this should be abstracted in object creation.
if __name__ == "__main__":

    scraper = FreeProxyListScraper()
    scraper.start_driver()
    scraper.get_page()
    scraper.scrape()
    scraper.manip_table()
    scraper.close_driver()
