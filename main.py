# Speech to text
# Library docs:
# https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst

# Tutorial:
# https://realpython.com/python-speech-recognition/

import speech_recognition as sr
import os

import Transcript_Audio_File
from Const import Const
from FileExceptions import FileExceptions
from Transcript_Audio_File import *

fname = ''
complete_fname = ''
text = ''

if __name__ == '__main__':
    while True:

        # The purpose of a Recognizer instance is to recognize speech.
        r = sr.Recognizer()
        print(Const.QUESTION_AUDIO_MICROPHONE)
        choice = input(Const.QUESTION_CHOICES)
        if choice == '3':
            print(Const.CLOSING_PROGRAM)
            break
        elif choice == '1':
            audio = read_file(r)
        elif choice == '2':
            audio = listen_microphone(r)
        try:
            text = transcript_file(r, audio)
            try:
                save_file(text)
            except:
                FileExceptions.print_file_exception()
        except:
            FileExceptions.print_general_exception()

    raise SystemExit()
