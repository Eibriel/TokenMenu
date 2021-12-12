lexicon = {
    "ICE-CREAM": {
        "ICE-CREAM-N1": {
            "DEFINITION": "",
            "EXAMPLE": "",

            "CAT": "N",
            "SYNTACTIC-STRUCTURE": {
                "ROOT": "$VAR0",
                "CAT": "N"
            },
            "SEMANTIC-STRUCTURE": "ICE-CREAM",
        }
    },

    "EAT": {
        "EAT-V1": {
            "DEFINITION": "ingest",
            "EXAMPLE": "He was eating (cheese).",

            "SYNTACTIC-STRUCTURE": [
                {
                    "SUBJECT": {
                        "ROOT": "$VAR1",
                        "CAT": "N"
                    },
                    "ROOT": "$VAR0",
                    "CAT": "V",
                    "DIRECTOBJECT": {
                        "ROOT": "$VAR2",
                        "OPT": "+",  # OPTIONAL
                        "CAT": "N"
                    }
                }
            ],

            "SEMANTIC-STRUCTURE": {
                "INGEST": {
                    "AGENT": "^$VAR1",  # ^ -> the meaning of
                    "BENEFICIARY": {
                        "VALUE": "^$VAR2",  # ^ -> the meaning of
                        "SEM": "FOOD"
                    }
                }
            }
        }
    }
}
