from __future__ import annotations

from typing import Optional, TYPE_CHECKING

from BaseClasses import CollectionState, Item, ItemClassification, Location
from Fill import fill_restrictive

from .Locations import ABYSSAL_ARMOR_PIECES_LOCATIONS, ARTIFACTS_LOCATIONS, DUNGEON_ITEMS_LOCATIONS, HEARTS_LOCATIONS, KEYS_LOCATIONS, ARMAGEDDON_LOCATIONS, SCYTHE_LOCATIONS, MOVES_LOCATIONS
from .Utils import json_read

if TYPE_CHECKING:
    from .World import DSWorld

ITEM_NAME_TO_ID = {}

item_name_groups = {}

item_json = json_read("Items.json")

for item_group, item_group_data in item_json.items():
    new_items = set()
    for item, item_data in item_group_data.items():
        ITEM_NAME_TO_ID[item] = item_data.get("ID")
        new_items.add(item)
    item_name_groups[item_group] = new_items

class DSItem(Item):

    game: str = "Darksiders"

def create_item_with_correct_classification(world: DSWorld, name: str) -> DSItem:

    item_json = json_read("Items.json")

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
            if name == "Beholder Key" or name == "Heart of the Chosen":
                classification = ItemClassification.progression
            else:
                classification = ItemClassification.useful
        case name if name in item_json.get("Gear"):
            classification = ItemClassification.progression
        case name if name in item_json.get("Health"):
            classification = ItemClassification.useful
        case name if name in item_json.get("Primary Weapons"):
            if name == "Chaoseater Level Up":
                classification = ItemClassification.useful
            else:
                classification = ItemClassification.progression
        case name if name in item_json.get("Secondary Weapons"):
            if name == "Tremor Gauntlet":
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

