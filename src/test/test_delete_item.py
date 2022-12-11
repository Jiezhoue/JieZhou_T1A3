items = {
    "1": {
        "name": "APPLE CRUMBLE CUPCAKE",
        "price": 5.5,
        "qty": 20
    },
    "2": {
        "name": "BANANA BREAD LATTE CUPCAKE",
        "price": 3.5,
        "qty": 0
    },
    "3": {
        "name": "CHOC VANILLA CUPCAKE",
        "price": 4.5,
        "qty": 40
    },
    "4": {
        "name": "RED VELVET CUPCAKE",
        "price": 8.5,
        "qty": 13
    },
    "5": {
        "name": "ROCKY ROAD CUPCAKE",
        "price": 7.5,
        "qty": 23
    }, 
    "6": {
        "name": "STRAWBERRY CUPCAKE",
        "price": 6,
        "qty": 10
    }, 
    "7": {
        "name": "MIX CHRISTMAS BOX",
        "price": 36,
        "qty": 8
    }
}

def delete_item(item_no, list):
    if list[item_no]["qty"] > 0:
        list[item_no]["qty"] -= 1
    elif list[item_no]["qty"] == 0:
        return "No items"
    
delete_item("1" , items)

def test_delete():
    assert items["1"]["qty"] == 19
    assert delete_item("2", items) == "No items"

    