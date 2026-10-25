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

    create_region_from_json(world, "Anvil Ford.json")
    create_region_from_json(world, "Ashlands.json")
    create_region_from_json(world, "Black Throne.json")
    create_region_from_json(world, "Broken Stairs.json")
    create_region_from_json(world, "Crossroads.json")
    create_region_from_json(world, "Choking Grounds.json")
    create_region_from_json(world, "Drowned Pass.json")
    create_region_from_json(world, "Dry Road.json")
    create_region_from_json(world, "Eden.json")
    create_region_from_json(world, "Hollows.json")
    create_region_from_json(world, "Iron Canopy.json")
    create_region_from_json(world, "Leviathan Drift.json")
    create_region_from_json(world, "Library.json")
    create_region_from_json(world, "Menu.json")
    create_region_from_json(world, "Scalding Gallow.json")
    create_region_from_json(world, "Serpent Holes.json")
    create_region_from_json(world, "Twilight Cathedral.json")

def connect_regions(world: DSWorld) -> None:

    create_entrances_from_json(world, "Anvil Ford.json")
    create_entrances_from_json(world, "Ashlands.json")
    create_entrances_from_json(world, "Broken Stairs.json")
    create_entrances_from_json(world, "Black Throne.json")
    create_entrances_from_json(world, "Choking Grounds.json")
    create_entrances_from_json(world, "Crossroads.json")
    create_entrances_from_json(world, "Drowned Pass.json")
    create_entrances_from_json(world, "Dry Road.json")
    create_entrances_from_json(world, "Eden.json")
    create_entrances_from_json(world, "Iron Canopy.json")
    create_entrances_from_json(world, "Hollows.json")
    create_entrances_from_json(world, "Leviathan Drift.json")
    create_entrances_from_json(world, "Library.json")
    create_entrances_from_json(world, "Menu.json")
    create_entrances_from_json(world, "Scalding Gallow.json")
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