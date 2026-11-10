from ..Locations import ABYSSAL_ARMOR_PIECES_LOCATIONS
from .bases import DSTestBase

class TestArmorRemoved(DSTestBase):
    options = {
        "armor": "remove",
        "armor_pieces": 7
        }

    def test_armor_pieces_absent(self) -> None:
        armor_pieces = self.get_items_by_name("Abyssal Armor Piece")

        with self.subTest("Test that there are no Abyssal Armor Piece in the pool"):
            self.assertEqual(len(armor_pieces), 0)

        with self.subTest("Test that no Abyssal Armor Piece are placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Abyssal Armor Piece"))

    def test_armor_absent(self) -> None:
        armor = self.get_items_by_name("Abyssal Armor")

        with self.subTest("Test that there is no Abyssal Armor in the pool"):
            self.assertEqual(len(armor), 0)

        with self.subTest("Test that no Abyssal Armor is placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Abyssal Armor"))

class TestArmorVanilla(DSTestBase):
    options = {
        "armor": "vanilla",
        "armor_pieces": 7
        }

    def test_armor_pieces_vanilla(self) -> None:
        armor_pieces = self.get_items_by_name("Abyssal Armor Piece")

        with self.subTest("Test that there is no Abyssal Armor in the pool"):
            self.assertEqual(len(armor_pieces), 0)

        with self.subTest("Test that Abyssal Armor Pieces are placed at all their vanilla location"):
            self.assertTrue(all(Location for Location in self.multiworld.get_locations() if Location.name in ABYSSAL_ARMOR_PIECES_LOCATIONS and Location.item and Location.item.name == "Abyssal Armor Piece"))
    
        with self.subTest("Test that no Abyssal Armor Piece is placed outside its vanilla location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.name not in ABYSSAL_ARMOR_PIECES_LOCATIONS and Location.item and Location.item.name == "Abyssal Armor Piece"))
    
        with self.subTest("Test that there are exactly 10 Abyssal Armor Pieces vanilla location"):
            PIECES_LOCATIONS = {location: item for location, item in ABYSSAL_ARMOR_PIECES_LOCATIONS.items() if item == "Abyssal Armor Piece"}
            self.assertEqual(len(PIECES_LOCATIONS), 10)

    def test_armor_vanilla(self) -> None:
        armor = self.get_items_by_name("Abyssal Armor")

        with self.subTest("Test that there is no Abyssal Armor in the pool"):
            self.assertEqual(len(armor), 0)
    
        with self.subTest("Test that no Abyssal Armor is placed outside its vanilla location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.name not in ABYSSAL_ARMOR_PIECES_LOCATIONS and Location.item and Location.item.name == "Abyssal Armor"))

class TestArmorOwnPieces(DSTestBase):
    options = {
        "armor": "own_pieces",
        "armor_pieces": 7
        }

    def test_armor_pieces_shuffled_own(self) -> None:
        armor_pieces = self.get_items_by_name("Abyssal Armor Piece")

        with self.subTest("Test that the number of Abyssal Armor Piece in the pool is exactly as the Options expect"):
            self.assertEqual(len(armor_pieces), 7)

        with self.subTest("Test that all Abyssal Armor Piece are part of the local item pool"):
            self.assertIn("Abyssal Armor Piece", self.multiworld.worlds[1].options.local_items)

    def test_armor_absent(self) -> None:
        armor = self.get_items_by_name("Abyssal Armor")

        with self.subTest("Test that there is no Abyssal Armor in the pool"):
            self.assertEqual(len(armor), 0)

        with self.subTest("Test that no Abyssal Armor is placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Abyssal Armor"))

class TestArmorOwnArmor(DSTestBase):
    options = {
        "armor": "own_armor",
        "armor_pieces": 7
        }

    def test_armor_pieces_absent(self) -> None:
        armor_pieces = self.get_items_by_name("Abyssal Armor Piece")

        with self.subTest("Test that there are no Abyssal Armor Piece in the pool"):
            self.assertEqual(len(armor_pieces), 0)

        with self.subTest("Test that no Abyssal Armor Piece are placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Abyssal Armor Piece"))

    def test_armor_absent(self) -> None:
        armor = self.get_items_by_name("Abyssal Armor")

        with self.subTest("Test that there is exactly 1 Abyssal Armor in the pool"):
            self.assertEqual(len(armor), 1)

        with self.subTest("Test that the Abyssal Armor is part of the local item pool"):
            self.assertIn("Abyssal Armor", self.multiworld.worlds[1].options.local_items)

class TestArmorPieceSanity(DSTestBase):
    options = {
        "armor": "armorsanity_pieces",
        "armor_pieces": 7
        }

    def test_armor_pieces_shuffled_own(self) -> None:
        armor_pieces = self.get_items_by_name("Abyssal Armor Piece")

        with self.subTest("Test that the number of Abyssal Armor Piece in the pool is exactly as the Options expect"):
            self.assertEqual(len(armor_pieces), 7)

        with self.subTest("Test that the Abyssal Armor Pieces are not part of the local item pool"):
            self.assertNotIn("Abyssal Armor Piece", self.multiworld.worlds[1].options.local_items)

    def test_armor_absent(self) -> None:
        armor = self.get_items_by_name("Abyssal Armor")

        with self.subTest("Test that there is no Abyssal Armor in the pool"):
            self.assertEqual(len(armor), 0)

        with self.subTest("Test that no Abyssal Armor is placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Abyssal Armor"))

class TestArmorArmorSanity(DSTestBase):
    options = {
        "armor": "armorsanity_armor",
        "armor_pieces": 7
        }

    def test_armor_pieces_absent(self) -> None:
        armor_pieces = self.get_items_by_name("Abyssal Armor Piece")

        with self.subTest("Test that there are no Abyssal Armor Piece in the pool"):
            self.assertEqual(len(armor_pieces), 0)

        with self.subTest("Test that no Abyssal Armor Piece are placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Abyssal Armor Piece"))

    def test_armor_absent(self) -> None:
        armor = self.get_items_by_name("Abyssal Armor")

        with self.subTest("Test that there is exactly 1 Abyssal Armor in the pool"):
            self.assertEqual(len(armor), 1)

        with self.subTest("Test that the Abyssal Armor is not part of the local item pool"):
            self.assertNotIn("Abyssal Armor", self.multiworld.worlds[1].options.local_items)