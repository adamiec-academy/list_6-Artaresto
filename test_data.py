GENERATE_ASSIGNMENTS_DATA = [
    (
        {

        },
        [
            "A",
            "B",
            "C",
        ]
    ),
    (
        {
            "A" : "B",
            "B" : "C",
            "C" : "D",
        },
        [
            "A",
            "B",
            "C",
            "D",
            "E",
        ]
    ),
    (
        {
            "A" : "B",
            "Z" : "Y",
            "W" : "Z",
            "Y" : "W",
        },
        [
            "A",
            "B",
            "C",
        ]
    ),
    (
        {
            "A" : "B",

        },
        [
            "A",
            "B",
            "C",
        ]
    ),
    (
        {
            "A" : "A",
            "B" : "A",
            "C" : "A",
            "D" : "A",
            "E" : "A",
            "F" : "A",
            "G" : "A",

        },
        [
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
        ]
    ),
]


GET_SEATS_DATA = [
    (   # 30: Rybnik
        9,
        {
            "PiS": 161160,
            "PO": 92493,
            "SLD": 32300,
            "Konfederacja": 23939,
            "PSL": 18816,
        },
        {
            "PiS": 5,
            "PO": 3,
            "SLD": 1,
            "Konfederacja": 0,
            "PSL": 0,
        }
    ),
    (   # 3: Wrocław
        14,
        {
            "PiS": 226915,
            "PO": 214629,
            "SLD": 100843,
            "Konfederacja": 48775,
            "PSL": 42269,
        },
        {
            "PiS": 5,
            "PO": 5,
            "SLD": 2,
            "Konfederacja": 1,
            "PSL": 1,
        }
    ),
    (   # 24: Białystok
        14,
        {
            "PiS": 270888,
            "PO": 109527,
            "PSL": 48566,
            "SLD": 47342,
            "Konfederacja": 36207,
            
        },
        {
            "PiS": 8,
            "PO": 3,
            "SLD": 1,
            "Konfederacja": 1,
            "PSL": 1,
        }
    ),
    (   # 21: Opole
        12,
        {
            "PiS": 152999,
            "PO": 108570,
            "SLD": 47699,
            "PSL": 41901,
            "Mniejszość Niemiecka": 32094,
            "Konfederacja": 23176,
            
        },
        {
            "PiS": 5,
            "PO": 4,
            "SLD": 1,
            "PSL": 1,
            "Mniejszość Niemiecka": 1,
            "Konfederacja": 0,
        }
    ),
]


PLAY_DATA = [
    (
        [
            [".", ".", "."], 
            [".", ".", "."], 
            [".", ".", "."], 
        ],
        7,
        [
            [".", ".", "."], 
            [".", ".", "."], 
            [".", ".", "."], 
        ],        
    ),
    (
        [
            [".", ".", ".", ".", ".", ".", ".",], 
            [".", ".", ".", "X", ".", ".", ".",], 
            [".", ".", ".", "X", ".", ".", ".",], 
            [".", ".", ".", "X", ".", ".", ".",], 
            [".", ".", ".", ".", ".", ".", ".",], 
        ],
        13,
        [
            [".", ".", ".", ".", ".", ".", ".",], 
            [".", ".", ".", ".", ".", ".", ".",], 
            [".", ".", "X", "X", "X", ".", ".",], 
            [".", ".", ".", ".", ".", ".", ".",], 
            [".", ".", ".", ".", ".", ".", ".",], 
        ],        
    ),
    (
        [
            [".", ".", ".", "."], 
            [".", "X", "X", "."], 
            [".", "X", "X", "."], 
            [".", ".", ".", "."], 
        ],
        9,
        [
            [".", ".", ".", "."], 
            [".", "X", "X", "."], 
            [".", "X", "X", "."], 
            [".", ".", ".", "."], 
        ],        
    ),
    (
        [
            [".", ".", ".", ".", ".", ".", ".",], 
            [".", "X", ".", "X", "X", "X", ".",], 
            [".", "X", ".", "X", ".", ".", ".",], 
            [".", "X", "X", "X", "X", "X", ".",], 
            [".", ".", ".", "X", ".", "X", ".",], 
            [".", "X", "X", "X", ".", "X", ".",],
            [".", ".", ".", ".", ".", ".", ".",], 
        ],
        5,
        [
            [".", ".", ".", ".", ".", ".", ".",], 
            [".", "X", ".", ".", "X", "X", ".",], 
            [".", "X", ".", ".", ".", ".", ".",], 
            [".", ".", ".", ".", ".", ".", ".",], 
            [".", ".", ".", ".", ".", "X", ".",], 
            [".", "X", "X", ".", ".", "X", ".",],
            [".", ".", ".", ".", ".", ".", ".",], 
        ],        
    ),
    (
        [
            [".", ".", ".", ".", ".", ".", ".",], 
            [".", "X", ".", "X", "X", "X", ".",], 
            [".", "X", ".", "X", ".", ".", ".",], 
            [".", "X", "X", "X", "X", "X", ".",], 
            [".", ".", ".", "X", ".", "X", ".",], 
            [".", "X", "X", "X", ".", "X", ".",],
            [".", ".", ".", ".", ".", ".", ".",], 
        ],
        6,
        [
            [".", ".", ".", ".", ".", ".", ".",], 
            [".", ".", ".", ".", ".", ".", ".",], 
            [".", ".", ".", ".", ".", ".", ".",], 
            [".", ".", ".", ".", ".", ".", ".",], 
            [".", ".", ".", ".", ".", ".", ".",], 
            [".", ".", ".", ".", ".", ".", ".",],
            [".", ".", ".", ".", ".", ".", ".",], 
        ],        
    ),
]
