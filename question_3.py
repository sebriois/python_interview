# A rocket is assembled as legos. It
# • has a capsule/head
# • has one or several floors
# • has an engine
# • can have one or several boosters.
#
# Several types of capsules/heads and engines exist.
# List of available capsules
# • capsuleC for crew
# • capsuleP for payload
#
# List of available engines
# • supraluminic engine
# • ionic engine
# • combustion engine
#
# A floor has a content and 2 connectors: top and bottom.
# • The top connector can link another floor or a capsule.
# • The bottom connector can link another floor or an engine.
#
# An engine can be connected to one or several boosters.
# The ignition and extinction for each engine type is different.
#
# A rocket accepts 3 actions:
# • launching: ignition of the engine is required
# • landing: ignition of the engine is required
# • holding orbit: extinction of the engine is required
#

# Task:
# Design the skeleton of a program to model the assembling and the use of a rocket.
# • create one rocket with a capsuleP, 1 floor and a supraluminic engine. Launch the rocket.
# • create one rocket with a capsuleC, 3 floors, an ionic engine. Land the rocket.
