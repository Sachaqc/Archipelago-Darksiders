from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Location
from rule_builder.rules import Has

from .Items import DSItem
from .Rules import CAN_BEAT_ABADDON, HAS_ABYSSAL_CHAIN, HAS_CHAOS_FORM, HAS_CROSSBLADE, HAS_GAUNTLET, HAS_MASK, HAS_RUIN, HAS_VOIDWALKER
from .Utils import data_path, json_read

if TYPE_CHECKING:
    from .World import DSWorld

abyssal_armor_pieces = {
    'Choking Grounds Access Tunnel Abyssal Armor Chest': 211,
    'Drowned Pass Abyssal Armor Piece': 1,
    'Hollows Abyssal Armor Piece': 2,
    'Scalding Gallow Abyssal Armor Piece Near Library': 3,
    'Scalding Gallow Abyssal Armor Piece Under Central Platform': 4,
    'Twilight Cathedral Abyssal Armor Piece': 5,
}

armaggedon_shards = {
    'Choking Grounds Armaggedon Blade Shard in North Building': 300,
}

artifacts = {
    'Broken Stair Artifact': 29,
    'Broken Stair Artifact Blocked by Ice': 30,
    #'Choking Grounds Access Cave Soldier Artifact',
    'Choking Grounds Artifact North of Vulgrim': 31,
    'Choking Grounds Artifact South in Sarcophagus': 32,
    'Crossroads Soldier Artifact in Subway Station': 33,
    'Drowned Pass Access Tunnel Champion Artifact': 34,
    'Drowned Pass Soldier Artifact Cave Under Waterfall': 35,
    'Drowned Pass Soldier Artifact Underwater Building': 36,
    'Dry Road Soldier Artifact': 37,
    'Dry Road Access Tunnel Soldier Artifact': 38,
    'Hollows Champion Artifact in Pipe Leading North': 39,
    'Hollows Soldier Artifact Underwater': 40,
    'Hollows Soldier Artifact South of Platforms': 41,
    'Library Artifact on West Side': 216,
    'Twilight Cathedral Champion Artifact North Wing': 42,
    'Twilight Cathedral Soldier Artifact South Wing': 43,
    'Twilight Cathedral Soldier Artifact Bridge Room': 44,
}

