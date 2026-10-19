from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from .Items import DSItem
from .Rules import CAN_BEAT_ABADDON, HAS_CHAOS_FORM, HAS_CROSSBLADE, HAS_GAUNTLET

if TYPE_CHECKING:
    from .World import DSWorld

abyssal_armor_pieces = {
    'Drowned Pass Abyssal Armor Piece': 1,
    'Hollows Abyssal Armor Piece': 1,
    'Scalding Gallow Abyssal Armor Piece Near Entrance': 1,
    'Scalding Gallow Abyssal Armor Piece Under Central Platform': 1,
    'Twilight Cathedral Abyssal Armor Piece': 1,
}

artifacts = {
    'Broken Stair Soldier Artifact Near Entrance': 30,
    #'Choking Grounds Access Cave Soldier Artifact',
    'Choking Grounds Soldier Artifact North of Vulgrim': 31,
    'Choking Grounds Soldier Artifact South in Sarcophagus': 32,
    'Crossroads Soldier Artifact in Subway Station': 33,
    'Drowned Pass Access Tunnel Champion Artifact': 15,
    'Drowned Pass Soldier Artifact Cave Under Waterfall': 15,
    'Drowned Pass Soldier Artifact Underwater Building': 15,
    'Dry Road Soldier Artifact': 15,
    'Dry Road Access Tunnel Soldier Artifact': 15,
    'The Hollows Champion Artifact in Pipe Leading North': 30,
    'The Hollows Soldier Artifact Underwater': 30,
    'The Hollows Soldier Artifact South of Platforms': 30,
    #'The Library Life Chest Entrance': 15,
    'Twilight Cathedral Champion Artifact North Wing': 15,
    'Twilight Cathedral Soldier Artifact South Wing': 15,
    'Twilight Cathedral Soldier Artifact Bridge Room': 15,
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
    'Twilight Cathedral Chained Cube': 90,
}

