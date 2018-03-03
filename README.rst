Ride Arranger
############

Some people have cars, some do not. Let's help arrange that via GroupMe

Basic Idea
##########

The arranger can be invoked by sending a hashtag on the GroupMe Group in which
the bot resides. The bot will listen for a hashtag '#rides', then query the
database for a list of drivers and passengers. It would then form a group of
one driver plus n number of passengers. n being the number of passengers
that driver can fit in his or her car. The app would then send the group
arrangements to the GroupMe Group using the GroupMe APIs.

Consideration
#############

Coordination among people who do not have cars and those who do depends on
serveral factors:

1. Location - Are the people who need rides close the driver?
2. Number of available seats - How many passengers can a driver fit?
3. Multiple drivers in area - Sometimes multiple drivers are available
   in the area. How do we decide who drives? Some ideas or to randomize
   the drivers, or to work off a pre-set schedule.
4. Optimizing space - Efficiency can be described as M / N x 100.
   Where M is the number of passenger seats filled, and N is the total number
   of passenger seats. The arranger needs to work in such a way to maximize
   efficiency.
