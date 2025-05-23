# Challenge Session 5: Asynchronous Web Scraper with aiohttp
# Problem: Develop an asynchronous web scraper that fetches HTML content from multiple URLs concurrently using aiohttp.
# Hint: Use the aiohttp library with asyncio.gather.

import asyncio
import aiohttp

async def fetch_html(session, url):
    async with session.get(url) as response:
        html = await response.text()
        print(f"Fetched {len(html)} characters from {url}")
        return html

async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_html(session, url) for url in urls]
        return await asyncio.gather(*tasks)

if __name__ == "__main__":
    urls = [
        "https://www.example.com",
        "https://www.python.org",
        "https://www.asyncio.org"
    ]
    asyncio.run(fetch_all(urls))
