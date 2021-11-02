# game.py will run my game. I will create a file for characters, rooms, treasures.

# The game:
    # You start out on a hill tall enough to see everything at a distance
    # To the North is forest
        # Forest has 2 locations
            # Left Path, small pond with fairies
                #Touch water, get amulet, return to hill
            # Right path, bear den
    # To the West is a lake
        # The lake has 2 locations
            # bank, there is a small boat and a talking mask
            # small island, On the island is a puppet with latches on its head (for mask)\
                #Put mask on puppet, transport to hill, gain mask
    # To the East is a small desert
        # The desert has one location
            # In the distance as you start to head towards the desert you see
            # a giant pool of water
            # Location, you suddenly appear in an Oasis after passing out.
                # Oasis, a skeleton next to a sword
                    #skeleton talks
    # To the South is a little house and a farm
        # The Farm has a barn, a cottage, and a fenced area with sheep
            # barn, has one Hay bail in the middle (holds key)
            # cottage, smells like cooking (can't go inside without key)
                # Once inside, there is nothing but cobwebs and a fork on the table
                    #Grab Fork, and transport to hill
            # fenced area, sheep that just bah!
    # After collecting all items, you appear on hill
        # If items == 4: you start moving downward on an elevator

    # Final Boss room, when elevator stops
        # Boss appears, no literally, it's your boss!
        # He pulls out a sword and screams "I know you lied about your sick leave!!"
            # Create D&D style fight that is all luck based.
            # You go first, try to swing? if no, "why?" If yes, then a a random int rolls 1-20
            # Boss goes, he will swing..
                # dice roll: random int 1-20
                    # if 1, you miss, 2-10, you hit for 1, if 11-15, hit for 2, 16-19, hit for 4, 20 hit for 1000.
                    # need to checkHealth
                    # If health goes to 0, you restart fight from beginning
                    #

                    #If you beat boss, you find Micheal, the ultimate employee

# Room(object), because everything willbe treated as its own spacial cube
    # Hill
    # Forest
        # smallPond
        # bearDen
    # Lake
        # Bank
        # Island
    # Desert
        # Oasis
    # Farm
        # Cottage
        # Barn
        # fencedArea
    # secretLair

# Creature
    # You
    # Bear
    # Fairy
    # Octopus
    # Skeleton
    # Sheep
    # Stranger
    # Boss
    # michealGarcia

# Treasure
    # Amulet
    # Sword


# Game.py
    # Main(object)
        # - checkHealth
        # - Fight
        # - NextArea
        # - Transport
