import edge_tts
import asyncio


async def audiofromscript(script:str,voice = "en-US-AndrewMultilingualNeural",outputfile = "output.mp3") -> None:
    voice_type = {
        "calm":{
            "pitch" : "-15Hz",
            "rate" : "-30%",
            "volume" : "-50%"
            }
        }
    communicate = edge_tts.Communicate(script, voice, volume=voice_type['calm']['volumne'],pitch=voice_type['calm']['pitch'], rate=voice_type['calm']['rate'])
    await communicate.save(outputfile)

async def get_voices():
    voices = await edge_tts.list_voices()
    return {f"{v['ShortName']} - {v['Locale']} ({v['Gender']})": v['ShortName'] for v in voices}

if __name__ == '__main__':
    script = """Welcome, dear seeker of inner peace. Let us begin our journey to tranquility and self-discovery. Close your eyes and take a deep, cleansing breath.
As you inhale, imagine a warm, golden light entering your body, filling you with calm and positive energy. As you exhale, release any tension, worry, or negative thoughts.
Now, focus your attention on your body. Feel the weight of your body against the surface beneath you. Notice any areas of tightness or discomfort, and with each breath, allow those sensations to soften and melt away.
Visualize yourself in a serene natural setting. Perhaps you're on a quiet beach, in a lush forest, or atop a majestic mountain. Let the peaceful sounds and sights of this place wash over you, further relaxing your mind and body.
As we continue, remember that your thoughts may wander. This is natural. When you notice your mind drifting, gently guide your attention back to your breath and this moment.
Now, let's practice a simple mantra. With each inhale, silently say to yourself, 'I am.' With each exhale, say, 'at peace.' Feel these words resonate within you, affirming your state of calm and presence.
As we conclude our session, bring your awareness back to your physical surroundings. Wiggle your fingers and toes, and when you're ready, slowly open your eyes.
Carry this sense of peace and mindfulness with you throughout your day. Namaste"""
    asyncio.run(audiofromscript(script,voice='en-US-AvaNeural',outputfile=f"output.mp3"))