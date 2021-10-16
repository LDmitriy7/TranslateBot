import asyncio

import mtranslate as translator


async def translate(text: str) -> str:
    loop = asyncio.get_event_loop()
    translation = await loop.run_in_executor(None, lambda: translator.translate(text))
    return translation
