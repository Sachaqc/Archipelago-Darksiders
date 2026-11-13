from ..Locations import SCYTHE_LOCATIONS
from .bases import DSTestBase

class TestStartScytheRemoved(DSTestBase):
    options = {
        "scythe": "remove",
        "weapons": "start_with_scythe"
        }

    def test_hellraiser_start_with(self) -> None:
        self.start_with_item("Hellraiser")

    def test_harvester_absent(self) -> None:
        self.absent_item("Harvester")

    def test_progressive_absent(self) -> None:
        self.absent_item("Progressive Scythe")

    def test_scythe_lvl_shuffled(self) -> None:
        self.shuffled_item("Scythe Level Up", count = 3)

class TestScytheRemoved(DSTestBase):
    options = {
        "scythe": "remove",
        "weapons": "start_with_sword"
        }

    def test_hellraiser_absent(self) -> None:
        self.absent_item("Hellraiser")

    def test_harvester_absent(self) -> None:
        self.absent_item("Harvester")

    def test_progressive_absent(self) -> None:
        self.absent_item("Progressive Scythe")

    def test_scythe_lvl_absent(self) -> None:
        self.absent_item("Scythe Level Up")

class TestStartScytheVanilla(DSTestBase):
    options = {
        "scythe": "vanilla",
        "weapons": "start_with_scythe"
        }

    def test_hellraiser_vanilla(self) -> None:
        self.vanilla_item("Hellraiser", SCYTHE_LOCATIONS)

    def test_harvester_vanilla(self) -> None:
        self.vanilla_item("Harvester", SCYTHE_LOCATIONS)

    def test_progressive_absent(self) -> None:
        self.absent_item("Progressive Scythe")

    def test_scythe_lvl_shuffled(self) -> None:
        self.shuffled_item("Scythe Level Up", count = 3)

class TestScytheVanilla(DSTestBase):
    options = {
        "scythe": "vanilla",
        "weapons": "start_with_sword"
        }

    def test_hellraiser_vanilla(self) -> None:
        self.vanilla_item("Hellraiser", SCYTHE_LOCATIONS)

    def test_harvester_vanilla(self) -> None:
        self.vanilla_item("Harvester", SCYTHE_LOCATIONS)

    def test_progressive_absent(self) -> None:
        self.absent_item("Progressive Scythe")

    def test_scythe_lvl_shuffled(self) -> None:
        self.shuffled_item("Scythe Level Up", count = 3)

class TestStartScytheHellraiser(DSTestBase):
    options = {
        "scythe": "hellraiser",
        "weapons": "start_with_scythe"
        }

    def test_hellraiser_start_with(self) -> None:
        self.start_with_item("Hellraiser")

    def test_harvester_absent(self) -> None:
        self.absent_item("Harvester")

    def test_progressive_absent(self) -> None:
        self.absent_item("Progressive Scythe")

    def test_scythe_lvl_shuffled(self) -> None:
        self.shuffled_item("Scythe Level Up", count = 3)

class TestScytheHellraiser(DSTestBase):
    options = {
        "scythe": "hellraiser",
        "weapons": "start_with_sword"
        }

    def test_hellraiser_shuffled(self) -> None:
        self.shuffled_item("Hellraiser")

    def test_harvester_absent(self) -> None:
        self.absent_item("Harvester")

    def test_progressive_absent(self) -> None:
        self.absent_item("Progressive Scythe")

    def test_scythe_lvl_shuffled(self) -> None:
        self.shuffled_item("Scythe Level Up", count = 3)

class TestStartScytheHarvester(DSTestBase):
    options = {
        "scythe": "harvester",
        "weapons": "start_with_scythe"
        }

    def test_hellraiser_absent(self) -> None:
        self.absent_item("Hellraiser")

    def test_harvester_start_with(self) -> None:
        self.start_with_item("Harvester")

    def test_progressive_absent(self) -> None:
        self.absent_item("Progressive Scythe")

    def test_scythe_lvl_shuffled(self) -> None:
        self.shuffled_item("Scythe Level Up", count = 3)

class TestScytheHarvester(DSTestBase):
    options = {
        "scythe": "harvester",
        "weapons": "start_with_sword"
        }

    def test_hellraiser_absent(self) -> None:
        self.absent_item("Hellraiser")

    def test_harvester_shuffled(self) -> None:
        self.shuffled_item("Harvester")

    def test_progressive_absent(self) -> None:
        self.absent_item("Progressive Scythe")

    def test_scythe_lvl_shuffled(self) -> None:
        self.shuffled_item("Scythe Level Up", count = 3)

class TestStartScytheProgressive(DSTestBase):
    options = {
        "scythe": "progressive", 
        "weapons": "start_with_scythe"
        }

    def test_hellraiser_absent(self) -> None:
        self.absent_item("Hellraiser")

    def test_harvester_absent(self) -> None:
        self.absent_item("Harvester")

    def test_progressive_start_with(self) -> None:
        self.start_with_item("Progressive Scythe", total_count = 2)

    def test_scythe_lvl_shuffled(self) -> None:
        self.shuffled_item("Scythe Level Up", count = 3)

class TestScytheProgressive(DSTestBase):
    options = {
        "scythe": "progressive",
        "weapons": "start_with_sword"
        }

    def test_hellraiser_absent(self) -> None:
        self.absent_item("Hellraiser")

    def test_harvester_absent(self) -> None:
        self.absent_item("Harvester")

    def test_progressive_shuffled(self) -> None:
        self.shuffled_item("Progressive Scythe", count = 2)

    def test_scythe_lvl_shuffled(self) -> None:
        self.shuffled_item("Scythe Level Up", count = 3)