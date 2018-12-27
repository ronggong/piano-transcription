import pretty_midi
import os

def midi_txt_converter(filename):
    """
    Parse midi note sequence ([note_start, note_pitch, note_dur], ...)
    and convert to txt
    """
    midi_data = pretty_midi.PrettyMIDI(filename)
    with open(filename+'.txt', 'w') as f: 
        for instrument in midi_data.instruments:
            if not instrument.is_drum:
                for note in instrument.notes:
                    f.write(str(note.start)+'\t'+str(note.pitch)+'\t'+str(note.end-note.start)+'\n')


if __name__ == "__main__":
    path_transcribed_midi = "/Users/ronggong/Documents_using/pianoAI/data/测试数据转谱"
    folders = os.listdir(path_transcribed_midi)
    for folder in folders:
        if '.DS_Store' not in folder:
            path_individual_student = os.path.join(path_transcribed_midi, folder)
            filenames_transcription = os.listdir(path_individual_student)
            for filename in filenames_transcription:
                if filename.endswith('.midi'):
                    midi_txt_converter(os.path.join(path_individual_student, filename))