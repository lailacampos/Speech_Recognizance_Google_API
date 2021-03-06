
import sndhdr
import os

import Const
from Const import *
from TranscriptAudio.Transcript_Audio_File import *
from TranscriptAudio.FileExceptions import *
from AnalyseText.ProcessText import *
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename


class Menu:

    # TODO Maybe add an ProcessText object as an attribute of the class so the keywords choices will persist?

    # Checks if file exists
    @staticmethod
    def check_if_file_exists(complete_file_path):
        """Checa se o arquivo existe"""

        if os.path.isfile(complete_file_path):
            return complete_file_path
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
                print(Const.SEPARATOR)
                print(Const.EMPTY_OR_WRONG_CHOICE)
                print(Const.SEPARATOR)
                return str(choice)
        else:
            print(Const.SEPARATOR)
            print(Const.EMPTY_OR_WRONG_CHOICE)
            print(Const.SEPARATOR)
            return str(choice)

    # TODO This function is obsolete and should be deleted
    # Checks whether an audio file is an wav file or not
    def validate_wav_audio_file(self, complete_file_path):
        """Checa de um arquivo de áudio é do formato wav"""

        file = self.check_if_file_exists(complete_file_path)

        # If file does not exist
        if file is None:
            """Se o arquivo não existir"""

            print(Const.SEPARATOR)
            print(Const.FILE_DOES_NOT_EXIST)
            print(Const.SEPARATOR)
            return None
        else:
            file_type = sndhdr.whathdr(complete_file_path)

            # If file exists and is in a supported audio format
            if file_type:
                """Se o arquivo existe e é um audio cujo formato é suportado"""

                # If file file_type is wav
                if file_type.filetype == 'wav':
                    """Se o formato do arquivo for wav"""

                    return complete_file_path
                else:
                    print('File not wav')
                    return None

            # If audio exists but is not in a supported format
            else:
                """Se o arquivo existe mas não está em um formato suportado"""

                print(Const.SEPARATOR)
                print(Const.FORMAT_NOT_SUPPORTED)
                print(Const.SEPARATOR)
                return None

    # TODO This function is obsolete and should be deleted
    # Checks if file is a .txt file
    def validate_text_file(self, complete_file_path):
        """Checa se um arquivo é do tipo .txt"""

        txt_file = self.check_if_file_exists(complete_file_path)

        # If file does not exist
        if txt_file is None:
            """Se o arquivo não existir"""
            print(Const.SEPARATOR)
            print(Const.FILE_DOES_NOT_EXIST)
            print(Const.SEPARATOR)
            return None

        else:
            # If file exists and is a .txt file
            if complete_file_path.lower().endswith('.txt'):
                """Se o arquivo existe e é do tipo .txt"""
                return complete_file_path

            # If file exists but is not a .txt file
            else:
                """Se o arquivo existe e não é do tipo .txt"""

                print(Const.SEPARATOR)
                print(Const.FORMAT_NOT_SUPPORTED)
                print(Const.SEPARATOR)
                return None

    # Transcripts an audio file
    def transcript_audio_file_function(self):

        root = Tk()
        root.attributes("-topmost", True)
        root.withdraw()

        print(Const.CHOOSE_AUDIO_FILE)
        input(Const.PRESS_ENTER)

        # file_name = input(Const.TYPE_FILE_NAME)

        # complete_file_path = '.\\Audio\\' + file_name  # Relative audio file path
        complete_file_path = askopenfilename()
        complete_file_path = self.validate_wav_audio_file(complete_file_path)

        if complete_file_path is not None:
            # file_name should be: file_name.wav
            file_name = os.path.basename(complete_file_path)
            """file_name deve estar no formato: nome_do_arquivo.wav"""

            if file_name is not None:

                transcript_audio_file_obj = TranscriptAudioFile(file_name, complete_file_path)

                try:
                    # Checks file size, decides whether the file needs to be sliced and either transcripts a single file or transcripts multiple
                    # slices files.
                    text = transcript_audio_file_obj.determine_single_or_multiple_transcript()
                    """Checa o tamanho do arquivo de áudio, decide se o arquivo precisa ser divido em partes menores e ou transcreve um único arquivo ou
                       transcreve múltiplos arquivos menores"""

                    transcript_audio_file_obj.fname = transcript_audio_file_obj.fname.replace('.txt', '')

                    try:
                        # file_name should be: file_name.wav
                        file_name = transcript_audio_file_obj.check_file_name()  # file_name should be: file_name

                        # Tk().withdraw()
                        # complete_file_path = askopenfilename()
                        complete_file_path = '.\\Transcripts\\' + file_name + '.txt'
                        transcript_audio_file_obj.complete_fname = complete_file_path
                        transcript_audio_file_obj.save_txt_file(text)

                    except WriteFileException:
                        raise WriteFileException()

                except TranscriptFileException:
                    raise TranscriptFileException()

        else:
            print(Const.NO_FILE_CHOSEN)
            print(Const.SEPARATOR)

    def analyse_text_function(self):

        Tk().withdraw()
        print(Const.CHOOSE_TEXT_FILE)
        input(Const.PRESS_ENTER)

        # print(Const.TEXT_FILE_LOCATION)

        # file_name = input(Const.TYPE_FILE_NAME)

        complete_file_path = askopenfilename()
        # complete_file_path = '.\\Transcripts\\' + file_name  # Relative audio file path
        complete_file_path = self.validate_text_file(complete_file_path)

        if complete_file_path is not None:
            # file_name should be: file_name.txt
            file_name = os.path.basename(complete_file_path)
            """file_name deve estar no formato: file_name.txt"""

            if file_name is not None:

                processText = ProcessText(file_name)
                processText.text_file_path = complete_file_path

                try:
                    processText.open_txt_file()
                    result_dict = processText.process_text()
                    result_text = processText.print_dict_results(result_dict)
                    complete_file_path = '.\\Resultado_Analise_de_Texto\\' + file_name
                    processText.text_file_path = complete_file_path
                    if result_text is not None:
                        processText.save_txt_file(complete_file_path, result_text)
                        print(Const.SEPARATOR)
                        print(Const.TEXT_FILE_SAVE_LOCATION)
                        print(Const.SEPARATOR)

                except WriteFileException:
                    raise WriteFileException
        else:
            print(Const.NO_FILE_CHOSEN)
            print(Const.SEPARATOR)

    @staticmethod
    def list_keywords_function():
        processText = ProcessText('')
        processText.print_complete_keyword_list()

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

                self.transcript_audio_file_function()

            # User chose to use the microphone
            elif user_choice == '2':
                """Usuário escolheu utilizar o microfone"""

                print(Const.SEPARATOR)

                # TODO implement capture and transcript microphone input here
                print(Const.FEATURE_NOT_IMPLEMENTED)
                print(Const.SEPARATOR)

        return user_choice

    def analyse_text_menu(self):

        while True:

            print(Const.TEXT_FILE_KEYWORD_QUESTION)
            user_choice = input(Const.TEXT_FILE_OR_KEYWORD_OPTIONS)
            user_choice = self.validate_user_input(user_choice, 4)

            # User chose return to previous menu
            if user_choice == '4':
                """Usuário escolheu retornar ao menu anterior"""

                print(Const.SEPARATOR)
                break

            # User chose to analyse a text file
            elif user_choice == '1':
                """Usuário escolheu analisar um arquivo de texto"""

                print(Const.SEPARATOR)

                self.analyse_text_function()

            # User chose to list keywords
            elif user_choice == '2':
                """Usuário escolheu listar as palavras-chaves"""

                print(Const.SEPARATOR)

                self.list_keywords_function()
                print(Const.SEPARATOR)

            # User chose to modify keyword list
            elif user_choice == '3':
                """Usuário escolheu modificar a lista de palavras-chaves"""

                # TODO implement modify keyword list here
                print(Const.SEPARATOR)
                self.modify_keywords_menu()

        return user_choice

    def modify_keywords_menu(self):

        while True:
            print(Const.TEXT_FILE_KEYWORD_QUESTION)
            user_choice = input(Const.MODIFY_KEYWORD_OPTIONS)
            user_choice = self.validate_user_input(user_choice, 2)

            # User chose to add keyword to the list
            if user_choice == '1':
                """Usuário escolheu adicionar palavra-chave à lista"""

                print(Const.SEPARATOR)
                print(Const.FEATURE_NOT_IMPLEMENTED)
                print(Const.SEPARATOR)
                break

            # user chose to remove keyword from the list
            elif user_choice == '2':
                """Usuário escolheu remover palavra chave da lista"""

                print(Const.SEPARATOR)
                print(Const.FEATURE_NOT_IMPLEMENTED)
                print(Const.SEPARATOR)
                break

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

            # User chose to transcript audio
            elif audio_or_text_choice == '1':
                """Usuário escolheu transcrever um áudio"""
                print(Const.SEPARATOR)

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
                user_choice = self.analyse_text_menu()

                # User chose to return to previous menu
                if user_choice == '4':
                    """Usuário escolheu retornar ao menu anterior"""
                    continue

        raise SystemExit()
