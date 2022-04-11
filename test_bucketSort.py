from bucketSort import sort

def testsortempty():
    inputarray = []
    expectedarray = []
    assert sort(inputarray) == expectedarray

def testsort1item():
    inputarray = [1]
    expectedarray = [1]
    assert sort(inputarray) == expectedarray