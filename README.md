# Piano Visualizer

## Description
A program that visualizes midi input from an electric piano with USB midi output. This project is made to be run on a raspberry pi with a small monitor in front next to the piano. This codebase does not need any form of network activity. It is reccomended to not connect the raspberry pi to your home network while running this project.

## Development
For starters, this is a python project so start off by creating a python venv.

`python -m venv ./venv`

Now Activate that environment.

`source ./venv/bin/activate`

Now install the dependencies of the project

`pip install -r requirements.txt`

Now you can run the project as is.

`python main.py`

## Usage
This project is designed to visualize midi input from a piano. There is no network activity involved within the code. To use this code first make sure you have the following:
- a digital piano with a USB port
- USB cable
- raspberry pi
- small monitor
- hdmi cable

1. setup your raspberry pi. Make sure you have python installed. When setting up your pi, make sure to power it next to the digital piano and to set the monitor on the digital piano.

2. Get the source code on the pi. This can be done in many ways. 
	1. Copy it over onto a USB (no internet needed)
	2. Clone the repo (internet required)

Note that if you choose to do 1, you will need to manually update the pi with a USB everytime there are useful updates to the code. You could also just clone the repo and turn off your network interface.

3. run the project
	1. open up a terminal
	2. navigate to the root directory of the repo
	3. create a venv `python -m venv ./venv`
	4. activate the venv `source ./venv/bin/activate`
	5. install dependencies `pip install -r requirements.txt`
	6. run the code `python main.py`

