from ..Locations import KEYS_LOCATIONS, get_location_list_from_json
from .bases import DSTestBase

class TestKeysRemoved(DSTestBase):
    options = {
        "keys": "remove"
        }

    def test_key_absent(self) -> None:
        keys = self.get_items_by_name("Beholder Key")

        with self.subTest("Test that there are no Beholder Keys in the pool"):
            self.assertEqual(len(keys), 0)

        with self.subTest("Test that no Beholder Keys are placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Beholder Key"))

class TestKeysVanilla(DSTestBase):
    options = {
        "keys": "vanilla"
        }

    def test_key_vanilla(self) -> None:
        keys = self.get_items_by_name("Beholder Key")

        with self.subTest("Test that there are no Beholder Keys in the pool"):
            self.assertEqual(len(keys), 0)

        with self.subTest("Test that Beholder Keys are placed at all their vanilla location"):
            self.assertTrue(all(Location for Location in self.multiworld.get_locations() if Location.name in KEYS_LOCATIONS and Location.item and Location.item.name == "Beholder Key"))
    
        with self.subTest("Test that no Beholder Key is placed outside its vanilla location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.name not in KEYS_LOCATIONS and Location.item and Location.item.name == "Beholder Key"))
    
        with self.subTest("Test that there are exactly 10 Beholder Keys vanilla location"):
            HOARDSEEKER_LOCATIONS = {location: item for location, item in KEYS_LOCATIONS.items() if item == "Beholder Key"}
            self.assertEqual(len(HOARDSEEKER_LOCATIONS), 10)

class TestKeysRegion(DSTestBase):
    options = {
        "keys": "region"
        }

    def test_key_region(self) -> None:
        BLACK_THRONE_LOCATIONS = get_location_list_from_json(self.world, "Black Throne.json")
        BROKEN_STAIRS_LOCATIONS = get_location_list_from_json(self.world, "Broken Stairs.json")
        HOLLOWS_LOCATIONS = get_location_list_from_json(self.world, "Hollows.json")
        IRON_CANOPY_LOCATIONS = get_location_list_from_json(self.world, "Iron Canopy.json")
        TWILIGHT_CATHEDRAL_LOCATIONS = get_location_list_from_json(self.world, "Twilight Cathedral.json")

        keys = self.get_items_by_name("Beholder Key")

        with self.subTest("Test that there are no Beholder Keys in the pool"):
            self.assertEqual(len(keys), 0)
    
        with self.subTest("Test that exactly 2 Beholder Key is placed in the Black Throne"):
            self.assertEqual(len([Location for Location in BLACK_THRONE_LOCATIONS if Location.item and Location.item.name == "Beholder Key"]), 2)
    
        with self.subTest("Test that exactly 1 Beholder Key is placed in the Broken Stairs"):
            self.assertEqual(len([Location for Location in BROKEN_STAIRS_LOCATIONS if Location.item and Location.item.name == "Beholder Key"]), 1)
    
        with self.subTest("Test that exactly 3 Beholder Key is placed in the Hollows"):
            self.assertEqual(len([Location for Location in HOLLOWS_LOCATIONS if Location.item and Location.item.name == "Beholder Key"]), 3)
    
        with self.subTest("Test that exactly 2 Beholder Key is placed in the Iron Canopy"):
            self.assertEqual(len([Location for Location in IRON_CANOPY_LOCATIONS if Location.item and Location.item.name == "Beholder Key"]), 2)
    
        with self.subTest("Test that exactly 2 Beholder Key is placed in the Twilight Cathedral"):
            self.assertEqual(len([Location for Location in TWILIGHT_CATHEDRAL_LOCATIONS if Location.item and Location.item.name == "Beholder Key"]), 2)
    
        with self.subTest("Test that exactly 10 Beholder Keys are placed in the World"):
            self.assertEqual(len([Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Beholder Key"]), 10)

class TestKeysOwn(DSTestBase):
    options = {
        "keys": "own"
        }

    def test_key_own(self) -> None:
        keys = self.get_items_by_name("Beholder Key")

        with self.subTest("Test that there are exactly 10 Beholder Keys in the pool"):
            self.assertEqual(len(keys), 10)

        with self.subTest("Test that all Beholder Keys are part of the local item pool"):
            self.assertIn("Beholder Key", self.multiworld.worlds[1].options.local_items)

class TestKeysSanity(DSTestBase):
    options = {
        "keys": "keysanity"
        }

    def test_key_anywhere(self) -> None:
        keys = self.get_items_by_name("Beholder Key")

        with self.subTest("Test that there are exactly 10 Beholder Keys in the pool"):
            self.assertEqual(len(keys), 10)

        with self.subTest("Test that no Beholder Keys are part of the local item pool"):
            self.assertNotIn("Beholder Key", self.multiworld.worlds[1].options.local_items)