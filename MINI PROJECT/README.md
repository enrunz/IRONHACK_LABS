<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# PANDEMYA
Enrique Unzueta

DAFT-0822 MEXICO August 19, 2022

## Content
- [Project Description](#projectdescription) 
- [Rules](#rules)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

## Project Description

Mastermind but with story that will have:

1.Pharma
2.Hero saving the world
3. Be European.
4. Maybe Zombies???



## Rules
As the ice in the poles melt, a new virus capable of infecting humans has emerged in Norway. This virus is more contagious and deadlier than Covid-19. Scientists are calling this the imminent start of a second pandemic. A group of people in Norway are resistant to the virus. A data scientist, Maik, realized this group shares one thing in common; they all have the same vaccine profile for Covid-19. This means the right combination of Covid-19 vaccines are preventing the new virus from infecting vaccinated humans. Unfortunately, Maik got infected and died before he could divulge the right combination of vaccines. However, he left a notebook with some information:

1. It is a combination of 4 vaccines
2. There's 7 possible vaccines 
3. The order matters.

Your mission, should you choose to accept it, is to find the right combination and save the world. 

Maik left something else! 

A black box that will take guesses for the right combination, and spit out whether the guess is right or wrong. 
If our guess is wrong it will give us some hints:

Remember the order matters
if the vaccine taken is correct and in the correct position, then a ‘Y’ will appear.
If the vaccine is not in the right position but it is part of the combination, then a ‘O’ will appear.
If the vaccine is not in the combination at all, then an ‘N’ will appear.

There’s a catch! 

The black box will only allow 4 guesses before it breaks. And it takes the information in CODE. 

DON’T WORRY! Maik left a table in his notebook and It’s simple to understand:



## Workflow
It is basically like master mind. 

The goal: 
The goal is to match a specific randomly generated profile on a vaccination card. The people who match this profile will be saved in the new pandemic.

The universe consists of all the possible combinations of vaccines in your body. Only a specific set of vaccines will be given. We will start with dosis of covid vaccines and take into consideration their brand (i.e. Astra Zeneca, Pfizer, etc).

The card will have a specified number of possible shots taken (I'll start with 4). Obviously combinations may allow repeat.

You will get 4 guesses before you lose. 

They clues will be given to you very much like wordle. Meaning you will know if you get one in the right place which one it is. 

There will be 7 vaccine brands. Abstention will not be counted as possible.

IF I WANNA COMPLICATE THINGS

-There will be a data base that will contain all possible profiles which will be smaller than the Universe. Meaning there will be profiles that won't exist at all so that the try doesn't count. Just like wordle if a word doesn't exist.   

## Organization
I used trello please se elink below:

TO PLAY: 

Please open the Jupyter Motebook called: PANDEMYA.ipynb and run it. 

## Links

[Trello](https://trello.com/b/VKHUZ4jT/pandemya)  
