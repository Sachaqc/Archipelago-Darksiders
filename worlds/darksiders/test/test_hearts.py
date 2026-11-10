from ..Locations import HEARTS_LOCATIONS
from .bases import DSTestBase

class TestHeartsRemoved(DSTestBase):
    options = {
        "hearts": "remove"
        }

    def test_hearts_absent(self) -> None:
        hearts = self.get_items_by_name("Heart of the Chosen")

        with self.subTest("Test that there are no Hearts of the Chosen in the pool"):
            self.assertEqual(len(hearts), 0)

        with self.subTest("Test that no Hearts of the Chosen are placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Heart of the Chosen"))

class TestHeartsVanilla(DSTestBase):
    options = {
        "hearts": "vanilla"
        }

    def test_hoardseeker_vanilla(self) -> None:
        hearts = self.get_items_by_name("Heart of the Chosen")

        with self.subTest("Test that there are no Hearts of the Chosen in the pool"):
            self.assertEqual(len(hearts), 0)

        with self.subTest("Test that Hearts of the Chosen are placed at all their vanilla location"):
            self.assertTrue(all(Location for Location in self.multiworld.get_locations() if Location.name in HEARTS_LOCATIONS and Location.item and Location.item.name == "Heart of the Chosen"))
    
        with self.subTest("Test that no Heart of the Chosen is placed outside its vanilla location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.name not in HEARTS_LOCATIONS and Location.item and Location.item.name == "Heart of the Chosen"))
    
        with self.subTest("Test that there are exactly 4 Hearts of the Chosen vanilla location"):
            HOARDSEEKER_LOCATIONS = {location: item for location, item in HEARTS_LOCATIONS.items() if item == "Heart of the Chosen"}
            self.assertEqual(len(HOARDSEEKER_LOCATIONS), 4)

class TestHeartsOwn(DSTestBase):
    options = {
        "hearts": "own"
        }

    def test_hoardseeker_own(self) -> None:
        hearts = self.get_items_by_name("Heart of the Chosen")

        with self.subTest("Test that there are exactly 4 Hearts of the Chosen in the pool"):
            self.assertEqual(len(hearts), 4)

        with self.subTest("Test that all Hearts of the Chosen are part of the local item pool"):
            self.assertIn("Heart of the Chosen", self.multiworld.worlds[1].options.local_items)

class TestHeartsSanity(DSTestBase):
    options = {
        "hearts": "heartsanity"
        }

    def test_hoardseeker_anywhere(self) -> None:
        hearts = self.get_items_by_name("Heart of the Chosen")

        with self.subTest("Test that there are exactly 4 Hearts of the Chosen in the pool"):
            self.assertEqual(len(hearts), 4)

        with self.subTest("Test that all Hearts of the Chosen are not part of the local item pool"):
            self.assertNotIn("Heart of the Chosen", self.multiworld.worlds[1].options.local_items)