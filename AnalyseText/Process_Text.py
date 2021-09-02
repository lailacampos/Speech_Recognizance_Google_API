from TranscriptAudio.FileExceptions import *

class ProcessText:

    def __init__(self, fname, complete_fname):
        self._fname = fname
        self._complete_fname = complete_fname

    # region Getters and Setters

    @property
    def fname(self):
        return self._fname

    @fname.setter
    def fname(self, new_fname):
        self._fname = new_fname

    @property
    def complete_fname(self):
        return self._complete_fname

    @ complete_fname.setter
    def complete_fname(self, new_complete_fname):
        self._complete_fname = new_complete_fname

    # endregion

    def save_text_file(self, text):
        try:
            with open(f'..\\TranscriptAudio\\Transcripts\\' + self.fname, 'w') as file:
                file.write(text)
        except WriteFileException:
            raise WriteFileException
