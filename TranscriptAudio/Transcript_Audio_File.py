# Transcript Audio File Class
# Library docs:
# https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst

# Tutorial:
# https://realpython.com/python-speech-recognition/

import contextlib
import wave
# from Slice_Audio_File import SliceAudioFile
from TranscriptAudio.Slice_Audio_File import SliceAudioFile
from TranscriptAudio.Read_Audio_File import *
from pathlib import Path
from Const import Const
from TranscriptAudio.FileExceptions import *


class TranscriptAudioFile:

    def __init__(self, fname, complete_fname):
        self._fname = fname
        self._complete_fname = complete_fname
        self._recognizer = sr.Recognizer()

    def __repr__(self):
        return f'TranscriptAudioFile class -  fname = {self._fname}, complete_fpath = {self._complete_fname}'

    # region Getters and setters

    # https://www.freecodecamp.org/news/python-property-decorator/
    # Getter using the property decorator:
    @property
    def fname(self):
        return self._fname

    # Setter using the property decorator:
    @fname.setter
    def fname(self, new_fname):
        self._fname = new_fname

    # Getter for _complete_path
    @property
    def complete_fname(self):
        return self._complete_fname

    # Setter for _complete_path
    @complete_fname.setter
    def complete_fname(self, new_path):
        self._complete_fname = new_path

    # Getter for _recognizer
    @property
    def recognizer(self):
        return self._recognizer

    # endregion

    # Saves audio file to disk:
    def export_audio_file(self, audio_obj):
        """Salva arquivo de áudio no disco"""
        try:
            # audio_path = .\Audio\audio_file.wav
            with open(self.complete_fname, 'wb') as file:
                file.write(audio_obj.get_wav_data())  # get_wav_data() is a speech_recognition method
        except Exception:
            raise WriteFileException()

    # Checks if the file name contains the file type. If so, removes it.
    def check_file_name(self):
        """Checa se o nome do arquivo contém o tipo de arquivo. Caso contenha, remove o tipo de arquivo do nome"""
        file_name = self.fname
        file_formats = ['.wav', '.aiff', '.aiffc', '.flac']
        for i in file_formats:

            # fname = audio_file.wav
            if i in self.fname:
                file_name = self.fname.replace(i, '')
        return file_name

    # Checks an audio file length
    def check_file_lenght(self):
        """Checa a duração de um arquivo de áudio em milissegundos"""

        # The duration is equal to the number of frames divided by the framerate (frames per second).
        # complete_file_path = .\Audio\audio_file.wav
        with contextlib.closing(wave.open(self.complete_fname, 'r')) as file:
            frames = file.getnframes()
            rate = file.getframerate()
            duration = frames / float(rate)
        return duration

    # Checks file size
    def check_file_size(self):
        """Checa o tamanho do arquivo de áudio em bytes e megabytes"""

        # complete_file_path = .\Audio\audio_file.wav
        file_size_bytes = Path(self.complete_fname).stat().st_size
        file_size_mb = file_size_bytes / 1024 * 1024
        file_lenght = self.check_file_lenght()
        return {'size_mb': file_size_mb, 'length': file_lenght}

    def save_txt_file(self, text):
        """Salva um arquivo de texto no disco"""
        try:
            # complete.fname = .\Transcripts\audio_file.txt
            with open(self.complete_fname, 'w') as txt_file:
                txt_file.write(text)
        except Exception:
            raise WriteFileException()

    def transcript_single_file(self, audio):
        """Transcreve um único arquivo de áudio"""
        text = ''
        try:
            # All recognize_*() methods of the Recognizer class require an audio_data argument.
            # audio_data must be an instance of SpeechRecognition’s AudioData class.
            # An AudioData instance can come from two sources: from an audio file or audio recorded by a microphone.
            text = self.recognizer.recognize_google(audio, language='pt-BR')
            print(Const.YOU_SAID, text, '\n')
        except Exception:
            error_msg = Const.UNKNOWN_VALUE_GOOGLE_ERROR
            text += error_msg
            print(Const.SEPARATOR)
            print(error_msg)
<<<<<<< HEAD
            self.complete_fname = (".\\Transcripts\\" + self.fname).replace('.wav', '.txt')
=======
            print(Const.SEPARATOR)
            self.complete_fname = ("..\\Transcripts\\" + self.fname).replace('.wav', '.txt')
>>>>>>> analyse-text
            self.save_txt_file(text)
            raise TranscriptSingleFileException()
        finally:
            return text

    # Transcripts a list of audio files and saves the result of each file's transcript as it iterates through the list
    def transcript_multiple_files(self, audio_slices_list):
        """Transcreve uma lista de arquivos de áudio e salva o resultado da transcrição de cada arquivo dinamicamente"""

        text = ''

        # fname initially = audio_file.wav
        self.fname = self.check_file_name()
        self.fname += '.txt'

<<<<<<< HEAD
        # complete_fname = .\Transcripts\audio_file.txt
=======
        # complete_file_path = .\Transcripts\audio_file.txt
>>>>>>> analyse-text
        self.complete_fname = '.\\Transcripts\\' + self.fname

        try:
            for index, audio in enumerate(audio_slices_list):
                try:
                    text += f'audio{index} - ' + self.recognizer.recognize_google(audio, language='pt-BR') + '\n\n'

                    # complete_file_path = .\Transcripts\audio_file.txt
                    self.save_txt_file(text)
                except Exception:
                    error_msg = Const.UNKNOWN_VALUE_GOOGLE_ERROR
                    text += error_msg
                    print(error_msg)
                    self.complete_fname = ("..\\Transcripts\\" + self.fname).replace('.wav', '.txt')
                    self.save_txt_file(text)
                    raise TranscriptMultipleFilesException
        except TranscriptFileException:
            raise TranscriptFileException()
        finally:
            return text

    # Decides whether the file needs to be sliced and either transcripts a single file or transcripts multiple slices files
    def determine_single_or_multiple_transcript(self):
        """Decide se o arquivo precisa ser dividido ou não, e a depender da decisão, chama a função que transcreve
            um único arquivo ou a função que transcreve múltiplos arquivos de áudio"""

        # complete_file_path = .\Audio\audio_file.wav
        size_length_dict = self.check_file_size()

        # Check if file larger than 10Mb or if file length more than 60 minutes
        if size_length_dict['size_mb'] > 10000000 or size_length_dict['length'] > 3600:
            try:

                # complete_file_path = .\Audio\audio_file.wav
                slice_audio_file = SliceAudioFile(self.complete_fname)
                sliced_audio_list = slice_audio_file.slice_audio()

                # fpath = .\Sliced_Audio_Files\audio_file
                slice_audio_file.export_audio_slices(sliced_audio_list)

                try:
                    read_audio_file = ReadAudioFile()
                    audio_list = read_audio_file.read_multiple_files(self.fname)
                    text = self.transcript_multiple_files(audio_list)
                    print(Const.FILE_TOO_LARGE)
                except Exception:
                    raise TranscriptMultipleFilesException()
            except Exception:
                raise SliceFileException()

        else:
            try:
                # complete_file_path = .\Audio\audio_file.wav
                read_audio_file = ReadAudioFile()
                audio = read_audio_file.read_single_file(self.complete_fname)
                text = self.transcript_single_file(audio)
            except Exception:
                raise TranscriptSingleFileException
        return text
