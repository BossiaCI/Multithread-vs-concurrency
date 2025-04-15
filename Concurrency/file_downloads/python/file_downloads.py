import asyncio
import aiohttp

async def fetch(url, session):
    async with session.get(url) as response:
        # Read the response text (could be Json, html...)
        return await response.text()

async def main():
    urls = [
        'https://www.python.org',
        'https://www.djangoproject.com',
        'https://www.asyncio.org'
    ]

    async with aiohttp.ClientSession() as session:
        # Create a list of tasks for each URL fetch
        tasks = [fetch(url, session) for url in urls]

        # Run all tasks concurrently and wait for them to complete
        pages = await asyncio.gather(*tasks)

        # Print a summary of each fetched page
        for url, page in zip(urls, pages):
            print(f"Fetched {len(page)} characters from {url}")

# Entry point for the asyncio program
if __name__ == "__main__":
    asyncio.run(main())