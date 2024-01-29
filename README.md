# 1-Decide

## File structure

```
1-Decide/
│
├── src/                        # Source files
│   ├── __init__.py             # Makes `src` a Python package
│   ├── decide.py               # Main DECIDE function and logic
│   ├── lic_conditions.py       # Definitions of the LIC conditions
│   ├── utils.py                # Utility functions, e.g., distance calculation, angle computation
│   └── data_structures.py      # Definitions of custom data structures, e.g., PARAMETERS, POINTS
│
├── tests/                      # Automated tests
│   ├── __init__.py             # Makes tests a Python package
│   ├── test_decide.py          # Tests for the DECIDE function
│   ├── test_lic_conditions.py  # Tests for individual LIC conditions
│   └── test_utils.py           # Tests for utility functions
│
├── docs/                       # Documentation
│   └── README.md               # Technical documentatoion
│
├── examples/                   # Example scripts and data
│   ├── example_input.py        # Example inputs to the system
│   └── run_example.py          # Script to run the system with example inputs
│
├── main.py             	# Main entry point of the program
│
├── requirements.txt            # Project dependencies
│
├── decide.pdf                  # Technical Specification
│
├── requirements.txt            # Project dependencies
│
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

TODO...

## Contributors

TODO...
