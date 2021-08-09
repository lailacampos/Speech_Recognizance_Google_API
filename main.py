# Speech to text
# Library docs:
# https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst

# Tutorial:
# https://realpython.com/python-speech-recognition/

import speech_recognition as sr
import os

import Transcript_Audio_File
from Const import Const
from FileExceptions import *
from Transcript_Audio_File import *

fname = ''
complete_fname = ''
text = ''

if __name__ == '__main__':
    while True:

        # The purpose of a Recognizer instance is to recognize speech.
        r = sr.Recognizer()

        # Menu that asks the user to choose between transcribing an audio file or using the microphone
        print(Const.QUESTION_AUDIO_MICROPHONE)
        choice = input(Const.QUESTION_CHOICES)
        if choice == '3':
            print(Const.CLOSING_PROGRAM)
            break
        elif choice == '1':
            fname = input(Const.TYPE_FILE_NAME)
            set_fname(fname)
            complete_fname = '.\\Audio' + '\\' + fname  # Relative file path
            try:
                if os.path.isfile(complete_fname):
                    # Checks file size, decides whether the file needs to be sliced and either transcripts a single file or
                    # transcripts multiple slices files
                    # audio = read_single_file(r, complete_fname)
                    text = check_file_size(r, fname, complete_fname)
                else:
                    print('O arquivo não foi encontrado.\nPor favor digite o nome de um arquivo válido:\n')

                try:
                    fname = check_file_name(fname)
                    complete_fname = ".\\Transcripts\\" + fname
                    save_file(text, complete_fname)
                except:
                    raise WriteFileException()
            except:
                raise GeneralException
        elif choice == '2':
            audio = listen_microphone(r)
            fname = 'recording.wav'
            set_fname(fname)
            complete_fname = '.\\Audio' + '\\' + fname  # Relative file path
            try:
                export_audio_file(complete_fname, audio)
            except:
                raise ExportAudioFileException
            try:
                text = check_file_size(r, fname, complete_fname)
                fname = check_file_name(fname)
                complete_fname = ".\\Transcripts\\" + fname
                save_file(text, complete_fname)
            except:
                raise WriteFileException()

    raise SystemExit()
