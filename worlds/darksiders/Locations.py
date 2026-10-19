from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location
from rule_builder.rules import Has

from .Items import DSItem
from .Rules import CAN_BEAT_ABADDON, HAS_ABYSSAL_CHAIN, HAS_CHAOS_FORM, HAS_CROSSBLADE, HAS_GAUNTLET, HAS_MASK, HAS_RUIN, HAS_VOIDWALKER

if TYPE_CHECKING:
    from .World import DSWorld

abyssal_armor_pieces = {
    'Drowned Pass Abyssal Armor Piece': 1,
    'Hollows Abyssal Armor Piece': 2,
    'Scalding Gallow Abyssal Armor Piece Near Entrance': 3,
    'Scalding Gallow Abyssal Armor Piece Under Central Platform': 4,
    'Twilight Cathedral Abyssal Armor Piece': 5,
}

artifacts = {
    'Broken Stair Soldier Artifact Near Entrance': 30,
    #'Choking Grounds Access Cave Soldier Artifact',
    'Choking Grounds Soldier Artifact North of Vulgrim': 31,
    'Choking Grounds Soldier Artifact South in Sarcophagus': 32,
    'Crossroads Soldier Artifact in Subway Station': 33,
    'Drowned Pass Access Tunnel Champion Artifact': 34,
    'Drowned Pass Soldier Artifact Cave Under Waterfall': 35,
    'Drowned Pass Soldier Artifact Underwater Building': 36,
    'Dry Road Soldier Artifact': 37,
    'Dry Road Access Tunnel Soldier Artifact': 38,
    'The Hollows Champion Artifact in Pipe Leading North': 39,
    'The Hollows Soldier Artifact Underwater': 40,
    'The Hollows Soldier Artifact South of Platforms': 41,
    #'The Library Life Chest Entrance': 15,
    'Twilight Cathedral Champion Artifact North Wing': 42,
    'Twilight Cathedral Soldier Artifact South Wing': 43,
    'Twilight Cathedral Soldier Artifact Bridge Room': 44,
}

"""
boss_defeated = {
    'Abaddon The Destroyer': 70,
    'Abyssal Gladiator': 71,
    'Ash Titan': 72,
    'Broodmother': 73,
    'Griever': 74,
    'Jailer': 75,
    'Phantom General': 76,
    'Shadow War': 77,
    'Silitha': 78,
    'Straga': 79,
    'Stygian': 80,
    'Three Guardians': 81,
    'Tiamat': 82,
    'Ulthane': 83,
    'Uriel First Encounter': 84,
    'Uriel Second Encounter': 85,
    'Wicked K': 85,
}
"""

chained_cubes = {
    'The Hollows Chained Cube': 90,
    'Twilight Cathedral Chained Cube': 91,
}

