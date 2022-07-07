# Overview
Takes a MIDI file as input and outputs the corresponding config statements to get it to play on Omnitik routers

# Usage
Uses the music21 library from MIT
```sh
$ pip3 install music21
```
Then run m2c.py with the .mid file as its only argument:
```sh
$ python3 m2c.py <filename>
```

It will ask for BPM - this will be what BPM was set to on whatever you've auditioned the MIDI file on but can be changed (Ardour's default setting is 120). And then it spits out the the config commands for copy-paste into a config file/template.

# Notes
- This function is a transform of a 2-dimensional representation (MIDI) of music into a 1-dimensional (beep-commands) representation. The concession is made that if multiple notes are sounding (in 2-D MIDI-space), then the most recently-played note will take over in 1-dimensional beep-space, as only one note can sound at a time in beep-space.
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
BPM?: 148
:delay 1163ms;
:beep frequency=293 length=176ms;
:delay 53ms;
:beep frequency=311 length=152ms;
:delay 43ms;
:beep frequency=329 length=217ms;
:beep frequency=523 length=335ms;
:delay 50ms;
:beep frequency=329 length=142ms;
:delay 80ms;
:beep frequency=523 length=321ms;
:delay 50ms;
:beep frequency=329 length=203ms;
:delay 30ms;
:beep frequency=523 length=933ms;
:delay 310ms;
:beep frequency=523 length=149ms;
:delay 58ms;
:beep frequency=587 length=158ms;
:beep frequency=622 length=171ms;
:delay 47ms;
:beep frequency=659 length=152ms;
:beep frequency=523 length=216ms;
:beep frequency=587 length=204ms;
:beep frequency=659 length=354ms;
:delay 22ms;
:beep frequency=493 length=134ms;
:delay 83ms;
:beep frequency=587 length=300ms;
:delay 139ms;
:beep frequency=523 length=1013ms;
```
