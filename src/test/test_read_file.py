import json

with open("original.txt") as f:
        data = f.read()
origial_dict = json.loads(data)


def test_readfile():
    assert len(origial_dict) == 7