chests = {
    'Anvil Ford Challenge Currency Chest Lower Platform': 100,
    'Anvil Ford Challenge Life Chest Inside Large Crystal': 101,
    'Anvil Ford Challenge Life Chest Inside Small Crystals': 102,
    'Anvil Ford Challenge Life Chest after Toss': 103,
    'Anvil Ford Challenge Life Chest before Toss': 104,
    'Anvil Ford Challenge Life Chest Elevator Shaft': 105,
    'Anvil Ford Challenge Life Chest East Uriel Arena': 106,
    'Anvil Ford Challenge Life Chest West Uriel Arena': 107,
    'Anvil Ford Challenge Wrath Chest after Demonic Growth': 108,
    #'Anvil Ford Challenge Wrath Chest after Demonic Growth': 1031,
    'The Ashlands Currency Chest up the Ramp': 109,
    'The Ashlands Access Tunnel Currency Chest by Three Goremaws': 110,
    'The Ashlands Access Tunnel Life Blocked by Ice': 111,
    'The Ashlands Access Tunnel Rare Chest by Goremaw': 112,
    'Broken Stair Access Tunnel Currency Chest': 113,
    'Broken Stair Beholder Key Chest': 114,
    'Broken Stair Currency Chest SE Down Stairs': 115,
    'Broken Stair Currency Chest SW 2nd Floor': 116,
    'Broken Stair Currency Chest after Geysers': 117,
    'Broken Stair Life Chest East Submerged Tunnel': 118,
    'Broken Stair Life Chest after Geysers': 119,
    'Choking Grounds Currency Chest North of Cemetery': 120,
    'Choking Grounds Currency Chest NE South of the ramp': 121,
    'Choking Grounds Currency Chest 1st Floor Left of Tormented Gate': 122,
    'Choking Grounds Life Chest in NE Building': 123,
    'Choking Grounds Life Chest North of Cemetery': 124,
    'Choking Grounds Wrath Chest 2nd Floor Left of Tormented Gate': 125,
    'Choking Grounds Secret Chest Destroy Gravestones with Crosses': 126,
    'Choking Grounds Access Cave Currency Chest in Lava Pool': 127,
    'Crossroads Currency Chest Down Stairs': 128,
    'Crossroads Currency Chest South Crater': 129,
    'Crossroads Currency Chest in Subway Station': 130,
    'Crossroads Life Chest Behind Gholen West': 131,
    'Crossroads Life Chest Behind Gholen North': 132,
    'Crossroads Life Chest NE Crater': 133,
    'Crossroads Rare Chest Blocked by Ice': 134,
    'Crossroads Secret Chest Destroy Fire Hydrants': 135,
    'Drowned Pass Currency Chest after Submerged Cave': 136,
    'Drowned Pass Currency Chest Building Semi Submerged': 137,
    'Drowned Pass Life Chest after Crystal Switch Platform': 138,
    'Drowned Pass Wrath Chest Blocked by Ice': 139,
    'Drowned Pass Access Tunnel Currency Chest East Nook': 140,
    'Dry Road Currency Chest South of Vulgrim': 141,
    'Dry Road Life Chest East of Artifact': 142,
    'Dry Road Access Tunnel Currency Chest North of Chronosphere': 143,
    'Dry Road Access Tunnel Currency Chest South of Entrance': 144,
    'Dry Road Access Tunnel Currency Chest Up the Stairs': 145,
    'The Hollows Beholder Key Chest after Chained Cube': 146,
    'The Hollows Beholder Key Chest in Current': 147,
    'The Hollows Beholder Key Chest inside Floor Hole': 148,
    'The Hollows Currency Chest after Submerged Passage': 149,
    'The Hollows Currency Chest between Ice Blocks': 150,
    'The Hollows Currency Chest SE of Locust Room': 151,
    'The Hollows Currency Chest South of Clocktower': 152,
    'The Hollows Currency Chest SW of Gas': 153,
    'The Hollows Currency Chest Top Balcony': 154,
    'The Hollows Currency Chest Top of Stairwell': 155,
    'The Hollows Currency Chest under Goremaw': 156,
    'The Hollows Hoardseeker Chest SW of Grappleclaws Room': 157,
    'The Hollows Life Chest after Chained Cube': 158,
    'The Hollows Life Chest after Water-Filled Hallway': 159,
    'The Hollows Life Chest before Boss Room': 160,
    'The Hollows Life Chest behind Train Cars': 161,
    'The Hollows Life Chest in Griever Tunnel': 162,
    'The Hollows Life Chest North of Locust Room': 163,
    'The Hollows Life Chest South Wall Nook': 164,
    'The Hollows Life Chest West Corridor': 165,
    'The Hollows Life Chest West of Grappleclaws Room': 166,
    'The Hollows Map Chest at Surface of Flooded Room': 167,
    'The Hollows Rare Chest over Submerged Passage': 168,
    'The Hollows Wrath Chest after Submerged Passage': 169,
    'The Hollows Wrath Chest after Water-Filled Hallway': 170,
    'The Hollows Wrath Chest over Flooded Room': 171,
    'The Hollows Access Tunnel Currency Chest Dead End': 172,
    'The Hollows Access Tunnel Currency Chest Stream Walkthrough': 173,
    #'The Crossroads Secret Chest Destroy Fire Hydrants': 15,
    #'The Crossroads Secret Chest Destroy Fire Hydrants': 15,
    'Library Currency Chest South of Fleshburners': 174,
    #'The Library Life Chest Entrance': 15,
    'Library Life Chest Entrance': 175,
    'Library Life Chest Submarine Cave': 176,
    'Library Life Chest North': 177,
    'Scalding Gallow Currency Chest 2nd Floor': 178,
    'Scalding Gallow Currency Chest West Near Vulgrim': 179,
    'Scalding Gallow Wrath Chest Above Vulgrim': 180,
    #'Seraphim Hotel Life Chest 1': 1029,
    #'Seraphim Hotel Life Chest 2': 1030,
    'Serpent Hole to Anvil\'s Ford Chest': 181,
    'Serpent Hole to Dry Road Chest': 182,
    'Serpent Hole to Twilight Cathedral Chest': 183,
    'Twilight Cathedral Beholder Key Chest South Wing': 184,
    'Twilight Cathedral Beholder Key Chest Three Blades East Path': 185,
    'Twilight Cathedral Currency Chest Below Abyssal Armor Chest': 186,
    'Twilight Cathedral Currency Chest East of Elevated Platforms': 187,
    'Twilight Cathedral Currency Chest Exterior Blocked by Ice': 188,
    'Twilight Cathedral Currency Chest NE of Exterior': 189,
    'Twilight Cathedral Currency Chest North after Lava Fall': 190,
    'Twilight Cathedral Currency Chest Rot Mauler Room': 191,
    'Twilight Cathedral Currency Chest South after Lava Fall': 192,
    'Twilight Cathedral Currency Chest South of Exterior': 193,
    'Twilight Cathedral Currency Chest South Wing Main Gallery': 194,
    'Twilight Cathedral Currency Chest South Wing Conscript Room': 195,
    'Twilight Cathedral Hoardseeker Chest South Wing': 196,
    'Twilight Cathedral Life Chest after The Jailer': 197,
    'Twilight Cathedral Life Chest before Platform Room': 198,
    'Twilight Cathedral Life Chest North of Three Statues': 199,
    'Twilight Cathedral Life Chest North Wing Basement': 200,
    'Twilight Cathedral Life Chest South Wing Conscript Room': 201,
    'Twilight Cathedral Life Chest South Wing First Room': 202,
    'Twilight Cathedral Life Chest North Wing Under Crystal': 203,
    'Twilight Cathedral Map Chest South Wing': 204,
    'Twilight Cathedral Rare Chest South Wing': 205,
    'Twilight Cathedral Secret Chest Light 8 Torches': 206,
    'Twilight Cathedral Wrath Chest before Platform Room': 207,
    'Twilight Cathedral Wrath Chest Below Abyssal Armor Chest': 208,
    'Twilight Cathedral Wrath Chest Three Blades East Path': 209,
}

