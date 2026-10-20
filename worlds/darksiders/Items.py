from __future__ import annotations

from typing import Optional, TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .World import DSWorld

abyssal_armor_pieces = {
    'Abyssal Armor Piece': 1, #armor/item_armorpiece
    #'Abyssal Armor Piece 1': 2,
    #'Abyssal Armor Piece 2': 3,
    #'Abyssal Armor Piece 3': 4,
    #'Abyssal Armor Piece 4': 5,
    #'Abyssal Armor Piece 5': 6,
    #'Abyssal Armor Piece 6': 7,
    #'Abyssal Armor Piece 7': 8,
    #'Abyssal Armor Piece 8': 9,
    #'Abyssal Armor Piece 9': 10,
    #'Abyssal Armor Piece 10': 11
    # Abyssal armor : armor/item_abyssumarmor
}

artifacts = {
    'Soldier Artifact': 20, #items/artifact_pawn
    'Champion Artifact': 21, #items/artifact_general
    'Overlord Artifact': 22, #items/artifact_master
    #'Champion Artifact 1': 23,
    #'Champion Artifact 2': 24,
    #'Champion Artifact 3': 25,
    #'Champion Artifact 4': 26,
    #'Champion Artifact 5': 27,
    #'Champion Artifact 6': 28,
    #'Soldier Artifact 1': 29,
    #'Soldier Artifact 2': 30,
    #'Soldier Artifact 3': 31,
    #'Soldier Artifact 4': 32,
    #'Soldier Artifact 5': 33,
    #'Soldier Artifact 6': 34,
    #'Soldier Artifact 7': 35,
    #'Soldier Artifact 8': 36,
    #'Soldier Artifact 9': 37,
    #'Soldier Artifact 10': 38,
    #'Soldier Artifact 11': 39,
    #'Soldier Artifact 12': 40,
    #'Soldier Artifact 13': 41,
    #'Soldier Artifact 14': 42,
    #'Soldier Artifact 15': 43,
    #'Soldier Artifact 16': 44,
    #'Soldier Artifact 17': 45,
    #'Soldier Artifact 18': 46,
    #'Soldier Artifact 19': 47,
    #'Soldier Artifact 20': 48
}

consumables = {
    'Empty Container': 50, #items/item_consumableslot
    'Life Essence': 51,
    'Greater Life Essence': 52,
    'Possession': 53,
    'Rage Essence': 54,
    'Greater Rage Essence': 55,
    'Undying': 56
}

enhancements = {
    'Bane' : 60, #weapon_enhancements/common_bane
    'Bloodthirst': 61, #weapon_enhancements/common_leech
    'Carnage': 62, #weapon_enhancements/common_ire
    'Combat Lore': 63, #weapon_enhancements/common_divination
    'Hellfire': 64, #weapon_enhancements/common_brimstone
    'Ravager': 65, #weapon_enhancements/common_desecration
    'Reaper': 66, #weapon_enhancements/common_reaper
    'Weapon Master': 67, #weapon_enhancements/common_transfixion
}

keys = {
    'Beholder Key': 59 #items/item_dungeonkey
}

legendary_enhancements = {
    'Wars Glory' : 75, #weapon_enhancements/legendary_warswrath
    'Strifes Offering' : 76, #weapon_enhancements/legendary_strifesprowess
    'Furys Embrace' : 77, #weapon_enhancements/legendary_furysmadness
    'Deaths Blessing' : 78, #weapon_enhancements/legendary_deathsblessing
}

gear_and_equipments = {
    'Abyssal Chain' : 80, #gear_ghosthook/playergearghosthook
    'Crossblade': 81, #gear_crossblade/playergearcrossblade
    'Earthcaller': 82, #gear_horn/playergearhorn
    'Mask of Shadows': 83, #gear_eyeoflilith/playergeareyeoflilith
    'Mercy': 84, #weapon_strifesgun/strifes_gun
    'Voidwalker': 85 #gear_voidwalker/playergearvoidwalker
}

hearts_of_the_chosen = {
    'Heart of the Chosen' : 87, #items/item_demonheart
}

lifestones = {
    'Lifestone':90 #items/item_healthstone
    #'Lifestone Griever': 91,
    #'Lifestone Silitha': 92,
    #'Lifestone Straga': 93,
    #'Lifestone Stygian': 94,
    #'Lifestone Tiamat': 95
}

