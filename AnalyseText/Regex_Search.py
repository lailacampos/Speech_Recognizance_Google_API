import re


class RegexSearch:

    def __init__(self):
        self._re_obj = ''

    # region Getters and Setters

    @property
    def re_obj(self):
        return self._re_obj

    @re_obj.setter
    def re_obj(self, new_re_obj):
        self._re_obj = new_re_obj

    # endregion

    # Define the search pattern as the word 'audio' followed by any number of digits, with at least one occurrence of a digit
    def define_audio_re_obj(self):
        """Define o padrão de busca como a palavra \"audio\" seguida de qualquer número de dígitos, sendo necessário ao menos um digito"""
        self.re_obj = re.compile(r'\b(audio[0-9]+)+\b')

    def split_string_by_regex(self, string):
        self.define_audio_re_obj()
        sentences = re.split(self.re_obj, string)
        return sentences

    def find_audio_keywords(self, string):
        self.define_audio_re_obj()
        matches = re.finditer(self.re_obj, string)
        dict_matches = dict()
        for i in matches:
            dict_matches[i] = i.__getitem__(0)
        return dict_matches

