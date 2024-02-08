homograph1 = "Homograph.py"
homograph2 = "..//Homograph.py"

if pos_tags == pos_tags2:
    return f"{word1} and {word2} are homographs with same part of speech tags."
else:
    return f"{word1} and {word2} are  homographs with different part of speech tags."

testcase1 = "test 1: homograph test Homograph.py == ..//Homograph.py"

result = homograph_compare(homograph1, homograph2)
expected_result = f"{homograph1} and {homograph2} are homographs with the same part of speech"

testcase2 = "test 2: homograph test Homograph.py == ././..Homograph.py"

testcase3 = "test 3: homograph test Homograph.py == .///.//Homograph.py"

