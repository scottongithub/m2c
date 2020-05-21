# Overview
Takes a MIDI file as input and outputs the corresponding config statements to get it to play on Omnitik routers

# Usage
Uses the music21 library from MIT
```sh
$ pip3 install music21
```
Then run it:
```sh
$ python3 m2c.py <filename>
```

It will ask for BPM - this will be what BPM was set to on whatever you've auditioned the MIDI file on but can be changed (Ardour's default setting is 120). And then it spits out the the config commands for copy-paste into a config file/template.

# Notes
- If multiple notes are sounding, the most recently played note takes over
- It reads 'track 0' of the MIDI file which seems to be what anything I've tested is using
- Suggestions are always welcome and appreciated

# Example
```sh
$ python3 m2c.py ~/m2c/take_8.mid
music21: Certain music21 functions might need these optional packages: matplotlib, numpy, scipy;
                   if you run into errors, install them by following the instructions at
                   http://mit.edu/music21/doc/installing/installAdditional.html
BPM?: 120
:delay 508ms;
:beep frequency=130 length=565ms;
:delay 468ms;
:beep frequency=146 length=540ms;
:delay 425ms;
:beep frequency=164 length=569ms;
:delay 370ms;
:beep frequency=174 length=537ms;
:delay 400ms;
:beep frequency=195 length=586ms;
:delay 339ms;
:beep frequency=130 length=453ms;
:beep frequency=146 length=433ms;
:beep frequency=164 length=459ms;
:beep frequency=174 length=426ms;
:beep frequency=195 length=441ms;
:delay 11ms;
:beep frequency=174 length=398ms;
:beep frequency=164 length=464ms;
:beep frequency=146 length=456ms;
:delay 5ms;
:beep frequency=130 length=647ms;
```
