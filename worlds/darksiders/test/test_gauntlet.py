from .bases import DSTestBase

class TestGauntletStart(DSTestBase):
    options = {
        "weapons": "start_with_gauntlet"
        }

    def test_gauntlet_start_with(self) -> None:
        self.start_with_item("Tremor Gauntlet")

    def test_gauntlet_lvl_shuffled(self) -> None:
        self.shuffled_item("Gauntlet Level Up", count = 3)

class TestGauntlet(DSTestBase):
    options = {
        "weapons": "start_with_sword"
        }

    def test_tremor_gauntlet_shuffled(self) -> None:
        self.shuffled_item("Tremor Gauntlet")

    def test_gauntlet_lvl_shuffled(self) -> None:
        self.shuffled_item("Gauntlet Level Up", count = 3)