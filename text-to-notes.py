from midiutil import MIDIFile

def ascii_to_midi(char):
    ascii_val = ord(char)
    return 21 + (ascii_val%88) #to fit in the range of MIDI notes 21-108

def word_to_midichord(word):
    return [ascii_to_midi(char) for char in word]

def text_to_midi_chords(text):
    words = text.split()
    midi_chords = [word_to_midichord(word) for word in words]
    return midi_chords

def save_midi_chords_to_file(midi_chords, filename):
    midifile = MIDIFile(1)
    track = 0
    time = 0

    midifile.addTrackName(track, time, "MIDI Chords")
    midifile.addTempo(track, time, 120)
    for chord in midi_chords:
        for note in chord:
            midifile.addNote(track, 0, note, time, 1, 100)
        time += 1
    
    with open(filename, "wb") as output_file:
        midifile.writeFile(output_file)
    return filename


def  main():
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    midi_chords = text_to_midi_chords(text)
    print("MIDI Chords:", midi_chords)
    midi_file = save_midi_chords_to_file(midi_chords, "output.mid")
    print(f"MIDI file saved as {midi_file}")

if __name__ == "__main__":
    main()