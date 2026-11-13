from ..Locations import ABYSSAL_ARMOR_PIECES_LOCATIONS
from .bases import DSTestBase

class TestArmorRemoved(DSTestBase):
    options = {
        "armor": "remove",
        "armor_pieces": 7
        }

    def test_armor_pieces_absent(self) -> None:
        self.absent_item("Abyssal Armor Piece")

    def test_armor_absent(self) -> None:
        self.absent_item("Abyssal Armor")

class TestArmorVanilla(DSTestBase):
    options = {
        "armor": "vanilla",
        "armor_pieces": 7
        }

    def test_armor_pieces_vanilla(self) -> None:
        self.vanilla_item("Abyssal Armor Piece", ABYSSAL_ARMOR_PIECES_LOCATIONS, count = 10)

    def test_armor_absent(self) -> None:
        #This is game client only
        self.absent_item("Abyssal Armor")

class TestArmorOwnPieces(DSTestBase):
    options = {
        "armor": "own_pieces",
        "armor_pieces": 7
        }

    def test_armor_pieces_shuffled_own(self) -> None:
        self.shuffled_item_local("Abyssal Armor Piece", count = 7)

    def test_armor_absent(self) -> None:
        self.absent_item("Abyssal Armor")

class TestArmorOwnArmor(DSTestBase):
    options = {
        "armor": "own_armor",
        "armor_pieces": 7
        }

    def test_armor_pieces_absent(self) -> None:
        self.absent_item("Abyssal Armor Piece")

    def test_armor_shuffled_own(self) -> None:
        self.shuffled_item_local("Abyssal Armor")

class TestArmorPieceSanity(DSTestBase):
    options = {
        "armor": "armorsanity_pieces",
        "armor_pieces": 7
        }

    def test_armor_pieces_shuffled_own(self) -> None:
        self.shuffled_item("Abyssal Armor Piece", count = 7)

    def test_armor_absent(self) -> None:
        self.absent_item("Abyssal Armor")

class TestArmorArmorSanity(DSTestBase):
    options = {
        "armor": "armorsanity_armor",
        "armor_pieces": 7
        }

    def test_armor_pieces_absent(self) -> None:
        self.absent_item("Abyssal Armor Piece")

    def test_armor_shuffled(self) -> None:
        self.shuffled_item("Abyssal Armor")