# Nine Levels To Mictlan

## Description
This game is centered arround aztecan mithology, specifically arround Mictlan, which is the aztecan version of afterlife

Its a 2D topview fighting game where you will find countless enemies all belonging to the aztecan, both pre and post hispanic mythology

## Contents
+ Present readme file
+ Executable packaged with Pyinstaller
+ Source code
+ imageHardcoder code to hardcode sprites and deliver a single executable with no additional required files
+ Licence

## Installation
The executable alone should be able to run in any Windows computer no installation required, just download it and open it

If the executable is in any way damaged or failing, or you don´t have a Windows OS, install any python IDE such as [Thonny](https://thonny.org/), [Vs Code](https://code.visualstudio.com/download) or [Microsoft Visual Studio](https://visualstudio.microsoft.com/) and use it to run the source code

You´ll have to install the necessary python libraries to do this, to do that, once you have installed and set up your IDE, execute the following commands in the command window:

```bash
pip install pygame
pip install pyttsx3
```

Additionally, you can attempt to package it to have your own functional executable by executing the following commands in the command window:

```bash
pip install pyinstaller
pyinstaller NineLevelsToMictlan.py --onefile --noconsole
```

## Usage
To play the game you´ll need a gaming controller, the game itself will require you to connect one if you haven´t already before launching

Once you have your controller ready, youll be able to navigate the menu using either the keyboard, mouse or controller and play with the controller

A GameData.json file may be created if you choose to exit the app with a game in progress, this ensures that your game can be reloaded once you launch the app again, this file will delete itself once you reopen the app, only to reappear if this process is triggered again. Deleting this file will not have any negative effect other than the fact that you´ll have to start the game from the beggining 

## Credits
### Collaborators 
+ [TezcatlipocaStudios](https://sites.google.com/view/tezcatlipocastudios/welcome)
### Resources
+ [pygame](https://www.pygame.org/)
+ [Tezcatlipoca](https://es.wikipedia.org/wiki/Tezcatlipoca)
### Sources
+ [Mictlan](https://es.wikipedia.org/wiki/Mictl%C3%A1n)
+ [Itzehecayan](https://es.wikipedia.org/wiki/Itzehec%C3%A1yan)
+ [Ramon Valdes](https://www.tiktok.com/@ramonvaldese)
+ [Tenochtitlan's fall omens](https://www.karaniart.com.mx/los-8-presagios-funestos-que-guiaron-a-la-caida-de-tenochtitlan/)
+ [Tezcatlipoca](https://es.wikipedia.org/wiki/Tezcatlipoca)
+ [Xolotl](https://es.wikipedia.org/wiki/X%C3%B3lotl_(divinidad))
+ [Macuahuitl](https://www.youtube.com/watch?v=HjN6zdktD4A)
+ [Native mexican species](https://biblioteca.semarnat.gob.mx/janium/Documentos/Cecadesu/Libros/100%20cosas%202.pdf)

## Licence
[GNU Affero General Public License v3.0](https://choosealicense.com/licenses/agpl-3.0/)