LOCATION_NAME_TO_ID = abyssal_armor_pieces | artifacts | chained_cubes | chests

class DSLocation(Location):

    game = "Darksiders Warmastered Edition"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:

    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def create_all_locations(world: DSWorld) -> None:

    create_regular_locations(world)
    create_events(world)

def create_regular_locations(world: DSWorld) -> None:

    anvil_ford = world.get_region("Anvil's Ford")
    anvil_ford_access_tunnel = world.get_region("Anvil's Ford Access Tunnel")
    anvil_ford_challenge_area = world.get_region("Anvil's Ford Challenge Area")
    ashlands_1 = world.get_region("The Ashlands 1")
    ashlands_2 = world.get_region("The Ashlands 2")
    ashlands_access_tunnel_1 = world.get_region("The Ashlands Access Tunnel 1")
    ashlands_access_tunnel_2 = world.get_region("The Ashlands Access Tunnel 2")
    black_throne_1 = world.get_region("Black Throne 1")
    black_throne_boss_room = world.get_region("Black Throne Boss Room")
    broken_stair = world.get_region("The Broken Stair")
    choking_grounds = world.get_region("The Choking Grounds")
    crossroads = world.get_region("The Crossroads")
    drowned_pass = world.get_region("Drowned Pass")
    drowned_pass_access_tunnel = world.get_region("Drowned Pass Access Tunnel")
    dry_road = world.get_region("The Dry Road")
    dry_road_access_tunnel_1 = world.get_region("The Dry Road Access Tunnel 1")
    dry_road_access_tunnel_2 = world.get_region("The Dry Road Access Tunnel 2")
    eden = world.get_region("Eden")
    hollows_1 = world.get_region("The Hollows 1")
    hollows_2 = world.get_region("The Hollows 2")
    hollows_3 = world.get_region("The Hollows 3")
    hollows_4 = world.get_region("The Hollows 4")
    hollows_5 = world.get_region("The Hollows 5")
    hollows_6 = world.get_region("The Hollows 6")
    hollows_7 = world.get_region("The Hollows 7")
    hollows_8 = world.get_region("The Hollows 8")
    hollows_9 = world.get_region("The Hollows 9")
    hollows_10 = world.get_region("The Hollows 10")
    hollows_boss_room = world.get_region("The Hollows Boss Room")
    hollows_access_tunnel = world.get_region("The Hollows Access Tunnel")
    iron_canopy_1 = world.get_region("Iron Canopy 1")
    leviathan_drift = world.get_region("Leviathan's Drift")
    menu = world.get_region("Menu")
    scalding_gallow = world.get_region("Scalding Gallow")
    #seraphim_hotel = world.get_region("Seraphim Hotel")
    silitha_loom = world.get_region("Silitha's Loom")
    serpent_holes = world.get_region("Serpent Holes")
    sh_to_anvil_ford = world.get_region("Serpent Hole to Anvil's Ford")
    sh_to_dry_road = world.get_region("Serpent Hole to Dry Road")
    sh_to_twilight_cathedral = world.get_region("Serpent Hole to Twilight Cathedral")
    tree_of_knowledge = world.get_region("Tree of Knowledge")
    twilight_cathedral_exterior = world.get_region("Twilight Cathedral Exterior")
    twilight_cathedral_1 = world.get_region("Twilight Cathedral 1")
    twilight_cathedral_2 = world.get_region("Twilight Cathedral 2")
    twilight_cathedral_3 = world.get_region("Twilight Cathedral 3")
    twilight_cathedral_boss_room = world.get_region("Twilight Cathedral Boss Room")
    vulgrim_shop = world.get_region("Vulgrim's Shop")

    anvil_ford_challenge_area_locations = get_location_names_with_ids([
        'Anvil Ford Challenge Currency Chest Lower Platform',
        'Anvil Ford Challenge Life Chest Inside Large Crystal',
        'Anvil Ford Challenge Life Chest Inside Small Crystals',
        'Anvil Ford Challenge Life Chest after Toss',
        'Anvil Ford Challenge Life Chest before Toss',
        'Anvil Ford Challenge Life Chest Elevator Shaft',
        'Anvil Ford Challenge Life Chest East Uriel Arena',
        'Anvil Ford Challenge Life Chest West Uriel Arena',
        'Anvil Ford Challenge Wrath Chest after Demonic Growth',
    ])
    anvil_ford_challenge_area.add_locations(anvil_ford_challenge_area_locations, DSLocation)

    ashlands_2_locations = get_location_names_with_ids([
        'The Ashlands Currency Chest up the Ramp',
    ])
    ashlands_2.add_locations(ashlands_2_locations, DSLocation)

    ashlands_access_tunnel_1_locations = get_location_names_with_ids([
        'The Ashlands Access Tunnel Currency Chest by Three Goremaws',
        'The Ashlands Access Tunnel Rare Chest by Goremaw',
    ])
    ashlands_access_tunnel_1.add_locations(ashlands_access_tunnel_1_locations, DSLocation)

    ashlands_access_tunnel_2_locations = get_location_names_with_ids([
        'The Ashlands Access Tunnel Life Blocked by Ice',
    ])
    ashlands_access_tunnel_2.add_locations(ashlands_access_tunnel_2_locations, DSLocation)

    broken_stair_locations = get_location_names_with_ids([
        'Broken Stair Soldier Artifact Near Entrance',
        'Broken Stair Access Tunnel Currency Chest',
        'Broken Stair Beholder Key Chest',
        'Broken Stair Currency Chest SE Down Stairs',
        'Broken Stair Currency Chest SW 2nd Floor',
        'Broken Stair Currency Chest after Geysers',
        'Broken Stair Life Chest East Submerged Tunnel',
        'Broken Stair Life Chest after Geysers',
    ])
    broken_stair.add_locations(broken_stair_locations, DSLocation)

    choking_grounds_locations = get_location_names_with_ids([
        'Choking Grounds Soldier Artifact North of Vulgrim',
        'Choking Grounds Soldier Artifact South in Sarcophagus',
        'Choking Grounds Currency Chest North of Cemetery',
        'Choking Grounds Currency Chest NE South of the ramp',
        'Choking Grounds Currency Chest 1st Floor Left of Tormented Gate',
        'Choking Grounds Life Chest in NE Building',
        'Choking Grounds Life Chest North of Cemetery',
        'Choking Grounds Wrath Chest 2nd Floor Left of Tormented Gate',
        'Choking Grounds Secret Chest Destroy Gravestones with Crosses',
        'Choking Grounds Access Cave Currency Chest in Lava Pool',
    ])
    choking_grounds.add_locations(choking_grounds_locations, DSLocation)

    crossroads_locations = get_location_names_with_ids([
         'Crossroads Currency Chest Down Stairs',
         'Crossroads Currency Chest South Crater',
         'Crossroads Currency Chest in Subway Station',
         'Crossroads Life Chest Behind Gholen West',
         'Crossroads Life Chest Behind Gholen North',
         'Crossroads Rare Chest Blocked by Ice',
         'Crossroads Life Chest NE Crater',
         'Crossroads Secret Chest Destroy Fire Hydrants',
         'Library Currency Chest South of Fleshburners',
         'Library Life Chest Entrance',
         'Library Life Chest Submarine Cave',
         'Library Life Chest North',
    ])
    crossroads.add_locations(crossroads_locations, DSLocation)

    drowned_pass_locations = get_location_names_with_ids([
        'Drowned Pass Abyssal Armor Piece',
        'Drowned Pass Soldier Artifact Cave Under Waterfall',
        'Drowned Pass Soldier Artifact Underwater Building',
        'Drowned Pass Currency Chest after Submerged Cave',
        'Drowned Pass Currency Chest Building Semi Submerged',
        'Drowned Pass Life Chest after Crystal Switch Platform',
        'Drowned Pass Wrath Chest Blocked by Ice',
    ])
    drowned_pass.add_locations(drowned_pass_locations, DSLocation)

    dry_road_locations = get_location_names_with_ids([
        'Dry Road Currency Chest South of Vulgrim',
        'Dry Road Life Chest East of Artifact',
        'Dry Road Soldier Artifact'
    ])
    dry_road.add_locations(dry_road_locations, DSLocation)

    drowned_pass_access_tunnel_locations = get_location_names_with_ids([
        'Drowned Pass Access Tunnel Champion Artifact',
        'Drowned Pass Access Tunnel Currency Chest East Nook',
    ])
    drowned_pass_access_tunnel.add_locations(drowned_pass_access_tunnel_locations, DSLocation)

    dry_road_access_tunnel_1_locations = get_location_names_with_ids([
        'Dry Road Access Tunnel Currency Chest South of Entrance',
    ])
    dry_road_access_tunnel_1.add_locations(dry_road_access_tunnel_1_locations, DSLocation)

    dry_road_access_tunnel_2_locations = get_location_names_with_ids([
        'Dry Road Access Tunnel Currency Chest North of Chronosphere',
        'Dry Road Access Tunnel Currency Chest Up the Stairs',
        'Dry Road Access Tunnel Soldier Artifact'
    ])
    dry_road_access_tunnel_2.add_locations(dry_road_access_tunnel_2_locations, DSLocation)

    hollows_1_locations = get_location_names_with_ids([
        'The Hollows Currency Chest Top Balcony',
        'The Hollows Currency Chest South of Clocktower',
        'The Hollows Currency Chest Top of Stairwell',
        'The Hollows Life Chest West Corridor',
    ])
    hollows_1.add_locations(hollows_1_locations, DSLocation)

    hollows_2_locations = get_location_names_with_ids([
        'Hollows Abyssal Armor Piece',
        'The Hollows Beholder Key Chest in Current',
        'The Hollows Currency Chest after Submerged Passage',
        'The Hollows Currency Chest SW of Gas',
        'The Hollows Life Chest South Wall Nook',
        'The Hollows Rare Chest over Submerged Passage',
        'The Hollows Wrath Chest after Submerged Passage',
    ])
    hollows_2.add_locations(hollows_2_locations, DSLocation)

    hollows_3_locations = get_location_names_with_ids([
        'The Hollows Chained Cube',
        'The Hollows Beholder Key Chest after Chained Cube',
        'The Hollows Life Chest after Chained Cube'
    ])
    hollows_3.add_locations(hollows_3_locations, DSLocation)

    hollows_4_locations = get_location_names_with_ids([
        'The Hollows Life Chest after Water-Filled Hallway',
        'The Hollows Map Chest at Surface of Flooded Room',
        'The Hollows Wrath Chest after Water-Filled Hallway',
        'The Hollows Soldier Artifact South of Platforms',
    ])
    hollows_4.add_locations(hollows_4_locations, DSLocation)

    hollows_5_locations = get_location_names_with_ids([
        'The Hollows Life Chest behind Train Cars'
    ])
    hollows_5.add_locations(hollows_5_locations, DSLocation)

    hollows_6_locations = get_location_names_with_ids([
        'The Hollows Currency Chest SE of Locust Room',
        'The Hollows Life Chest North of Locust Room',
    ])
    hollows_6.add_locations(hollows_6_locations, DSLocation)

    hollows_7_locations = get_location_names_with_ids([
        'The Hollows Currency Chest between Ice Blocks',
    ])
    hollows_7.add_locations(hollows_7_locations, DSLocation)

    hollows_8_locations = get_location_names_with_ids([
        'The Hollows Champion Artifact in Pipe Leading North',
        'The Hollows Beholder Key Chest inside Floor Hole',
    ])
    hollows_8.add_locations(hollows_8_locations, DSLocation)

    hollows_9_locations = get_location_names_with_ids([
        'The Hollows Life Chest in Griever Tunnel',
        'The Hollows Currency Chest under Goremaw',
        'The Hollows Hoardseeker Chest SW of Grappleclaws Room',
        'The Hollows Life Chest West of Grappleclaws Room',
    ])
    hollows_9.add_locations(hollows_9_locations, DSLocation)

    hollows_10_locations = get_location_names_with_ids([
        'The Hollows Life Chest before Boss Room',
        'The Hollows Wrath Chest over Flooded Room',
    ])
    hollows_10.add_locations(hollows_10_locations, DSLocation)

    hollows_access_tunnel_locations = get_location_names_with_ids([
        'The Hollows Access Tunnel Currency Chest Dead End',
        'The Hollows Access Tunnel Currency Chest Stream Walkthrough',
    ])
    hollows_access_tunnel.add_locations(hollows_access_tunnel_locations, DSLocation)

    scalding_gallow_locations = get_location_names_with_ids([
        'Scalding Gallow Abyssal Armor Piece Near Entrance',
        'Scalding Gallow Abyssal Armor Piece Under Central Platform',
        'Scalding Gallow Currency Chest 2nd Floor',
        'Scalding Gallow Currency Chest West Near Vulgrim',
        'Scalding Gallow Wrath Chest Above Vulgrim',
    ])
    scalding_gallow.add_locations(scalding_gallow_locations, DSLocation)

    #seraphim_hotel_locations = get_location_names_with_ids([
    #    'Seraphim Hotel Life Chest 1',
    #    'Seraphim Hotel Life Chest 2'
    #])
    #seraphim_hotel.add_locations(seraphim_hotel_locations, DSLocation)

    sh_to_anvil_ford_locations = get_location_names_with_ids([
    'Serpent Hole to Anvil\'s Ford Chest',
    ])
    sh_to_anvil_ford.add_locations(sh_to_anvil_ford_locations, DSLocation)

    sh_to_dry_road_locations = get_location_names_with_ids([
    'Serpent Hole to Dry Road Chest',
    ])
    sh_to_dry_road.add_locations(sh_to_dry_road_locations, DSLocation)

    sh_to_twilight_cathedral_locations = get_location_names_with_ids([
    'Serpent Hole to Twilight Cathedral Chest',
    ])
    sh_to_twilight_cathedral.add_locations(sh_to_twilight_cathedral_locations, DSLocation)

    twilight_cathedral_exterior_locations = get_location_names_with_ids([
        'Twilight Cathedral Currency Chest Exterior Blocked by Ice',
        'Twilight Cathedral Currency Chest NE of Exterior',
        'Twilight Cathedral Currency Chest South of Exterior'
    ])
    twilight_cathedral_exterior.add_locations(twilight_cathedral_exterior_locations, DSLocation)

    twilight_cathedral_1_locations = get_location_names_with_ids([
        'Twilight Cathedral Soldier Artifact South Wing',
        'Twilight Cathedral Currency Chest South Wing Main Gallery',
        'Twilight Cathedral Life Chest South Wing First Room',
        'Twilight Cathedral Rare Chest South Wing',
        'Twilight Cathedral Beholder Key Chest South Wing',
        'Twilight Cathedral Hoardseeker Chest South Wing',
        'Twilight Cathedral Map Chest South Wing'
    ])
    twilight_cathedral_1.add_locations(twilight_cathedral_1_locations, DSLocation)

    twilight_cathedral_2_locations = get_location_names_with_ids([
        'Twilight Cathedral Chained Cube',
        'Twilight Cathedral Champion Artifact North Wing',
        'Twilight Cathedral Currency Chest South Wing Conscript Room',
        'Twilight Cathedral Life Chest North Wing Basement',
        'Twilight Cathedral Life Chest North Wing Under Crystal',
        'Twilight Cathedral Life Chest South Wing Conscript Room',
    ])
    twilight_cathedral_2.add_locations(twilight_cathedral_2_locations, DSLocation)

    twilight_cathedral_3_locations = get_location_names_with_ids([
        'Twilight Cathedral Abyssal Armor Piece',
        'Twilight Cathedral Soldier Artifact Bridge Room',
        'Twilight Cathedral Beholder Key Chest Three Blades East Path',
        'Twilight Cathedral Currency Chest Below Abyssal Armor Chest',
        'Twilight Cathedral Currency Chest East of Elevated Platforms',
        'Twilight Cathedral Currency Chest North after Lava Fall',
        'Twilight Cathedral Currency Chest Rot Mauler Room',
        'Twilight Cathedral Currency Chest South after Lava Fall',
        'Twilight Cathedral Life Chest after The Jailer',
        'Twilight Cathedral Life Chest before Platform Room',
        'Twilight Cathedral Life Chest North of Three Statues',
        'Twilight Cathedral Wrath Chest before Platform Room',
        'Twilight Cathedral Wrath Chest Below Abyssal Armor Chest',
        'Twilight Cathedral Wrath Chest Three Blades East Path',
        'Twilight Cathedral Secret Chest Light 8 Torches'
    ])
    twilight_cathedral_3.add_locations(twilight_cathedral_3_locations, DSLocation)

