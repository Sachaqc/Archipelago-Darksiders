from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Location

from .Items import DSItem
from .Locations import DSLocation
from .Utils import data_path, json_read

if TYPE_CHECKING:
    from .World import DSWorld

def create_all_events(world: DSWorld) -> None:

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