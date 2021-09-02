# Slice Audio File Class

# Slice audio file in smaller segments
# Reference:
# https://stackoverflow.com/questions/36632511/split-audio-file-into-several-files-each-below-a-size-threshold

# Co-relation between wav file size and duration is given by:
# wav_file_size_in_bytes = (sample rate (44100) * bit rate (16-bit) * number of channels (2 for stereo)
#   * number of seconds) / 8 (8 bits = 1 byte)

# import contextlib
import math
# import wave
from FileExceptions import *
from pathlib import Path
from pydub import AudioSegment
from pydub.utils import make_chunks, mediainfo


class SliceAudioFile:

    def __init__(self, fpath):
        self._fpath = fpath

    # region Getters and Setters

    # Getter for fpath
    @property
    def fpath(self):
        return self._fpath

    # Setter for path
    @fpath.setter
    def fpath(self, new_path):
        self._fpath = new_path

    # endregion

    # Checks if directory exists
    def check_if_directory_exists(self):
        """Checa se o diretório existe"""
        file_formats = ['.wav', '.aiff', '.aiffc', '.flac']

        # fpath = .\Audio\audio_file.wav
        fname = self.fpath.replace('.\\Audio\\', '')
        for i in file_formats:
            if i in fname:
                fname = fname.replace(i, '')
        directory = '.\\Sliced_Audio_Files\\' + fname
        if Path(directory).is_dir():
            print('Pasta já existe.')
        else:
            self.create_directory(directory)
        return directory

    @staticmethod
    def create_directory(directory):
        # https://docs.python.org/3/library/pathlib.html#pathlib.Path.mkdir
        Path(directory).mkdir(parents=True, exist_ok=True)

    # Slices an audio file into several files of roughly 10Mb in size.
    # Returns a list with all slices of audio.
    def slice_audio(self):
        """Divide um arquivo de áudio em vários pedaços de aproximadamente 10mb de tamanho cada um.

        Retorna uma lista com todas as fatias de áudio do áudio dividido"""
        try:
            # fpath = .\Audio\audio_file.wav
            audio = AudioSegment.from_wav(self.fpath)

            # Get channels
            channel_count = audio.channels

            # Get frame rate
            sample_rate = audio.frame_rate

            # Length of audio in seconds
            duration_in_sec = len(audio) / 1000

            # Bit rate
            bit_rate = mediainfo(self.fpath)

            # Wav file size in bytes
            wav_file_size_bytes = (sample_rate * int(bit_rate['bits_per_sample']) * channel_count * duration_in_sec) / 8

            # 10Mb or 10000000 bytes
            # file_split_size = 10000000

            # Integer division ( \\ ) returns the closest integer value which is less than or equal to a specified expression or value.
            # total_chunks = wav_file_size_bytes // file_split_size

            # duration_in_sec (X) -->  wav_file_size (Y)
            # duration in sec (K) -->  file size of 10Mb
            # K * Y = X * 10Mb
            # K = (x * 10Mb) / Y

            # math.ceil() rounds a number upward to its nearest integer.
            chunk_length_in_secs = math.ceil((duration_in_sec * 10000000) / wav_file_size_bytes)  # In seconds
            chunk_length_in_ms = chunk_length_in_secs * 1000

            chunks = make_chunks(audio, chunk_length_in_ms)

        except Exception:
            raise SliceFileException()

        return chunks

    # Exports audio slices
    def export_audio_slices(self, audio_slices_list):
        """Exporta os pedaços do áudio divido"""

        # fpath = .\Sliced_Audio_Files\audio_file
        directory = self.check_if_directory_exists()
        # Exports all of the individual sliced audio files as wav files
        for i, chunk in enumerate(audio_slices_list):
            chunk_name = f'audio{i}.wav'

            try:
                chunk.export(directory + '\\' + chunk_name, format='wav')
                print(f'Salvando arquivo {chunk_name}')
            except Exception:
                raise WriteFileException()
