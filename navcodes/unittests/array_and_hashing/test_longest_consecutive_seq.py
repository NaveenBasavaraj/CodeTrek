# tests/test_longest_consecutive.py
import pytest
from navcodes.array_and_hashing.longest_consecutive_seq import LongestConsecutive

@pytest.fixture
def solver():
    return LongestConsecutive()

# Test cases: (input, expected_longest_length)
CASES = [
    ([100, 4, 200, 1, 3, 2], 4),        # example: sequence 1,2,3,4
    ([], 0),                           # empty list -> 0
    ([5], 1),                          # single element -> 1
    ([1,2,0,1], 3),                    # 0,1,2 -> length 3 (duplicates tolerated)
    ([9,1,4,7,3,-1,0,5,8,-1,6], 7),    # consecutive 3..9 -> length 7
    (list(range(1000)), 1000),         # large unique consecutive => full length
    ([1,3,5,7], 1),                    # no consecutive neighbors -> 1
]

@pytest.mark.parametrize("method_name", ["brute_force", "using_hash_set", "using_hash_maps"])
@pytest.mark.parametrize("nums, expected", CASES)
def test_all_methods_return_expected_lengths(solver, method_name, nums, expected):
    """
    Run the same cases against all three implementations.
    All should return the same integer result.
    """
    method = getattr(solver, method_name)
    assert method(nums) == expected

def test_duplicate_values_do_not_break_logic(solver):
    nums = [1, 2, 2, 3, 3, 4]
    # longest consecutive is 1,2,3,4 => length 4
    assert solver.brute_force(nums) == 4
    assert solver.using_hash_set(nums) == 4
    assert solver.using_hash_maps(nums) == 4
