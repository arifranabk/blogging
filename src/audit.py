import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd
import logging

class SEOAuditor:
    def __init__(self):
        self.results = []
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    def fetch_page(self, url):
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            logging.error(f"Error fetching {url}: {e}")
            return None

    def analyze_content(self, html, url):
        soup = BeautifulSoup(html, 'lxml')
        data = {
            'url': url,
            'status_code': 200,
            'title': None,
            'title_length': 0,
            'meta_description': None,
            'meta_desc_length': 0,
            'h1_count': 0,
            'h1_content': None,
            'canonical': None,
            'word_count': 0
        }

        # Title Analysis
        if soup.title:
            data['title'] = soup.title.string.strip() if soup.title.string else ""
            data['title_length'] = len(data['title'])

        # Meta Description
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        if meta_desc:
            data['meta_description'] = meta_desc.get('content', '').strip()
            data['meta_desc_length'] = len(data['meta_description'])

        # H1 Analysis
        h1_tags = soup.find_all('h1')
        data['h1_count'] = len(h1_tags)
        if h1_tags:
            data['h1_content'] = h1_tags[0].get_text(strip=True)

        # Canonical
        canonical = soup.find('link', attrs={'rel': 'canonical'})
        if canonical:
            data['canonical'] = canonical.get('href')

        # Content Analysis (Basic Word Count)
        text = soup.get_text(separator=' ')
        data['word_count'] = len(text.split())

        return data

    def audit_url(self, url):
        response = self.fetch_page(url)
        if not response:
            return {'url': url, 'error': 'Failed to fetch'}
        
        return self.analyze_content(response.text, url)
