from playsound import playsound 
global WhileTrue
WhileTrue = 1
def concentrationCall():
    concentrationCheck = 1
    playsound('concentration_sound.wav')
    return None

def fatigueCall():
    fatigueCheck = 1
    playsound('fatigue_sound.wav')
    return None