chests = {
    'Anvil Ford Challenge Currency Chest Lower Platform': 1031,
    'Anvil Ford Challenge Life Chest Inside Large Crystal': 1031,
    'Anvil Ford Challenge Life Chest Inside Small Crystals': 1031,
    'Anvil Ford Challenge Life Chest after Toss': 1031,
    'Anvil Ford Challenge Life Chest before Toss': 1031,
    'Anvil Ford Challenge Life Chest Elevator Shaft': 1031,
    'Anvil Ford Challenge Life Chest East Uriel Arena': 1031,
    'Anvil Ford Challenge Life Chest West Uriel Arena': 1031,
    'Anvil Ford Challenge Wrath Chest after Demonic Growth': 1031,
    #'Anvil Ford Challenge Wrath Chest after Demonic Growth': 1031,
    'The Ashlands Currency Chest up the Ramp': 1020,
    'The Ashlands Access Tunnel Currency Chest by Three Goremaws': 1020,
    'The Ashlands Access Tunnel Life Blocked by Ice': 1020,
    'The Ashlands Access Tunnel Rare Chest by Goremaw': 1020,
    'Broken Stair Access Tunnel Currency Chest': 1001,
    'Broken Stair Beholder Key Chest': 1002,
    'Broken Stair Currency Chest SE Down Stairs': 1003,
    'Broken Stair Currency Chest SW 2nd Floor': 1004,
    'Broken Stair Currency Chest after Geysers': 1005,
    'Broken Stair Life Chest East Submerged Tunnel': 1006,
    'Broken Stair Life Chest after Geysers': 1007,
    'Choking Grounds Currency Chest North of Cemetery': 1008,
    'Choking Grounds Currency Chest NE South of the ramp': 1009,
    'Choking Grounds Currency Chest 1st Floor Left of Tormented Gate': 1010,
    'Choking Grounds Life Chest in NE Building': 15,
    'Choking Grounds Life Chest North of Cemetery': 1011,
    'Choking Grounds Wrath Chest 2nd Floor Left of Tormented Gate': 1012,
    'Choking Grounds Secret Chest Destroy Gravestones with Crosses': 1013,
    'Choking Grounds Access Cave Currency Chest in Lava Pool': 1014,
    'Crossroads Currency Chest Down Stairs': 1015,
    'Crossroads Currency Chest South Crater': 1016,
    'Crossroads Currency Chest in Subway Station': 1017,
    'Crossroads Life Chest Behind Gholen West': 1018,
    'Crossroads Life Chest Behind Gholen North': 1019,
    'Crossroads Life Chest NE Crater': 1020,
    'Crossroads Rare Chest Blocked by Ice': 1020,
    'Crossroads Secret Chest Destroy Fire Hydrants': 1021,
    'Drowned Pass Currency Chest after Submerged Cave': 1021,
    'Drowned Pass Currency Chest Building Semi Submerged': 1021,
    'Drowned Pass Life Chest after Crystal Switch Platform': 1021,
    'Drowned Pass Wrath Chest Blocked by Ice': 1021,
    'Drowned Pass Access Tunnel Currency Chest East Nook': 1021,
    'Dry Road Currency Chest South of Vulgrim': 1021,
    'Dry Road Life Chest East of Artifact': 1021,
    'Dry Road Access Tunnel Currency Chest North of Chronosphere': 1021,
    'Dry Road Access Tunnel Currency Chest South of Entrance': 1021,
    'Dry Road Access Tunnel Currency Chest Up the Stairs': 1021,
    'The Hollows Beholder Key Chest after Chained Cube': 1031,
    'The Hollows Beholder Key Chest in Current': 1031,
    'The Hollows Beholder Key Chest inside Floor Hole': 1031,
    'The Hollows Currency Chest after Submerged Passage': 1031,
    'The Hollows Currency Chest between Ice Blocks': 1031,
    'The Hollows Currency Chest SE of Locust Room': 1031,
    'The Hollows Currency Chest South of Clocktower': 1031,
    'The Hollows Currency Chest SW of Gas': 1031,
    'The Hollows Currency Chest Top Balcony': 1031,
    'The Hollows Currency Chest Top of Stairwell': 1031,
    'The Hollows Currency Chest under Goremaw': 1031,
    'The Hollows Hoardseeker Chest SW of Grappleclaws Room': 1031,
    'The Hollows Life Chest after Chained Cube': 1031,
    'The Hollows Life Chest after Water-Filled Hallway': 1031,
    'The Hollows Life Chest before Boss Room': 1031,
    'The Hollows Life Chest behind Train Cars': 1031,
    'The Hollows Life Chest in Griever Tunnel': 1031,
    'The Hollows Life Chest North of Locust Room': 1031,
    'The Hollows Life Chest South Wall Nook': 1031,
    'The Hollows Life Chest West Corridor': 1031,
    'The Hollows Life Chest West of Grappleclaws Room': 1031,
    'The Hollows Map Chest at Surface of Flooded Room': 1031,
    'The Hollows Rare Chest over Submerged Passage': 1031,
    'The Hollows Wrath Chest after Submerged Passage': 1031,
    'The Hollows Wrath Chest after Water-Filled Hallway': 1031,
    'The Hollows Wrath Chest over Flooded Room': 1031,
    'The Hollows Access Tunnel Currency Chest Dead End': 1021,
    'The Hollows Access Tunnel Currency Chest Stream Walkthrough': 1021,
    #'The Crossroads Secret Chest Destroy Fire Hydrants': 15,
    #'The Crossroads Secret Chest Destroy Fire Hydrants': 15,
    'Library Currency Chest South of Fleshburners': 1022,
    #'The Library Life Chest Entrance': 15,
    'Library Life Chest Entrance': 1023,
    'Library Life Chest Submarine Cave': 1024,
    'Library Life Chest North': 1025,
    'Scalding Gallow Currency Chest 2nd Floor': 1026,
    'Scalding Gallow Currency Chest West Near Vulgrim': 1027,
    'Scalding Gallow Wrath Chest Above Vulgrim': 1028,
    #'Seraphim Hotel Life Chest 1': 1029,
    #'Seraphim Hotel Life Chest 2': 1030,
    'Serpent Hole to Anvil\'s Ford Chest': 1030,
    'Serpent Hole to Dry Road Chest': 1030,
    'Serpent Hole to Twilight Cathedral Chest': 1030,
    'Twilight Cathedral Beholder Key Chest South Wing': 1031,
    'Twilight Cathedral Beholder Key Chest Three Blades East Path': 1031,
    'Twilight Cathedral Currency Chest Below Abyssal Armor Chest': 1031,
    'Twilight Cathedral Currency Chest East of Elevated Platforms': 1031,
    'Twilight Cathedral Currency Chest Exterior Blocked by Ice': 1031,
    'Twilight Cathedral Currency Chest NE of Exterior': 1031,
    'Twilight Cathedral Currency Chest North after Lava Fall': 1031,
    'Twilight Cathedral Currency Chest Rot Mauler Room': 1031,
    'Twilight Cathedral Currency Chest South after Lava Fall': 1031,
    'Twilight Cathedral Currency Chest South of Exterior': 1031,
    'Twilight Cathedral Currency Chest South Wing Main Gallery': 1031,
    'Twilight Cathedral Currency Chest South Wing Conscript Room': 1031,
    'Twilight Cathedral Hoardseeker Chest South Wing': 1031,
    'Twilight Cathedral Life Chest after The Jailer': 1031,
    'Twilight Cathedral Life Chest before Platform Room': 1031,
    'Twilight Cathedral Life Chest North of Three Statues': 1031,
    'Twilight Cathedral Life Chest North Wing Basement': 1031,
    'Twilight Cathedral Life Chest South Wing Conscript Room': 1031,
    'Twilight Cathedral Life Chest South Wing First Room': 1031,
    'Twilight Cathedral Life Chest North Wing Under Crystal': 1031,
    'Twilight Cathedral Map Chest South Wing': 1031,
    'Twilight Cathedral Rare Chest South Wing': 1031,
    'Twilight Cathedral Secret Chest Light 8 Torches': 1031,
    'Twilight Cathedral Wrath Chest before Platform Room': 1031,
    'Twilight Cathedral Wrath Chest Below Abyssal Armor Chest': 1031,
    'Twilight Cathedral Wrath Chest Three Blades East Path': 1031,
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
    black_throne = world.get_region("Black Throne")
    broken_stair = world.get_region("The Broken Stair")
    choking_grounds = world.get_region("The Choking Grounds")
    crossroads = world.get_region("The Crossroads")
    destroyed_city = world.get_region("The Destroyed City")
    drowned_pass = world.get_region("Drowned Pass")
    drowned_pass_access_tunnel = world.get_region("Drowned Pass Access Tunnel")
    dry_road = world.get_region("The Dry Road")
    dry_road_access_tunnel_1 = world.get_region("The Dry Road Access Tunnel 1")
    dry_road_access_tunnel_2 = world.get_region("The Dry Road Access Tunnel 2")
    earth = world.get_region("Earth")
    eden = world.get_region("Eden")
    heaven = world.get_region("Heaven")
    hell = world.get_region("Hell")
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
    iron_canopy = world.get_region("Iron Canopy")
    leviathan_drift = world.get_region("Leviathan's Drift")
    menu = world.get_region("Menu")
    scalding_gallow = world.get_region("Scalding Gallow")
    #seraphim_hotel = world.get_region("Seraphim Hotel")
    shadow_realm = world.get_region("Shadow Realm")
    silitha_loom = world.get_region("Silitha's Loom")
    sh_to_anvil_ford = world.get_region("Serpent Hole to Anvil's Ford")
    sh_to_dry_road = world.get_region("Serpent Hole to Dry Road")
    sh_to_twilight_cathedral = world.get_region("Serpent Hole to Twilight Cathedral")
    soul_bridge = world.get_region("Soul Bridge")
    broken_stair = world.get_region("The Broken Stair")
    crossroads = world.get_region("The Crossroads")
    three_kingdoms = world.get_region("Three Kingdoms")
    tree_of_knowledge = world.get_region("Tree of Knowledge")
    twilight_cathedral_exterior = world.get_region("Twilight Cathedral Exterior")
    twilight_cathedral_1 = world.get_region("Twilight Cathedral 1")
    twilight_cathedral_2 = world.get_region("Twilight Cathedral 2")
    twilight_cathedral_3 = world.get_region("Twilight Cathedral 3")
    twilight_cathedral_boss_room = world.get_region("Twilight Cathedral Boss Room")
    well_of_souls = world.get_region("Well of Souls")

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
    black_throne = world.get_region("Black Throne")
    broken_stair = world.get_region("The Broken Stair")
    choking_grounds = world.get_region("The Choking Grounds")
    crossroads = world.get_region("The Crossroads")
    destroyed_city = world.get_region("The Destroyed City")
    drowned_pass = world.get_region("Drowned Pass")
    drowned_pass_access_tunnel = world.get_region("Drowned Pass Access Tunnel")
    dry_road = world.get_region("The Dry Road")
    earth = world.get_region("Earth")
    eden = world.get_region("Eden")
    heaven = world.get_region("Heaven")
    hell = world.get_region("Hell")
    hollows_1 = world.get_region("The Hollows 1")
    hollows_2 = world.get_region("The Hollows 2")
    hollows_3 = world.get_region("The Hollows 3")
    hollows_4 = world.get_region("The Hollows 4")
    hollows_boss_room = world.get_region("The Hollows Boss Room")
    iron_canopy = world.get_region("Iron Canopy")
    leviathan_drift = world.get_region("Leviathan's Drift")
    menu = world.get_region("Menu")
    scalding_gallow = world.get_region("Scalding Gallow")
    #seraphim_hotel = world.get_region("Seraphim Hotel")
    shadow_realm = world.get_region("Shadow Realm")
    silitha_loom = world.get_region("Silitha's Loom")
    sh_to_anvil_ford = world.get_region("Serpent Hole to Anvil's Ford")
    sh_to_dry_road = world.get_region("Serpent Hole to Dry Road")
    sh_to_twilight_cathedral = world.get_region("Serpent Hole to Twilight Cathedral")
    soul_bridge = world.get_region("Soul Bridge")
    broken_stair = world.get_region("The Broken Stair")
    crossroads = world.get_region("The Crossroads")
    three_kingdoms = world.get_region("Three Kingdoms")
    tree_of_knowledge = world.get_region("Tree of Knowledge")
    twilight_cathedral_exterior = world.get_region("Twilight Cathedral Exterior")
    twilight_cathedral_1 = world.get_region("Twilight Cathedral 1")
    twilight_cathedral_2 = world.get_region("Twilight Cathedral 2")
    twilight_cathedral_3 = world.get_region("Twilight Cathedral 3")
    twilight_cathedral_boss_room = world.get_region("Twilight Cathedral Boss Room")
    vulgrim_shop = world.get_region("Vulgrim's Shop")
    well_of_souls = world.get_region("Well of Souls")

    anvil_ford.add_event(location_name = "Ulthane defeated", rule = HAS_CHAOS_FORM, location_type = DSLocation)
    anvil_ford_challenge_area.add_event(location_name = "Ulthane outscored", rule = HAS_CHAOS_FORM, location_type = DSLocation)
    anvil_ford_challenge_area.add_event(location_name = "Uriel defeated", rule = HAS_CROSSBLADE, location_type = DSLocation)
    hollows_boss_room.add_event(location_name = "The Griever defeated", rule = HAS_GAUNTLET, location_type = DSLocation)
    leviathan_drift.add_event(location_name = "Abaddon The Destroyer defeated", item_name = "Victory", rule = CAN_BEAT_ABADDON, location_type = DSLocation, item_type = DSItem)
    scalding_gallow.add_event(location_name = "Phantom General defeated", location_type = DSLocation)
    scalding_gallow.add_event(location_name = "Samael's first Reward", location_type = DSLocation)
    scalding_gallow.add_event(location_name = "Trade first Heart of the Chosen", location_type = DSLocation)
    scalding_gallow.add_event(location_name = "Trade second Heart of the Chosen", location_type = DSLocation)
    twilight_cathedral_2.add_event(location_name = "The Jailer defeated", location_type = DSLocation)
    twilight_cathedral_boss_room.add_event(location_name = "Tiamat defeated", rule = HAS_CROSSBLADE, location_type = DSLocation)