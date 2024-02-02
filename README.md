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

## Contributors

Olle Jenrström
Love Lindgren
Selma Özdere
Siham Shahoud

# Statement of contribution

The work was devided as follows:

Olle Jenrström: PUM, FUV, README and DECIDE

Love Lindgren: LIC1, LIC4, LIC7, LIC10, LIC13 and their test functions

Siham Shahoud: LIC2, LIC5, LIC8, LIC11, LIC14 and their test functions

Selma Özdere: LIC0, LIC3, LIC6, LIC9, LIC12 and their test functions
