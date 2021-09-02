# Read Audio File Class

import speech_recognition as sr
from pathlib import Path


class ReadAudioFile:

    def __init__(self):
        self.recognizer = sr.Recognizer()

    def __repr__(self):
        return f'TranscriptAudioFile class - recognizer = {self.recognizer}'

    # Checks if the file name contains the file type. If so, removes it.
    @staticmethod
    def check_file_name(fname):
        """Checa se o nome do arquivo contém a extensão e a remove"""

        file_name = fname
        file_formats = ['.wav', '.aiff', '.aiffc', '.flac']
        for i in file_formats:

            # fname = audio_file.wav
            if i in fname:
                file_name = fname.replace(i, '')
        file_name += '.txt'

        # file_name = audio_file.txt
        return file_name

    # Reads a single audio file
    def read_single_file(self, complete_fname):
        """Lê um único arquivo de áudio"""

        # complete_fname = .\Audio\audio_file.wav
        audio_file = sr.AudioFile(complete_fname)

        # Opens the file and reads its contents, storing the data in an AudioFile instance called source.
        with audio_file as source:
            self.recognizer.adjust_for_ambient_noise(source)

            # The record() method records the data from the entire file into an AudioData instance, audio.
            audio = self.recognizer.record(source)
        return audio

    # Reads multiple audio files and returns a list of audio objects
    def read_multiple_files(self, fname):
        """Lê múltiplos arquivos de áudio e retorna uma lista de objetos de áudio"""

        audio_list = list()

        # fname = audio_file.txt
        fname = self.check_file_name(fname).replace('.txt', '')
        directory_path = f'.\\Sliced_Audio_Files\\{fname}'

        # Check if directory exists:
        if Path(directory_path).is_dir():
            i = 0

            # Set path to first audio file
            # complete_fname = .\Sliced_Audio_Files\audio_file\audio{number}.wav
            complete_fname = directory_path + '\\' + f'audio{i}.wav'

            # While there are files in folder, reads audio files
            while Path(complete_fname).is_file():
                audio_file = sr.AudioFile(complete_fname)

                with audio_file as source:
                    self.recognizer.adjust_for_ambient_noise(source)
                    audio = self.recognizer.record(source)
                audio_list.append(audio)
                i += 1
                complete_fname = directory_path + '\\' + f'audio{i}.wav'
        else:
            print('\nDiretório não existe\n')
        return audio_list
