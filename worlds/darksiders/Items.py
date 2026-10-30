from __future__ import annotations

from typing import Optional, TYPE_CHECKING

from BaseClasses import CollectionState, Item, ItemClassification, Location
from Fill import fill_restrictive

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
            if name == "Beholder Key" or name == "Heart of the Chosen":
                classification = ItemClassification.progression
            else:
                classification = ItemClassification.useful
        case name if name in item_json.get("Gear"):
            classification = ItemClassification.progression
        case name if name in item_json.get("Health"):
            classification = ItemClassification.useful
        case name if name in item_json.get("Primary Weapons"):
            if name == "Chaoseater" or name == "Chaoseater Level Up":
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
    local_itempool: list[Item] = []
    pre_fill_itempool: list[Item] = []
    item_json = json_read(data_path("Items.json"))

    for item, item_data in item_json.get("Abilities").items():
        shuffle_itempool.append(world.create_item(item))

    match world.options.armor:
        #case 0 is skipped because the pieces aren't obtainable
        case 1:
            for _ in range(item_json.get("Abyssal Armor").get("Abyssal Armor Piece").get("number")):
                pre_fill_itempool.append(world.create_item("Abyssal Armor Piece"))
        case 2:
            for _ in range(world.options.armor_pieces):
                local_itempool.append(world.create_item("Abyssal Armor Piece"))
        case 3:
            local_itempool.append(world.create_item("Abyssal Armor"))
        case 4:
            for _ in range(world.options.armor_pieces):
                shuffle_itempool.append(world.create_item("Abyssal Armor Piece"))
        case 5:
            shuffle_itempool.append(world.create_item("Abyssal Armor"))

    match world.options.artifacts:
        #case 0 is skipped because the artifacts aren't obtainable
        case 1:
            for _ in range(item_json.get("Artifacts").get("Soldier Artifact").get("number")):
                pre_fill_itempool.append(world.create_item("Soldier Artifact"))
            for _ in range(item_json.get("Artifacts").get("Champion Artifact").get("number")):
                pre_fill_itempool.append(world.create_item("Champion Artifact"))
            pre_fill_itempool.append(world.create_item("Overlord Artifact"))
        case 2:
            for _ in range(world.options.soldier_artifacts):
                local_itempool.append(world.create_item("Soldier Artifact"))
            for _ in range(world.options.champion_artifacts):
                local_itempool.append(world.create_item("Champion Artifact"))
            local_itempool.append(world.create_item("Overlord Artifact"))
        case 3:
            for _ in range(world.options.soldier_artifacts):
                shuffle_itempool.append(world.create_item("Soldier Artifact"))
            for _ in range(world.options.champion_artifacts):
                shuffle_itempool.append(world.create_item("Champion Artifact"))
            shuffle_itempool.append(world.create_item("Overlord Artifact"))

    for _ in range(world.options.containers - 1):#War starts with a container
        shuffle_itempool.append(world.create_item("Empty Container"))

    for item, item_data in item_json.get("Enhancements").items():
        shuffle_itempool.append(world.create_item(item))

    match world.options.keys:
        #case 0 is skipped because the keys aren't obtainable
        case 1:
            for _ in range(item_json.get("Keys").get("Beholder Key").get("number")):
                pre_fill_itempool.append(world.create_item("Beholder Key"))
        case 2:
            for _ in range(item_json.get("Keys").get("Beholder Key").get("number")):
                pre_fill_itempool.append(world.create_item("Beholder Key"))
        case 3:
            for _ in range(item_json.get("Keys").get("Beholder Key").get("number")):
                local_itempool.append(world.create_item("Beholder Key"))
        case 4:
            for _ in range(item_json.get("Keys").get("Beholder Key").get("number")):
                shuffle_itempool.append(world.create_item("Beholder Key"))

    match world.options.hearts:
        #case 0 is skipped because the hearts aren't obtainable
        case 1:
            for _ in range(item_json.get("Keys").get("Heart of the Chosen").get("number")):
                pre_fill_itempool.append(world.create_item("Heart of the Chosen"))
        case 2:
            for _ in range(item_json.get("Keys").get("Heart of the Chosen").get("number")):
                local_itempool.append(world.create_item("Heart of the Chosen"))
        case 3:
            for _ in range(item_json.get("Keys").get("Heart of the Chosen").get("number")):
                shuffle_itempool.append(world.create_item("Heart of the Chosen"))

    match world.options.dungeon_items:
        #case 0 is skipped because the maps and hoardseekers aren't obtainable
        case 1:
            for _ in range(item_json.get("Keys").get("Map").get("number")):
                pre_fill_itempool.append(world.create_item("Map"))
            for _ in range(item_json.get("Keys").get("Hoardseeker").get("number")):
                pre_fill_itempool.append(world.create_item("Hoardseeker"))
        #case 2 is skipped because the maps and hoardseekers have already been granted to the player
        case 3:
            for _ in range(item_json.get("Keys").get("Map").get("number")):
                pre_fill_itempool.append(world.create_item("Map"))
            for _ in range(item_json.get("Keys").get("Hoardseeker").get("number")):
                pre_fill_itempool.append(world.create_item("Hoardseeker"))
        case 4:
            for _ in range(item_json.get("Keys").get("Map").get("number")):
                local_itempool.append(world.create_item("Map"))
            for _ in range(item_json.get("Keys").get("Hoardseeker").get("number")):
                local_itempool.append(world.create_item("Hoardseeker"))
        case 5:
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
        #case 0 is skipped because Chaoseaster isn't obtainable
        case 1:
            for _ in range(item_json.get("Primary Weapons").get("Armageddon Blade Shard").get("number")):
                pre_fill_itempool.append(world.create_item("Armageddon Blade Shard"))
            if world.options.weapons != 1:
                shuffle_itempool.append(world.create_item('Chaoseater'))
            pre_fill_itempool.append(world.create_item("Armageddon Blade"))
        case 2:
            for _ in range(world.options.armageddon):
                shuffle_itempool.append(world.create_item('Armageddon Blade Shard'))
            if world.options.weapons != 1:
                shuffle_itempool.append(world.create_item('Chaoseater'))
            pre_fill_itempool.append(world.create_item("Armageddon Blade"))
        case 3:
            shuffle_itempool.append(world.create_item('Progressive Sword'))
            if world.options.weapons != 1:
                shuffle_itempool.append(world.create_item('Progressive Sword'))

    match world.options.scythe:
        #case 0 is skipped because Hellraiser and Harvester isn't obtainable
        case 1:
            pre_fill_itempool.append(world.create_item("Hellraiser"))
            pre_fill_itempool.append(world.create_item("Harvester"))
        case 2:
            if world.options.weapons != 2:
                shuffle_itempool.append(world.create_item('Hellraiser'))
        case 3:
            if world.options.weapons != 2:
                shuffle_itempool.append(world.create_item('Harvester'))
        case 4:
            shuffle_itempool.append(world.create_item('Progressive Scythe'))
            if world.options.weapons != 2:
                shuffle_itempool.append(world.create_item('Progressive Scythe'))
    
    shuffle_itempool.append(world.create_item("Tremor Gauntlet"))

    for _ in range(item_json.get("Primary Weapons").get("Chaoseater Level Up").get("number")):
        shuffle_itempool.append(world.create_item("Chaoseater Level Up"))
    for _ in range(item_json.get("Secondary Weapons").get("Scythe Level Up").get("number")):
        shuffle_itempool.append(world.create_item("Scythe Level Up"))
    for _ in range(item_json.get("Secondary Weapons").get("Gauntlet Level Up").get("number")):
        shuffle_itempool.append(world.create_item("Gauntlet Level Up"))

    match world.options.moves:
        #case 0 is skipped because combos and moves are removed from the game
        case 1:
            for item, item_data in item_json.get("Gauntlet Combos").items():
                for _ in range(item_data.get("number")):
                    pre_fill_itempool.append(world.create_item(item))
            for item, item_data in item_json.get("Scythe Combos").items():
                for _ in range(item_data.get("number")):
                    pre_fill_itempool.append(world.create_item(item))
            for item, item_data in item_json.get("Sword Combos").items():
                for _ in range(item_data.get("number")):
                    pre_fill_itempool.append(world.create_item(item))
        case 2:
            for item, item_data in item_json.get("Gauntlet Combos").items():
                for _ in range(item_data.get("number")):
                    local_itempool.append(world.create_item(item))
            for item, item_data in item_json.get("Scythe Combos").items():
                for _ in range(item_data.get("number")):
                    local_itempool.append(world.create_item(item))
            for item, item_data in item_json.get("Sword Combos").items():
                for _ in range(item_data.get("number")):
                    local_itempool.append(world.create_item(item))
        case 3:
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
    
    number_of_items = len(shuffle_itempool) + len(pre_fill_itempool) + len(local_itempool)
    #print(f"Il y a {number_of_items} items dont {len(shuffle_itempool)} à mélanger, {len(pre_fill_itempool)} à pré-remplir et {len(local_itempool)} à placer localement.")
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    #print(f"On compte {needed_number_of_filler_items} fillers à placer.")
    shuffle_itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
    world.multiworld.itempool += shuffle_itempool
    #print(f"Shuffled item pool of length {len(shuffle_itempool)} : {shuffle_itempool}")
    #print(f"Local item pool of length {len(local_itempool)} : {local_itempool}")
    #print(f"Pre fill item pool of length {len(pre_fill_itempool)} : {pre_fill_itempool}")

