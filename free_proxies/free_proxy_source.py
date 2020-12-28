import trio
from async_web_scrapper import Retriever
from async_web_scrapper.proxy import ProxySource
from .proxy_scrapper import ProxyScrapper


class FreeProxySource(ProxySource):
    def __init__(self):
        self.proxy_set = set()

    async def update_list(self):
        async with trio.open_nursery() as nursery:
            retriever = Retriever()
            retriever_scope = await nursery.start(retriever.start)
            
            scrapper = ProxyScrapper(retriever)
            scrapper_scope = await nursery.start(scrapper.start)
            await scrapper.done

            retriever_scope.cancel()
            scrapper_scope.cancel()
        
        async for proxy in scrapper.result_receive_channel:
            self.proxy_set.add(proxy)

    async def get_proxies(self):
        await self.update_list()
        return list(self.proxy_set)