def create_events(world: DSWorld) -> None:

    anvil_ford = world.get_region("Anvil's Ford")
    anvil_ford_access_tunnel = world.get_region("Anvil's Ford Access Tunnel")
    anvil_ford_challenge_area = world.get_region("Anvil's Ford Challenge Area")
    ashlands_1 = world.get_region("The Ashlands 1")
    ashlands_2 = world.get_region("The Ashlands 2")
    ashlands_access_tunnel_1 = world.get_region("The Ashlands Access Tunnel 1")
    ashlands_access_tunnel_2 = world.get_region("The Ashlands Access Tunnel 2")
    black_throne_1 = world.get_region("Black Throne 1")
    black_throne_boss_room = world.get_region("Black Throne Boss Room")
    broken_stair = world.get_region("The Broken Stair")
    choking_grounds = world.get_region("The Choking Grounds")
    crossroads = world.get_region("The Crossroads")
    drowned_pass = world.get_region("Drowned Pass")
    drowned_pass_access_tunnel = world.get_region("Drowned Pass Access Tunnel")
    dry_road = world.get_region("The Dry Road")
    dry_road_access_tunnel_1 = world.get_region("The Dry Road Access Tunnel 1")
    dry_road_access_tunnel_2 = world.get_region("The Dry Road Access Tunnel 2")
    eden = world.get_region("Eden")
    hollows_1 = world.get_region("The Hollows 1")
    hollows_2 = world.get_region("The Hollows 2")
    hollows_3 = world.get_region("The Hollows 3")
    hollows_4 = world.get_region("The Hollows 4")
    hollows_5 = world.get_region("The Hollows 5")
    hollows_6 = world.get_region("The Hollows 6")
    hollows_7 = world.get_region("The Hollows 7")
    hollows_8 = world.get_region("The Hollows 8")
    hollows_9 = world.get_region("The Hollows 9")
    hollows_10 = world.get_region("The Hollows 10")
    hollows_boss_room = world.get_region("The Hollows Boss Room")
    hollows_access_tunnel = world.get_region("The Hollows Access Tunnel")
    iron_canopy_1 = world.get_region("Iron Canopy 1")
    leviathan_drift = world.get_region("Leviathan's Drift")
    menu = world.get_region("Menu")
    scalding_gallow = world.get_region("Scalding Gallow")
    #seraphim_hotel = world.get_region("Seraphim Hotel")
    silitha_loom = world.get_region("Silitha's Loom")
    serpent_holes = world.get_region("Serpent Holes")
    sh_to_anvil_ford = world.get_region("Serpent Hole to Anvil's Ford")
    sh_to_dry_road = world.get_region("Serpent Hole to Dry Road")
    sh_to_twilight_cathedral = world.get_region("Serpent Hole to Twilight Cathedral")
    tree_of_knowledge = world.get_region("Tree of Knowledge")
    twilight_cathedral_exterior = world.get_region("Twilight Cathedral Exterior")
    twilight_cathedral_1 = world.get_region("Twilight Cathedral 1")
    twilight_cathedral_2 = world.get_region("Twilight Cathedral 2")
    twilight_cathedral_3 = world.get_region("Twilight Cathedral 3")
    twilight_cathedral_boss_room = world.get_region("Twilight Cathedral Boss Room")
    vulgrim_shop = world.get_region("Vulgrim's Shop")

    anvil_ford.add_event(location_name = "Ulthane defeated", rule = HAS_CHAOS_FORM, location_type = DSLocation)
    anvil_ford_challenge_area.add_event(location_name = "Ulthane outscored", rule = HAS_CHAOS_FORM, location_type = DSLocation)
    anvil_ford_challenge_area.add_event(location_name = "Uriel 1 defeated", rule = HAS_CROSSBLADE, location_type = DSLocation)
    black_throne_boss_room.add_event(location_name = "Stygian defeated", item_name = "Heart of the Chosen", rule = HAS_RUIN, location_type = DSLocation)
    black_throne_boss_room.add_event(location_name = "Stygian Item Reward", rule = HAS_RUIN, location_type = DSLocation)
    dry_road.add_event(location_name = "Uriel 2 defeated", rule = Has("Armageddon Blade Shards", count = 1), location_type = DSLocation)
    eden.add_event(location_name = "Shadow War defeated", rule = HAS_MASK, location_type = DSLocation)
    hollows_boss_room.add_event(location_name = "The Griever defeated", item_name = "Heart of the Chosen", rule = HAS_GAUNTLET, location_type = DSLocation)
    hollows_boss_room.add_event(location_name = "The Griever Item Reward", rule = HAS_GAUNTLET, location_type = DSLocation)
    leviathan_drift.add_event(location_name = "Abaddon The Destroyer defeated", item_name = "Victory", rule = CAN_BEAT_ABADDON, location_type = DSLocation, item_type = DSItem)
    leviathan_drift.add_event(location_name = "Straga defeated", item_name = "Straga Defeated", rule = HAS_VOIDWALKER, location_type = DSLocation)
    leviathan_drift.add_event(location_name = "Straga Item Reward", rule = HAS_VOIDWALKER, location_type = DSLocation)
    scalding_gallow.add_event(location_name = "Phantom General defeated", location_type = DSLocation)
    scalding_gallow.add_event(location_name = "Samael's first Reward", location_type = DSLocation)
    scalding_gallow.add_event(location_name = "Trade first Heart of the Chosen", rule = Has("Heart of the Chosen", count = 1), location_type = DSLocation)
    scalding_gallow.add_event(location_name = "Trade second Heart of the Chosen", rule = Has("Heart of the Chosen", count = 2), location_type = DSLocation)
    scalding_gallow.add_event(location_name = "Trade third Heart of the Chosen", rule = Has("Heart of the Chosen", count = 3), location_type = DSLocation)
    scalding_gallow.add_event(location_name = "Trade fourth Heart of the Chosen", rule = Has("Heart of the Chosen", count = 4), location_type = DSLocation)
    silitha_loom.add_event(location_name = "Silitha defeated", item_name = "Heart of the Chosen", rule = HAS_ABYSSAL_CHAIN, location_type = DSLocation)
    silitha_loom.add_event(location_name = "Silitha Item Reward", rule = HAS_ABYSSAL_CHAIN, location_type = DSLocation)
    twilight_cathedral_2.add_event(location_name = "The Jailer defeated", location_type = DSLocation)
    twilight_cathedral_boss_room.add_event(location_name = "Tiamat defeated", item_name = "Heart of the Chosen", rule = HAS_CROSSBLADE, location_type = DSLocation)
    twilight_cathedral_boss_room.add_event(location_name = "Tiamat Item Reward", rule = HAS_CROSSBLADE, location_type = DSLocation)