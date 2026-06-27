import re

def count_urls(text):
    urls = re.findall(r'https?://\\S+|www\\.\\S+', text)
    return len(urls)