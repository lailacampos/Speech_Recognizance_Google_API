# Listen to Microphone

import speech_recognition as sr
from FileExceptions import *
from Const import *


class ListenMicrophone:

    def __init__(self):
        self.recognizer = sr.Recognizer()

    # Captures audio from default microphone
    def listen_microphone(self):
        '''Captura áudio do microfone padrão'''
        try:
            # Just like the AudioFile class, Microphone is a context manager.
            mic = sr.Microphone()

            with mic as source:
                print(Const.LISTENING)
                self.recognizer.adjust_for_ambient_noise(source)

                # Capture input from the microphone using the listen() method of the Recognizer class.
                # Records input from the source until silence is detected.
                audio = self.recognizer.listen(source, timeout=5)
            return audio
        except Exception:
            raise MicrophoneException()
