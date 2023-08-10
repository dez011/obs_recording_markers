# obs_recording_markers
<h2>Will have tutorials on this on my YouTube channel as well as Warzone and other gaming content</h2>
<a href="https://www.youtube.com/c/DEZACTUALTWO?sub_confirmation=1">Subscribe to DEZACTUALTWO on YouTube</a>

<h1>Installation</h1>
<h2>Get the python path if you have a valid version installer or download Python 3.6 on Windows</h2>
<h3> 3.6 works with obs version 27 - 29.  If you have a different version check if your obs version supports it </h3>
<ol>
  <li>Go to the <a href="https://www.python.org/downloads/">Python official website</a>.</li>
  <li>Click on the Python 3.6 version link.</li>
  <li>Download the Windows Installer for Python 3.6.</li>
  <li>Open the installer and follow the steps to complete the installation.</li>
  <li>You can copy the python install path from here</li>
</ol>

<h2>Setting up OBS</h2>
<ol>
  <li>tools -> scripts -> python settings.  Set the python path here</li>
  <li>Then tab over to scripts press + and find the script</li>
  <li>Set up the Hotkeys (8 fields, don't have to use all)</li>
  <li>Copy your OBS output directory in the Recording Path field</li>
  <li>Enter a name for your file with a .csv extension ie. Events.csv.  Might have to enter an absolute path if you do not see your file when you restart OBS</li>
  <li>If you use .mp4 files checking/unchecking the Remux box will not affect anything.  If you record in .mkv and remux check this box</li>
  <li>Restart OBS</li>
  <li>settings -> hotkeys. Add your hotkeys to Hotkey 1-7 if you are using them</li>
</ol>

<h4>OBS RECORDING MARKER will add hotkey events to a file
Which will later be used to automatically clip the VOD</h4>

<h2>Other products worth using</h2>
<h3>Catch a clip. (OBS Automatic VOD Clipper)
<p>Will use the file generated here to clip your content<p>

<h3>Example of valid input in the hotkey text fields (tools -> scripts -> pyscript.py: valid ex.: 40:40)</h3>
<ol>
	<li>40:10 - start:end format will clip 40 seconds back and 10 seconds forward from timestamp</li>
	<li>10:10 mod - will modify last row and add (or subtract if - start or end) the seconds to start and/or end</li>
	<li>del - will delete the last row</li>
	<li>01:30:05 - hh:mm:ss fomrat will clip one hour thirty minutes and five seconds from captured time mod doesn't work forthis format</li>
</ol>
<h2>OBS Filename Formatting (Stream is the name of your file, must have the date in that format, do not check save file without spaces): STREAM %MM-%DD-%YY </h2>
<h4>Exaples</h4>
Hotkey 1: 45:10<br>								
Hotkey 2: 10:10	<br>								
Hotkey 3: 00:30:00<br>
Hotkey 4: 30:00 mod<br>		
Hotkey 5: del<br> 
Hotkey 6: 600:25<br> 


   	
		   


