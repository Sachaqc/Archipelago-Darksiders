from ..Locations import ARTIFACTS_LOCATIONS
from .bases import DSTestBase

class TestArtifactRemoved(DSTestBase):
    options = {
        "artifacts": "remove",
        "soldier_artifacts": 15,
        "champion_artifacts": 2
        }

    def test_soldier_artifacts_absent(self) -> None:
        soldier_artifacts = self.get_items_by_name("Soldier Artifact")

        with self.subTest("Test that there are no Soldier Artifact in the pool"):
            self.assertEqual(len(soldier_artifacts), 0)

        with self.subTest("Test that no Soldier Artifact are placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Soldier Artifact"))

    def test_champion_artifacts_absent(self) -> None:
        champion_artifacts = self.get_items_by_name("Champion Artifact")

        with self.subTest("Test that there are no Champion Artifact in the pool"):
            self.assertEqual(len(champion_artifacts), 0)

        with self.subTest("Test that no Champion Artifact is placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Champion Artifact"))

    def test_overlord_artifact_absent(self) -> None:
        overlord_artifacts = self.get_items_by_name("Overlord Artifact")

        with self.subTest("Test that there is no Overlord Artifact in the pool"):
            self.assertEqual(len(overlord_artifacts), 0)

        with self.subTest("Test that no Overlord Artifact is placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Overlord Artifact"))

