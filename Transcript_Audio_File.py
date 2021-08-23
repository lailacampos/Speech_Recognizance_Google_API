# Speech to text
# Library docs:
# https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst

# Tutorial:
# https://realpython.com/python-speech-recognition/

import speech_recognition as sr
from Slice_Audio_File import *
from Const import Const
from FileExceptions import *

fname = ''


# Saves audio file to disk
def export_audio_file(audio_path, audio_obj):
    try:
        with open(audio_path, 'wb') as file:
            file.write(audio_obj.get_wav_data())
    except Exception:
        raise WriteFileException


def set_fname(file_name):
    global fname
    fname = file_name


def read_single_file(recognizer, complete_fname):
    audio_file = sr.AudioFile(complete_fname)

    #  Opens the file and reads its contents, storing the data in an AudioFile instance called source.
    #  Then the record() method records the data from the entire file into an AudioData instance, audio.
    with audio_file as source:
        # r -> speech_recognition.Recognizer() instance
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.record(source)
    return audio


def read_multiple_files(recognizer):
    global fname

    audio_list = []
    fname = check_file_name(fname).replace('.txt', '')
    directory_path = f'.\\Sliced_Audio_Files\\{fname}'

    # Check if directory exists
    if Path(directory_path).is_dir():
        i = 0
        complete_fpath = directory_path + '\\' + f'audio{i}.wav'
        while Path(complete_fpath).is_file():
            audio_file = sr.AudioFile(complete_fpath)

            with audio_file as source:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.record(source)
            audio_list.append(audio)
            i += 1
            complete_fpath = directory_path + '\\' + f'audio{i}.wav'
    return audio_list


def listen_microphone(recognizer):
    global fname

    try:
        # Just like the AudioFile class, Microphone is a context manager.
        mic = sr.Microphone()
        with mic as source:
            print(Const.LISTENING)
            recognizer.adjust_for_ambient_noise(source)

            # Capture input from the microphone using the listen() method of the Recognizer class.
            # Records input from the source until silence is detected.
            audio = recognizer.listen(source, timeout=5)
        return audio
    except Exception:
        raise MicrophoneException


# Checks if the file name contains the file type. If so, removes it.
def check_file_name(file_name):
    file_formats = ['.wav', '.aiff', '.aiffc', '.flac']
    for i in file_formats:
        if i in file_name:
            file_name = file_name.replace(i, '')
    file_name += '.txt'
    return file_name


# TODO Modularize function (it's too big and it does multiple stuff right now. It needs to be split into multiple functions)
# Checks file size, decides whether the file needs to be sliced and either transcripts a single file or transcripts
# multiple slices files
def check_file_size(recognizer, complete_fname):
    global fname

    try:
        file_size_bytes = Path(complete_fname).stat().st_size
        file_size_mb = file_size_bytes / 1024 * 1024
        file_length = check_file_length(complete_fname)
    except Exception:
        raise FileDoesNotExistException

    # Check if file larger than 10Mb or if file length more than 60 minutes
    if file_size_mb > 10000000 or file_length > 3600:
        try:
            sliced_audio_list = slice_audio(complete_fname)
            export_audio_slices(sliced_audio_list, complete_fname)

            try:
                audio_list = read_multiple_files(recognizer)
                text = transcript_multiple_files(recognizer, audio_list, fname)
                print('Arquivo muito grande ou muito longo. O arquivo de audio foi dividido em várias partes.\n'
                      'O arquivo de texto encontra-se na pasta "Transcripts"')
            except Exception:
                raise TranscriptMultipleFiles()
        except Exception:
            raise TranscriptFileError()
    else:
        try:
            audio = read_single_file(recognizer, complete_fname)
            text = transcript_single_file(recognizer, audio)
        except Exception:
            raise TranscriptSingleFile()

    return text


def transcript_single_file(recognizer, audio):

    # All recognize_*() methods of the Recognizer class require an audio_data argument.
    # audio_data must be an instance of SpeechRecognition’s AudioData class.
    # An AudioData instance can come from two sources: from an audio file or audio recorded by a microphone.
    text = recognizer.recognize_google(audio, language='pt-BR')
    print(Const.YOU_SAID, text, '\n')
    return text


# Transcripts a list of audio files and saves the result of each file's transcript as it iterates through the list
def transcript_multiple_files(recognizer, audio_slices_list, fname):
    text = ''
    fname = check_file_name(fname)
    complete_fname = ".\\Transcripts\\" + fname

    for index, audio in enumerate(audio_slices_list):
        try:
            text += f'audio{index} - ' + recognizer.recognize_google(audio, language='pt-BR') + '\n\n'
        except Exception as e:
            print(f'\n\nUm erro aconteceu ao transcrever o arquivo audio{index}.\nGoogle não entendeu o áudio.\n'
                  f'Por favor, tente novamente após tratar o arquivo.\n')
            print(f'Exceção: {e}\n')
        save_file(text, complete_fname)
    return text


def save_file(text, complete_fname):
    try:
        with open(complete_fname, 'w') as txt_file:
            txt_file.write(text)
    except Exception:
        raise WriteFileException
