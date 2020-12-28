import logging
from enum import Enum
from async_web_scrapper import GenericPage, PageResult
from async_web_scrapper.proxy.proxy_types import *


class PageEnum(Enum):
    SOCKS = 0
    HTTPS = 1
    ANON = 2
    UK = 3
    US = 4


class _ProxyPage:
    async def parse_entries(self):
        html = await self.retriever.retrieve_html(self.url, failsafe=True)
        return map(
            lambda x: list(map(lambda y: y.text.strip(), x.find_all('td'))), 
            html.find('table').find('tbody').find_all('tr')
        )


class SOCKSPage(GenericPage, _ProxyPage):
    async def process(self):
        logging.info('Parsing page with SOCKS proxies')
        entries = await self.parse_entries()
        return PageResult(
            items=list(map(lambda x: SOCKS4Proxy(*x[:3]) if x[4].lower() == 'socks4' else SOCKS5Proxy(*x[:3]), entries))
        )


class HTTPSPage(GenericPage, _ProxyPage):
    async def process(self):
        logging.info('Parsing page with HTTPS proxies')
        entries = await self.parse_entries()
        return PageResult(
            items=list(map(lambda x: HTTPSProxy(*x[:3]), entries))
        )


class AnonPage(GenericPage, _ProxyPage):
    async def process(self):
        logging.info('Parsing page with anonymous proxies')
        entries = await self.parse_entries()
        return PageResult(
            items=list(map(lambda x: HTTPSProxy(*x[:3]) if x[6].lower() == 'yes' else HTTPProxy(*x[:3]), entries))
        )


class UKPage(AnonPage):
    pass


class USPage(AnonPage):
    pass
