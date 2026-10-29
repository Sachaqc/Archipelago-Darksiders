from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from BaseClasses import Item
from worlds.AutoWorld import World

from . import Items, Locations, Options, Regions, Rules, WebWorld

class DSWorld(World):
    """Darksiders is an hack-and-slash action-adventure game where the player takes the role of War, one of the four horsemen of the Apocalypse stranded alone on Earth after the event of the Apocalypse."""
    
    game: str = "Darksiders"

    web = WebWorld.DSWeb()

    options_dataclass = Options.DSOptions
    options: Options.DSOptions

    location_name_to_id = Locations.LOCATION_NAME_TO_ID
    location_name_to_item = Locations.LOCATION_NAME_TO_ITEM
    item_name_to_id = Items.ITEM_NAME_TO_ID

    def create_regions(self) -> None:

        Regions.create_and_connect_regions(self)
        Locations.create_all_locations(self)

    def create_items(self) -> None:

        Items.create_all_items(self)

    def set_rules(self) -> None:

        Rules.set_all_rules(self)

    def pre_fill(self) -> None:

        Locations.place_vanilla_items(self)
        Items.prefill_dungeon(self, "Ashlands.json")
        Items.prefill_dungeon(self, "Broken Stairs.json")
        Items.prefill_dungeon(self, "Twilight Cathedral.json")
        Items.prefill_dungeon(self, "Hollows.json")
        Items.prefill_dungeon(self, "Iron Canopy.json")
        Items.prefill_dungeon(self, "Black Throne.json")

    def get_pre_fill_items(self) -> list[Item]:

        pre_fill_items = []

        if self.options.armor == 1:
            for _, vanilla_item in Locations.ABYSSAL_ARMOR_PIECES_LOCATIONS.items():
                new_item = self.create_item(vanilla_item)
                pre_fill_items.append(new_item)

        if self.options.artifacts == 1:
            for _, vanilla_item in Locations.ARTIFACTS_LOCATIONS.items():
                new_item = self.create_item(vanilla_item)
                pre_fill_items.append(new_item)

        if self.options.keys == 1 or self.options.keys == 2 :
            for _, vanilla_item in Locations.KEYS_LOCATIONS.items():
                new_item = self.create_item(vanilla_item)
                pre_fill_items.append(new_item)

        if self.options.hearts == 1:
            for _, vanilla_item in Locations.HEARTS_LOCATIONS.items():
                new_item = self.create_item(vanilla_item)
                pre_fill_items.append(new_item)

        if self.options.dungeon_items == 1 or self.options.dungeon_items == 3:
            for _, vanilla_item in Locations.DUNGEON_ITEMS_LOCATIONS.items():
                new_item = self.create_item(vanilla_item)
                pre_fill_items.append(new_item)

        if self.options.sword == 1:
            for _, vanilla_item in Locations.ARMAGEDDON_LOCATIONS.items():
                new_item = self.create_item(vanilla_item)
                pre_fill_items.append(new_item)

        if self.options.scythe == 1:
            for _, vanilla_item in Locations.SCYTHE_LOCATIONS.items():
                new_item = self.create_item(vanilla_item)
                pre_fill_items.append(new_item)

        if self.options.moves == 1:
            for _, vanilla_item in Locations.MOVES_LOCATIONS.items():
                new_item = self.create_item(vanilla_item)
                pre_fill_items.append(new_item)
        print(f"The World's pre-fill item list is : {pre_fill_items}")
        return pre_fill_items

    def fill_slot_data(self) -> Mapping[str, Any]:

        return self.options.as_dict(
            "difficulty_level",
        )

    def create_item(self, name: str) -> Items.DSItem:

        return Items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:

        return Items.get_random_filler_item_name(self)