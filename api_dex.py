import asyncio
import aiohttp
import json
import time

async def fetch_fov_data():
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get("https://api.dexscreener.com/latest/dex/search?q=FOV/TON") as response:
                if response.status == 200:
                    data = await response.json()
                    fov_tokens = []
                    if 'pairs' in data:
                        for pair in data['pairs']:
                            if 'FOV' in pair.get('baseToken', {}).get('symbol', '') or 'FOV' in pair.get('quoteToken', {}).get('symbol', ''):
                                fov_tokens.append(pair)
                                if pair["baseToken"].get("name") == "fovcoin":
                                    price_usd = pair.get("priceUsd")
                                    price_ton = pair.get("priceNative") 
                                    if price_usd:
                                        print(price_usd, price_ton)
                                        return price_usd, price_ton
                else:
                    print(f"Ошибка при получении данных: {response.status} - {await response.text()}")
                    return None
        except aiohttp.ClientError as e:
            print(f"Ошибка сети: {e}")
            return None

