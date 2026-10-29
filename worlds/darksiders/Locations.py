from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, Location

from .Items import DSItem
from .Utils import data_path, json_read

if TYPE_CHECKING:
    from .World import DSWorld

def create_location_table_from_json(filename) -> None:

    region_json = json_read(data_path(filename))

    for region in region_json:
        if 'locations' in region:
            for location, location_data in region.get("locations").items():
                LOCATION_NAME_TO_ID[location] = location_data.get("ID")
                LOCATION_NAME_TO_ITEM[location] = location_data.get("vanilla item")

LOCATION_NAME_TO_ID = {}
LOCATION_NAME_TO_ITEM = {}

create_location_table_from_json("Anvil Ford.json")
create_location_table_from_json("Ashlands.json")
create_location_table_from_json("Black Throne.json")
create_location_table_from_json("Broken Stairs.json")
create_location_table_from_json("Choking Grounds.json")
create_location_table_from_json("Crossroads.json")
create_location_table_from_json("Drowned Pass.json")
create_location_table_from_json("Dry Road.json")
create_location_table_from_json("Eden.json")
create_location_table_from_json("Hollows.json")
create_location_table_from_json("Iron Canopy.json")
create_location_table_from_json("Leviathan Drift.json")
create_location_table_from_json("Library.json")
create_location_table_from_json("Menu.json")
create_location_table_from_json("Scalding Gallow.json")
create_location_table_from_json("Serpent Holes.json")
create_location_table_from_json("Twilight Cathedral.json")

ABYSSAL_ARMOR_PIECES_LOCATIONS = {}
ARTIFACTS_LOCATIONS = {}
DUNGEON_ITEMS_LOCATIONS = {}
HEARTS_LOCATIONS = {}
KEYS_LOCATIONS = {}
ARMAGEDDON_LOCATIONS = {}
SCYTHE_LOCATIONS = {}
MOVES_LOCATIONS = {}

item_json = json_read(data_path("Items.json"))

ABYSSAL_ARMOR_PIECES_LOCATIONS = {location: item for location, item in LOCATION_NAME_TO_ITEM.items() if item in item_json.get("Abyssal Armor")}
ARTIFACTS_LOCATIONS = {location: item for location, item in LOCATION_NAME_TO_ITEM.items() if item in item_json.get("Artifacts")}
DUNGEON_ITEMS_LOCATIONS = {location: item for location, item in LOCATION_NAME_TO_ITEM.items() if item in {"Map", "Hoardseeker"}}
HEARTS_LOCATIONS = {location: item for location, item in LOCATION_NAME_TO_ITEM.items() if item == "Heart of the Chosen"}
KEYS_LOCATIONS = {location: item for location, item in LOCATION_NAME_TO_ITEM.items() if item == "Beholder Key"}
ARMAGEDDON_LOCATIONS = {location: item for location, item in LOCATION_NAME_TO_ITEM.items() if item in {"Armageddon Blade", "Armageddon Blade Shard"}}
SCYTHE_LOCATIONS = {location: item for location, item in LOCATION_NAME_TO_ITEM.items() if item in {"Hellraiser", "Harvester"}}
MOVES_LOCATIONS = {location: item for location, item in LOCATION_NAME_TO_ITEM.items() if item in item_json.get("Gauntlet Combos") or item in item_json.get("Scythe Combos") or item in item_json.get("Sword Combos")}

class DSLocation(Location):

    game = "Darksiders"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:

    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def create_all_locations(world: DSWorld) -> None:

    create_regular_locations(world)
    create_events(world)

