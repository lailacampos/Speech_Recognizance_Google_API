# Natural Language Processing in Portuguese
# http://www.nltk.org/howto/portuguese_en.html

# Useful sites:
# https://stanfordnlp.github.io/stanza/
# https://lars76.github.io/2018/05/08/portuguese-lemmatizers.html
# https://www.analyticsvidhya.com/blog/2020/11/words-that-matter-a-simple-guide-to-keyword-extraction-in-python/

import stanza
from TranscriptAudio.FileExceptions import *
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from Regex_Search import RegexSearch


class ProcessText:

    def __init__(self, raw_text):
        self._raw_text = raw_text
        self._audio_keyword_dictionary = dict()
        self._keyword_list = list()

    # region Getters and Setters

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
        return self.keyword_list

    @keyword_list.setter
    def keyword_list(self, new_kw_list):
        self._keyword_list = new_kw_list

    # endregion

    """Saves processed raw_text to a txt file located in the folder Results, inside package AnalyseText"""
    def save_txt_file(self, complete_fname, new_text):
        """Salva um texto processado em um arquivo txt localizado na pasta Results, dentro do pacote AnalyseText"""

        try:
            # complete_fname = .\\Results\\fname.txt
            with open(complete_fname, 'w') as file:
                file.write(new_text)
        except WriteFileException as e:
            print(f'Exception: {e}')

    """Tokenization is the process of breaking up the original raw raw_text into component pieces which are known as tokens.
       Tokenização é o process de quebrar o texto original em pedaços conhecidos como tokens.
       Breaks a raw_text into a list of words"""
    def tokenize_raw_text(self):
        """Quebra um texto e o transforma em uma lista de palavras"""
        words = word_tokenize(self.raw_text)
        return words

    """Stopwords are words which are filtered out before or after processing of natural language data.
       Stopwords são palavras que são filtradas e retiradas do texto analisado antes ou depois do processamento de linguagem natural.
       Filters a list of words from stop words and returns a filtered list. Returns a filtered list."""
    def filter_stop_words(self):
        """Filtra um lista de palavras e remove stopwords. Devolve uma lista filtrada"""
        words = self.tokenize_raw_text()
        stop_words = set(stopwords.words('portuguese'))
        filtered_text_list = [word for word in words if word.casefold() not in stop_words]
        return filtered_text_list

    """Turns a list of word tokens into a string"""
    @staticmethod
    def turn_list_into_string(words_list):
        """Transforma uma lista de tokens (palavras) em uma string"""
        result_string = ' '.join(str(item) for item in words_list)
        return result_string

    """Lemmatization is the process of reducing words to their core meaning
    Lematização é o processo de reduzir palavras ao seu significado base"""
    @staticmethod
    # Takes a string and reduces all the words to their core meaning (lemmatize). Returns a list of lemmatized words.
    def lemmatize_text(filtered_text):
        """Recebe uma string e reduz todas as palavras da mesma ao seu significado base (lematizar). Retorna uma lista de palavras lematizadas."""

        npl = stanza.Pipeline('Pt')
        doc = npl(filtered_text)
        lemmatized_words_list = [doc_word.lemma for sentence in doc.sentences for doc_word in sentence.words]
        return lemmatized_words_list

    @staticmethod
    def feed_keyword_list(keyword_word):
        keyword_list = list()
        keyword_list.append(keyword_word)
        return keyword_list

    """Concatenates two lists. Returns the resulting list"""
    @staticmethod
    def concatenate_key_words(keyword_list, lemmatized_keyword_list):
        """Concatena duas listas. Retorna a lista resultante"""

        full_keyword_string = list(set(keyword_list + lemmatized_keyword_list))
        full_keyword_string.sort()
        return full_keyword_string

    """Takes a keyword word and appends it to a list of keywords. Returns a list of keywords"""
    def create_keyword_complete_list(self, keyword_list):
        """Recebe uma palavra-chave a adiciona a uma lista de palavras-chaves. Retorna a lista de palavras-chaves"""
        keyword_string = self.turn_list_into_string(keyword_list)
        lemmatized_keyword_list = self.lemmatize_text(keyword_string)
        complete_kw_list = list(set(self.concatenate_key_words(keyword_list, lemmatized_keyword_list)))
        return complete_kw_list

    """Iterates over a list of sentences and searches for keywords in each sentence. If no audio{number} keywords are found, returns a dictionary
    where key = sentence and value = set of keywords found.
    If audio{number} keywords are found, returns a dictionary where key = audio{number} and value = a dictionary (where key = sentence 
    and value = set of keywords)"""
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

    """Process text. Receives a list of keywords, filters raw text from stopwords, lemmatizes filtered text, splits filtered text into sentences, 
       searches for each keyword in each sentence. Returns a dictionary with the results."""
    def process_text(self, complete_keyword_list):
        """Processa o texto. Recebe uma lista de palavras-chaves, filtra o texto e retira stopwords, divide o texto filtrado em frases, procura
        por cada palavra-chave em cada frase. Retorna um dicionário com os resultados"""
        rs = RegexSearch()
        filtered_list = self.filter_stop_words()
        filtered_string = self.turn_list_into_string(filtered_list)
        lemmatized_list = self.lemmatize_text(filtered_string)
        lemmatized_text = self.turn_list_into_string(lemmatized_list)
        sentences = rs.split_string_by_regex(lemmatized_text)
        self._audio_keyword_dictionary = rs.find_audio_keywords(lemmatized_text)
        result_dictionary = self.iterate_keywords(sentences, complete_keyword_list)
        return result_dictionary

    """Receives a dictionary and prints its items"""
    def print_dict_results(self, result_dictionary):
        """Recebe um dicionário e imprime os items"""
        if result_dictionary:
            if self.audio_keyword_dictionary:
                for key, value in result_dictionary.items():
                    for k, v in value.items():
                        print(f'{key} - {v} {k}\n')

            else:
                for key, value in result_dictionary.items():
                    print(f'{value} {key}')
        else:
            print('\nNehuma palavra chave encontrada')


with open('..\\TranscriptAudio\\Transcripts\\tiranossauro.txt', 'r') as file:
    text = file.read()
processText = ProcessText(text)
keyword_list = ['frequência', 'frequencia', 'patrocínio', 'patrocinio', 'apoio', 'comercial', 'endereço', 'avenida', 'localização',
                'localizado', 'localizada', 'promoção', 'custo', 'compra', 'comprar', 'grátis', 'gratuito', 'reais', 'garantia', 'preço',
                'orçamento', 'revenda', 'brinde', 'comércio', 'comercio']

complete_kw_list = processText.create_keyword_complete_list(keyword_list)

result_dict = processText.process_text(complete_kw_list)
processText.print_dict_results(result_dict)


