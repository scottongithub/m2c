import sys
from music21 import *

infile = str(sys.argv[1])
bpm = int(input("BPM?: "))

# open MIDI file and map object 'mt' to track 0 of the MIDI file
mf = midi.MidiFile()
mf.open(infile)
mf.read()
mt = mf.tracks[0].events
tpq = mf.ticksPerQuarterNote
ms_per_tick = (60000) / (bpm * tpq)

# MIDI 'pitch' to Hz
def note_to_freq( _note ):
    _freq = (2 ** ((_note - 69) / 12)) * 440
    return(_freq)

# prints the note that's in the buffer
def spit_out_note():
    if (ms_per_tick * time_buffer) > 10: # less than 10ms notes generate warning messages and will be rounded down to 0
        print(":beep frequency=%i" % note_to_freq(curr_pitch), "length=%ims;" % (ms_per_tick * time_buffer))

# delay of note length plus whitespace that's in the buffer
def spit_out_delay():
    if (ms_per_tick * time_buffer) > 10: # less than 10ms delays generate warning messages and will be rounded down to 0
        print(":delay %ims;" % (ms_per_tick * time_buffer))

# initialize counters
time_buffer = 0
note_qty = 0
curr_pitch = 0

# business starts here. when two notes are sounding at the same time
# in MIDI, the most recently-played note takes over here (the router
# can only play one note at at time)
for event in mt:
    if isinstance(event.time, int) and (event.time > 0):
        # all time entries (DeltaTime) get thrown into the buffer
        time_buffer += event.time
    elif event.isNoteOn() and note_qty == 0:
        # must've been whitespace - print it and set info of the new note
        spit_out_delay()
        time_buffer = 0
        note_qty = 1
        curr_pitch = event.pitch
    elif event.isNoteOn() and note_qty >= 1:
        # a new note overlaps - spit out the previous note and start the new one
        spit_out_note()
        spit_out_delay()
        time_buffer = 0
        note_qty += 1
        curr_pitch = event.pitch
    elif event.isNoteOff() and note_qty > 1:
        note_qty -=1
    elif event.isNoteOff() and note_qty == 1:
        # must be no overlap so print the previous note and start whitespace
        spit_out_note() 
        note_qty = 0
spit_out_delay() # get that last note's delay ;)