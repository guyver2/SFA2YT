# Abstract:  

- Quick launch:  
	* Open your emulator and set up a fight
	* Stack two videos side by side, as shown in the examples
	* `python main.py`
	* Let the software learn the background for a few seconds, and then click on `Turn on`
	* Finally click on the emulator so that it becomes the active window
- Download:  
	`git clone https://github.com/guyver2/SFA2YT.git`  



# Introduction:  

This project has been inspired by this : https://www.twitch.tv/fishplaystreetfighter .
From there, the idea was to make something a little more dynamic and also add **combos!** So instead of using cute but not so active fish, this project is designed to use YouTube videos. In its current implementation it has been tested with 2 live streams ; one from a roundabout somewhere in Netherlands and the other one from a shark aquarium in California (links bellow). The software can easily be modified to use any kind of video input, as it actually take screenshots from user specified areas of the desktop. 
This project has only been tested on Street Fighter Alpha 2 on SNES. Combos (and super combos) have been implemented for Ryu and Sagat (other characters might come later on). 



# Installation:   

- Requirements:  
	* Pyside (or PyQt), OpenCv for python (cv2), numpy PyUserInput, and PIL (or Pillow)
	* `git clone https://github.com/guyver2/SFA2YT.git`

# Credits & Licence:  

- Code:   
	Antoine Letouzey -- [antoine.letouzey@gmail.com](antoine.letouzey@gmail.com)
- Licence:   
	LGPL


# Videos:
Ryu Vs Sagat Round 1

[![Round 1](https://img.youtube.com/vi/G3_bott9pNY/0.jpg)](https://www.youtube.com/watch?v=G3_bott9pNY)


RyuVs Sagat Round 2

[![Round 2](https://img.youtube.com/vi/eXTodnQl9dk/0.jpg)](https://www.youtube.com/watch?v=eXTodnQl9dk)


# Links:
Videos were actually poorly chosen. The roundabout being located in Europe and the Aquarium on US west coast, the time difference only allows for a small time window during which both feeds are live and useful, around 4pm GMT.
Roundabout Cam : https://www.youtube.com/watch?v=262xjjNxqZ0
Aquarium Cam : https://www.youtube.com/watch?v=TStjLJIc3DY
