# obs_recording_markers
Installation

<h2>Downloading Python 3.6 on Windows</h2>

<ol>
  <li>Go to the <a href="https://www.python.org/downloads/">Python official website</a>.</li>
  <li>Click on the Python 3.6 version link.</li>
  <li>Download the Windows Installer for Python 3.6.</li>
  <li>Open the installer and follow the steps to complete the installation.</li>
</ol>

<h2>Setting the Path</h2>

<ol>
  <li>Right-click on the Computer icon and select Properties.</li>
  <li>Click on Advanced system settings.</li>
  <li>Click on the Environment Variables button.</li>
  <li>Under System Variables, scroll down and find the Path variable.</li>
  <li>Click on Edit.</li>
  <li>Add the path to the Python installation (e.g., `C:\Python36\`).</li>
  <li>Click OK to save the changes.</li>
  <li>Open a new Command Prompt window to verify that the path has been set correctly by running `python --version`.</li>
</ol>

<p>That's it! Python 3.6 has now been installed and its path has been set on your Windows system.</p>



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
		   
You have to select a Python 3.6.X version folder <br>

*** OBS Filename Formatting (Stream is the name of your file, must have the date in that format, 
    do not check save file without spaces): STREAM %MM-%DD-%YY <br>

*** Copy the OBS Recording Path to the script Recording Path field <br>

*** Script Events path recommendation: Use/recording/path/SCRIPTS/Events.csv<br>
<br>
Exaple of how the hotkeys in tools -> scripts -> click ObsRecoirdingMarker.py<br>
Hotkey 1: 45:10<br>								
Hotkey 2: 10:10	<br>								
Hotkey 3: 00:30:00<br>
Hotkey 4: 30:00 mod<br>		
Hotkey 5: del<br>


   	
		   


