# Secret-Santa
A Python utility for creating Secret Santa matches.

This script takes in a list of names and emails and then matches them up into pairs, and sends that pairing information to the gift giver. A master copy is then stored on the server, and can optionally be sent to another email address.

## Getting Started
Easy clone:
```
git clone https://github.com/JeremyEudy/Secret-Santa
```

## Usage
Load names and emails from structured input files (currently supports .json and .csv), or manually input users.

```
python3 Secret-Santa.py -t <file type> -i <input file> -m <master email destination>
```

Input files need to be structured the same way as the sample files in order to be parsed correctly.
