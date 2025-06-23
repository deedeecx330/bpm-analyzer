import audio
import FreeSimpleGUI as fsg
import os

DATA = []
fsg.theme('DarkGrey11')
layout = [
    [fsg.Button('Browse Files'), fsg.Button('Browse Folder')],
    [fsg.Table(DATA, headings=['File', 'BPM', 'Key'], expand_x=True, expand_y=True, justification='left', row_height = 24, pad = 8, display_row_numbers=False, key='-TABLE-')],
    [fsg.Text('', key='-TEXT-', expand_x=True, justification='center')]
]

def getFilesMultiple():
    return(fsg.popup_get_file('Select Files For Analysis', multiple_files=True, title='Browse Files'))

def getDirectory():
    return(fsg.popup_get_folder('Select Folder For Analysis', title='Browse Folder'))

def drawGUI():
    window = fsg.Window('BPM Analyzer', layout, size=(640, 480))
    while True:
        event, values = window.read()
        if event == fsg.WINDOW_CLOSED or event == None:
            break
        elif event == 'Browse Files':
            filesFunc = getFilesMultiple()
            if not isinstance(filesFunc, type(None)):
                files = [f for f in filesFunc.split(';') if os.path.isfile(f)]
                filesNum = len(files)
                fileProcessed = 0
                for file in files:
                    fileProcessed += 1
                    window['-TEXT-'].update("Analyzing file {currentFile}/{allFiles}".format(currentFile=fileProcessed, allFiles=filesNum))
                    fileBaseName = os.path.basename(file)
                    DATA.append([fileBaseName, 'Analyzing...', ''])
                    window['-TABLE-'].update(values=DATA)
                    window.refresh()
                    if audio.isAudioFile(file):
                        DATA.pop()
                        DATA.append([fileBaseName, audio.getTempo(file), audio.getKey(file)])
                    else:
                        DATA.pop()
                        DATA.append([fileBaseName, 'Not Audio', ''])
                    window['-TABLE-'].update(values=DATA)
                    window.refresh()
                fsg.popup_ok("Finished analyzing {fileNum} files".format(fileNum=filesNum), no_titlebar=True)
                fileProcessed = 0
        elif event == 'Browse Folder':
            directory = getDirectory()
            if not isinstance(directory, type(None)):
                if not os.path.isdir(directory):
                    fsg.popup_ok("Finished analyzing 0 files", no_titlebar=True)
                else:
                    files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
                    filesNum = len(files)
                    fileProcessed = 0
                    for file in files:
                        fileProcessed += 1
                        window['-TEXT-'].update("Analyzing file {currentFile}/{allFiles}".format(currentFile=fileProcessed, allFiles=filesNum))
                        fileBaseName = os.path.basename(file)
                        DATA.append([fileBaseName, 'Analyzing...', ''])
                        window['-TABLE-'].update(values=DATA)
                        window.refresh()
                        if audio.isAudioFile(file):
                            DATA.pop()
                            DATA.append([fileBaseName, audio.getTempo(file), audio.getKey(file)])
                        else:
                            DATA.pop()
                            DATA.append([fileBaseName, 'Not Audio', ''])
                        window['-TABLE-'].update(values=DATA)
                        window.refresh()
                    fsg.popup_ok("Finished analyzing {fileNum} files".format(fileNum=filesNum), no_titlebar=True)
                    fileProcessed = 0
    window.close()
