from playsound import playsound
import pygame

# Initialize pygame mixer globally
pygame.mixer.init()

global WhileTrue
WhileTrue = 1

def concentrationCall():
    """
    Plays the concentration alert sound using pygame.
    Ensures the sound is played and resources are released after playback.
    """
    try:
        concentrationCheck = 1
        pygame.mixer.music.load(r"C:\Users\kumar\Downloads\natHACKS2024-Project\my_project\src\concentration_sound.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():  # Wait for the playback to finish
            continue
        pygame.mixer.music.stop()
    except Exception as e:
        print(f"Error in concentrationCall: {e}")
    finally:
        pygame.mixer.quit()  # Ensure resources are released
    return None

def fatigueCall():
    """
    Plays the fatigue alert sound using playsound.
    """
    try:
        fatigueCheck = 1
        print("Playing fatigue sound...")
        playsound(r"C:\Users\kumar\Downloads\natHACKS2024-Project\my_project\src\fatigue_sound.wav")
    except Exception as e:
        print(f"Error in fatigueCall: {e}")
    return None