def get_random_filler_item_name(world: DSWorld) -> str:

    item_json = json_read(data_path("Items.json"))

    return world.random.choice(list(item_json.get("Consumables").keys() | item_json.get("Souls").keys()))

def prefill_dungeon(world: DSWorld, filename) -> None:

    region_json = json_read(data_path(filename))
    available_locations: list[Location] = []
    items_to_place: list[Item] = []

    for region in region_json:
        if "locations" in region:
            for location, location_data in region.get("locations").items():
                if world.get_location(location).item is None:
                    available_locations.append(world.get_location(location))
                if world.options.keys == 2:
                    if location_data.get("vanilla item") == "Beholder Key":
                        #print(location, location_data)
                        items_to_place.append(world.create_item("Beholder Key"))
                if world.options.dungeon_items == 3:
                    #print(location, location_data)
                    if location_data.get("vanilla item") == "Map":
                        items_to_place.append(world.create_item("Map"))
                    if location_data.get("vanilla item") == "Hoardseeker":
                        items_to_place.append(world.create_item("Hoardseeker"))

    all_state_base = CollectionState(world.multiworld)
    for item in world.multiworld.itempool:
        all_state_base.collect(item)
    for item in items_to_place:
        all_state_base.collect(item)
    #for region in region_json:
        #if "events" in region:
            #for event, event_data in region.get("events").items():
                #all_state_base.collect(DSItem(event_data.get("item"), ItemClassification.progression, None, world.player))
    all_state_base.sweep_for_advancements()

    world.random.shuffle(available_locations)
    #world.random.shuffle(items_to_place)
    #print(items_to_place)

    if items_to_place:
        fill_restrictive(multiworld = world.multiworld, base_state = all_state_base, locations = available_locations, item_pool = items_to_place, single_player_placement = True, lock = True, allow_excluded = True)
