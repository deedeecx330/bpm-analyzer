import essentia.standard as ess
import magic, librosa, numpy

def isAudioFile(FilePath):
    mime = magic.from_file(FilePath, mime=True)
    return(mime.startswith('audio'))

def getKey(AudioFile):
    keys = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    y, sr = librosa.load(AudioFile)
    chromagram = librosa.feature.chroma_stft(y=y, sr=sr)
    estimatedKey = keys[numpy.argmax(numpy.mean(chromagram, axis=1))]
    return(estimatedKey)

def getTempo(AudioFile):
    audio = ess.MonoLoader(filename=AudioFile)()
    rhythmExtractor = ess.RhythmExtractor2013(method="multifeature")
    bpm, beats, beatsConfidence, _, beatsIntervals = rhythmExtractor(audio)
    return(round(bpm))
