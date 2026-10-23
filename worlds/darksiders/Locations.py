from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Location
from rule_builder.rules import Has

from .Items import DSItem
from .Rules import CAN_BEAT_ABADDON, HAS_ABYSSAL_CHAIN, HAS_CHAOS_FORM, HAS_CROSSBLADE, HAS_GAUNTLET, HAS_MASK, HAS_RUIN, HAS_VOIDWALKER
from .Utils import data_path, json_read

if TYPE_CHECKING:
    from .World import DSWorld

def create_location_table_from_json(filename) -> None:

    region_json = json_read(data_path(filename))

    for region in region_json:
        if 'locations' in region:
            for location, location_data in region.get("locations").items():
                print(location)
                LOCATION_NAME_TO_ID[location] = location_data.get("ID")

LOCATION_NAME_TO_ID = {}

create_location_table_from_json("Anvil Ford.json")
create_location_table_from_json("Ashlands.json")
#create_location_table_from_json("Black Throne.json")
create_location_table_from_json("Broken Stairs.json")
create_location_table_from_json("Choking Grounds.json")
create_location_table_from_json("Crossroads.json")
create_location_table_from_json("Drowned Pass.json")
create_location_table_from_json("Dry Road.json")
#create_location_table_from_json("Eden.json")
create_location_table_from_json("Hollows.json")
#create_location_table_from_json("Iron Canopy.json")
#create_location_table_from_json("Leviathan Drift.json")
create_location_table_from_json("Library.json")
create_location_table_from_json("Menu.json")
create_location_table_from_json("Scalding Gallow.json")
create_location_table_from_json("Serpent Holes.json")
create_location_table_from_json("Twilight Cathedral.json")

#location_json = json_read(data_path("Anvil Ford.json"))

#for Region, region_data in location_json.items():
#    if 'locations' in region_data:
#        for location, location_data in region_data.items():
#            LOCATION_NAME_TO_ID[location] = location_data.get("ID")

class DSLocation(Location):

    game = "Darksiders"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:

    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def create_all_locations(world: DSWorld) -> None:

    create_regular_locations(world)
    create_events(world)

def create_regular_locations(world: DSWorld) -> None:

    #seraphim_hotel = world.get_region("Seraphim Hotel")

    create_locations_from_json(world, "Anvil Ford.json")
    create_locations_from_json(world, "Ashlands.json")
    create_locations_from_json(world, "Broken Stairs.json")
    create_locations_from_json(world, "Choking Grounds.json")
    create_locations_from_json(world, "Crossroads.json")
    create_locations_from_json(world, "Drowned Pass.json")
    create_locations_from_json(world, "Dry Road.json")
    create_locations_from_json(world, "Hollows.json")
    create_locations_from_json(world, "Library.json")
    create_locations_from_json(world, "Menu.json")
    create_locations_from_json(world, "Scalding Gallow.json")

    #seraphim_hotel_locations = get_location_names_with_ids([
    #    'Seraphim Hotel Life Chest 1',
    #    'Seraphim Hotel Life Chest 2'
    #])
    #seraphim_hotel.add_locations(seraphim_hotel_locations, DSLocation)

    create_locations_from_json(world, "Serpent Holes.json")
    create_locations_from_json(world, "Twilight Cathedral.json")

