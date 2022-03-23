import asyncio
import random

import settings


async def random_sleep(min_sleep: int, max_sleep: int) -> None:
    if not settings.DEBUG:
        await asyncio.sleep(random.randint(min_sleep, max_sleep + 1))
