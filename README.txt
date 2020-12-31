Created by Lugen
12-31-2020

V0.1 --------

Directions for use at end of this update message!

Currently the program only takes a screenshot with the bbox parameters of 400, 400, 1400, 500.
This is roughly where the outcome of the relics are, so that pytesseract can read it. It doesn't
always read them correctly, so some work will have to be done to perhaps process the photo
to make it easier for pytesseract to see it clearly. Names that are shorter, like "Boar Prime Barrel"
almost always are read correctly. Longer ones like "Stradavar Prime Blueprint" are read incorrectly
due to the text being "higher" than the rest, resulting in a mess like "StradavarBoar Prime Barrel".

An easy fix would to be to take four screenshots of each different reward, but that'll be tested in
the next version as this is just a quick and dirty code to get the basic fundamentals working
other than the waframe.market integration.

I also have concerns about the possibility of too many people pinging the market if this tool becomes
widespread enough, as one squad is twelve pings already, a hundred squads would be over a thousand.
I could have the program check the prices at a set interval and keep them in memory as the top
items should stay around the same price day to day, and setting an exception for new items would
be easy enough as well as items that aren't seen very often. Drops for rarely seen things such as
kubrow collars could be kept out of the initial scan of the market and only done when it drops, for
example.

TO USE: 

Open Warframe Relic2Plat in a Python Editor (exe version coming once the program is worth
the effort to compile). 

Change the directory after "im.save(r" to a location suitable for you on your computer.
Example: im.save(r'C:\Users\James\Desktop\imagegrab.png') or im.save(r'C:\Users\James\Desktop\WarframeFolder\imagegrab.png')

Change the directory after the "image_to_string_" in the same way, to the same location as the one you just made after "im.save".

You may have to install cv2, pytesseract, and pyscreenshot to use this program in the current state it is in. Later versions
will have this functionality built in and will not require you to download and install these.

CLOSING:

This is a personal project of mine for education purposes and should not be distributed for sale, although if you
wish to share it around that is perfectly fine. Just do keep in mind that this project may or may not be updated
or abandoned as is my will, if I get bored or find that I've learned all I wish to, then the ultimate purpose
of doing this has been achieved. To create a perfect program with no bugs is not the end goal, it is to learn
and hopefully create something useful for myself and others to use.

If you want to contribute I do ask that you create a separate fork for yours, as the one I have up here is for my own
purposes. Thank you for understanding.