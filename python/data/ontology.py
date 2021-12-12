ontology = {
    "ICE-CREAM": {
        "IS-A": "FOOD"
    },

    "FOOD": {
        "IS-A": "GOOD",
        "HAS-KIND": "ICE-CREAM",
        "USED-BY": "ANIMAL"
    },

    "EAT": {
        "IS-A": "EVENT",
        "HAS-KIND": "ICE-CREAM",
        "USED-BY": "ANIMAL"
    },

    "HAPPINESS": {
        "DOMAIN": "ANIMAL",
        "RANGE": [0, 1]
    },

    "PURCHASING": {
        "IS-A": {
            "VALUE": "HUMAN-ACTIVITY"
        },
        "AGENT": {
            "DEFAULT": "SELLER",
            "SEM": "HUMAN",
            "RELAXABLE-TO": "SOCIAL-OBJECT"
        },
        "THEME": {
            "DEFAULT": "GOOD"
        },
        "INSTRUMENT": {
            "SEM": "MONEY"
        },
        "HAS-EVENT-AS-PART": {
            "SEM": ["BUY", "SELL"]
        },
        "LOCATION": {
            "DEFAULT": "CITY",
            "SEM": "PLACE",
            "RELAXABLE-TO": "PHYSICAL-OBJECT"
        }
    }
}
