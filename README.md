# Speech_Recognizance_Google_API

Windows application with Python using natural language processing and speech recognition libraries as well as libraries for audio processing.

The main goal of the application is to transcribe audio recordings to text and to analyze the generated text using natural language processing and search for given keywords as well as identify common patterns.


---
### **Step by step install instructions for dependencies:**
###

####Speech Recognition
```
pip install SpeechRecognition
```

###

####Pydub
```
pip install pydub
```
###

####Nltk
```
pip install nltk install
```
###

####PyAudio
Download corresponding PyAudio wheel from https://www.lfd.uci.edu/~gohlke/pythonlibs/

```
pip install C:/full-package-path/package-name.whl
```
###
####Stanza
```
pip install stanza
```
```
>>> import stanza
>>> stanza.download('pt')
```

---
###**Creating the executable**
###

After downloading the portuguese model, create a folder called Stanza in the same directory as Main.py.

Place `pt` folder and `resources.json` file inside Stanza folder
###

####Ffmpeg
Download Ffmpeg binary from https://ffmpeg.org/download.html.

Place the Ffmpeg folder (with the `ffmpeg.exe` and `ffprobe.exe` files) inside the project directory, at the same level as Main.py

###
####pyinstaller
```
pip install pyinstaller

pyinstaller --add-data "Ffmpeg/bin/ffmpeg.exe;." --add-data "Ffmpeg/bin/ffprobe.exe;." --add-data "Stanza;Stanza" --hidden-import=stanza Main.py
```
###
###**Pyinsaller instructions breakdown**
###
```
--add-data "Ffmpeg/bin/ffmpeg.exe;."
```
Will add `ffmpeg.exe` to binary folder after it is generated. Same with `ffprobe.exe`
###

```
--add-data "Stanza;Stanza"
```
Will add contents of `Stanza` folder *(that should be located in the same directory as `Main.py` and that should contain `pt` folder and `resources.json` file)* to binary folder after it is generated.
###
```
--hidden-import=stanza
```
Will add `stanza` module as a hidden import

