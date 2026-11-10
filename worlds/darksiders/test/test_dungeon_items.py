from ..Locations import DUNGEON_ITEMS_LOCATIONS, get_location_list_from_json
from .bases import DSTestBase

class TestDungeonItemsRemoved(DSTestBase):
    options = {
        "dungeon_items": "remove"
        }

    def test_hoardseeker_absent(self) -> None:
        hoardseekers = self.get_items_by_name("Hoardseeker")

        with self.subTest("Test that there are no Hoardseekers in the pool"):
            self.assertEqual(len(hoardseekers), 0)

        with self.subTest("Test that no Hoardseekers are placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Hoardseeker"))

    def test_map_absent(self) -> None:
        maps = self.get_items_by_name("Map")

        with self.subTest("Test that there are no Maps in the pool"):
            self.assertEqual(len(maps), 0)

        with self.subTest("Test that no Maps are placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Map"))

class TestDungeonItemsVanilla(DSTestBase):
    options = {
        "dungeon_items": "vanilla"
        }

    def test_hoardseeker_vanilla(self) -> None:
        hoardseekers = self.get_items_by_name("Hoardseeker")

        with self.subTest("Test that there are no Hoardseekers in the pool"):
            self.assertEqual(len(hoardseekers), 0)

        with self.subTest("Test that Hoardseekers are placed at all their vanilla location"):
            self.assertTrue(all(Location for Location in self.multiworld.get_locations() if Location.name in DUNGEON_ITEMS_LOCATIONS and Location.item and Location.item.name == "Hoardseeker"))
    
        with self.subTest("Test that no Hoardseeker is placed outside its vanilla location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.name not in DUNGEON_ITEMS_LOCATIONS and Location.item and Location.item.name == "Hoardseeker"))
    
        with self.subTest("Test that there are exactly 4 Hoardseekers vanilla location"):
            HOARDSEEKER_LOCATIONS = {location: item for location, item in DUNGEON_ITEMS_LOCATIONS.items() if item == "Hoardseeker"}
            self.assertEqual(len(HOARDSEEKER_LOCATIONS), 4)

    def test_map_vanilla(self) -> None:
        maps = self.get_items_by_name("Map")

        with self.subTest("Test that there are no Maps in the pool"):
            self.assertEqual(len(maps), 0)

        with self.subTest("Test that Maps are placed at all their vanilla location"):
            self.assertTrue(all(Location for Location in self.multiworld.get_locations() if Location.name in DUNGEON_ITEMS_LOCATIONS and Location.item and Location.item.name == "Map"))
    
        with self.subTest("Test that no Map is placed outside its vanilla location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.name not in DUNGEON_ITEMS_LOCATIONS and Location.item and Location.item.name == "Map"))
    
        with self.subTest("Test that there are exactly 4 Map vanilla location"):
            MAP_LOCATIONS = {location: item for location, item in DUNGEON_ITEMS_LOCATIONS.items() if item == "Map"}
            self.assertEqual(len(MAP_LOCATIONS), 4)

class TestDungeonItemsStart(DSTestBase):
    options = {
        "dungeon_items": "start_with"
        }

    def test_hoardseeker_start(self) -> None:
        hoardseekers = self.get_items_by_name("Hoardseeker")

        with self.subTest("Test that there are no Hoardseekers in the pool"):
            self.assertEqual(len(hoardseekers), 0)
    
        with self.subTest("Test that no Hoardseeker is placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Hoardseeker"))

    def test_map_start(self) -> None:
        maps = self.get_items_by_name("Map")

        with self.subTest("Test that there are no Maps in the pool"):
            self.assertEqual(len(maps), 0)
    
        with self.subTest("Test that no Map is placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Map"))

