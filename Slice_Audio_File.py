# Slice audio file in smaller segments
# Reference:
# https://stackoverflow.com/questions/36632511/split-audio-file-into-several-files-each-below-a-size-threshold

# To do:
# Check if file smaller than 10mb:
# If yes, check if file smaller than 60 minutes
# If yes, slice audio file in multiple small files
# Save small files in a folder
# Append small files' paths in a list
# Return list with paths to small files

# Co-relation between wav file size and duration is given by:
# wav_file_size_in_bytes = (sample rate (44100) * bit rate (16-bit) * number of channels (2 for stereo)
#   * number of seconds) / 8 (8 bits = 1 byte)

import contextlib
import math
import wave
from pathlib import Path
from pydub import AudioSegment
from pydub.utils import make_chunks, mediainfo


# Slices an audio file into several files of roughly 10Mb in size.
# Returns a list with all slices of audio.
def slice_audio(fpath):
    audio = AudioSegment.from_wav(fpath)

    # Get channels
    channel_count = audio.channels
    print(f'Channel count = {channel_count}')

    # Get frame rate
    sample_rate = audio.frame_rate
    print(f'Sample rate = {sample_rate}')

    # Length of audio in seconds
    duration_in_sec = len(audio) / 1000
    print(f'Duration in seconds = {duration_in_sec}')

    # Bit rate
    bit_rate = mediainfo(fpath)
    print(f'Bit rate = {bit_rate["bits_per_sample"]}')

    # Wav file size in bytes
    wav_file_size = (sample_rate * int(bit_rate['bits_per_sample']) * channel_count * duration_in_sec) / 8

    print(f'wav_file_size = {wav_file_size}')

    # 10Mb or 10000000 bytes
    file_split_size = 10000000

    # Integer division return the closest integer value which is less than or equal to a specified expression or value.
    total_chunks = wav_file_size // file_split_size

    # duration_in_sec (X) -->  wav_file_size (Y)
    # duration in sec (K) -->  file size of 10Mb
    # K * Y = X * 10Mb
    # K = (x * 10Mb) / Y

    # math.ceil() rounds a number upward to its nearest integer.
    chuck_len_in_secs = math.ceil((duration_in_sec * 10000000) / wav_file_size)  # In seconds
    chuck_len_in_ms = chuck_len_in_secs * 1000
    chunks = make_chunks(audio, chuck_len_in_ms)

    return chunks


def check_directory(fpath):
    file_formats = ['.wav', '.aiff', '.aiffc', '.flac']
    fname = fpath.replace('.\\Audio\\', '')
    for i in file_formats:
        if i in fname:
            fname = fname.replace(i, '')
    directory = '.\\Sliced_Audio_Files\\' + fname

    # https://docs.python.org/3/library/pathlib.html#pathlib.Path.mkdir
    Path(directory).mkdir(parents=True, exist_ok=True)
    return directory


def export_audio_slices(audio_slices_list, fpath):
    # Exports all of the individual sliced audio files as wav files
    for i, chunk in enumerate(audio_slices_list):
        chunk_name = f'audio{i}.wav'
        print(f'Salvando arquivo {chunk_name}')
        directory = check_directory(fpath)
        chunk.export(directory + '\\' + chunk_name, format='wav')


def check_file_length(fpath):
    # The duration is equal to the number of frames divided by the framerate (frames per second).
    with contextlib.closing(wave.open(fpath, 'r')) as file:
        frames = file.getnframes()
        rate = file.getfranerate()
        duration = frames / float(rate)
        print(duration)
        return duration


def check_file_size(fpath):
    file_size_bytes = Path(fpath).stat().st_size
    file_size_mb = file_size_bytes / 1024 * 1024

    # Check if file less than 10Mb
    if file_size_mb < 10:

        # Check if file length less than 60 minutes
        if check_file_length(fpath) < 3600:
            sliced_audio_list = slice_audio(fpath)
            export_audio_slices(sliced_audio_list)

        else:
            print('Erro: Arquivo mais longo do que 60 minutos')

    else:
        print('Erro: Arquivo maior do que 10Mb')


anatel_audio_1 = '.\\Audio\\anatel_1.wav'
audio_slices = slice_audio(anatel_audio_1)
export_audio_slices(audio_slices, anatel_audio_1)
