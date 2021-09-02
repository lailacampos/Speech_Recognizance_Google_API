# Main revised script

# Speech to text
# Library docs:
# https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst

# Useful tutorial:
# https://realpython.com/python-speech-recognition/

import os
from Transcript_Audio_File import *
from Listen_Microphone import ListenMicrophone

if __name__ == '__main__':
    while True:

        # Menu that asks the user to choose between transcribing an audio file or using the microphone
        print(Const.QUESTION_AUDIO_MICROPHONE)
        choice = input(Const.QUESTION_CHOICES)

        # Close the application
        if choice == '3':
            print(Const.CLOSING_PROGRAM)
            break

        # Transcript audio file
        elif choice == '1':

            fname = input(Const.TYPE_FILE_NAME)  # fname = audio_file.wav
            complete_fname = '.\\Audio\\' + fname  # Relative audio file path

            try:
                transcript_audio_file = TranscriptAudioFile(fname, complete_fname)
                # Checks if file exists
                if os.path.isfile(complete_fname):

                    # Checks file size, decides whether the file needs to be sliced and either transcripts a single file or transcripts multiple
                    # slices files.
                    text = transcript_audio_file.determine_single_or_multiple_transcript()
                    transcript_audio_file.fname = transcript_audio_file.fname.replace('.txt', '')

                    try:

                        # fname = audio_file.wav
                        fname = transcript_audio_file.check_file_name()
                        complete_fname = '.\\Transcripts\\' + fname + '.txt'
                        transcript_audio_file.complete_fname = complete_fname
                        transcript_audio_file.save_txt_file(text)

                    except Exception:
                        raise WriteFileException()
                else:
                    print('\nO arquivo não foi encontrado.\nPor favor digite o nome de um arquivo válido:\n')
            except Exception:
                raise TranscriptFileError()

        # Capture input from microphone
        elif choice == '2':
            listen_mic = ListenMicrophone()
            audio = listen_mic.listen_microphone()
            fname = 'recording.wav'
            complete_fname = '.\\Audio' + '\\' + fname  # Relative file path
            transcript_audio_file = TranscriptAudioFile(fname, complete_fname)

            try:
                transcript_audio_file.export_audio_file(audio)
            except Exception:
                raise ExportAudioFileException()

            try:
                text = transcript_audio_file.determine_single_or_multiple_transcript()
                fname = transcript_audio_file.check_file_name()
                fname += '.txt'
                transcript_audio_file.complete_fname = ".\\Transcripts\\" + fname
                transcript_audio_file.save_txt_file(text)
            except Exception:
                raise WriteFileException()
    raise SystemExit()