class TestArtifactVanilla(DSTestBase):
    options = {
        "artifacts": "vanilla",
        "soldier_artifacts": 15,
        "champion_artifacts": 2
        }

    def test_soldier_artifacts_vanilla(self) -> None:
        soldier_artifacts = self.get_items_by_name("Soldier Artifact")

        with self.subTest("Test that there is no Soldier Artifact in the pool"):
            self.assertEqual(len(soldier_artifacts), 0)

        with self.subTest("Test that Soldier Artifact are placed at all their vanilla location"):
            self.assertTrue(all(Location for Location in self.multiworld.get_locations() if Location.name in ARTIFACTS_LOCATIONS and Location.item and Location.item.name == "Soldier Artifact"))
    
        with self.subTest("Test that no Soldier Artifact is placed outside its vanilla location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.name not in ARTIFACTS_LOCATIONS and Location.item and Location.item.name == "Soldier Artifact"))
    
        with self.subTest("Test that there are exactly 20 Soldier Artifact vanilla location"):
            SOLDIER_ARTIFACT_LOCATIONS = {location: item for location, item in ARTIFACTS_LOCATIONS.items() if item == "Soldier Artifact"}
            self.assertEqual(len(SOLDIER_ARTIFACT_LOCATIONS), 20)

    def test_champion_artifacts_vanilla(self) -> None:
        champion_artifacts = self.get_items_by_name("Champion Artifact")

        with self.subTest("Test that there is no Champion Artifact in the pool"):
            self.assertEqual(len(champion_artifacts), 0)

        with self.subTest("Test that Champion Artifacts are placed at all their vanilla location"):
            self.assertTrue(all(Location for Location in self.multiworld.get_locations() if Location.name in ARTIFACTS_LOCATIONS and Location.item and Location.item.name == "Champion Artifact"))
    
        with self.subTest("Test that no Champion Artifact is placed outside its vanilla location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.name not in ARTIFACTS_LOCATIONS and Location.item and Location.item.name == "Champion Artifact"))
    
        with self.subTest("Test that there are exactly 6 Champion Artifact vanilla location"):
            CHAMPION_ARTIFACT_LOCATIONS = {location: item for location, item in ARTIFACTS_LOCATIONS.items() if item == "Champion Artifact"}
            self.assertEqual(len(CHAMPION_ARTIFACT_LOCATIONS), 6)

    def test_overlord_artifact_vanilla(self) -> None:
        overlord_artifacts = self.get_items_by_name("Overlord Artifact")

        with self.subTest("Test that there is no Overlord Artifact in the pool"):
            self.assertEqual(len(overlord_artifacts), 0)

        with self.subTest("Test that the Overlord Artifacts is placed at its vanilla location"):
            self.assertTrue(all(Location for Location in self.multiworld.get_locations() if Location.name in ARTIFACTS_LOCATIONS and Location.item and Location.item.name == "Overlord Artifact"))
    
        with self.subTest("Test that no Overlord Artifact is placed outside its vanilla location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.name not in ARTIFACTS_LOCATIONS and Location.item and Location.item.name == "Overlord Artifact"))
    
        with self.subTest("Test that there is exactly 1 Overlord Artifact vanilla location"):
            OVERLORD_ARTIFACT_LOCATIONS = {location: item for location, item in ARTIFACTS_LOCATIONS.items() if item == "Overlord Artifact"}
            self.assertEqual(len(OVERLORD_ARTIFACT_LOCATIONS), 1)

class TestArtifactOwn(DSTestBase):
    options = {
        "artifacts": "own",
        "soldier_artifacts": 15,
        "champion_artifacts": 2
        }

    def test_soldier_artifacts_shuffled_own(self) -> None:
        soldier_artifacts = self.get_items_by_name("Soldier Artifact")

        with self.subTest("Test that the number of Soldier Artifact in the pool is exactly as the Options expect"):
            self.assertEqual(len(soldier_artifacts), 15)

        with self.subTest("Test that all Soldier Artifact are part of the local item pool"):
            self.assertIn("Soldier Artifact", self.multiworld.worlds[1].options.local_items)

    def test_champion_artifacts_shuffled_own(self) -> None:
        champion_artifacts = self.get_items_by_name("Champion Artifact")

        with self.subTest("Test that the number of Champion Artifact in the pool is exactly as the Options expect"):
            self.assertEqual(len(champion_artifacts), 2)

        with self.subTest("Test that all Champion Artifact are part of the local item pool"):
            self.assertIn("Champion Artifact", self.multiworld.worlds[1].options.local_items)

    def test_overlord_artifact_shuffled_own(self) -> None:
        overlord_artifacts = self.get_items_by_name("Overlord Artifact")

        with self.subTest("Test that there is exactly one Overlord Artifact in the pool"):
            self.assertEqual(len(overlord_artifacts), 1)

        with self.subTest("Test that all Overlord Artifact are part of the local item pool"):
            self.assertIn("Overlord Artifact", self.multiworld.worlds[1].options.local_items)

class TestArtifactArtisanity(DSTestBase):
    options = {
        "artifacts": "artisanity",
        "soldier_artifacts": 15,
        "champion_artifacts": 2
        }

    def test_soldier_artifacts_shuffled(self) -> None:
        soldier_artifacts = self.get_items_by_name("Soldier Artifact")

        with self.subTest("Test that the number of Soldier Artifact in the pool is exactly as the Options expect"):
            self.assertEqual(len(soldier_artifacts), 15)

        with self.subTest("Test that no Soldier Artifact are part of the local item pool"):
            self.assertNotIn("Soldier Artifact", self.multiworld.worlds[1].options.local_items)

    def test_champion_artifacts_shuffled(self) -> None:
        champion_artifacts = self.get_items_by_name("Champion Artifact")

        with self.subTest("Test that the number of Champion Artifact in the pool is exactly as the Options expect"):
            self.assertEqual(len(champion_artifacts), 2)

        with self.subTest("Test that no Champion Artifact are part of the local item pool"):
            self.assertNotIn("Champion Artifact", self.multiworld.worlds[1].options.local_items)

    def test_overlord_artifact_shuffled(self) -> None:
        overlord_artifacts = self.get_items_by_name("Overlord Artifact")

        with self.subTest("Test that there is exactly one Overlord Artifact in the pool"):
            self.assertEqual(len(overlord_artifacts), 1)

        with self.subTest("Test that no Overlord Artifact are part of the local item pool"):
            self.assertNotIn("Overlord Artifact", self.multiworld.worlds[1].options.local_items)