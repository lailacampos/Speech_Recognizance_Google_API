class Const:
    # General constants
    EMPTY_OR_WRONG_CHOICE = '\nPor favor, digite uma opção válida.\n'
    PRESS_ENTER = '\nPressione qualquer tecla para continuar...\n'
    NO_FILE_CHOSEN = '\nNenhum arquivo escolhido.\n'

    # Analyse text or transcript audio constants
    QUESTION_TRANSCRIPT_OR_ANALYSE_TEXT = '\nVocê gostaria de transcrever um ' \
                                          'áudio ou analisar um arquivo de texto?\n'
    TRANSCRIPT_OR_ANALYSE_TEXT_CHOICES = '[1] - Transcrever áudio \n[2] - Analisar arquivo de texto \n[3] - Sair\n'

    # Transcript audio constants
    QUESTION_AUDIO_MICROPHONE = '\nVocê gostaria de transcrever um arquivo de áudio ou usar o microfone?\n'
    TRANSCRIPT_CHOICES = '[1] - Arquivo de áudio \n[2] - Microfone \n[3] - Retornar ao menu anterior \n[4] - Sair\n'
    AUDIO_FILE_DIRECTORY = '\nO arquivo de áudio deve estar localizado na pasta "Audio", localizada no mesmo diretório que o executável.\n' \
                           'Por favor, digite um arquivo do tipo "nome_do_arquivo.wav"\n'
    CHOOSE_AUDIO_FILE = '\nPor favor selecione um arquivo de audio do tipo wav.\n'
    FILE_TOO_LARGE = '\nArquivo muito grande ou muito longo. O arquivo de audio foi dividido em várias partes.\n' \
                     'O arquivo de texto foi salvo na pasta "Transcripts", no mesmo diretório que o executável\n'
    LISTENING = 'Ouvindo...'
    YOU_SAID = '\nTranscrição:\n'

    # Analyse text constants
    TEXT_FILE_KEYWORD_QUESTION = '\nEscolha uma das opções abaixo:\n'
    TEXT_FILE_OR_KEYWORD_OPTIONS = '[1] - Analisar um arquivo de texto\n[2] - Listar as palavras-chaves\n[3] - Modificar a lista de palavras chaves\n' \
                                   '[4] - Voltar ao menu anterior\n'
    LIST_KEYWORDS_INFO = '\nLista de palavras-chaves em uso:\n'
    MODIFY_KEYWORD_OPTIONS = '[1] - Adicionar palavra-chave à lista\n[2] - Remover palavra-chave da lista\n'
    TEXT_FILE_LOCATION = '\nO arquivo de texto deve estar localizado dentro da pasta "Transcripts", localizada no mesmo diretório que o executável.\n' \
                         'Por favor, digite um nome de arquivo do tipo "nome_do_arquivo.txt"\n'
    CHOOSE_TEXT_FILE = '\nPor favor selecione um arquivo do tipo txt\n'
    NO_KEYWORD_FOUND = '\nNenhuma palavra chave encontrada'
    TEXT_FILE_SAVE_LOCATION = '\nO arquivo foi salvo na pasta "Resultado_Analise_de_Texto", localizada no mesmo diretório que o executável.\n'

    # Closing application constant
    CLOSING_PROGRAM = '\nAté mais!'

    # Directory related constants
    DIRECTORY_DOES_NOT_EXIST = '\nDiretório não existe\n'

    # File related constants
    TYPE_FILE_NAME = 'Por favor digite o nome do arquivo (com extensão): '
    FILE_SAVED = 'O texto foi salvo em um arquivo de nome '
    FILE_ALREADY_EXISTS = 'Um arquivo de texto com este nome já existe. ' \
                          'Por favor digite um novo nome para o arquivo, sem extensão: '
    FILE_DOES_NOT_EXIST = '\nO arquivo não foi encontrado.\nDigite um caminho de arquivo válido.\n'
    FORMAT_NOT_SUPPORTED = '\nFormato não suportado. Por favor escolha um arquivo válido.\n'

    # New features contants
    FEATURE_NOT_IMPLEMENTED = '\nDesculpe! Essa função ainda não foi implementada. :(\n'

    # Error related constants
    UNKNOWN_VALUE_GOOGLE_ERROR = f'\nUm erro aconteceu ao transcrever o arquivo.\nGoogle não entendeu o áudio.\n' \
                                 f'Por favor, tente novamente após tratar o arquivo.\n'

    # Visual effect constants
    SEPARATOR = '#############################################################################################'
    LOGO = '''    
    
      .o.                ooooooooooooo          ooooooooooooo                .o.           
     .888.               8'   888   `8          8'   888   `8               .888.          
    .8"888.                   888                    888                   .8"888.         
   .8' `888.                  888                    888                  .8' `888.        
  .88ooo8888.                 888                    888                 .88ooo8888.       
 .8'     `888.  .o.           888      .o.           888      .o.       .8'     `888.  .o. 
o88o     o8888o Y8P          o888o     Y8P          o888o     Y8P      o88o     o8888o Y8P 
                                 
                                                                            
Análise de Texto e Transcrição de Áudio
'''
