import asyncio
import aiohttp
import json
import os
import time

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "traffic-config.json")

def load_config():
    try:
        with open(CONFIG_PATH, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading config: {e}")
        return {"enabled": False, "requests_per_second": 0, "target_url": ""}

async def send_request(session, url):
    if not url or url == "http://SERVER_LB_IP_HERE":
        return
    try:
        async with session.get(url, timeout=5) as response:
            await response.read()
    except Exception as e:
        print(f"Request failed: {e}")

async def producer_loop():
    async with aiohttp.ClientSession() as session:
        while True:
            config = load_config()
            if not config.get("enabled", False):
                await asyncio.sleep(1)
                continue
                
            rps = config.get("requests_per_second", 0)
            url = config.get("target_url", "")
            
            if rps <= 0:
                await asyncio.sleep(1)
                continue
                
            tasks = []
            for _ in range(rps):
                tasks.append(asyncio.create_task(send_request(session, url)))
                
            await asyncio.sleep(1)
            # We don't await the tasks here to keep firing at the required rate
            # They will complete in the background

if __name__ == "__main__":
    print("Producer started.")
    asyncio.run(producer_loop())
