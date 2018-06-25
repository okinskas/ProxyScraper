# ProxyScraper #
Python library for scraping proxies from popular providers.

## Basic Usage ##

### Scraping from Free Proxy List ###

```python
from proxyscraper.scrapers.freeproxylist import FreeProxyListScraper

scraper = FreeProxyListScraper()
proxies = scraper.get_proxy_list()

f = open("/path/to/file.txt", 'w+')
for proxy in proxies:
    out = ', '.join(str(x) for x in [proxy.ip, proxy.port, proxy.code, proxy.country, proxy.anon])
    out += '\n'
    f.write(out)
f.close()

```
file.txt

```text
177.204.85.203, 80, BR, Brazil, elite proxy
182.16.175.9, 53281, ID, Indonesia, elite proxy
93.190.142.240, 80, NL, Netherlands, anonymous
173.212.202.65, 443, DE, Germany, elite proxy
74.209.243.116, 3128, US, United States, anonymous
...
```

## License

MIT License

Copyright (c) 2018 Ovidijus Okinskas

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