class TestDungeonItemsRegion(DSTestBase):
    options = {
        "dungeon_items": "region"
        }

    def test_hoardseeker_region(self) -> None:
        BLACK_THRONE_LOCATIONS = get_location_list_from_json(self.world, "Black Throne.json")
        HOLLOWS_LOCATIONS = get_location_list_from_json(self.world, "Hollows.json")
        IRON_CANOPY_LOCATIONS = get_location_list_from_json(self.world, "Iron Canopy.json")
        TWILIGHT_CATHEDRAL_LOCATIONS = get_location_list_from_json(self.world, "Twilight Cathedral.json")

        hoardseekers = self.get_items_by_name("Hoardseeker")

        with self.subTest("Test that there are no Hoardseekers in the pool"):
            self.assertEqual(len(hoardseekers), 0)
    
        with self.subTest("Test that exactly 1 Hoardseeker is placed in the Black Throne"):
            self.assertEqual(len([Location for Location in BLACK_THRONE_LOCATIONS if Location.item and Location.item.name == "Hoardseeker"]), 1)
    
        with self.subTest("Test that exactly 1 Hoardseeker is placed in the Hollows"):
            self.assertEqual(len([Location for Location in HOLLOWS_LOCATIONS if Location.item and Location.item.name == "Hoardseeker"]), 1)
    
        with self.subTest("Test that exactly 1 Hoardseeker is placed in the Iron Canopy"):
            self.assertEqual(len([Location for Location in IRON_CANOPY_LOCATIONS if Location.item and Location.item.name == "Hoardseeker"]), 1)
    
        with self.subTest("Test that exactly 1 Hoardseeker is placed in the Twilight Cathedral"):
            self.assertEqual(len([Location for Location in TWILIGHT_CATHEDRAL_LOCATIONS if Location.item and Location.item.name == "Hoardseeker"]), 1)
    
        with self.subTest("Test that exactly 4 Hoardseekers are placed in the World"):
            self.assertEqual(len([Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Hoardseeker"]), 4)

    def test_map_region(self) -> None:
        BLACK_THRONE_LOCATIONS = get_location_list_from_json(self.world, "Black Throne.json")
        HOLLOWS_LOCATIONS = get_location_list_from_json(self.world, "Hollows.json")
        IRON_CANOPY_LOCATIONS = get_location_list_from_json(self.world, "Iron Canopy.json")
        TWILIGHT_CATHEDRAL_LOCATIONS = get_location_list_from_json(self.world, "Twilight Cathedral.json")

        maps = self.get_items_by_name("Hoardseeker")

        with self.subTest("Test that there are no Maps in the pool"):
            self.assertEqual(len(maps), 0)
    
        with self.subTest("Test that exactly 1 Map is placed in the Black Throne"):
            self.assertEqual(len([Location for Location in BLACK_THRONE_LOCATIONS if Location.item and Location.item.name == "Map"]), 1)
    
        with self.subTest("Test that exactly 1 Map is placed in the Hollows"):
            self.assertEqual(len([Location for Location in HOLLOWS_LOCATIONS if Location.item and Location.item.name == "Map"]), 1)
    
        with self.subTest("Test that exactly 1 Map is placed in the Iron Canopy"):
            self.assertEqual(len([Location for Location in IRON_CANOPY_LOCATIONS if Location.item and Location.item.name == "Map"]), 1)
    
        with self.subTest("Test that exactly 1 Map is placed in the Twilight Cathedral"):
            self.assertEqual(len([Location for Location in TWILIGHT_CATHEDRAL_LOCATIONS if Location.item and Location.item.name == "Map"]), 1)
    
        with self.subTest("Test that exactly 4 Maps are placed in the World"):
            self.assertEqual(len([Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Map"]), 4)

class TestDungeonItemsOwn(DSTestBase):
    options = {
        "dungeon_items": "own"
        }

    def test_hoardseeker_own(self) -> None:
        hoardseekers = self.get_items_by_name("Hoardseeker")

        with self.subTest("Test that there are exactly 4 Hoardseekers in the pool"):
            self.assertEqual(len(hoardseekers), 4)

        with self.subTest("Test that all Hoardseekers are part of the local item pool"):
            self.assertIn("Hoardseeker", self.multiworld.worlds[1].options.local_items)

    def test_map_own(self) -> None:
        maps = self.get_items_by_name("Map")

        with self.subTest("Test that there are exactly 4 Maps in the pool"):
            self.assertEqual(len(maps), 4)

        with self.subTest("Test that all Maps are part of the local item pool"):
            self.assertIn("Map", self.multiworld.worlds[1].options.local_items)

class TestDungeonItemsSanity(DSTestBase):
    options = {
        "dungeon_items": "anywhere"
        }

    def test_hoardseeker_anywhere(self) -> None:
        hoardseekers = self.get_items_by_name("Hoardseeker")

        with self.subTest("Test that there are exactly 4 Hoardseekers in the pool"):
            self.assertEqual(len(hoardseekers), 4)

        with self.subTest("Test that all Hoardseekers are part of the local item pool"):
            self.assertNotIn("Hoardseeker", self.multiworld.worlds[1].options.local_items)

    def test_map_anywhere(self) -> None:
        maps = self.get_items_by_name("Map")

        with self.subTest("Test that there are exactly 4 Maps in the pool"):
            self.assertEqual(len(maps), 4)

        with self.subTest("Test that all Maps are part of the local item pool"):
            self.assertNotIn("Map", self.multiworld.worlds[1].options.local_items)