# Speech to text
# Library docs:
# https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst

# Tutorial:
# https://realpython.com/python-speech-recognition/

import speech_recognition as sr
import os
from Const import Const
from FileExceptions import FileExceptions

# r = sr.Recognizer()


def read_file(recognizer):
    global fname
    fname = input(Const.TYPE_FILE_NAME)
    fpath = '.\\Audio' + '\\' + fname  # Relative file path
    audio_file = sr.AudioFile(fpath)

    #  Opens the file and reads its contents, storing the data in an AudioFile instance called source.
    #  Then the record() method records the data from the entire file into an AudioData instance, audio.
    with audio_file as source:

        # r -> speech_recognition.Recognizer() instance
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.record(source)
    return audio


def listen_microphone(recognizer):
    global fname

    # Just like the AudioFile class, Microphone is a context manager.
    mic = sr.Microphone()
    with mic as source:
        print(Const.LISTENING)
        recognizer.adjust_for_ambient_noise(source)

        # Capture input from the microphone using the listen() method of the Recognizer class.
        # Records input from the source until silence is detected.
        audio = recognizer.listen(source)
    fname = 'recording'
    return audio


# Checks if the file name contains the file type. If so, removes it.
def check_file_name(file_name):
    file_formats = ['.wav', '.aiff', '.aiffc', '.flac']
    for i in file_formats:
        if i in file_name:
            file_name = file_name.replace(i, '')
    file_name += '.txt'
    return file_name


def transcript_file(recognizer, audio):
    global fname
    global complete_fname

    save_path = '.\\Transcripts'

    # All recognize_*() methods of the Recognizer class require an audio_data argument.
    # audio_data must be an instance of SpeechRecognition’s AudioData class.
    # An AudioData instance can come from two sources: from an audio file or audio recorded by a microphone.
    text = recognizer.recognize_google(audio, language='pt-BR')
    print(Const.YOU_SAID, text, '\n')

    fname = check_file_name(fname)
    complete_fname = os.path.join(save_path, fname)

    # Checks if file already exists
    if os.path.exists(complete_fname):
        fname = input(Const.FILE_ALREADY_EXISTS)
        fname = check_file_name(fname)
        complete_fname = os.path.join(save_path, fname)
    print(Const.FILE_SAVED + fname + '\n')
    return text


def save_file(text):
    global complete_fname

    with open(complete_fname, 'w') as txt_file:
        txt_file.write(text)
