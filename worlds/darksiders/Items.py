from __future__ import annotations

from typing import Optional, TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .World import DSWorld

abyssal_armor = {
    'Abyssal Armor Piece': 1, #armor/item_armorpiece
    'Abyssal armor': 2, #armor/item_abyssumarmor
}

artifacts = {
    'Soldier Artifact': 10, #items/artifact_pawn
    'Champion Artifact': 11, #items/artifact_general
    'Overlord Artifact': 12, #items/artifact_master
}

consumables = {
    'Empty Container': 20, #items/item_consumableslot
    'Life Essence': 21,
    'Greater Life Essence': 22,
    'Possession': 23,
    'Rage Essence': 24,
    'Greater Rage Essence': 25,
    'Undying': 26
}

enhancements = {
    'Bane' : 30, #weapon_enhancements/common_bane
    'Bloodthirst': 31, #weapon_enhancements/common_leech
    'Carnage': 32, #weapon_enhancements/common_ire
    'Combat Lore': 33, #weapon_enhancements/common_divination
    'Hellfire': 34, #weapon_enhancements/common_brimstone
    'Ravager': 35, #weapon_enhancements/common_desecration
    'Reaper': 36, #weapon_enhancements/common_reaper
    'Weapon Master': 37, #weapon_enhancements/common_transfixion
    'Wars Glory' : 40, #weapon_enhancements/legendary_warswrath
    'Strifes Offering' : 41, #weapon_enhancements/legendary_strifesprowess
    'Furys Embrace' : 42, #weapon_enhancements/legendary_furysmadness
    'Deaths Blessing' : 43, #weapon_enhancements/legendary_deathsblessing
}

keys = {
    'Beholder Key': 50 #items/item_dungeonkey
}

gear_and_equipments = {
    'Abyssal Chain' : 60, #gear_ghosthook/playergearghosthook
    'Crossblade': 61, #gear_crossblade/playergearcrossblade
    'Earthcaller': 62, #gear_horn/playergearhorn
    'Mask of Shadows': 63, #gear_eyeoflilith/playergeareyeoflilith
    'Mercy': 64, #weapon_strifesgun/strifes_gun
    'Voidwalker': 65 #gear_voidwalker/playergearvoidwalker
}

health = {
    'Lifestone': 70, #items/item_healthstone
    'Lifestone Shard': 71, #items/item_healthshard
}

hearts_of_the_chosen = {
    'Heart of the Chosen' : 80, #items/item_demonheart
}

passive_abilities = {
    'Block Counter': 90, #items/item_blockcounter
    'Chaos Form': 91, #item_havocform/item_havocform
    'Chronomancer': 92, #item_frenzy/item_frenzy
    'Ruin': 93, #items/item_ruinshard
    'Serpent Holes': 94, #items/item_teleportability
    'Shadowflight': 95, #gear_tempestcloak/playergeartempestcloak
    'Soul Bridge': 96, #items/item_soulbridgeshard
}

primary_weapons = {
    'Progressive Chaoseater': 100,
    'Chaoseater': 101, #sword/warsword
    'Armageddon Blade': 102, #items/item_armageddonsword
    'Armageddon Blade Shards': 103 #items/item_swordpiece
    #'Sword Key': 104, #ch_com/weapon_swordkey
}

secondary_weapons = {
    'Progressive Scythe': 110,
    'Harvester': 111, #harvester/harvester
    'Scythe': 112, #hellraiser/hellraiser
    'Progressive Gauntlet': 113,
    'Tremor Gauntlet': 114 #gauntlets/weapon_gauntlets
}

souls_chests = {
    'Currency': 150,
    'Health': 151,
    'Wrath': 152
}

wrath = {
    'Wrath Core': 120, #items/item_wrathstone
    'Wrath Shard': 121, #items/item_wrathshard
}

wrath_abilities = {
    'Affliction': 130, #wrath_affliction/wrath_affliction
    'Blade Geyser': 131, #wrath_bladegeyser/wrath_bladegeyser ???????
    'Immolation': 132, #wrath_immolation/wrath_immolation
    'Stoneskin': 133 #wrath_stoneskin/wrath_stoneskin
}

ITEM_NAME_TO_ID = abyssal_armor | artifacts | consumables | enhancements | gear_and_equipments | health | hearts_of_the_chosen | keys | passive_abilities | primary_weapons | secondary_weapons | souls_chests | wrath | wrath_abilities

DEFAULT_ITEM_CLASSIFICATION = {
    "abyssal_armor": ItemClassification.useful,
    "artifacts": ItemClassification.progression,
    "consumables": ItemClassification.filler,
    "enhancements": ItemClassification.useful,
    "gear_and_equipments": ItemClassification.progression,
    "health": ItemClassification.useful,
    "hearts_of_the_chosen": ItemClassification.progression,
    "keys": ItemClassification.progression,
    "passive_abilities": ItemClassification.progression,
    "primary_weapons": ItemClassification.progression,
    "secondary_weapons": ItemClassification.useful,
    "souls_chests": ItemClassification.filler,
    "wrath": ItemClassification.useful,
    "wrath_abilities": ItemClassification.useful,
}

class DSItem(Item):

    game: str = "Darksiders"

def create_item_with_correct_classification(world: DSWorld, name: str) -> DSItem:

    match name:
        case name if name in abyssal_armor:
            classification = DEFAULT_ITEM_CLASSIFICATION["abyssal_armor"]
        case name if name in artifacts:
            classification = DEFAULT_ITEM_CLASSIFICATION["artifacts"]
        case name if name in enhancements:
            classification = DEFAULT_ITEM_CLASSIFICATION["enhancements"]
        case name if name in keys:
            classification = DEFAULT_ITEM_CLASSIFICATION["keys"]
        case name if name in gear_and_equipments:
            classification = DEFAULT_ITEM_CLASSIFICATION["gear_and_equipments"]
        case name if name in health:
            classification = DEFAULT_ITEM_CLASSIFICATION["health"]
        case name if name in hearts_of_the_chosen:
            classification = DEFAULT_ITEM_CLASSIFICATION["hearts_of_the_chosen"]
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
        case name if name in wrath:
            classification = DEFAULT_ITEM_CLASSIFICATION["wrath"]
        case name if name in wrath_abilities:
            classification = DEFAULT_ITEM_CLASSIFICATION["wrath_abilities"]
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