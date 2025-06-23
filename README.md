# bpm-analyzer
Graphical BPM and song key analyzer

# Overview
This is a graphical BPM and song key analyzer utilizing FreeSimpleGUI, Essentia and Librosa.

# Installation
To run the application, you need Python with Tkinter (install via distribution package manager) and a couple of other modules, namely Essentia*, Python-Magic, Librosa and FreeSimpleGUI.
To install them, run:

```
pip3 install essentia librosa FreeSimpleGUI python-magic
```

* As of the time of writing, Essentia will not build with Python > 3.11, as the built-in Imp library was deprecated
