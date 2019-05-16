from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware
from scrapy.exceptions import NotConfigured
from collections import defaultdict
import json
import random
import re


class RandomHttpProxyMiddleware(HttpProxyMiddleware):
    pass
'''
    @classmethod
    def from_crawler(cls, crawler):
        # 从配置文件中读取用户验证信息的编码
        auth_coding = crawler.settings.get('HTTPPROXY_AUTH_ENCODING', 'latin-1')

        # 从配置文件中读取代理服务器列表文件(json)的路径
        proxy_file_file = crawler.settings.get("HTTPPROXY_PROXY_LIST_FILE")

        return cls(auth_coding, proxy_file_file)

    def __init__(self, auth_encoding='latin-1', proxy_list_file=None):
        if not proxy_list_file:
            raise NotConfigured

        self.auth_encoding = auth_encoding
        self.proxies = defaultdict(list)

        # 从json文件中读取代理服务器信息，填入self.proxies
        with open(proxy_list_file) as f:
            proxy_list = json.loads(f.read())
            for proxy in proxy_list:
                scheme = proxy['proxy_scheme']
                url = proxy['proxy']
                self.proxies[scheme].append(self._get_proxy(url, scheme))

    def process_request(self, request, spider):
        # 随机选择一个代理
        scheme = re.findall("(.*?):", request.url)[0].upper()
        creds, proxy = random.choice(self.proxies[scheme])
        request.meta['proxy'] = proxy
        if creds:
            request.headers['Proxy-Authorization'] = b'Basic' + creds
'''