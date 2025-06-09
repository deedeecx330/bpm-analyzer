# bpm-analyzer
Graphical BPM Analyzer

# Overview
This is a graphical BPM Analyzer utilizing FreeSimpleGUI, Essentia and Librosa.
When running analysis, it will try to use Essentia for the initial analysis;
If the confidence level is too low, it will throw a wild guess using the simpler Librosa module.

# Installation
To run the application, you need Python with Tkinter (install via distribution package manager) and a couple of other modules, namely Essentia*, Python-Magic, Librosa and FreeSimpleGUI.
To install them, run:

```
pip3 install essentia librosa FreeSimpleGUI python-magic
```

* As of the time of writing, Essentia will not build with Python > 3.11, as the built-in Imp library was deprecated
