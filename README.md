# Matchbox

Count occurrences of a regex pattern in PDF or RTF files.

## Usage

```bash
matchbox data/file.pdf --pattern '^\d{4}$'
```

Or as a module from the project root:

```bash
python3 -m src data/file.pdf --pattern '^\d{4}$'
```

RTF files are also supported — the file type is detected by extension:

```bash
matchbox data/file.rtf --pattern '\d{4}'
```

## Installation

```bash
pip install -e .
```

## Running Tests

```bash
python3 -m unittest discover tests
```
