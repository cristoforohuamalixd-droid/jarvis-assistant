import edge_tts
import asyncio

async def main():
    voices = await edge_tts.list_voices()
    for v in voices:
        if 'es' in v['Locale']:
            print(f"{v['ShortName']} - {v['Gender']} - {v['Locale']}")

asyncio.run(main())
