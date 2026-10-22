from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

from .Utils import data_path, json_read

if TYPE_CHECKING:
    from .World import DSWorld

def create_and_connect_regions(world: DSWorld) -> None:

    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: DSWorld) -> None:

    black_throne_1 = Region("Black Throne 1", world.player, world.multiworld)
    black_throne_boss_room = Region("Black Throne Boss Room", world.player, world.multiworld)
    eden = Region("Eden", world.player, world.multiworld)
    hollows_1 = Region("The Hollows 1", world.player, world.multiworld) #Before gas pipes
    hollows_2 = Region("The Hollows 2", world.player, world.multiworld) #Before First Beholder Key
    hollows_3 = Region("The Hollows 3", world.player, world.multiworld) #Before Second Beholder Key
    hollows_4 = Region("The Hollows 4", world.player, world.multiworld) #After Second Beholder Key and Gauntlet
    hollows_5 = Region("The Hollows 5", world.player, world.multiworld) #Branching from Hollows Entrance, after Block of Ice
    hollows_6 = Region("The Hollows 6", world.player, world.multiworld) #Passed Gas Pipes again
    hollows_7 = Region("The Hollows 7", world.player, world.multiworld) #Passed Geysers
    hollows_8 = Region("The Hollows 8", world.player, world.multiworld) #Passed yet another Gas Pipe Puzzle
    hollows_9 = Region("The Hollows 9", world.player, world.multiworld) #Branching from Train Cars Room, Passed Third Beholder Key
    hollows_10 = Region("The Hollows 10", world.player, world.multiworld) #Passed Block of Ice filling room with water
    hollows_boss_room = Region("The Hollows Boss Room", world.player, world.multiworld)
    hollows_access_tunnel = Region("The Hollows Access Tunnel", world.player, world.multiworld)
    iron_canopy_1 = Region("Iron Canopy 1", world.player, world.multiworld)
    leviathan_drift = Region("Leviathan's Drift", world.player, world.multiworld)
    #seraphim_hotel = Region("Seraphim Hotel", world.player, world.multiworld)
    silitha_loom = Region("Silitha's Loom", world.player, world.multiworld)
    tree_of_knowledge = Region("Tree of Knowledge", world.player, world.multiworld)

    regions = [
        black_throne_1,
        black_throne_boss_room,
        eden,
        hollows_1,
        hollows_2,
        hollows_3,
        hollows_4,
        hollows_5,
        hollows_6,
        hollows_7,
        hollows_8,
        hollows_9,
        hollows_10,
        hollows_boss_room,
        hollows_access_tunnel,
        iron_canopy_1,
        leviathan_drift,
        #seraphim_hotel,
        silitha_loom,
        tree_of_knowledge,
    ]

    world.multiworld.regions += regions

    create_region_from_json(world, "Anvil ford.json")
    create_region_from_json(world, "Ashlands.json")
    create_region_from_json(world, "Crossroads.json")
    create_region_from_json(world, "Choking Grounds.json")
    create_region_from_json(world, "Drowned Pass.json")
    create_region_from_json(world, "Dry Road.json")
    create_region_from_json(world, "Library.json")
    create_region_from_json(world, "Menu.json")
    create_region_from_json(world, "Scalding Gallow.json")
    create_region_from_json(world, "Serpent Holes.json")
    create_region_from_json(world, "Twilight Cathedral.json")

