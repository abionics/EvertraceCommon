import aiohttp


async def fetch(url: str, data: dict) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data, verify_ssl=False) as response:
            response = await response.json()
            if response['exception']:
                reason = response['reason']
                raise Exception(f'Exception occurs in sub service: {reason=}, {url=}')
            return response['result']
