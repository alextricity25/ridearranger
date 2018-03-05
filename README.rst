Ride Arranger
############

Some people have cars, some do not. Let's help arrange that via GroupMe

Basic Idea
##########

The arranger can be invoked by sending a hashtag on the GroupMe Group in which
the bot resides. The bot will listen for a hashtag '#rides', then query the
database for a list of drivers and passengers. It would then form groups of
one driver plus n number of passengers. n being the number of passengers
that driver can fit in his or her car. The app would then send the group
arrangements to the GroupMe Group using the GroupMe APIs.

Considerations
##############

Coordination among people who do not have cars and those who do depends on
serveral factors:

1. Location - Are the people who need rides close the driver?
2. Number of available seats - How many passengers can a driver fit?
3. Multiple drivers in area - Sometimes multiple drivers are available
   in the area. How do we decide who drives? Some ideas are to randomize
   the drivers, or to work off a pre-set schedule.
4. Optimizing space - Efficiency can be described as M / N x 100.
   Where M is the number of passenger seats filled, and N is the total number
   of passenger seats. The arranger needs to work in such a way to maximize
   efficiency.

Example Usage
#############

In the GroupMe Group, the user could write the following:

.. code-block::

   #rides-initialize

Initially, this would tell the ride arranger to grab a list of all the members in this group. The admin can then designate who on the list is a driver, passenager, locations, and type of car for each driver via Django.

.. code-block::

   #rides

This will tell the ride arranger to group drivers with passengers based on
location first, then availability. The ride aranger will return a table
of the arrangements.

Availability can be designated via the hastag like so:

.. code-bock::

   #rides -alex

If 'alex' is a driver, then ride arranger would mark him as unavailable
and no group will be created with alex as the driver nor passenger.
If 'alex' is a passenger, then he will not be considered when arranging
rides.

Extra passengers can be specified like so:

.. code-block::

   #rides +joey

Joey will now be considered as a passenger, and the ride arranger will attempt
to group Joey with a driver.

If a driver does not have a car available for a certain reason, the driver
role can be omitted for a person like so:

.. code-block::

   #rides ~alex

Alex will now only be considered as a passenger, and not a driver, even
though he orginally had the "driver" status.


Scenarios
#########

Sometimes, location shouldn't be used as the primary deciding factor for
arranging rides. The Ride Arranger should give the admin the option of
defining certain scenarios and invoke them using a modifier.

This is important because it's not always the case that people are
leaving from different locations. Sometimes they are leaving from the
same location. Likewise, sometimes they might be going to different
locations based on an arbitrary parameter.

Scenarios should be able to be defined via the django admin panel.
Once scenarios have been created, they can be used by using the
'$' modifier:

.. code-block::

   #rides $<scenario-name>
   #rides $going-home
   #rides $leaving-campus
   #rides $same-dest


Useful scenarios
################

Say, for example, that you have a group of 10 people who live in two different
neighborhoods. There are 2 drivers in the 1st neighboorhood, and 3 available
drivers in the 2nd neighboorhood. One of the 10 people would send the hashtag
"#rides" to the GroupMe group with the ride arranger bot. The bot would then
calculate the most optimized arragment for those 10 people.
If some of those 10 people want to be excluded from the arrangment, or
someone outside the group of 10 people needs to be added, then the modifiers
would be used.

This can be useful when there are carpool situations that might change. It
could also be useful in establishing a rotation for drivers for weekly and
daily events.
