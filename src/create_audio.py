import edge_tts
import asyncio


async def audiofromscript(script:str,voice = "en-US-AndrewMultilingualNeural",outputfile = "output.mp3") -> None:
    communicate = edge_tts.Communicate(script, voice)
    await communicate.save(outputfile)

async def get_voices():
    voices = await edge_tts.list_voices()
    return {f"{v['ShortName']} - {v['Locale']} ({v['Gender']})": v['ShortName'] for v in voices}

if __name__ == '__main__':
    script = """Good morning, this is Sarah Chen with your financial news update. Here are the top stories that could move markets today:
First, the Federal Reserve is set to announce its latest interest rate decision this afternoon. Analysts widely expect rates to remain unchanged, but investors will be closely watching Chair Powell's comments for any hints about future policy moves."""
    asyncio.run(audiofromscript(script,voice='en-US-AvaNeural',outputfile=f"output.mp3"))