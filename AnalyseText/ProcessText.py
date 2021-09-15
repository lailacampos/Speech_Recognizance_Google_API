# Natural Language Processing in Portuguese
# http://www.nltk.org/howto/portuguese_en.html

# Useful sites:
# https://stanfordnlp.github.io/stanza/
# https://lars76.github.io/2018/05/08/portuguese-lemmatizers.html
# https://www.analyticsvidhya.com/blog/2020/11/words-that-matter-a-simple-guide-to-keyword-extraction-in-python/

import stanza
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from AnalyseText.Regex_Search import RegexSearch
from TranscriptAudio.FileExceptions import *
from Const import *
from pathlib import Path
import os

class ProcessText:

    def __init__(self, text_file_name):
        self._text_file_name = text_file_name
        self._text_file_path = ''
        self._raw_text = ""
        self._audio_keyword_dictionary = dict()
        self._keyword_list = ['frequência', 'frequencia', 'patrocínio', 'patrocinio', 'apoio', 'comercial', 'endereço', 'avenida', 'localização',
                              'localizado', 'localizada', 'promoção', 'custo', 'compra', 'comprar', 'grátis', 'gratuito', 'reais', 'garantia',
                              'preço', 'orçamento', 'revenda', 'brinde', 'comércio', 'comercio']

    # region Getters and Setters

    @property
    def text_file_name(self):
        return self._text_file_name

    @text_file_name.setter
    def text_file_name(self, new_text_fname):
        self._text_file_name = new_text_fname

    @property
    def text_file_path(self):
        return self._text_file_path

    @text_file_path.setter
    def text_file_path(self, new_text_file):
        self._text_file_path = new_text_file

    @property
    def raw_text(self):
        return self._raw_text

    @raw_text.setter
    def raw_text(self, new_raw_text):
        self._raw_text = new_raw_text

    @property
    def audio_keyword_dictionary(self):
        return self._audio_keyword_dictionary

    @audio_keyword_dictionary.setter
    def audio_keyword_dictionary(self, new_audio_kw_dict):
        self._audio_keyword_dictionary = new_audio_kw_dict

    @property
    def keyword_list(self):
        return self._keyword_list

    @keyword_list.setter
    def keyword_list(self, new_kw_list):
        self._keyword_list = new_kw_list

    # endregion

    #

    # Opens and reads a text file
    def open_txt_file(self):
        """Abre e lê um arquivo de texto"""

        try:
            with open(self.text_file_path, 'r') as file:
                self.raw_text = file.read()
        except WriteFileException:
            raise WriteFileException

    # Check if a directory exists
    def check_if_directory_exists(self, complete_fname):
        """Checa se o diretório existe"""

        directory = os.path.dirname(complete_fname)

        if not Path(directory).is_dir():
            self.create_directory(directory)
        return directory

    # Creates a directory
    @staticmethod
    def create_directory(directory):
        """Cria um diretório"""

        # directory should be: .\\Resultado_Analise_de_Texto
        Path(directory).mkdir(parents=True, exist_ok=True)

    # Saves processed raw_text to a txt file located in the folder Results, inside package AnalyseText
    def save_txt_file(self, complete_fname, new_text):
        """Salva um texto processado em um arquivo txt localizado na pasta Results, dentro do pacote AnalyseText"""

        try:
            fname = os.path.basename(complete_fname)

            # complete_file_path should be = .\\Resultado_Analise_de_Texto\\fname.txt
            complete_fname = self.check_if_directory_exists(complete_fname)
            complete_fname = complete_fname + '\\' + fname
            with open(complete_fname, 'w') as file:
                file.write(new_text)
        except WriteFileException as e:
            print(f'Exception: {e}')

    # Tokenization is the process of breaking up the original raw raw_text into component pieces which are known as tokens.
    # Tokenização é o process de quebrar o texto original em pedaços conhecidos como tokens.

    # Breaks a raw_text into a list of words
    def tokenize_raw_text(self):
        """Quebra um texto e o transforma em uma lista de palavras"""

        words = word_tokenize(self.raw_text)
        return words

    # Stopwords are words which are filtered out before or after processing of natural language data.
    # Stopwords são palavras que são filtradas e retiradas do texto analisado antes ou depois do processamento de linguagem natural.

    # Filters a list of words from stop words and returns a filtered list. Returns a filtered list.
    def filter_stop_words(self):
        """Filtra um lista de palavras e remove stopwords. Devolve uma lista filtrada"""

        words = self.tokenize_raw_text()
        stop_words = set(stopwords.words('portuguese'))
        filtered_text_list = [word for word in words if word.casefold() not in stop_words]
        return filtered_text_list

    # Turns a list of word tokens into a string
    @staticmethod
    def turn_list_into_string(words_list):
        """Transforma uma lista de tokens (palavras) em uma string"""

        result_string = ' '.join(str(item) for item in words_list)
        return result_string

    # Lemmatization is the process of reducing words to their core meaning
    # Lematização é o processo de reduzir palavras ao seu significado base

    @staticmethod
    # Takes a string and reduces all the words to their core meaning (lemmatize). Returns a list of lemmatized words.
    def lemmatize_text(filtered_text):
        """Recebe uma string e reduz todas as palavras da mesma ao seu significado base (lematizar). Retorna uma lista de palavras lematizadas."""

        # npl = stanza.Pipeline(lang='Pt', model_dir='.\\Stanza')
        npl = stanza.Pipeline('Pt')
        doc = npl(filtered_text)
        lemmatized_words_list = [doc_word.lemma for sentence in doc.sentences for doc_word in sentence.words]
        return lemmatized_words_list


    # Adds a keyword to the list
    def feed_keyword_list(self, keyword_word):
        """Adiciona uma palavra chave à lista"""

        self.keyword_list.append(keyword_word)

    # Removes a keyword from the list
    def remove_keyword_from_list(self, keyword_word):
        """Remove uma palavra chave da lista"""

        self.keyword_list.remove(keyword_word)

    # Concatenates two lists. Returns the resulting list
    def concatenate_key_words(self, lemmatized_keyword_list):
        """Concatena duas listas. Retorna a lista resultante"""

        full_keyword_string = list(set(self.keyword_list + lemmatized_keyword_list))
        full_keyword_string.sort()
        return full_keyword_string

    # Takes a keyword word and appends it to a list of keywords. Returns a list of keywords
    def generate_keyword_complete_list(self):
        """Recebe uma palavra-chave a adiciona a uma lista de palavras-chaves. Retorna a lista de palavras-chaves"""

        keyword_string = self.turn_list_into_string(self.keyword_list)
        lemmatized_keyword_list = self.lemmatize_text(keyword_string)
        complete_kw_list = list(set(self.concatenate_key_words(lemmatized_keyword_list)))
        return complete_kw_list

    # Prints a each list in a list of keywords
    def print_complete_keyword_list(self):
        """Imprime cada palavra-chave em uma lista de palavras-chaves"""

        keyword_string = self.turn_list_into_string(self.keyword_list)
        lemmatized_keyword_list = self.lemmatize_text(keyword_string)
        complete_kw_list = list(set(self.concatenate_key_words(lemmatized_keyword_list)))

        print(Const.SEPARATOR)
        print(Const.LIST_KEYWORDS_INFO)
        for keyword in complete_kw_list:
            print(keyword)

    # Iterates over a list of sentences and searches for keywords in each sentence. If no audio{number} keywords are found, returns a dictionary
    # where key = sentence and value = set of keywords found.
    # If audio{number} keywords are found, returns a dictionary where key = audio{number} and value = a dictionary (where key = sentence
    # and value = set of keywords)
    def iterate_keywords(self, sentences, complete_keyword_set):
        """Itera uma lista se frases e procura por palavras-chaves em cada frase. Se nenhuma palavra-chave do tipo audio{número} for encontrada,
           retorna um dicionário onde chave = frase e valor = set de palavras-chaves encontradas.

           Se uma palavra-chave do tipo audio{número} for encontrada, retorna um dicionário onde chave = audio{número} e valor = dicionário (onde
           chave = frase e valor = set de palavras-chaves)"""
        audio_nested_dictionary = dict()
        keyword_dict = dict()
        for index, sentence in enumerate(sentences):
            keyword_set_inside_dict = set()
            for each_keyword in complete_keyword_set:
                if each_keyword in sentence:
                    keyword_dict = dict()
                    keyword_set_inside_dict.add(each_keyword)

                    # Dictionary where key = sentence and value = set of keywords found
                    keyword_dict[sentence] = keyword_set_inside_dict

                    if self.audio_keyword_dictionary:
                        # each_value = audio{number}
                        for each_value in self.audio_keyword_dictionary.values():

                            if each_value in sentences[index - 1] and sentences[index - 1] != '':
                                # Dictionary where key = audio{number} and value = a dictionary (where key = sentence and value = set of keywords)
                                audio_nested_dictionary[each_value] = keyword_dict

        if self.audio_keyword_dictionary:
            return audio_nested_dictionary
        else:
            return keyword_dict

    # Process text. Receives a list of keywords, filters raw text from stopwords, lemmatizes filtered text, splits filtered text into sentences,
    # searches for each keyword in each sentence. Returns a dictionary with the results.
    def process_text(self):
        """Processa o texto. Recebe uma lista de palavras-chaves, filtra o texto e retira stopwords, divide o texto filtrado em frases, procura
        por cada palavra-chave em cada frase. Retorna um dicionário com os resultados"""
        rs = RegexSearch()
        complete_keyword_list = self.generate_keyword_complete_list()
        filtered_list = self.filter_stop_words()
        filtered_string = self.turn_list_into_string(filtered_list)
        lemmatized_list = self.lemmatize_text(filtered_string)
        lemmatized_text = self.turn_list_into_string(lemmatized_list)
        sentences = rs.split_string_by_regex(lemmatized_text)
        self._audio_keyword_dictionary = rs.find_audio_keywords(lemmatized_text)
        result_dictionary = self.iterate_keywords(sentences, complete_keyword_list)
        return result_dictionary

    # Receives a dictionary and prints its items
    def print_dict_results(self, result_dictionary):
        """Recebe um dicionário e imprime os items"""

        final_text = ''
        if result_dictionary:
            if self.audio_keyword_dictionary:
                for key, value in result_dictionary.items():
                    for k, v in value.items():
                        final_text += f'\n{key} - {v} {k}\n'
                        # print(f'{key} - {v} {k}\n')
                print(final_text)
            else:
                final_text = 'Palavras-chaves: '
                for key, value in result_dictionary.items():
                    final_text += f'{value}\nTexto: {key}\n'
                    # print(f'{value} {key}')
                    print(final_text)
            return final_text
        else:
            print(Const.NO_KEYWORD_FOUND)
            return None
