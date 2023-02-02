# obs_recording_markers

Installation

The script tested with OBS Studio versions 27.x and using python 3.6. 

You need Python 3 installed on your PC. The bit version of your Python installation 
must match your OBS installation - use "x86-64" for 64 bit OBS Studio and "x86" for 32 bit OBS Studio. 
In the menu in OBS Studio, go to Tools and then Scripts. Then in the "Python Settings" tab, set the path to point to the Python installation folder.

Add the obs script to the "Scripts" window using the '+' icon on the bottom left. 
Select the script in the "Loaded Scripts" panel.

OBS RECORDING MARKER will add hotkey events to a file
Which will later be used to automatically clip the VOD
OBS VOD Clipper and Manager coming soon!

VOD Clipper: Clips automatically from markers, 
	crop cam and stack for vertical videos
Manager: Automatically upload videos and organize

ARGS:	arg - explanation

	40:10 - start:end format will clip 40 seconds back 
	        and 10 seconds forward from timestamp

	10:10 mod - will modify last row and add (or subtract if - start 
	            or end) the seconds to start and/or end

	del - will delete the last row

	01:30:05 - hh:mm:ss fomrat will clip one hour thirty minutes and 
	           five seconds from captured time mod doesn't work for 
		   this format

Restart OBS after adding the script
You have to select a Python 3.6.X version folder 

*** OBS Filename Formatting (Stream is the name of your file, must have the date in that format, 
    do not check save file without spaces): STREAM %MM-%DD-%YY 
*** Copy the OBS Recording Path to the script Recording Path field 
*** Script Events path recommendation: Use/recording/path/SCRIPTS/Events.csv

Exaple of how the hotkeys in tools -> scripts -> click ObsRecoirdingMarker.py
Hotkey 1: 45:10
Hotkey 2: 10:10
Hotkey 3: 00:30:00
Hotkey 4: 30:00 mod
Hotkey 5: del