def create_all_items(world: DSWorld) -> None:

    shuffle_itempool: list[Item] = []
    item_json = json_read("Items.json")

    for item, item_data in item_json.get("Abilities").items():
        shuffle_itempool.append(world.create_item(item))

    match world.options.armor:
        case 0 :
            #case 0 is skipped because the items aren't obtainable with the currently selected options
            pass
        case 1 :
            for location, vanilla_item in ABYSSAL_ARMOR_PIECES_LOCATIONS.items():
                world.get_location(location).place_locked_item(world.create_item(vanilla_item))
        case 2 | 4 :
            for _ in range(world.options.armor_pieces):
                shuffle_itempool.append(world.create_item("Abyssal Armor Piece"))
        case 3 | 5 :
            shuffle_itempool.append(world.create_item("Abyssal Armor"))

    match world.options.artifacts:
        case 0 :
            #case 0 is skipped because the items aren't obtainable with the currently selected options
            pass
        case 1 :
            for location, vanilla_item in ARTIFACTS_LOCATIONS.items():
                world.get_location(location).place_locked_item(world.create_item(vanilla_item))
        case _ :
            for _ in range(world.options.soldier_artifacts):
                shuffle_itempool.append(world.create_item("Soldier Artifact"))
            for _ in range(world.options.champion_artifacts):
                shuffle_itempool.append(world.create_item("Champion Artifact"))
            shuffle_itempool.append(world.create_item("Overlord Artifact"))

    world.multiworld.push_precollected(world.create_item("Empty Vessel"))#War starts with a container
    for _ in range(world.options.containers - 1):
        shuffle_itempool.append(world.create_item("Empty Vessel"))

    for item, item_data in item_json.get("Enhancements").items():
        shuffle_itempool.append(world.create_item(item))

    match world.options.keys:
        case 0 | 2 :
            #case 0 is skipped because the items aren't obtainable with the currently selected options
            #case 2 is skipped because the items are not part of the randomization
            pass
        case 1 :
            for location, vanilla_item in KEYS_LOCATIONS.items():
                world.get_location(location).place_locked_item(world.create_item(vanilla_item))
        case _ :
            for _ in range(item_json.get("Keys").get("Beholder Key").get("number")):
                shuffle_itempool.append(world.create_item("Beholder Key"))

    match world.options.hearts:
        case 0 :
            #case 0 is skipped because the items aren't obtainable with the currently selected options
            pass
        case 1 :
            for location, vanilla_item in HEARTS_LOCATIONS.items():
                world.get_location(location).place_locked_item(world.create_item(vanilla_item))
        case _ :
            for _ in range(item_json.get("Keys").get("Heart of the Chosen").get("number")):
                shuffle_itempool.append(world.create_item("Heart of the Chosen"))

    match world.options.dungeon_items:
        case "remove" | "region" :
            #case 0 is skipped because the items aren't obtainable with the currently selected options
            #case 3 is skipped because the items are not part of the randomization
            pass
        case "vanilla" :
            for location, vanilla_item in DUNGEON_ITEMS_LOCATIONS.items():
                world.get_location(location).place_locked_item(world.create_item(vanilla_item))
        case "start_with" :
            for _ in range(item_json.get("Keys").get("Map").get("number")):
                world.multiworld.push_precollected(world.create_item("Map"))
            for _ in range(item_json.get("Keys").get("Hoardseeker").get("number")):
                world.multiworld.push_precollected(world.create_item("Hoardseeker"))
        case _ :
            for _ in range(item_json.get("Keys").get("Map").get("number")):
                shuffle_itempool.append(world.create_item("Map"))
            for _ in range(item_json.get("Keys").get("Hoardseeker").get("number")):
                shuffle_itempool.append(world.create_item("Hoardseeker"))

    for item, item_data in item_json.get("Gear").items():
        shuffle_itempool.append(world.create_item(item))


    for _ in range(world.options.lifestones):
        shuffle_itempool.append(world.create_item("Lifestone"))

    if world.options.lifestones_shards > 0:
        starting_health = 1
        for _ in range(10 - starting_health - world.options.lifestones):
            for _ in range(world.options.lifestones_shards*2):
                shuffle_itempool.append(world.create_item('Lifestone Shard'))

    match world.options.sword:
        case "remove" :
            if world.options.weapons != "start_with_sword":
                shuffle_itempool.append(world.create_item('Armageddon Blade'))
            else:
                world.multiworld.push_precollected(world.create_item('Armageddon Blade'))
        case "vanilla" :
            for location, vanilla_item in ARMAGEDDON_LOCATIONS.items():
                world.get_location(location).place_locked_item(world.create_item(vanilla_item))
            if world.options.weapons != 1:
                shuffle_itempool.append(world.create_item('Chaoseater'))
            else:
                world.multiworld.push_precollected(world.create_item('Chaoseater'))
            for _ in range(item_json.get("Primary Weapons").get("Chaoseater Level Up").get("number")):
                shuffle_itempool.append(world.create_item("Chaoseater Level Up"))
        case "shards" :
            world.get_location("Anvil's Ford Reforge the Blade").place_locked_item(world.create_item("Armageddon Blade"))
            for _ in range(world.options.armageddon):
                shuffle_itempool.append(world.create_item('Armageddon Blade Shard'))
            if world.options.weapons != 1:
                shuffle_itempool.append(world.create_item('Chaoseater'))
            else:
                world.multiworld.push_precollected(world.create_item('Chaoseater'))
            for _ in range(item_json.get("Primary Weapons").get("Chaoseater Level Up").get("number")):
                shuffle_itempool.append(world.create_item("Chaoseater Level Up"))
        case "progressive" :
            shuffle_itempool.append(world.create_item('Progressive Sword'))
            if world.options.weapons != 1:
                shuffle_itempool.append(world.create_item('Progressive Sword'))
            else:
                world.multiworld.push_precollected(world.create_item('Progressive Sword'))
            for _ in range(item_json.get("Primary Weapons").get("Chaoseater Level Up").get("number")):
                shuffle_itempool.append(world.create_item("Chaoseater Level Up"))

    match world.options.scythe:
        case "remove":
            if world.options.weapons == "start_with_scythe":
                world.multiworld.push_precollected(world.create_item('Hellraiser'))
                for _ in range(item_json.get("Secondary Weapons").get("Scythe Level Up").get("number")):
                    shuffle_itempool.append(world.create_item("Scythe Level Up"))
        case "vanilla":
            for location, vanilla_item in SCYTHE_LOCATIONS.items():
                world.get_location(location).place_locked_item(world.create_item(vanilla_item))
            for _ in range(item_json.get("Secondary Weapons").get("Scythe Level Up").get("number")):
                shuffle_itempool.append(world.create_item("Scythe Level Up"))
        case "hellraiser":
            if world.options.weapons != "start_with_scythe":
                shuffle_itempool.append(world.create_item('Hellraiser'))
            else:
                world.multiworld.push_precollected(world.create_item('Hellraiser'))
            for _ in range(item_json.get("Secondary Weapons").get("Scythe Level Up").get("number")):
                shuffle_itempool.append(world.create_item("Scythe Level Up"))
        case "harvester":
            if world.options.weapons != 2:
                shuffle_itempool.append(world.create_item('Harvester'))
            else:
                world.multiworld.push_precollected(world.create_item('Harvester'))
            for _ in range(item_json.get("Secondary Weapons").get("Scythe Level Up").get("number")):
                shuffle_itempool.append(world.create_item("Scythe Level Up"))
        case "progressive":
            shuffle_itempool.append(world.create_item('Progressive Scythe'))
            if world.options.weapons != 2:
                shuffle_itempool.append(world.create_item('Progressive Scythe'))
            else:
                world.multiworld.push_precollected(world.create_item('Progressive Scythe'))
            for _ in range(item_json.get("Secondary Weapons").get("Scythe Level Up").get("number")):
                shuffle_itempool.append(world.create_item("Scythe Level Up"))

    if world.options.weapons != 3:
        shuffle_itempool.append(world.create_item("Tremor Gauntlet"))
    else:
        world.multiworld.push_precollected(world.create_item('Tremor Gauntlet'))

    for _ in range(item_json.get("Secondary Weapons").get("Gauntlet Level Up").get("number")):
        shuffle_itempool.append(world.create_item("Gauntlet Level Up"))

    match world.options.moves:
        case 0 :
            #case 0 is skipped because the items aren't obtainable with the currently selected options
            pass
        case 1 :
            for location, vanilla_item in MOVES_LOCATIONS.items():
                world.get_location(location).place_locked_item(world.create_item(vanilla_item))
        case 2 :
            for item, item_data in item_json.get("Gauntlet Combos").items():
                for _ in range(item_data.get("number")):
                    shuffle_itempool.append(world.create_item(item))
            for item, item_data in item_json.get("Scythe Combos").items():
                for _ in range(item_data.get("number")):
                    shuffle_itempool.append(world.create_item(item))
            for item, item_data in item_json.get("Sword Combos").items():
                for _ in range(item_data.get("number")):
                    shuffle_itempool.append(world.create_item(item))

    for item, item_data in item_json.get("Upgrades").items():
        for _ in range(item_data.get("number")):
            shuffle_itempool.append(world.create_item(item))

    for _ in range(world.options.wrath_cores):
        shuffle_itempool.append(world.create_item('Wrath Core'))

    if world.options.wrath_cores > 0:
        starting_wrath = 2
        for _ in range(10 - starting_wrath - world.options.wrath_cores):
            for _ in range(world.options.wrath_cores*2):
                shuffle_itempool.append(world.create_item('Wrath Shard'))

    for item, item_data in item_json.get("Wrath Abilities").items():
        for _ in range(item_data.get("number")):
            shuffle_itempool.append(world.create_item(item))
    
    number_of_items = len(shuffle_itempool) + len(world.get_pre_fill_items())
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    shuffle_itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
    world.multiworld.itempool += shuffle_itempool

