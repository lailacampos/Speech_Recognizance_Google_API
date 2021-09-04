class Const:

    # General constants
    EMPTY_OR_WRONG_CHOICE = '\nPor favor, digite uma opção válida.\n'

    # Analyse text or transcript audio constants
    QUESTION_TRANSCRIPT_OR_ANALYSE_TEXT = '\nVocê gostaria de transcrever um ' \
                                          'áudio ou analisar um arquivo de texto?\n'
    TRANSCRIPT_OR_ANALYSE_TEXT_CHOICES = '[1] - Transcrever áudio \n[2] - Analisar arquivo de texto \n[3] - Sair\n'

    # Transcript audio constants
    QUESTION_AUDIO_MICROPHONE = '\nVocê gostaria de transcrever um arquivo de áudio ou usar o microfone?\n'
    TRANSCRIPT_CHOICES = '[1] - Arquivo de áudio \n[2] - Microfone \n[3] - Retornar ao menu anterior \n[4] - Sair\n'
    AUDIO_FILE_DIRECTORY = 'O arquivo de áudio deve estar na pasta Audio, contida na mesma '
    LISTENING = 'Ouvindo...'
    YOU_SAID = 'Você disse: '

    # Analyse text constants


    # Closing application constant
    CLOSING_PROGRAM = '\nAté mais!'

    # File related constants
    TYPE_FILE_NAME = 'Por favor digite o nome do arquivo (com extensão): '
    FILE_SAVED = 'O texto foi salvo em um arquivo de nome '
    FILE_ALREADY_EXISTS = 'Um arquivo de texto com este nome já existe. ' \
                          'Por favor digite um novo nome para o arquivo, sem extensão: '
    FILE_DOES_NOT_EXIST = '\nArquivo não existe.\nDigite um caminho válido:\n'
    FORMAT_NOT_SUPPORTED = '\nFormato não suportado. Por favor escolha um arquivo válido:\n'

    # New features contants
    FEATURE_NOT_IMPLEMENTED = '\nDesculpe! Essa função ainda não foi implementada. :(\n'

    # Visual effect constants
    SEPARATOR = '###################################################################################'
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
