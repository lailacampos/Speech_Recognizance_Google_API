
import os
from TranscriptAudio import Const, FileExceptions

fname = input(Const.Const.TYPE_FILE_NAME)
complete_fname = "..\\TranscriptAudio\\Transcripts\\" + fname


if os.path.isfile(complete_fname):

    with open(complete_fname, 'r') as file:
        text = file.read()
    print(text)

else: print()
