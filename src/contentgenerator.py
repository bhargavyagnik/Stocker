from create_script import generate_script
from create_audio import generate_audio
from create_video import create_video

def main():
    # Generate script
    script = generate_script()
    
    # Generate audio
    audio_file = "narration.mp3"
    generate_audio(script, audio_file)
    
    # Create video
    create_video(script, audio_file)

if __name__ == "__main__":
    main()