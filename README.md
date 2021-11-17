<p align="center">
  <a href="https://www.yushi.dev/" target="_blank" rel="noreferrer"><img src="https://user-images.githubusercontent.com/81379254/133644694-2c1149b8-01be-40f7-88ee-6110922bcf8a.png" alt="my banner"></a>
</p>

Pycraft is an OpenGL, OpenWorld, Video Game made entirely with Python. This project is a test to shed some light on OpenGL programming in Python as it is a seldom touched area of Python's vast amount of uses. Feel free to give this project a run, and message me if you have any feedback! <br />
Made with Python 64-bit and Microsoft Visual Studio Code.

[![](https://img.shields.io/badge/python-3.10-blue.svg)](www.python.org/downloads/release/python-3100) [![](https://img.shields.io/badge/python-3.9-blue.svg)](www.python.org/downloads/release/python-390) [![](https://img.shields.io/badge/python-3.8-blue.svg)](www.python.org/downloads/release/python-380) [![](https://img.shields.io/badge/python-3.7-blue.svg)](www.python.org/downloads/release/python-370) <br />
![](https://img.shields.io/github/license/PycraftDeveloper/Pycraft) ![](https://img.shields.io/github/stars/PycraftDeveloper/Pycraft) ![](https://img.shields.io/github/forks/PycraftDeveloper/Pycraft) ![](https://img.shields.io/github/issues/PycraftDeveloper/Pycraft) ![GitHub commits since tagged version](https://img.shields.io/github/commits-since/PycraftDeveloper/Pycraft/Pycraft-v0.0) ![GitHub all releases](https://img.shields.io/github/downloads/PycraftDeveloper/Pycraft/total) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/PycraftDeveloper/Pycraft) ![](https://img.shields.io/pypi/wheel/python-pycraft)

Progress towards Pycraft v0.9.3: ![Progress](https://progress-bar.dev/55)

## About

Pycraft is a 3D open-source, open-world video game made in Python. For a long time attempts to make large 3D games in python has been ignored, I believe there are two reasons: one; People use Python primarily for data handling and processing and not graphics and, two; there is little to no documentation out there to do anything more than make a 3D rotating cube in Python. Making a 3D game in Python for me hasn’t been an easy experience, far from it but I have decided to share my project, complete with tutorials, explanations, articles and code explanations in the hope that 3D game development in Python can be seen as a more easily attainable target, and to fill that ga in documentation. Pycraft then is a trial project, as I learn and experiment on what goes best where and how thing go together, this is why development can sometimes appear to have stopped, because I’m learning and testing what I've learned, so hopefully for people in the future it will be an easier experience. Also, don’t forget there is more to game development than just graphics, there is AI, sound, physics and all the other GUIs that go with it, and as I learn the quality of the overall program will improve. Pycraft is not going to be the final name of the game, however until something better becomes available, we shall stick to it.

## Preview Video

Here is a YouTube link to a showcase of Pycraft v0.9.1 (Developer Build): (https://youtu.be/shAprkrcaiI)

## Setup

### The following instructions are for installing Pycraft via the new recommended method, through Pypi:
Installing Pycraft is now easier than ever, simply copy the command: pip install python-pycraft
Into Terminal (on Apple devices), or Command Prompt (on Windows based machines), and then once its installed, both the project and the modules it requires simply open Python's IDLE or a code editor of your choice (I personally recommend Visual Studio Code), create a new Python file and do: import Pycraft
It's that simple now! However if you are a fan of the GitHub releases then feel free to head over there and download the files as normal if you wish!

### For anyone reading this README on my GitHub page, then the instructions below will be more helpful for you:
When setting up and installing this project you can either run the bare bones file which is likely found above this 'README.md' file if your viewing this on the GitHub website then please follow the steps below for more information on the setup and installation of this project however where possible it is recommended that you use the executable file (.exe) under the most recent releases page as this will run regardless of where you place the file or if you have python or even if you have any of the installed modules this project depends on because its compiled into one file (hence the larger file size). which makes removing the file much easier and also sharing and transporting the file easier and more convenient. However, if you are planning to use the project in its uncompiled format (which as mentioned will be at the top of this page if you are on the GitHub website) then it is recommended you follow the below steps to make sure the project works properly.

The project will download as a (.zip) compressed file. Please make sure you have the project decompressed before use. Next make sure that any folders and files outside of the 'Pycraft' folder are removed and that the 'Pycraft' file is in the intended place for the file to be run from. This file can be freely moved around, transported between drives, computers and folders in this form. A video guide to this will be uploaded here and in YouTube in the coming months.

When running the program please make sure you have a minimum of 1GB of free space on the drive and also have Python 3 installed on your device. This can be found here: (www.python.org/downloads). The sub version of Python isn't too important in this circumstance however the project has been tested in Python 3.9.5 and is known to work. In addition to all this please make sure you have the following modules installed on your device:
Pygame, Numpy, PyOpenGL, Pillow, PyAutoGUI, Psutil, PyWaveFront, CPUinfo and Ctypes. 
For those not familiar they can be found here: (pypi.org) and you can use the following syntax to install, update and remove these modules:
```
pip install <module>
pip uninstall <module>
pip update <module>
```

Here is a short video tutorial explain all this (It’s really not too bad), this is the link to the YouTube video: (youtu.be/DG5YbE-umw0)

## Running The Program
### For anyone reading this README on my GitHub page, then we also recommend you read through this:

When running the program, you will either have a (.exe) file, downloaded from the releases page, or you will have the developer preview, if you have the developer preview, which can be found in the files section of this repository then this is how you run that program. Pycraft has recently undergone some large structural redesigning, so to run the program the advice is now different:

Now you have the program properly installed hopefully (you’ll find out if you haven’t promptly!) you need to locate the file "main.py" basically all this program does is run the right modules, initiates the main program, and catches any errors that might arise in the program in a nicely rendered error screen, if it crashes on your first run then chances are you haven’t installed the program correctly, if it still doesn’t work then you can drop me an email @ "ThomasJebbo@gmail.com" or comment here on the repository, I do hope however that it works alright for you and you have a pleasant experience. I might also add this program has been developed on a Windows 64-bit computer however should run fine on a 32-bit Windows machine (uncompiled) or through MacOS although they remain untested for now. 

I recommend creating a shortcut for the "main.py" file too so it’s easier to locate.

## Credits

#### With thanks to; <br />
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![OpenGL](https://img.shields.io/badge/OpenGL-%23FFFFFF.svg?style=for-the-badge&logo=opengl) ![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white) ![Blender](https://img.shields.io/badge/blender-%23F5792A.svg?style=for-the-badge&logo=blender&logoColor=white) ![Canva](https://img.shields.io/badge/Canva-%2300C4CC.svg?style=for-the-badge&logo=Canva&logoColor=white) ![Figma](https://img.shields.io/badge/figma-%23F24E1E.svg?style=for-the-badge&logo=figma&logoColor=white) ![Gimp Gnu Image Manipulation Program](https://img.shields.io/badge/Gimp-657D8B?style=for-the-badge&logo=gimp&logoColor=FFFFFF) ![Inkscape](https://img.shields.io/badge/Inkscape-e0e0e0?style=for-the-badge&logo=inkscape&logoColor=080A13) ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white) ![Visual Studio](https://img.shields.io/badge/Visual%20Studio-5C2D91.svg?style=for-the-badge&logo=visual-studio&logoColor=white) 	![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white) ![Stack Overflow](https://img.shields.io/badge/-Stackoverflow-FE7A16?style=for-the-badge&logo=stack-overflow&logoColor=white) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) 	![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white) ![Edge](https://img.shields.io/badge/Edge-0078D7?style=for-the-badge&logo=Microsoft-edge&logoColor=white) 
- Thomas Jebbo (PycraftDeveloper) @ www.github.com/PycraftDeveloper <br />
- Count of Freshness Traversal @ https://twitter.com/DmitryChunikhinn <br />
- Pypi @ www.pypi.org <br />
- Pillow (PIL) @ www.python-pillow.org <br />
- Pygame @ www.pygame.org <br />
- Freesound: - Erokia's "ambient wave compilation" @ www.freesound.org/s/473545 <br />
- Freesound: - Soundholder's "ambient meadow near forest" @ www.freesound.org/s/425368 <br />
- Freesound: - monte32's "Footsteps_6_Dirt_shoe" @ www.freesound.org/people/monte32/sounds/353799 <br />

## Uncompiled Pycraft's Dependencies <br />

When you’re installing the uncompiled Pycraft variant from here you need to install the following 'modules', which can be done through your Control Panel in Windows (First; press the windows key + r then type "cmd" then run the below syntax) or on Apple systems in Terminal.

```
pip install <module>
pip uninstall <module>
pip update <module>
```
pip is usually installed by default when installing Python with most versions.

- PIL (Pillow or Python Imaging Library) @ www.github.com/python-pillow/Pillow <br />
- Pygame @ www.github.com/pygame/pygame <br />
- Numpy @ www.github.com/numpy/numpy <br />
- PyOpenGL (and its counterpart PyOpenGL-accelerate) @ www.github.com/mcfletch/pyopengl <br />
- PyAutoGUI @ www.github.com/asweigart/pyautogui <br />
- Psutil @ www.github.com/giampaolo/psutil <br />
- PyWaveFront @ www.github.com/pywavefront/PyWavefront <br />
- Py-CPUinfo @ www.github.com/pytorch/cpuinfo <br />
- GPUtil @ www.github.com/anderskm/gputil <br />
- Tabulate @ www.github.com/p-ranav/tabulate <br />

_Disclaimer; unfortunately, lots of these python modules (first and third party) can require some external modules that will be installed during the installing process of the above modules, unfortunately this makes it really difficult to give credit to those modules, if you have any recommendations, please contact me appropriately._

## Changes

Pycraft v0.9.2 is now live! Here is a list of all the added features to this sub-release: <br />

* Feature: Reprogrammed 'Devmode' graph feature, now scales with screen better (but NOT completely on resize as yet), when switching between modes of full-screen and windowed. <br />
* Feature: Parallelized CPU data collection to create a more accurate graph in 'Devmode'. <br />
* Feature: Labelled text at the top of 'Devmode' and added more useful information. <br />
* Feature: Tweaked caption in 'Devmode' to now include some new features. <br />
* Feature: Fixed mouse movement in game to the centre of the display, and polished mouse detection effects. <br />
* Feature: Improved inventory backdrop snapshot with a blur effect. <br />
* Feature: Created a small sub-program that runs parallel to the main program, this checks all the variables that have the potential to hit the 32/64-bit integer limit. <br />
* Feature: Added better implementations of the 'Adaptive' setting mode, now this dynamically changes FPS to boost performance, detail and keeping system from running hot. This also takes data from the Benchmark mode function based on scores, this is an early feature preview so expect some changes here. (This is run in parallel.) <br />
* Feature: Major performance improvements to the game engine. <br />
* Feature: VBOs have been added to Pycraft! This makes way for some significant changes to come, as well as netting significant performance improvements! <br />
* Feature: The skybox has been pinned to the players camera now. <br />
* Feature: Rotations and movements have been tweaked, but still will need a little bit of work into Pycraft v0.0.3 <br />
* Feature (disabled... for now): Parallelization of the Collisions and Drawing algorithms. <br />
* Feature (disabled... for now): Pycraft’s fog and weather engine has not been working for some time, however a later edition of Pycraft is intended to address this. <br />
* Bug Fix: Prevented the music in game from playing loud, and uncontrollably on start-up, and after certain menu interactions. <br />
* Bug Fix: Some internal clearing up after the big change that came with the last pre-release regarding the programming restructuring. <br />
* Bug Fix: Added and tweaked some internal values for the game and it's saves. <br />
* Bug Fix: Fixed an issue with the animation on the Home Screen changing speed with FPS changes. <br />
* Bug Fix: Cleaned up the game engine a touch, removing unnecessary code and variables. <br />

Again, feedback would be much appreciated this update was released on; 6/11/2021 (UK date) DD/MM/YYYY. As always, we hope you enjoy this new release and feel free to leave feedback.

## Update Timeline
Pycraft will be continually updated for a long time yet. The next few releases, Pycraft v0.9.x will not feature as a (.exe) release but only as a code release. Pycraft will now updated gradually, not all in one go, however (.exe) releases will likely only occur at major releases like the upcoming Pycraft v0.10! The following plan was taken from my Medium article: How We are Making a Video Game in Python #2 (here: https://medium.com/@PycraftDev/how-we-are-making-a-video-game-in-python-2-547b504bbd67) <br />

At present this looks to be the schedule for Pycraft updates: <br />
* Pycraft v0.9.3 — Will add better lighting, as well as a sun to the game! This update will also include the introduction of day and night cycles (20 minutes from sunset to sunrise), including clouds and dynamic skyboxes (featuring stars and night and day scenes). <br />
* Pycraft v0.9.4 — This will add weather events to the sky box, as well as updated sounds, including libraries for night sounds, day sounds, rain sounds, snow sounds, ambient music, footstep sounds on wet ground, footstep sounds on snow, hurt sounds, civilisation sounds, ocean sounds, and environmental sounds (like trees and grass). <br />
* Pycraft v0.9.5 — This will add an ocean to the OpenGL environment, as well as hopefully fixed collisions and much improved frame rates in game. <br />
* Pycraft v0.9.6 — This update will add structures (like buildings, trees, grass, boats, people) to the game. <br />
* Pycraft v0.9.7 — This update will feature interactions with the objects added in the previous update. <br />
* Pycraft v0.9.8 — This update will feature the addition of a story line to the game. <br />
* Pycraft v0.9.9 — This update will feature a start position in game, as well as saving your progress and loading them on a start screen, this update will also begin the process of playthrough! <br />
* Pycraft v0.9.10 — This update will feature a GUI, as well as an in-game character! <br />
* Pycraft v0.10 — This update is set to be released in Spring of 2022 at the earliest! This will showcase all the sub-updates to Pycraft v0.9, as well as featuring a compiled version. This update will also improve upon features added in sub-updates, as well as improving performance, and lots of bug fixes. <br />
* Pycraft v0.10.1 — This update will feature the addition of inventory items. <br />
* Pycraft v0.10.2 — This update will feature improvements to the inventory and map GUIs, this is as far as the plan reaches so far! <br />

## Our Update Policy
New releases will be introduced regularly, it is likely that there will be some form of error or bug, therefore unless you intend to use this project for development and feedback purposes (Thank you all!) we recommend you use the latest stable release; below is how to identify the stable releases.

## Version Naming
Versions have changed pretty dramatically the past few days, don’t panic I'm here to help! In sort the new version naming system more closely follows the Semantic Naming system:
For example; Pycraft v0.9.2.1 The first number is relevant to if the project is in a finished state. The second number relates to the number of updates Pycraft has had. The third number relates to smaller sub-updates (that likely will not feature a (.exe) release). The last number there is rarely used, this is typically for PyPi releases only, as we can't edit uploaded version of the project, we use this number if there is an important change to the project description, those updates will not include any code changing!

## (.exe) Releases

Right time to tackle some of the confusion behind the (.exe) releases that will now be a feature of all main releases. Now when installing and running the (.exe) release its actually much, much easier to do, you just have to download the file attached and simply double click on the file to run it, typically the file will be downloaded to the downloads folder on your computer. The project might take a second or two to appear to start to do something (as everything it requires is loaded) then from there it will work without having any modules installed, any connection (like ALL other releases) or any extra downloads required, its all-in-one for much easier use, and this isn’t an app that installs anything onto your computer outside of the file so to remove you simply have to delete the 'Pycraft.exe' file. Simple!

## The Planned Storyline

In Pycraft the plan is that you will start at sea on a boat, there you will learn that you have left your home on a separate island to find work and safety on this new one, when you arrive you are shown to your room and the next day join a small groups of trainee knights, each training to be part of the Royal Guards system that protects the island from the dangers on the island, you quickly rise in rank as your skills shine until one day all your skills are put to the test. Will you follow through? Well, you don't know yet, I've got to make the game first!

## Other Sources

I have started writing an article on medium which is released at the start of every month, this compliments the weekly updates that are posted on my twitter profile, it would be greatly appreciated if you wanted to check it out here at this link: (link.medium.com/Mhqd8qIAhjb). And recommendations and feedback are, as always, greatly appreciated, a lot of time and work goes into making this happen!

## Final Notices

Thank you greatly for supporting this project simply by running it, I am sorry in advance for any spelling mistakes. The programs will be updated frequently and I shall do my best to keep this up to date too. I also want to add that you are welcome to view and change the program and share it with your friends however please may I have some credit, just a name would do and if you find any bugs or errors, please feel free to comment in the comments section any feedback so I can improve my program, it will all be much appreciated and give as much detail as you wish to give out. BY INSTALLING THIS PROJECT ONTO YOUR COMPUTER AND RUNNING IT I; Tom Jebbo DOES NOT TAKE ANY RESPONSIBILITY FOR ANY DAMAGES THIS MAY CAUSE HOWEVER UNLIKELY, AND YOU AGREE TO HAVE EXTERNAL MODULES INSTALLED ONTO YOUR COMPUTER (WHEN NOT CHOOSING THE RECOMMENDED EXECUTABLE VERSION) ALSO, OF WHICH I HAVE NO CONTROL OVER, PLEASE USE THIS PROGRAM RESPONSIBLY AND DO NOT USE IT TO CAUSE HARM. YOU MUST ALSO HAVE PERMISSION FROM THE DEVICES MANAGER OR ADMINISTRATOR TO INSTALL AND USE COMMAND PROMPT OR TERMINAL. NO DATA THIS PROGRAM COLLECTS IS STORED ANYWHERE BUT, ON YOUR DEVICE, AND AT ANY POINT NO CONNECTION TO A NETWORK IS REQUIRED. THIS PROGRAM DOES NOT SEND ANY DATA TO THE DEVELOPER OR ANYONE ELSE ABOUT THIS PROGRAM. Thank you.
