from ..Locations import ARTIFACTS_LOCATIONS
from .bases import DSTestBase

class TestArtifactRemoved(DSTestBase):
    options = {
        "artifacts": "remove",
        "soldier_artifacts": 15,
        "champion_artifacts": 2
        }

    def test_soldier_artifacts_absent(self) -> None:
        self.absent_item("Soldier Artifact")

    def test_champion_artifacts_absent(self) -> None:
        self.absent_item("Champion Artifact")

    def test_overlord_artifact_absent(self) -> None:
        self.absent_item("Overlord Artifact")

class TestArtifactVanilla(DSTestBase):
    options = {
        "artifacts": "vanilla",
        "soldier_artifacts": 15,
        "champion_artifacts": 2
        }

    def test_soldier_artifacts_vanilla(self) -> None:
        self.vanilla_item("Soldier Artifact", ARTIFACTS_LOCATIONS, count = 20)

    def test_champion_artifacts_vanilla(self) -> None:
        self.vanilla_item("Champion Artifact", ARTIFACTS_LOCATIONS, count = 6)

    def test_overlord_artifact_vanilla(self) -> None:
        self.vanilla_item("Overlord Artifact", ARTIFACTS_LOCATIONS)

class TestArtifactOwn(DSTestBase):
    options = {
        "artifacts": "own",
        "soldier_artifacts": 15,
        "champion_artifacts": 2
        }

    def test_soldier_artifacts_shuffled_own(self) -> None:
        self.shuffled_item_local("Soldier Artifact", count = 15)

    def test_champion_artifacts_shuffled_own(self) -> None:
        self.shuffled_item_local("Champion Artifact", count = 2)

    def test_overlord_artifact_shuffled_own(self) -> None:
        self.shuffled_item_local("Overlord Artifact")

class TestArtifactArtisanity(DSTestBase):
    options = {
        "artifacts": "artisanity",
        "soldier_artifacts": 15,
        "champion_artifacts": 2
        }

    def test_soldier_artifacts_shuffled(self) -> None:
        self.shuffled_item("Soldier Artifact", count = 15)

    def test_champion_artifacts_shuffled(self) -> None:
        self.shuffled_item("Champion Artifact", count = 2)

    def test_overlord_artifact_shuffled(self) -> None:
        self.shuffled_item("Overlord Artifact")