lifestone_shards = {
    'Lifestone Shard':100 #items/item_healthshard
    #'Lifestone Shard 1': 101,
    #'Lifestone Shard 2': 102,
    #'Lifestone Shard 3': 103,
    #'Lifestone Shard 4': 105,
    #'Lifestone Shard 5': 105,
    #'Lifestone Shard 6': 106,
    #'Lifestone Shard 7': 107,
    #'Lifestone Shard 8': 108,
    #'Lifestone Shard 9': 109,
    #'Lifestone Shard 10': 110,
    #'Lifestone Shard 11': 111,
    #'Lifestone Shard 12': 112,
    #'Lifestone Shard 13': 113,
    #'Lifestone Shard 14': 114,
    #'Lifestone Shard 15': 115,
    #'Lifestone Shard 16': 116
}

passive_abilities = {
    'Block Counter': 120, #items/item_blockcounter
    'Chaos Form': 121, #item_havocform/item_havocform
    'Chronomancer': 122, #item_frenzy/item_frenzy
    'Ruin': 123, #items/item_ruinshard
    'Serpent Holes': 124, #items/item_teleportability
    'Shadowflight': 125, #gear_tempestcloak/playergeartempestcloak
    'Soul Bridge': 126, #items/item_soulbridgeshard
}

primary_weapons = {
    'Progressive Chaoseater': 130,
    #'Chaoseater': 131,
    'Armageddon Blade': 132, #items/item_armageddonsword
    'Armageddon Blade Shards': 133 #items/item_swordpiece
    #'Sword Key': 131, #ch_com/weapon_swordkey
}

secondary_weapons = {
    'Progressive Scythe': 140,
    #'Harvester': 141, #harvester/harvester
    #'Scythe': 142, #hellraiser/hellraiser
    'Progressive Gauntlet': 143,
    #'Tremor Gauntlet': 144 #gauntlets/weapon_gauntlets
}

souls_chests = {
    'Currency': 150,
    'Health': 151,
    'Wrath': 152
}

wrath_abilities = {
    'Affliction': 160, #wrath_affliction/wrath_affliction
    'Blade Geyser': 161, #wrath_bladegeyser/wrath_bladegeyser ???????
    'Immolation': 162, #wrath_immolation/wrath_immolation
    'Stoneskin': 163 #wrath_stoneskin/wrath_stoneskin
}

wrath_cores = {
    'Wrath Core': 170, #items/item_wrathstone
    #'Wrath Core 1': 171,
    #'Wrath Core 2': 172,
    #'Wrath Core 3': 173
}

wrath_shards = {
    'Wrath Shard': 180, #items/item_wrathshard
    #'Wrath Shard 1': 181,
    #'Wrath Shard 2': 182,
    #'Wrath Shard 3': 183,
    #'Wrath Shard 4': 184,
    #'Wrath Shard 5': 185,
    #'Wrath Shard 6': 186,
    #'Wrath Shard 7': 187,
    #'Wrath Shard 8': 188,
    #'Wrath Shard 9': 189,
    #'Wrath Shard 10': 190,
    #'Wrath Shard 11': 191,
    #'Wrath Shard 12': 192,
    #'Wrath Shard 13': 193,
    #'Wrath Shard 14': 194,
    #'Wrath Shard 15': 195,
    #'Wrath Shard 16': 196,
    #'Wrath Shard 17': 197,
    #'Wrath Shard 18': 198,
    #'Wrath Shard 19': 199,
    #'Wrath Shard 20': 200
}

ITEM_NAME_TO_ID = abyssal_armor_pieces | artifacts | consumables | enhancements | keys | legendary_enhancements | gear_and_equipments | hearts_of_the_chosen | lifestones | lifestone_shards | passive_abilities | primary_weapons | secondary_weapons | souls_chests | wrath_abilities | wrath_cores | wrath_shards

DEFAULT_ITEM_CLASSIFICATION = {
    "abyssal_armor_pieces": ItemClassification.useful,
    "artifacts": ItemClassification.progression,
    "consumables": ItemClassification.filler,
    "enhancements": ItemClassification.useful,
    "legendary_enhancements": ItemClassification.useful,
    "gear_and_equipments": ItemClassification.progression,
    "keys": ItemClassification.progression,
    "hearts_of_the_chosen": ItemClassification.progression,
    "lifestones": ItemClassification.useful,
    "lifestone_shards": ItemClassification.useful,
    "passive_abilities": ItemClassification.progression,
    "primary_weapons": ItemClassification.progression,
    "secondary_weapons": ItemClassification.useful,
    "souls_chests": ItemClassification.filler,
    "wrath_abilities": ItemClassification.useful,
    "wrath_cores": ItemClassification.useful,
    "wrath_shards": ItemClassification.useful
}

class DSItem(Item):

    game: str = "Darksiders Warmastered Edition"

