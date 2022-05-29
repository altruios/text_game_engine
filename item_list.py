from item import Item


potions_map={
    "health":"a drink from this and you'll be fine",
    "defence":"a drink from this and you'll be strong",
    "wit":"a drink from this and you'll be smart",
    "speed":"a drink from this and you'll be fast",
    "vision":"a drink from this and you'll see far",
    "dexterity":"a drink from this and you'll have clever hands",
    "wisdom":"a drink from this and you'll know what to do",
    "confidence":"a drink from this and you'll be sure of yourself",
    "fear":"a drink from this and you'll be afraid",
    "misery":"a drink from this and you'll be in misery",
    "hate":"a drink from this and you're blood will boil",
    "delerium":"a drink from this and you'll see sounds and hear lights",
    "love":"a drink from this and you'll phyiscially vommit",
    "happy":"a drink from this and you'll be euphoric",
    "doom":"a drink from this and you won't be fine",
    "anxiety":"a drink from this and you'll be overprepared",
    "dreams":"a drink from this and you'll have vivid dreams",
    "desire":"a drink from this and you'll be desirable",
    "risk":"a drink from this and you will be unaware of risk",
    "spite":"a drink from this and you'll be spiteful",
    "determination":"a drink from this and you'll perciver",
    "honesty":"a drink from this and you'll be honest",
    "calm":"a drink from this and you'll be calm",
    "sad":"a drink from this and you'll be sad",
    "curiosity":"a drink from this and you'll be curious",
    "level":"a drink from this and you'll level up",
    "respawn":"a drink from this and you'll respawn",
}
keys_map={
    "wood key":"a key of wood",
    "stone key":"a key of stone",
    "obsidian key":"a key of obsidian",
    "iron key":"a key of iron",
    "steel key":"a key of steel",
    "soul key":"a key to the heart",
}
items_map={
    "button":"a shiny button",
    "cloth":"a bit of linen",
    "book":"a story book",
}
weapons_map={
    "sword":"a long sword - cheap and rusty",
    "cane":"a stick of wood - used for walking"
} 

potions=[Item(x,1,y) for  x,y in potions_map.items()]
keys=[Item(x,1,y) for  x,y in keys_map.items()]
items=[Item(x,1,y) for  x,y in items_map.items()]
weapons=[Item(x,1,y) for  x,y in weapons_map.items()]
_item_list=[]
for x in potions:
    _item_list.append(x)
for x in items:
    _item_list.append(x)
for x in keys:
    _item_list.append(x)
for x in weapons:
    _item_list.append(x)

def get_item(item_name):
    for x in _item_list:
        print("searching")
        if x.name==item_name:
            return x
    return None