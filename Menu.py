
import sndhdr
import os
from Const import *
from TranscriptAudio.Transcript_Audio_File import *


class Menu:

    # Checks if file exists
    @staticmethod
    def check_if_file_exists(complete_fname):
        """Checa se o arquivo existe"""

        if os.path.isfile(complete_fname):
            return complete_fname
        else:
            return None

    # Checks if user input is not empty and a valid digit
    @staticmethod
    def validate_user_input(choice, number_of_choices):
        """Checa se o input do usuário não está vazio e é uma número válido"""

        choice.strip()

        # If input is not empty
        if not choice or choice == ' ':
            print(Const.EMPTY_OR_WRONG_CHOICE)

        # If user input is a valid number
        elif choice.isnumeric():
            """Se o input do usuário for um número"""

            choice = int(choice)

            # If user input is a valid option
            if 0 < choice <= number_of_choices:
                """Se o input do usuário for uma opção válida"""
                return str(choice)
            else:
                print(Const.EMPTY_OR_WRONG_CHOICE)
                return str(choice)
        else:
            print(Const.EMPTY_OR_WRONG_CHOICE)
            return str(choice)

    # Checks whether an audio file is an wav file or not
    def validate_wav_audio_file(self, complete_fpath):
        """Checa de um arquivo de áudio é do formato wav"""

        file = self.check_if_file_exists(complete_fpath)

        # If file does not exist
        if file is None:
            """Se o arquivo não existir"""

            print(Const.FILE_DOES_NOT_EXIST)
        else:
            type = sndhdr.whathdr(complete_fpath)

            # If file exists and is in a supported audio format
            if type:
                """Se o arquivo existe e é um audio cujo formato é suportado"""

                # If file type is wav
                if type.filetype == 'wav':
                    """Se o formato do arquivo for wav"""

                    return type.filetype
                else:
                    print('File not wav')
                    return None

            # If audio exists but is not in a supported format
            else:
                """Se o arquivo existe mas não está em um formato suportado"""

                print(Const.FORMAT_NOT_SUPPORTED)

    # Main menu
    def main_menu(self):
        """Menu principal"""

        print(Const.LOGO)

        while True:

            print(Const.QUESTION_TRANSCRIPT_OR_ANALYSE_TEXT)
            audio_or_text_choice = input(Const.TRANSCRIPT_OR_ANALYSE_TEXT_CHOICES)
            audio_or_text_choice = self.validate_user_input(audio_or_text_choice, 3)

            if audio_or_text_choice == '3':
                print(Const.CLOSING_PROGRAM)
                break

            # User chose to ranscript audio
            elif audio_or_text_choice == '1':
                """Usuário escolheu transcrever um áudio"""
                print(Const.SEPARATOR)

                # TODO Implement transcript audio menu here
                user_choice = self.transcript_audio_menu()

                # User chose to exit application
                if user_choice == '4':
                    """Usuário escolheu sair do programa"""
                    break

                # User chose to return to previous menu
                elif user_choice == '3':
                    """Usuário escolheu retornar ao menu anterior"""
                    continue

            # User chose to analyse text
            elif audio_or_text_choice == '2':
                """Usuário escolheu analisar um arquivo de texto"""

                print(Const.SEPARATOR)

                # TODO Implement analyse text menu here
                print(Const.FEATURE_NOT_IMPLEMENTED)

        raise SystemExit()

    # Menu that asks the user to choose between transcribing an audio file or using the microphone
    def transcript_audio_menu(self):
        """Menu para a sessão de transcrever áudios. Usuário escolhe entre transcrever um arquivo de áudio no formato .wav ou entre usar o
           microfone"""

        while True:
            print(Const.QUESTION_AUDIO_MICROPHONE)
            user_choice = input(Const.TRANSCRIPT_CHOICES)
            user_choice = self.validate_user_input(user_choice, 4)

            # User chose to exit application
            if user_choice == '4':
                """Usuário escolheu sair da aplicação"""
                print(Const.CLOSING_PROGRAM)
                break

            # User chose to return to previous menu
            elif user_choice == '3':
                """Usuário escolheu retornar ao menu anterior"""

                print(Const.SEPARATOR)
                break

            # User chose to transcript an audio file
            elif user_choice == '1':
                """Usuário escolheu transcrever um arquivo de áudio"""

                print(Const.SEPARATOR)

                # TODO implement transcript audio file menu
                print(Const.FEATURE_NOT_IMPLEMENTED)
                pass

                # # fname should be fname.wav
                # fname = input(Const.TYPE_FILE_NAME)
                # fname = self.validate_user_input(fname)
                # """Fname deve estar no formato nome_do_arquivo.wav"""

            # User chose to use the microphone
            elif user_choice == '2':
                """Usuário escolheu utilizar o microfone"""

                print(Const.SEPARATOR)

                # TODO implement capture and transcript microphone input here
                print(Const.FEATURE_NOT_IMPLEMENTED)

        return user_choice

    # def analyse_text_menu(self):


    # # Transcripts an audio file
    # def transcript_audio_file_function(self):



menu = Menu()


menu.main_menu()

# validation = menu.validate_wav_audio_file(".\\TranscriptAudio\\Audio\\Audio.zip")
# print(validation)
