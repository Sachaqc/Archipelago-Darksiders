from __future__ import annotations

from typing import Optional, TYPE_CHECKING

from BaseClasses import Item, ItemClassification

from .Utils import data_path, json_read

if TYPE_CHECKING:
    from .World import DSWorld

ITEM_NAME_TO_ID = {}

item_json = json_read(data_path("Items.json"))

for item_group, item_group_data in item_json.items():
    for item, item_data in item_group_data.items():
        ITEM_NAME_TO_ID[item] = item_data.get("ID")

class DSItem(Item):

    game: str = "Darksiders"

def create_item_with_correct_classification(world: DSWorld, name: str) -> DSItem:

    item_json = json_read(data_path("Items.json"))

    match name:
        case name if name in item_json.get("Abilities"):
            classification = ItemClassification.progression
        case name if name in item_json.get("Abyssal Armor"):
            classification = ItemClassification.useful
        case name if name in item_json.get("Artifacts"):
            classification = ItemClassification.progression
        case name if name in item_json.get("Enhancements"):
            classification = ItemClassification.useful
        case name if name in item_json.get("Keys"):
            classification = ItemClassification.progression
        case name if name in item_json.get("Gear"):
            classification = ItemClassification.progression
        case name if name in item_json.get("Health"):
            classification = ItemClassification.useful
        case name if name in item_json.get("Primary Weapons"):
            if name == "Progressive Chaoseater":
                classification = ItemClassification.useful
            else:
                classification = ItemClassification.progression
        case name if name in item_json.get("Secondary Weapons"):
            if name == "Progressive Gauntlet":
                classification = ItemClassification.progression
            else:
                classification = ItemClassification.useful
        case name if name in item_json.get("Wrath"):
            classification = ItemClassification.useful
        case name if name in item_json.get("Wrath Abilities"):
            classification = ItemClassification.useful
        case _: 
            classification = ItemClassification.filler

    return DSItem(name, classification, ITEM_NAME_TO_ID[name], world.player)

def get_random_filler_item_name(world: DSWorld) -> str:

    item_json = json_read(data_path("Items.json"))

    return world.random.choice(list(item_json.get("Consumables").keys() | item_json.get("Souls").keys()))

def create_all_items(world: DSWorld) -> None:

    itempool: list[Item] = []

    item_json = json_read(data_path("Items.json"))

    for item_group, item_group_data in item_json.items():
        for item, item_data in item_group_data.items():
            if 'number' in item_data:
                print(item_data.get("number"))
                for i in range(item_data.get("number")):
                    itempool.append(world.create_item(item))

    if world.options.abyssanity:
        for i in range(10):
            itempool.append(world.create_item("Abyssal Armor Piece"))

    if world.options.artisanity:
        for i in range(20):
            itempool.append(world.create_item("Soldier Artifact"))
        for i in range(6):
            itempool.append(world.create_item("Champion Artifact"))
        itempool.append(world.create_item("Overlord Artifact"))

    for i in range(world.options.lifestones):
        itempool.append(world.create_item("Lifestone"))

    if world.options.lifestones_shards > 0:
        starting_health = 1
        for i in range(10 - starting_health - world.options.lifestones):
            for i in range(world.options.lifestones_shards*2):
                itempool.append(world.create_item('Lifestone Shard'))

    for i in range(world.options.wrath_cores):
        itempool.append(world.create_item('Wrath Core'))

    if world.options.wrath_cores > 0:
        starting_wrath = 2
        for i in range(10 - starting_wrath - world.options.wrath_cores):
            for i in range(world.options.wrath_cores*2):
                itempool.append(world.create_item('Wrath Shard'))
    
    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
    world.multiworld.itempool += itempool