from test.bases import WorldTestBase

from ..World import DSWorld

class DSTestBase(WorldTestBase):
    
    game = "Darksiders"
    world: DSWorld


# The actual tests you write should be in files whose names start with "test_".
# Ideally, you should group similar tests together in one file, where each file has some overarching significance.

# The best order to read these tests in is:
# 1. test_easy_mode.py
# 2. test_hard_mode.py
# 3. test_extra_starting_chest.py
# 4. test_hammer.py