def connect_regions(world: DSWorld) -> None:

    black_throne_1 = world.get_region("Black Throne 1")
    black_throne_boss_room = world.get_region("Black Throne Boss Room")
    eden = world.get_region("Eden")
    hollows_1 = world.get_region("The Hollows 1")
    hollows_2 = world.get_region("The Hollows 2")
    hollows_3 = world.get_region("The Hollows 3")
    hollows_4 = world.get_region("The Hollows 4")
    hollows_5 = world.get_region("The Hollows 5")
    hollows_6 = world.get_region("The Hollows 6")
    hollows_7 = world.get_region("The Hollows 7")
    hollows_8 = world.get_region("The Hollows 8")
    hollows_9 = world.get_region("The Hollows 9")
    hollows_10 = world.get_region("The Hollows 10")
    hollows_boss_room = world.get_region("The Hollows Boss Room")
    hollows_access_tunnel = world.get_region("The Hollows Access Tunnel")
    iron_canopy_1 = world.get_region("Iron Canopy 1")
    leviathan_drift = world.get_region("Leviathan's Drift")
    #seraphim_hotel = world.get_region("Seraphim Hotel")
    silitha_loom = world.get_region("Silitha's Loom")
    tree_of_knowledge = world.get_region("Tree of Knowledge")

    create_entrances_from_json(world, "Anvil Ford.json")
    create_entrances_from_json(world, "Ashlands.json")

    black_throne_1_to_black_throne_boss_room = Entrance(world.player, "Black Throne 1 to Black Throne Boss Room", parent = black_throne_1)
    black_throne_1.exits.append(black_throne_1_to_black_throne_boss_room)
    black_throne_1_to_black_throne_boss_room.connect(black_throne_boss_room)

    create_entrances_from_json(world, "Choking grounds.json")
    create_entrances_from_json(world, "Crossroads.json")
    create_entrances_from_json(world, "Drowned Pass.json")
    create_entrances_from_json(world, "Dry Road.json")

    eden_to_tree_of_knowledge = Entrance(world.player, "Eden to Three of Knowledge", parent = eden)
    eden.exits.append(eden_to_tree_of_knowledge)
    eden_to_tree_of_knowledge.connect(tree_of_knowledge)

    hollows_1_to_hollows_2 = Entrance(world.player, "The Hollows 1 to The Hollows 2", parent = hollows_1)
    hollows_1.exits.append(hollows_1_to_hollows_2)
    hollows_1_to_hollows_2.connect(hollows_2)

    hollows_1_to_hollows_5 = Entrance(world.player, "The Hollows 1 to The Hollows 5", parent = hollows_1)
    hollows_1.exits.append(hollows_1_to_hollows_5)
    hollows_1_to_hollows_5.connect(hollows_5)

    hollows_2_to_hollows_3 = Entrance(world.player, "The Hollows 2 to The Hollows 3", parent = hollows_2)
    hollows_2.exits.append(hollows_2_to_hollows_3)
    hollows_2_to_hollows_3.connect(hollows_3)

    hollows_3_to_hollows_4 = Entrance(world.player, "The Hollows 3 to The Hollows 4", parent = hollows_3)
    hollows_3.exits.append(hollows_3_to_hollows_4)
    hollows_3_to_hollows_4.connect(hollows_4)

    hollows_4_to_hollows_1 = Entrance(world.player, "The Hollows 4 to The Hollows 1", parent = hollows_4)
    hollows_4.exits.append(hollows_4_to_hollows_1)
    hollows_4_to_hollows_1.connect(hollows_1)

    hollows_5_to_hollows_6 = Entrance(world.player, "The Hollows 5 to The Hollows 6", parent = hollows_5)
    hollows_5.exits.append(hollows_5_to_hollows_6)
    hollows_5_to_hollows_6.connect(hollows_6)

    hollows_5_to_hollows_9 = Entrance(world.player, "The Hollows 5 to The Hollows 9", parent = hollows_5)
    hollows_5.exits.append(hollows_5_to_hollows_9)
    hollows_5_to_hollows_9.connect(hollows_9)

    hollows_6_to_hollows_7 = Entrance(world.player, "The Hollows 6 to The Hollows 7", parent = hollows_6)
    hollows_6.exits.append(hollows_6_to_hollows_7)
    hollows_6_to_hollows_7.connect(hollows_7)

    hollows_7_to_hollows_8 = Entrance(world.player, "The Hollows 7 to The Hollows 8", parent = hollows_7)
    hollows_7.exits.append(hollows_7_to_hollows_8)
    hollows_7_to_hollows_8.connect(hollows_8)

    hollows_9_to_hollows_10 = Entrance(world.player, "The Hollows 9 to The Hollows 10", parent = hollows_9)
    hollows_9.exits.append(hollows_9_to_hollows_10)
    hollows_9_to_hollows_10.connect(hollows_10)

    hollows_10_to_hollows_boss_room = Entrance(world.player, "The Hollows 10 to The Hollows Boss Room", parent = hollows_10)
    hollows_10.exits.append(hollows_10_to_hollows_boss_room)
    hollows_10_to_hollows_boss_room.connect(hollows_boss_room)

    iron_canopy_1_to_silitha_loom = Entrance(world.player, "Iron Canopy 1 to Silitha's Loom", parent = iron_canopy_1)
    iron_canopy_1.exits.append(iron_canopy_1_to_silitha_loom)
    iron_canopy_1_to_silitha_loom.connect(silitha_loom)

    hollows_access_tunnel_to_hollows_1 = Entrance(world.player, "The Hollows Access Tunnel to The Hollows 1", parent = hollows_access_tunnel)
    hollows_access_tunnel.exits.append(hollows_access_tunnel_to_hollows_1)
    hollows_access_tunnel_to_hollows_1.connect(hollows_1)

    leviathan_drift_to_eden = Entrance(world.player, "Leviathan's Drift to Eden", parent = leviathan_drift)
    leviathan_drift.exits.append(leviathan_drift_to_eden)
    leviathan_drift_to_eden.connect(eden)
    
    create_entrances_from_json(world, "Library.json")
    create_entrances_from_json(world, "Menu.json")
    create_entrances_from_json(world, "Scalding Gallow.json")

    #seraphim_hotel_to_crossroads = Entrance(world.player, "Seraphim Hotel to The Crossroads", parent = seraphim_hotel)
    #seraphim_hotel.exits.append(seraphim_hotel_to_crossroads)
    #seraphim_hotel_to_crossroads.connect(crossroads)
    
    create_entrances_from_json(world, "Serpent Holes.json")
    create_entrances_from_json(world, "Twilight Cathedral.json")

def create_entrances_from_json(world: DSWorld, filename) -> None:

    region_json = json_read(data_path(filename))

    for region in region_json:
        if 'entrances' in region:
            this_region = world.get_region(region.get("name"))
            for entrance_name, entrance_data in region.get("entrances").items():
                new_entrance = Entrance(world.player, entrance_name, this_region)
                this_region.exits.append(new_entrance)
                new_target = world.get_region(entrance_data.get("vanilla target"))
                new_entrance.connect(new_target)

def create_region_from_json(world: DSWorld, filename) -> None:

    region_json = json_read(data_path(filename))

    for region in region_json:
        new_region = Region(region["name"], world.player, world.multiworld)
        world.multiworld.regions += [new_region]