# Course.ai
Application that optimizes a students school schedule for them

Explanation of the program:

This program will take in all the scheduled (1) lecture sections and (2) Lab/seminar sections of each class that is input into it. The goal of this program is to integrate it with the (1) Carleton override request form page and/or the (2) coursicle web page to make it easier to find a combination of course sections that fit one's schedule without any time conflicts. One issue that students have is finding the Absolute best schedule for their classes. They may have a schedule but it could definitely be better.

Inputs:
	- X amount of lecture sections (for example SYSC 2004 A through C would be 3 lecture sections)
	- X amount of lab/seminar sections (for example SYSC 2004 L1 through L8 would be 8 sections)
	- Start time of each lecture and lab section
	- End time of each lecture and lab section
	- The days that the lectures and labs are on
Outputs:
	- An organized list of each lecture and lab/seminar section for each class in order to create a schedule
	- Repeat this process of finding the combination of sections that do not create a time conflict until there are no more cases. Essentially print out all combinations of lecture/lab/seminar sections with their respective time slots.
	- Create a visual representation of this using an outside library
