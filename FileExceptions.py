# About class methods:
# https://realpython.com/instance-class-and-static-methods-demystified/


class GeneralException(Exception):
    def __init__(self, msg='General Error occured'):
        self.msg = msg
        super().__init__(self.msg)


class TranscriptFileError(Exception):
    def __init__(self, msg='Error while transcripting file'):
        self.msg = msg
        super().__init__(self.msg)


class TranscriptSingleFile(Exception):
    def __init__(self, msg='Error while transcripting single file'):
        self.msg = msg
        super().__init__(self.msg)


class TranscriptMultipleFiles(Exception):
    def __init__(self, msg='Error while transcripting multiple files'):
        self.msg = msg
        super().__init__(self.msg)


class WriteFileException(Exception):
    def __init__(self, msg='Error while trying to write to txt file'):
        self.msg = msg
        super().__init__(self.msg)


class SliceFileException(Exception):
    def __init__(self, msg='Error while slicing audio file'):
        self.msg = msg
        super().__init__(self.msg)


class MicrophoneException(Exception):
    def __init__(self, msg='Error while capturing sound from microphone'):
        self.msg = msg
        super().__init__(self.msg)


class ExportAudioFileException(Exception):
    def __init__(self, msg='Error while writing audio file to disk'):
        self.msg = msg
        super().__init__(self.msg)


class FileDoesNotExistException(Exception):
    def __init__(self, msg='Error while opening file: File does not exist.'):
        self.msg = msg
        super().__init__(self.msg)