def create_events(world: DSWorld) -> None:

    black_throne_boss_room = world.get_region("Black Throne Boss Room")
    dry_road = world.get_region("Dry Road")
    eden = world.get_region("Eden")
    hollows_boss_room = world.get_region("Hollows Boss Room")
    leviathan_drift = world.get_region("Leviathan's Drift")
    #seraphim_hotel = world.get_region("Seraphim Hotel")
    silitha_loom = world.get_region("Silitha's Loom")

    #anvil_ford.add_event(location_name = "Ulthane defeated", rule = HAS_CHAOS_FORM, location_type = DSLocation)
    #anvil_ford_challenge_area.add_event(location_name = "Ulthane outscored", rule = HAS_CHAOS_FORM, location_type = DSLocation)
    #anvil_ford_challenge_area.add_event(location_name = "Uriel 1 defeated", rule = HAS_CROSSBLADE, location_type = DSLocation)
    black_throne_boss_room.add_event(location_name = "Straga defeated", item_name = "Straga Defeated", rule = HAS_VOIDWALKER, location_type = DSLocation)
    black_throne_boss_room.add_event(location_name = "Straga Item Reward", rule = HAS_VOIDWALKER, location_type = DSLocation)
    dry_road.add_event(location_name = "Uriel 2 defeated", rule = Has("Armageddon Blade Shards", count = 1), location_type = DSLocation)
    eden.add_event(location_name = "Shadow War defeated", rule = HAS_MASK, location_type = DSLocation)
    hollows_boss_room.add_event(location_name = "Griever defeated", item_name = "Heart of Chosen", rule = HAS_GAUNTLET, location_type = DSLocation)
    hollows_boss_room.add_event(location_name = "Griever Item Reward", rule = HAS_GAUNTLET, location_type = DSLocation)
    leviathan_drift.add_event(location_name = "Abaddon Destroyer defeated", item_name = "Victory", rule = CAN_BEAT_ABADDON, location_type = DSLocation, item_type = DSItem)
    leviathan_drift.add_event(location_name = "Stygian defeated", item_name = "Heart of Chosen", rule = HAS_RUIN, location_type = DSLocation)
    leviathan_drift.add_event(location_name = "Stygian Item Reward", rule = HAS_RUIN, location_type = DSLocation)
    #scalding_gallow.add_event(location_name = "Phantom General defeated", location_type = DSLocation)
    #scalding_gallow.add_event(location_name = "Samael's first Reward", location_type = DSLocation)
    #scalding_gallow.add_event(location_name = "Trade first Heart of Chosen", rule = Has("Heart of Chosen", count = 1), location_type = DSLocation)
    #scalding_gallow.add_event(location_name = "Trade second Heart of Chosen", rule = Has("Heart of Chosen", count = 2), location_type = DSLocation)
    #scalding_gallow.add_event(location_name = "Trade third Heart of Chosen", rule = Has("Heart of Chosen", count = 3), location_type = DSLocation)
    #scalding_gallow.add_event(location_name = "Trade fourth Heart of Chosen", rule = Has("Heart of Chosen", count = 4), location_type = DSLocation)
    silitha_loom.add_event(location_name = "Silitha defeated", item_name = "Heart of Chosen", rule = HAS_ABYSSAL_CHAIN, location_type = DSLocation)
    silitha_loom.add_event(location_name = "Silitha Item Reward", rule = HAS_ABYSSAL_CHAIN, location_type = DSLocation)
    #twilight_cathedral_2.add_event(location_name = "Jailer defeated", location_type = DSLocation)
    #twilight_cathedral_boss_room.add_event(location_name = "Tiamat defeated", item_name = "Heart of Chosen", rule = HAS_CROSSBLADE, location_type = DSLocation)
    #twilight_cathedral_boss_room.add_event(location_name = "Tiamat Item Reward", rule = HAS_CROSSBLADE, location_type = DSLocation)

def create_events_from_json(world: DSWorld, filename) -> None:

    region_json = json_read(data_path(filename))

    for region in region_json:
        if 'events' in region:
            this_region = world.get_region(region.get("name"))
            for event_name, event_data in region.get("events").items():
                if 'forced reward' in event_data:
                    this_region.add_event(location_name = event_name, item_name = event_data.get("forced reward"), rule = event_data.get("rule"), location_type = DSLocation, item_type = DSItem)
                else:
                    this_region.add_event(location_name = event_name, rule = event_data.get("rule"), location_type = DSLocation)

def create_locations_from_json(world: DSWorld, filename) -> None:

    region_json = json_read(data_path(filename))

    for region in region_json:
        if 'locations' in region:
            this_region = world.get_region(region_name = region.get("name"))
            region_locations = get_location_names_with_ids(location_names = region.get("locations"))
            this_region.add_locations(locations = region_locations, location_type = DSLocation)