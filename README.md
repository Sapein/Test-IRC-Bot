#Simple Bot

####What is Simple Bot?
Simple bot is an IRC bot written in Python that simply does stuff. It does some things from my Basic IRC bot, but it's also designed to be larger, and more modular. 

####Installation
Simply download the files and run:

python3 bot.py 

however that does little at this time.

##PFAQ (Possibly Frequently Asked Questions)

####Why do you append your functions and variables with lowercase letters?
Because I like Apps Hungarian. I'm trying to use it more. While it's not as necessary with python, I still prefer it due to the fact that when it is used properly then it's easier to quickly spot errors. However the prefixes I use aren't exactly completely finalized yet, so they will probably change.  

An example of this is in my Basic IRC Bot program. If you look I use r[var] (mainly rData) and sp[var] (mainly spData). rData marks raw data (should probably be rb data for raw bite/byte data), however rData should never be read to the screen or used. Instead it should be converted into a string. sb[var] marks a variable that was split, and as such should not be called directly in anything that requires a whole string. 

####Eww, Hungarian Notation!
Not a question, however it's not that bad, [if it's used correctly.](http://www.joelonsoftware.com/articles/Wrong.html)

####Why Make this instead of adding onto Basic IRC Bot?
Well, because of the fact that Basic IRC Bot's purpose is to do one thing and one thing only (aside from the required ones of .help and .disconnect :| (README_PFAQ: Colon Pipe!)) So I decided to make this. 

Also adding commands would be a bitch, so I decided to split it up and allow commands to be done seperately.

####What do you plan for this to be?
I don't really know yet. It's probably just going to be a basic framework of sorts for others to build ontop of. Hell I might even port my other IRC Bot (Zatch) to Python as well! I've wanted to do it for a while, and I could use it with this project :P

####Why isn't there a license?
I don't know what I want to license it under yet. However if you want to use the code until I add a license, just ask and I will let you!

####Why Python 3?
Because it's easy, and it's what I know.

####Do you like Python 3P
Yes

####Why did you add P at the of the question above?
It's a refrence to the MIT-AI Jargon file. (I read the catb version, so it's more like the catb jargon file that I know :/) However, it has it's roots in LISP and generally is something used when a yes/no response is expected (but it's not mandatory). I basically reached for that one though :| (REAME_PFAQ: Colon Pipe!). 
