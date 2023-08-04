from main import print_hi

def test_unique_elements():
    result = print_hi([1, 2, 3, 4])
    assert result == "List has unique elements"

def test_duplicate_elements():
    result = print_hi([1, 2, 2, 4])
    assert result == "List has duplicate elements"
