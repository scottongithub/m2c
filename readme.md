# Overview
Takes a MIDI file as input and outputs the corresponding config statements to get it to play on Mikrotik/Omnitik routers

# Usage
Uses the music21 library from MIT by directly installing with `pip3 install music21`, or use Pipenv to get a package-locked environment `pipenv install`.

Then run m2c.py with the .mid file as its only argument:
```sh
$ python3 m2c.py <filename>
```

It will ask for BPM - this will be what BPM was set to on whatever you've auditioned the MIDI file on but can be changed (Ardour's default setting is 120). And then it spits out the the config commands for copy-paste into a config file/template.

# Notes
- This function is a transform of a 2-dimensional representation (MIDI) of music into a 1-dimensional (beep-commands) representation. The concession is made that if multiple notes are sounding at once (in 2-D MIDI-space), then the most recently-started note will take over in 1-dimensional beep-space, as only one note can sound at a time in beep-space.
- By default it reads 'track 0' of the MIDI file which seems to be what anything I've tested is using
- Suggestions are always welcome and appreciated

# Example

The opening melody (minus octaves) of The Entertainer (Scott Joplin, 1902) looks like this in MIDI space:

<p align="center">
<img src="https://user-images.githubusercontent.com/21364725/177835552-e8b6eac7-aecd-41a9-b563-ba758fee4df7.png" />
</p>

And will look like the beep commands below when m2c.py is run as:

```sh
$ python3 m2c.py The_Entertainer.mid
BPM?: 120
:delay 1080ms;
:beep frequency=146 length=150ms;
:delay 169ms;
:beep frequency=155 length=114ms;
:delay 204ms;
:beep frequency=164 length=153ms;
:delay 200ms;
:beep frequency=261 length=304ms;
:delay 365ms;
:beep frequency=164 length=142ms;
:delay 223ms;
:beep frequency=261 length=295ms;
:delay 382ms;
:beep frequency=164 length=161ms;
:delay 216ms;
:beep frequency=261 length=794ms;
:delay 987ms;
:beep frequency=261 length=192ms;
:delay 192ms;
:beep frequency=293 length=148ms;
:delay 184ms;
:beep frequency=311 length=140ms;
:delay 208ms;
:beep frequency=329 length=138ms;
:delay 145ms;
:beep frequency=261 length=198ms;
:delay 226ms;
:beep frequency=293 length=130ms;
:delay 189ms;
:beep frequency=329 length=343ms;
:delay 379ms;
:beep frequency=246 length=164ms;
:delay 215ms;
:beep frequency=293 length=221ms;
:delay 396ms;
:beep frequency=261 length=794ms;
:delay 794ms;
```
