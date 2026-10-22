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
    iron_canopy_1 = Region("Iron Canopy 1", world.player, world.multiworld)
    leviathan_drift = Region("Leviathan's Drift", world.player, world.multiworld)
    #seraphim_hotel = Region("Seraphim Hotel", world.player, world.multiworld)
    silitha_loom = Region("Silitha's Loom", world.player, world.multiworld)
    tree_of_knowledge = Region("Tree of Knowledge", world.player, world.multiworld)

    regions = [
        black_throne_1,
        black_throne_boss_room,
        eden,
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
    create_region_from_json(world, "Hollows.json")
    create_region_from_json(world, "Library.json")
    create_region_from_json(world, "Menu.json")
    create_region_from_json(world, "Scalding Gallow.json")
    create_region_from_json(world, "Serpent Holes.json")
    create_region_from_json(world, "Twilight Cathedral.json")

def connect_regions(world: DSWorld) -> None:

    black_throne_1 = world.get_region("Black Throne 1")
    black_throne_boss_room = world.get_region("Black Throne Boss Room")
    eden = world.get_region("Eden")
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

    iron_canopy_1_to_silitha_loom = Entrance(world.player, "Iron Canopy 1 to Silitha's Loom", parent = iron_canopy_1)
    iron_canopy_1.exits.append(iron_canopy_1_to_silitha_loom)
    iron_canopy_1_to_silitha_loom.connect(silitha_loom)

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