def create_item_with_correct_classification(world: DSWorld, name: str) -> DSItem:

    match name:
        case name if name in abyssal_armor_pieces:
            classification = DEFAULT_ITEM_CLASSIFICATION["abyssal_armor_pieces"]
        case name if name in artifacts:
            classification = DEFAULT_ITEM_CLASSIFICATION["artifacts"]
        case name if name in enhancements:
            classification = DEFAULT_ITEM_CLASSIFICATION["enhancements"]
        case name if name in legendary_enhancements:
            classification = DEFAULT_ITEM_CLASSIFICATION["legendary_enhancements"]
        case name if name in keys:
            classification = DEFAULT_ITEM_CLASSIFICATION["keys"]
        case name if name in gear_and_equipments:
            classification = DEFAULT_ITEM_CLASSIFICATION["gear_and_equipments"]
        case name if name in hearts_of_the_chosen:
            classification = DEFAULT_ITEM_CLASSIFICATION["hearts_of_the_chosen"]
        case name if name in lifestones:
            classification = DEFAULT_ITEM_CLASSIFICATION["lifestones"]
        case name if name in lifestone_shards:
            classification = DEFAULT_ITEM_CLASSIFICATION["lifestone_shards"]
        case name if name in passive_abilities:
            classification = DEFAULT_ITEM_CLASSIFICATION["passive_abilities"]
        case name if name in primary_weapons:
            if name == "Progressive Chaoseater":
                classification = ItemClassification.useful
            else:
                classification = DEFAULT_ITEM_CLASSIFICATION["primary_weapons"]
        case name if name in secondary_weapons:
            if name == "Progressive Gauntlet":
                classification = ItemClassification.progression
            else:
                classification = DEFAULT_ITEM_CLASSIFICATION["secondary_weapons"]
        case name if name in souls_chests:
            classification = DEFAULT_ITEM_CLASSIFICATION["souls_chests"]
        case name if name in wrath_abilities:
            classification = DEFAULT_ITEM_CLASSIFICATION["wrath_abilities"]
        case name if name in wrath_cores:
            classification = DEFAULT_ITEM_CLASSIFICATION["wrath_cores"]
        case name if name in wrath_shards:
            classification = DEFAULT_ITEM_CLASSIFICATION["wrath_shards"]
        case _: 
            classification = ItemClassification.filler

    return DSItem(name, classification, ITEM_NAME_TO_ID[name], world.player)

def get_random_filler_item_name(world: DSWorld) -> str:

    return world.random.choice(list(consumables.keys() | souls_chests.keys()))

def create_all_items(world: DSWorld) -> None:

    itempool: list[Item] = []

    if world.options.abyssanity:
        for i in range(10):
            itempool.append(world.create_item("Abyssal Armor Piece"))

    if world.options.artisanity:
        for i in range(20):
            itempool.append(world.create_item("Soldier Artifact"))
        for i in range(6):
            itempool.append(world.create_item("Champion Artifact"))
        itempool.append(world.create_item("Overlord Artifact"))

    match world.options.enhansanity:
        case 1:
            for name, item_id in enhancements.items():
                itempool.append(world.create_item(name))
        case 2:
            for name, item_id in legendary_enhancements.items():
                itempool.append(world.create_item(name))
        case 3:
            for name, item_id in enhancements.items():
                itempool.append(world.create_item(name))
            for name, item_id in legendary_enhancements.items():
                itempool.append(world.create_item(name))

    for i in range(4):
        itempool.append(world.create_item("Beholder Key"))

    for name, item_id in gear_and_equipments.items():
        itempool.append(world.create_item(name))

    for i in range (4):
        itempool.append(world.create_item("Heart of the Chosen"))

    for i in range(world.options.lifestones):
        itempool.append(world.create_item("Lifestone"))

    if world.options.lifestones_shards > 0:
        starting_health = 1
        for i in range(10 - starting_health - world.options.lifestones):
            for i in range(4):
                itempool.append(world.create_item('Lifestone Shard'))

    for name, item_id in passive_abilities.items():
        itempool.append(world.create_item(name))

    for i in range(4):
        itempool.append(world.create_item('Progressive Chaoseater'))
    for i in range(7):
        itempool.append(world.create_item('Armageddon Blade Shards'))

    for i in range(4):
        itempool.append(world.create_item('Progressive Scythe'))

    itempool.append(world.create_item('Progressive Gauntlet'))
    for i in range(4):
        itempool.append(world.create_item('Progressive Gauntlet'))

    for name, item_id in wrath_abilities.items():
        itempool.append(world.create_item(name))

    for i in range(world.options.wrath_cores):
        itempool.append(world.create_item('Wrath Core'))

    if world.options.wrath_shards > 0:
        starting_wrath = 2
        for i in range(10 - starting_wrath - world.options.wrath_cores):
            for i in range(4):
                itempool.append(world.create_item('Wrath Shard'))
    
    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
    world.multiworld.itempool += itempool