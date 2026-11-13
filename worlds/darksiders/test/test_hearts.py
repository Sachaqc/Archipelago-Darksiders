from ..Locations import HEARTS_LOCATIONS
from .bases import DSTestBase

class TestHeartsRemoved(DSTestBase):
    options = {
        "hearts": "remove"
        }

    def test_hearts_absent(self) -> None:
        self.absent_item("Heart of the Chosen")

class TestHeartsVanilla(DSTestBase):
    options = {
        "hearts": "vanilla"
        }

    def test_hearts_vanilla(self) -> None:
        self.vanilla_item("Heart of the Chosen", HEARTS_LOCATIONS, count = 4)

class TestHeartsOwn(DSTestBase):
    options = {
        "hearts": "own"
        }

    def test_hearts_own(self) -> None:
        self.shuffled_item_local("Heart of the Chosen", count = 4)

class TestHeartsSanity(DSTestBase):
    options = {
        "hearts": "heartsanity"
        }

    def test_hearts_anywhere(self) -> None:
        self.shuffled_item("Heart of the Chosen", count = 4)