# Speech to text
# Library docs:
# https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst

# Tutorial:
# https://realpython.com/python-speech-recognition/

import speech_recognition as sr
import os
from Const import Const
from FileExceptions import FileExceptions

fname = ''
complete_fname = ''
text = ''


def read_file():
    global fname
    fname = input(Const.TYPE_FILE_NAME)
    fpath = '.\\Audio' + '\\' + fname  # Relative file path
    audio_file = sr.AudioFile(fpath)

    #  Opens the file and reads its contents, storing the data in an AudioFile instance called source.
    #  Then the record() method records the data from the entire file into an AudioData instance, audio.
    with audio_file as source:

        # The adjust_for_ambient_noise() method reads the first second of the file stream and calibrates the recognizer
        # to the noise level of the audio.
        # Therefore, that portion of the stream is consumed before you call record() to capture the data.
        r.adjust_for_ambient_noise(source)
        audio = r.record(source)

    return audio


def listen_microphone():
    global fname

    # Just like the AudioFile class, Microphone is a context manager.
    mic = sr.Microphone()
    with mic as source:
        print(Const.LISTENING)
        r.adjust_for_ambient_noise(source)

        # Capture input from the microphone using the listen() method of the Recognizer class.
        # Records input from the source until silence is detected.
        audio = r.listen(source)
    fname = 'recording'
    return audio


# Checks if the file name contains the file type. If so, removes it.
def check_file_name(file_formats_list, file_name):
    for i in file_formats_list:
        if i in file_name:
            file_name = file_name.replace(i, '')
    file_name += '.txt'
    return file_name


# Transforms audio in text and saves to .txt file
def transcript_file():
    global complete_fname
    global fname
    global text

    # All recognize_*() methods of the Recognizer class require an audio_data argument.
    # audio_data must be an instance of SpeechRecognition’s AudioData class.
    # An AudioData instance can come from two sources: from an audio file or audio recorded by a microphone.
    text = r.recognize_google(audio, language='pt-BR')
    print(Const.YOU_SAID, text, '\n')
    save_path = '.\Transcripts'
    file_formats = ['.wav', '.aiff', '.aiffc', '.flac']

    # Checks if the file name contains the file type. If so, removes it.
    fname = check_file_name(file_formats, fname)
    complete_fname = os.path.join(save_path, fname)

    # Checks if file already exists
    if os.path.exists(complete_fname):
        fname = input(Const.FILE_ALREADY_EXISTS)
        fname = check_file_name(file_formats, fname)
        complete_fname = os.path.join(save_path, fname)
    print(Const.FILE_SAVED + fname + '\n')


def save_file():
    txt_file = open(complete_fname, 'w')
    txt_file.write(text)
    txt_file.close()


while True:

    # The purpose of a Recognizer instance is to recognize speech.
    r = sr.Recognizer()
    print(Const.QUESTION_AUDIO_MICROPHONE)
    choice = input(Const.QUESTION_CHOICES)
    if choice == '3':
        print(Const.CLOSING_PROGRAM)
        break
    elif choice == '1':
        audio = read_file()
    elif choice == '2':
        audio = listen_microphone()
    try:
        transcript_file()
        try:
            save_file()
        except:
            FileExceptions.print_file_exception()
    except:
        FileExceptions.print_general_exception()

raise SystemExit()