def create_regular_locations(world: DSWorld) -> None:

    create_locations_from_json(world, "Anvil Ford.json")
    create_locations_from_json(world, "Ashlands.json")
    create_locations_from_json(world, "Black Throne.json")
    create_locations_from_json(world, "Broken Stairs.json")
    create_locations_from_json(world, "Choking Grounds.json")
    create_locations_from_json(world, "Crossroads.json")
    create_locations_from_json(world, "Drowned Pass.json")
    create_locations_from_json(world, "Dry Road.json")
    create_locations_from_json(world, "Eden.json")
    create_locations_from_json(world, "Hollows.json")
    create_locations_from_json(world, "Iron Canopy.json")
    create_locations_from_json(world, "Leviathan Drift.json")
    create_locations_from_json(world, "Library.json")
    create_locations_from_json(world, "Menu.json")
    create_locations_from_json(world, "Scalding Gallow.json")
    create_locations_from_json(world, "Serpent Holes.json")
    create_locations_from_json(world, "Twilight Cathedral.json")

def create_events(world: DSWorld) -> None:

    create_events_from_json(world, "Anvil Ford.json")
    create_events_from_json(world, "Ashlands.json")
    create_events_from_json(world, "Black Throne.json")
    create_events_from_json(world, "Broken Stairs.json")
    create_events_from_json(world, "Choking Grounds.json")
    create_events_from_json(world, "Crossroads.json")
    create_events_from_json(world, "Drowned Pass.json")
    create_events_from_json(world, "Dry Road.json")
    create_events_from_json(world, "Eden.json")
    create_events_from_json(world, "Hollows.json")
    create_events_from_json(world, "Iron Canopy.json")
    create_events_from_json(world, "Leviathan Drift.json")
    create_events_from_json(world, "Library.json")
    create_events_from_json(world, "Menu.json")
    create_events_from_json(world, "Scalding Gallow.json")
    create_events_from_json(world, "Serpent Holes.json")
    create_events_from_json(world, "Twilight Cathedral.json")

def create_events_from_json(world: DSWorld, filename) -> None:

    region_json = json_read(data_path(filename))

    for region in region_json:
        if 'events' in region:
            for event, event_data in region.get("events").items():
                this_region = world.get_region(region_name = region.get("name"))
                this_region.add_event(location_name = event, item_name = event_data.get("item"), location_type = DSLocation, item_type = DSItem)

def create_locations_from_json(world: DSWorld, filename) -> None:

    region_json = json_read(data_path(filename))

    for region in region_json:
        if 'locations' in region:
            this_region = world.get_region(region_name = region.get("name"))
            region_locations = get_location_names_with_ids(location_names = region.get("locations"))
            this_region.add_locations(locations = region_locations, location_type = DSLocation)

def place_vanilla_items(world: DSWorld) -> None:

    if world.options.armor == 1:
        for location, vanilla_item in ABYSSAL_ARMOR_PIECES_LOCATIONS.items():
            new_item = world.create_item(vanilla_item)
            world.get_location(location).place_locked_item(new_item)

    if world.options.artifacts == 1:
        for location, vanilla_item in ARTIFACTS_LOCATIONS.items():
            new_item = world.create_item(vanilla_item)
            world.get_location(location).place_locked_item(new_item)

    if world.options.keys == 1:
        for location, vanilla_item in KEYS_LOCATIONS.items():
            new_item = world.create_item(vanilla_item)
            world.get_location(location).place_locked_item(new_item)

    if world.options.hearts == 1:
        for location, vanilla_item in HEARTS_LOCATIONS.items():
            new_item = world.create_item(vanilla_item)
            world.get_location(location).place_locked_item(new_item)

    if world.options.dungeon_items == 1:
        for location, vanilla_item in DUNGEON_ITEMS_LOCATIONS.items():
            new_item = world.create_item(vanilla_item)
            world.get_location(location).place_locked_item(new_item)

    if world.options.sword == 1:
        for location, vanilla_item in ARMAGEDDON_LOCATIONS.items():
            new_item = world.create_item(vanilla_item)
            world.get_location(location).place_locked_item(new_item)

    if world.options.scythe == 1:
        for location, vanilla_item in SCYTHE_LOCATIONS.items():
            new_item = world.create_item(vanilla_item)
            world.get_location(location).place_locked_item(new_item)

    if world.options.moves == 1:
        for location, vanilla_item in MOVES_LOCATIONS.items():
            new_item = world.create_item(vanilla_item)
            world.get_location(location).place_locked_item(new_item)