def get_random_filler_item_name(world: DSWorld) -> str:

    item_json = json_read("Items.json")
    consumables = item_json.get("Consumables").keys()
    filler_consumables = [item for item in consumables if item != "Empty Vessel"]
    souls = item_json.get("Souls").keys()
    fillers = list(filler_consumables | souls)

    return world.random.choice(fillers)

def prefill_dungeon(world: DSWorld, filename) -> None:

    region_json = json_read(filename)
    available_locations: list[Location] = []
    items_to_place: list[Item] = []

    for region in region_json:
        if "locations" in region:
            for location, location_data in region.get("locations").items():
                if world.get_location(location).item is None:
                    available_locations.append(world.get_location(location))
                if world.options.keys == 2:
                    if location_data.get("vanilla item") == "Beholder Key":
                        items_to_place.append(world.create_item("Beholder Key"))
                if world.options.dungeon_items == 3:
                    if location_data.get("vanilla item") == "Map":
                        items_to_place.append(world.create_item("Map"))
                    if location_data.get("vanilla item") == "Hoardseeker":
                        items_to_place.append(world.create_item("Hoardseeker"))

    all_state_base = CollectionState(world.multiworld)
    for item in world.multiworld.itempool:
        all_state_base.collect(item, prevent_sweep = True)
    all_state_base.sweep_for_advancements()

    world.random.shuffle(available_locations)

    if items_to_place:
        fill_restrictive(multiworld = world.multiworld, base_state = all_state_base, locations = available_locations, item_pool = items_to_place, single_player_placement = True, lock = True, allow_excluded = True)
