from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from BaseClasses import Item
from worlds.AutoWorld import World

from . import Locations, Items, Events, Options, Regions, Rules, WebWorld

class DSWorld(World):
    """Darksiders is an hack-and-slash action-adventure game where the player takes the role of War, one of the four horsemen of the Apocalypse stranded alone on Earth after the event of the Apocalypse."""
    
    game: str = "Darksiders"

    web = WebWorld.DSWeb()

    options_dataclass = Options.DSOptions
    options: Options.DSOptions

    location_name_to_id = Locations.LOCATION_NAME_TO_ID
    location_name_to_item = Locations.LOCATION_NAME_TO_ITEM
    item_name_to_id = Items.ITEM_NAME_TO_ID

    def generate_early(self) -> None:

        options = self.options

        if self.options.armor == 2 :
            options.local_items.value.add("Abyssal Armor Piece")
        elif self.options.armor == 3:
            options.local_items.value.add("Abyssal Armor")

        if self.options.artifacts == 2 :
            options.local_items.value.add("Soldier Artifact")
            options.local_items.value.add("Champion Artifact")
            options.local_items.value.add("Overlord Artifact")

        if self.options.keys == 3 :
            options.local_items.value.add("Beholder Key")

        if self.options.hearts == 2 :
            options.local_items.value.add("Heart of the Chosen")

        if self.options.dungeon_items == 4 :
            options.local_items.value.add("Hoardseeker")
            options.local_items.value.add("Map")

    def create_regions(self) -> None:

        Regions.create_and_connect_regions(self)
        Locations.create_all_locations(self)
        Events.create_all_events(self)

    def create_items(self) -> None:

        Items.create_all_items(self)

    def set_rules(self) -> None:

        Rules.set_all_rules(self)

    def pre_fill(self) -> None:

        Items.prefill_dungeon(self, "Broken Stairs.json")
        Items.prefill_dungeon(self, "Twilight Cathedral.json")
        Items.prefill_dungeon(self, "Hollows.json")
        Items.prefill_dungeon(self, "Iron Canopy.json")
        Items.prefill_dungeon(self, "Black Throne.json")

        #for location in self.get_locations():
        #    if location.item is not None:
        #        print(f"Location : {location} has this item : {location.item}")

    def get_pre_fill_items(self) -> list[Item]:

        pre_fill_items = []
        if self.options.keys == 2 :
            for _, vanilla_item in Locations.KEYS_LOCATIONS.items():
                pre_fill_items.append(self.create_item(vanilla_item))

        if self.options.dungeon_items == 3:
            for _, vanilla_item in Locations.DUNGEON_ITEMS_LOCATIONS.items():
                pre_fill_items.append(self.create_item(vanilla_item))
        return pre_fill_items

    def fill_slot_data(self) -> Mapping[str, Any]:

        return self.options.as_dict(
            "difficulty_level",
        )

    def create_item(self, name: str) -> Items.DSItem:

        return Items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:

        return Items.get_random_filler_item_name(self)