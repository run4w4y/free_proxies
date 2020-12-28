from .pages import *
from async_web_scrapper import GenericScrapper


class ProxyScrapper(GenericScrapper):
    def base_url(self, page):
        urls_dict = {
            PageEnum.SOCKS: 'https://www.socks-proxy.net/',
            PageEnum.HTTPS: 'https://www.sslproxies.org/',
            PageEnum.ANON: 'https://free-proxy-list.net/anonymous-proxy.html',
            PageEnum.UK: 'https://free-proxy-list.net/uk-proxy.html',
            PageEnum.US: 'https://www.us-proxy.org/'
        }
        return urls_dict[page]
    
    @property
    async def pages(self):
        return [
            SOCKSPage(self.base_url(PageEnum.SOCKS), self.retriever),
            HTTPSPage(self.base_url(PageEnum.HTTPS), self.retriever),
            AnonPage(self.base_url(PageEnum.ANON), self.retriever),
            UKPage(self.base_url(PageEnum.UK), self.retriever),
            USPage(self.base_url(PageEnum.US), self.retriever)
        ]