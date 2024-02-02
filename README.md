# 1-Decide

## File structure

```
1-Decide/
│
├── src/                        # Source files
│   ├── __init__.py             # Makes `src` a Python package
│   ├── decide.py               # Main DECIDE function and logic
│   └── ...                     # Source code
│
├── tests/                      # Automated tests
│   ├── __init__.py             # Makes tests a Python package
│   └── ...                     # Unittests
│
├── docs/                       # Documentation
│   └── README.md               # Technical documentatoion
│
├── main.py                 	# Main entry point of the program
├── requirements.txt            # Project dependencies
├── decide.pdf                  # Technical Specification
├── requirements.txt            # Project dependencies
└── README.md                   # This file. General project documentation
```

## Quickstart

### 1. Create a virtual envrionment called `venv`

Mac/Linux: `python3 -m venv venv`

Windows: `python -m venv venv`

### 2. Activate the venv

Mac/Linux: `source venv/bin/activate`

Windows: `venv/bin/Activate.ps1`

### 3. Install the dependencies

Mac/Linux: `python3 -m pip install -r requirements.txt`

Windows: `python -m pip install -r requirements.txt`

### 4. Run the program

Mac/Linux: `python3 main.py`

Windows: `python main.py`

## Code style

Ruff is used for linting the project. Lint the code by using `ruff .`

Black is used for formatting the procjet. Format the code by using `black .`

## Running the test suite

Run `pystest` from the root

## Way of working

Based on the Essence standard v1.2 criteria for evaluating a team's way of working, our team is currently at the "Foundation Established" stage because we have picked the main practices and tools we need to work together, but we haven't started using them in our actual work yet. The reason we're here is that we're a new team with some members who are new to coding and using tools like git, and we're facing challenges in communicating effectively, partly because we use Discord poorly and we have team members who speak different languages and English is no ones first language. This makes it hard for everyone to understand each other well. To move to the "In Use" stage, where we're supposed to be actively using our chosen practices and tools, we need to get better at complying to the assignment instructions, find better ways to communicate despite our language differences, and maybe look for other tools that can help us work together more smoothly.

## Contributors

- Olle Jenrström
- Love Lindgren
- Selma Özdere
- Siham Shahoud
