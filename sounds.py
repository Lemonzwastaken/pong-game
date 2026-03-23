import winsound
import os
import sys
BASE_DIR = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

def play_sound(file):
    path = os.path.join(BASE_DIR, file)
    winsound.PlaySound(path, winsound.SND_FILENAME | winsound.SND_ASYNC)
