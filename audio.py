import essentia.standard as ess
import magic, librosa, numpy

# Do not bother if the file is not even audio
def isAudioFile(FilePath):
    mime = magic.from_file(FilePath, mime=True)
    return(mime.startswith('audio'))

# Throw a wild guess if essentia is not confident
def getTempoLibrosa(AudioFile):
    y, sr = librosa.load(AudioFile)
    tempo, beatFrames = librosa.beat.beat_track(y=y, sr=sr)
    if isinstance(tempo, numpy.ndarray):
        return(round(tempo.item()))
    else:
        return(0)

# Get the tempo using essentia
def getTempo(AudioFile):
    audio = ess.MonoLoader(filename=AudioFile)()
    rhythmExtractor = ess.RhythmExtractor2013(method="multifeature")
    bpm, beats, beatsConfidence, _, beatsIntervals = rhythmExtractor(audio)
    if beatsConfidence >= 1.5:
        return(round(bpm))
    else:
        return(getTempoLibrosa(AudioFile))