"""
boss_defeated = {
    'Abaddon Destroyer': 70,
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
    'Hollows Chained Cube': 90,
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
    'Ashlands Currency Chest up the Ramp': 109,
    'Ashlands Access Tunnel Currency Chest by Three Goremaws': 110,
    'Ashlands Access Tunnel Life Blocked by Ice': 111,
    'Ashlands Access Tunnel Rare Chest by Goremaw': 112,
    'Broken Stair Access Tunnel Chest': 113,
    'Broken Stair Chest after Waterway': 114,
    'Broken Stair Chest inside Building': 115,
    'Broken Stair Chest near Vulgrim': 116,
    'Broken Stair Chest at Highway\'s end': 117,
    'Broken Stair Chest Bottom Floor of Last Building': 118,
    'Broken Stair Chest Middle Floor of Last Building': 119,
    'Broken Stair Chest under Billboard': 210,
    'Choking Grounds Access Tunnel Chest in Lava River': 120,
    'Choking Grounds Chest Bottom Floor of North Building': 121,
    'Choking Grounds Chest NE South of the Ramp': 122,
    'Choking Grounds Chest South Down the Stairs': 123,
    'Choking Grounds Chest Top Floor of North Building Blocked by Ice': 124,
    'Choking Grounds Chest North of Cemetery': 125,
    'Choking Grounds Chest Top Floor of North Building': 126,
    'Choking Grounds Chest 2nd Floor of North Building': 127,
    'Choking Grounds Rare Chest of North Building': 212,
    'Choking Grounds Secret Chest Destroy Gravestones with Crosses': 215,
    'Crossroads Currency Chest Down Back Alley Stairs': 128,
    'Crossroads Currency Chest in North Building': 129,
    'Crossroads Currency Chest South Crater': 130,
    'Crossroads Currency Chest in Subway Station': 131,
    'Crossroads Life Chest East Crater': 132,
    'Crossroads Life Chest in NE Back Alley': 133,
    'Crossroads Life Chest West of Library': 134,
    'Crossroads Rare Chest Blocked by Ice': 135,
    'Crossroads Secret Chest Destroy Fire Hydrants': 213,
    'Crossroads Soldier Artifact in Subway Station': 214,
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
    'Hollows Beholder Key Chest after Chained Cube': 146,
    'Hollows Beholder Key Chest in Current': 147,
    'Hollows Beholder Key Chest inside Floor Hole': 148,
    'Hollows Currency Chest after Submerged Passage': 149,
    'Hollows Currency Chest between Ice Blocks': 150,
    'Hollows Currency Chest SE of Locust Room': 151,
    'Hollows Currency Chest South of Clocktower': 152,
    'Hollows Currency Chest SW of Gas': 153,
    'Hollows Currency Chest Top Balcony': 154,
    'Hollows Currency Chest Top of Stairwell': 155,
    'Hollows Currency Chest under Goremaw': 156,
    'Hollows Hoardseeker Chest SW of Grappleclaws Room': 157,
    'Hollows Life Chest after Chained Cube': 158,
    'Hollows Life Chest after Water-Filled Hallway': 159,
    'Hollows Life Chest before Boss Room': 160,
    'Hollows Life Chest behind Train Cars': 161,
    'Hollows Life Chest in Griever Tunnel': 162,
    'Hollows Life Chest North of Locust Room': 163,
    'Hollows Life Chest South Wall Nook': 164,
    'Hollows Life Chest West Corridor': 165,
    'Hollows Life Chest West of Grappleclaws Room': 166,
    'Hollows Map Chest at Surface of Flooded Room': 167,
    'Hollows Rare Chest over Submerged Passage': 168,
    'Hollows Wrath Chest after Submerged Passage': 169,
    'Hollows Wrath Chest after Water-Filled Hallway': 170,
    'Hollows Wrath Chest over Flooded Room': 171,
    'Hollows Access Tunnel Currency Chest Dead End': 172,
    'Hollows Access Tunnel Currency Chest Stream Walkthrough': 173,
    'Library Chest South of Fleshburners': 174,
    'Library Wrath Chest North': 217,
    'Library Life Chest Entrance': 175,
    'Library Life Chest Submarine Cave': 176,
    'Library Life Chest North': 177,
    'Scalding Gallow Chest 2nd Floor Near Library': 178,
    'Scalding Gallow Chest Near Vulgrim': 179,
    'Scalding Gallow Chest Above Vulgrim': 180,
    'Serpent Hole to Anvil\'s Ford Chest': 181,
    'Serpent Hole to Dry Road Chest': 182,
    'Serpent Hole to Twilight Cathedral Chest': 183,
    'Twilight Cathedral Beholder Key Chest South Wing': 184,
    'Twilight Cathedral Beholder Key Chest Three Blades East Path': 185,
    'Twilight Cathedral Currency Chest Below Abyssal Armor Chest': 186,
    'Twilight Cathedral Currency Chest East of Elevated Platforms': 187,
    'Twilight Cathedral Exterior Chest Blocked by Ice': 188,
    'Twilight Cathedral Exterior Chest NE of Entrance': 189,
    'Twilight Cathedral Currency Chest North after Lava Fall': 190,
    'Twilight Cathedral Currency Chest Rot Mauler Room': 191,
    'Twilight Cathedral Currency Chest South after Lava Fall': 192,
    'Twilight Cathedral Exterior Chest South of Exterior': 193,
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
    'Twilight Cathedral Exterior Chest NW after Hooks': 220,
}

LOCATION_NAME_TO_ID = abyssal_armor_pieces | armaggedon_shards | artifacts | chained_cubes | chests

#location_json = json_read(data_path("Anvil Ford.json"))

#for Region, region_data in location_json.items():
#    if 'locations' in region_data:
#        for location, location_data in region_data.items():
#            LOCATION_NAME_TO_ID[location] = location_data.get("ID")

class DSLocation(Location):

    game = "Darksiders"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:

    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def create_all_locations(world: DSWorld) -> None:

    create_regular_locations(world)
    create_events(world)

def create_regular_locations(world: DSWorld) -> None:

    #seraphim_hotel = world.get_region("Seraphim Hotel")

    create_locations_from_json(world, "Anvil Ford.json")
    create_locations_from_json(world, "Ashlands.json")
    create_locations_from_json(world, "Broken Stairs.json")
    create_locations_from_json(world, "Choking Grounds.json")
    create_locations_from_json(world, "Crossroads.json")
    create_locations_from_json(world, "Drowned Pass.json")
    create_locations_from_json(world, "Dry Road.json")
    create_locations_from_json(world, "Hollows.json")
    create_locations_from_json(world, "Library.json")
    create_locations_from_json(world, "Menu.json")
    create_locations_from_json(world, "Scalding Gallow.json")

    #seraphim_hotel_locations = get_location_names_with_ids([
    #    'Seraphim Hotel Life Chest 1',
    #    'Seraphim Hotel Life Chest 2'
    #])
    #seraphim_hotel.add_locations(seraphim_hotel_locations, DSLocation)

    create_locations_from_json(world, "Serpent Holes.json")
    create_locations_from_json(world, "Twilight Cathedral.json")

def create_events(world: DSWorld) -> None:

    black_throne_boss_room = world.get_region("Black Throne Boss Room")
    dry_road = world.get_region("Dry Road")
    eden = world.get_region("Eden")
    hollows_boss_room = world.get_region("Hollows Boss Room")
    leviathan_drift = world.get_region("Leviathan's Drift")
    #seraphim_hotel = world.get_region("Seraphim Hotel")
    silitha_loom = world.get_region("Silitha's Loom")

    #anvil_ford.add_event(location_name = "Ulthane defeated", rule = HAS_CHAOS_FORM, location_type = DSLocation)
    #anvil_ford_challenge_area.add_event(location_name = "Ulthane outscored", rule = HAS_CHAOS_FORM, location_type = DSLocation)
    #anvil_ford_challenge_area.add_event(location_name = "Uriel 1 defeated", rule = HAS_CROSSBLADE, location_type = DSLocation)
    black_throne_boss_room.add_event(location_name = "Straga defeated", item_name = "Straga Defeated", rule = HAS_VOIDWALKER, location_type = DSLocation)
    black_throne_boss_room.add_event(location_name = "Straga Item Reward", rule = HAS_VOIDWALKER, location_type = DSLocation)
    dry_road.add_event(location_name = "Uriel 2 defeated", rule = Has("Armageddon Blade Shards", count = 1), location_type = DSLocation)
    eden.add_event(location_name = "Shadow War defeated", rule = HAS_MASK, location_type = DSLocation)
    hollows_boss_room.add_event(location_name = "Griever defeated", item_name = "Heart of Chosen", rule = HAS_GAUNTLET, location_type = DSLocation)
    hollows_boss_room.add_event(location_name = "Griever Item Reward", rule = HAS_GAUNTLET, location_type = DSLocation)
    leviathan_drift.add_event(location_name = "Abaddon Destroyer defeated", item_name = "Victory", rule = CAN_BEAT_ABADDON, location_type = DSLocation, item_type = DSItem)
    leviathan_drift.add_event(location_name = "Stygian defeated", item_name = "Heart of Chosen", rule = HAS_RUIN, location_type = DSLocation)
    leviathan_drift.add_event(location_name = "Stygian Item Reward", rule = HAS_RUIN, location_type = DSLocation)
    #scalding_gallow.add_event(location_name = "Phantom General defeated", location_type = DSLocation)
    #scalding_gallow.add_event(location_name = "Samael's first Reward", location_type = DSLocation)
    #scalding_gallow.add_event(location_name = "Trade first Heart of Chosen", rule = Has("Heart of Chosen", count = 1), location_type = DSLocation)
    #scalding_gallow.add_event(location_name = "Trade second Heart of Chosen", rule = Has("Heart of Chosen", count = 2), location_type = DSLocation)
    #scalding_gallow.add_event(location_name = "Trade third Heart of Chosen", rule = Has("Heart of Chosen", count = 3), location_type = DSLocation)
    #scalding_gallow.add_event(location_name = "Trade fourth Heart of Chosen", rule = Has("Heart of Chosen", count = 4), location_type = DSLocation)
    silitha_loom.add_event(location_name = "Silitha defeated", item_name = "Heart of Chosen", rule = HAS_ABYSSAL_CHAIN, location_type = DSLocation)
    silitha_loom.add_event(location_name = "Silitha Item Reward", rule = HAS_ABYSSAL_CHAIN, location_type = DSLocation)
    #twilight_cathedral_2.add_event(location_name = "Jailer defeated", location_type = DSLocation)
    #twilight_cathedral_boss_room.add_event(location_name = "Tiamat defeated", item_name = "Heart of Chosen", rule = HAS_CROSSBLADE, location_type = DSLocation)
    #twilight_cathedral_boss_room.add_event(location_name = "Tiamat Item Reward", rule = HAS_CROSSBLADE, location_type = DSLocation)

def create_events_from_json(world: DSWorld, filename) -> None:

    region_json = json_read(data_path(filename))

    for region in region_json:
        if 'events' in region:
            this_region = world.get_region(region.get("name"))
            for event_name, event_data in region.get("events").items():
                if 'forced reward' in event_data:
                    this_region.add_event(location_name = event_name, item_name = event_data.get("forced reward"), rule = event_data.get("rule"), location_type = DSLocation, item_type = DSItem)
                else:
                    this_region.add_event(location_name = event_name, rule = event_data.get("rule"), location_type = DSLocation)

def create_locations_from_json(world: DSWorld, filename) -> None:

    region_json = json_read(data_path(filename))

    for region in region_json:
        if 'locations' in region:
            this_region = world.get_region(region_name = region.get("name"))
            region_locations = get_location_names_with_ids(location_names = region.get("locations"))
            this_region.add_locations(locations = region_locations, location_type = DSLocation)