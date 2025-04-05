def generate_mob_prompt():
    mob_types = {
        "small": {
            "name": "give a name for a small/weak fantasy creature",
            "status": "hostile",
            "health": "10 - 50",
            "type": "ground or flying",
            "entry_prompt": "write a short little entry message for when the creature enters, like it's talking to the player. This creature is a small creature that really won't be a pest to the player except for early game."
        },
        "medium": {
            "name": "give a name for a medium/strong fantasy creature",
            "status": "hostile",
            "health": "50 - 100",
            "type": "ground or flying",
            "entry_prompt": "write a short little entry message for when the creature enters, like it's talking to the player. This creature is a medium creature that can maybe be a problem but not a whole lot."
        },
        "large": {
            "name": "give a name for a large/really strong fantasy creature",
            "status": "hostile",
            "health": "100 - 200",
            "type": "ground or flying",
            "entry_prompt": "write a short little entry message for when the creature enters, like it's talking to the player. This creature is a large creature that can be a problem for the player."
        },
        "boss": {
            "name": "give a name for a boss fantasy creature",
            "status": "hostile",
            "health": "200 - 1000",
            "type": "ground or flying",
            "entry_prompt": "write a short little entry message for when the creature enters, like it's talking to the player. This creature is a boss, it should be scary."
        }
    }
