import sys
from music21 import *
#from pprint import pprint

infile = str(sys.argv[1])
bpm = int(input("BPM?: "))

#open MIDI file and map object 'mt' to track 0 of the MIDI file
mf = midi.MidiFile()
mf.open(infile)
mf.read()
mt = mf.tracks[0].events
tpq = mf.ticksPerQuarterNote
ms_per_tick = (60000) / (bpm * tpq)

#MIDI 'pitch' to Hz
def note_to_freq( _note ):
    _freq = (2 ** ((_note - 69) / 12)) * 440
    return(_freq)

#prints the note that's in the buffer
def spit_out_note():
    print(":beep frequency=%i" % note_to_freq(curr_pitch), "length=%ims;" % (ms_per_tick * note_buffer))

#prints the whitespace that's in the buffer
def spit_out_whitespace():
    print(":delay %ims;" % (ms_per_tick * note_buffer))

#initialize counters
note_buffer = 0
note_qty = 0
curr_pitch = 0

#business starts here. when two notes are sounding at the same time
#in MIDI, the most recently-played note takes over here (can only play one note)
for event in mt:
    #all time entries (DeltaTime) get thrown into the buffer
    if isinstance(event.time, int) and (event.time > 0):
        note_buffer = note_buffer + event.time
    elif event.isNoteOn() and note_qty == 0:
        #must've been whitespace - print it and set info of the new note
        spit_out_whitespace()
        note_buffer = 0
        note_qty = 1
        curr_pitch = event.pitch
    elif event.isNoteOn() and note_qty >= 1:
        #a new note overlaps - spit out the previous note and start the new one
        spit_out_note()
        note_buffer = 0
        note_qty += 1
        curr_pitch = event.pitch
    elif event.isNoteOff() and note_qty > 1:
        note_qty -=1
    elif event.isNoteOff() and note_qty == 1:
        #must be no overlap so print the previous note and start whitespace
        spit_out_note()
        note_buffer = 0
        note_qty = 0
