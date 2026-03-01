# Match Counter

## Prerequisites

- Python 3.x

## Usage

From the project root directory, run:

```bash
python3 -m src <path_to_rtf_file> <regex_pattern>
```

Example:
```bash
python3 -m src data/test-data.rtf "Hello"
```


## Options

Run with `--help` to see all available arguments:

```bash
python3 -m src --help
```

## Running Tests

To run all unit tests, use the following command:

```bash
python3 -m unittest discover tests
```
