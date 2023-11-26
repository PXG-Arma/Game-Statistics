# PXG Game Statistics

Statistics data of Phoenix Group ops, and tools to analyze it.
For the purposes of improving member experience, accountability, and, occasionally, boasting.


## Repo Structure

- `/data`: raw statistics data in plain text form
- `/scripts`: executable scripts for data analysis


## Data Format

Data is contained in plain text files and organized in columns. Column separator is the horizontal tab character, which allows easy import into any spreadsheet software. The first line of each file contains column headers.

The files are named by the following convention:
```text
{year}-{quarter}-{data type}.dat
```

The meanings of columns are as follows (up to date as of 2023-Q4):

| Column Header     | Description                                             |
|-------------------|---------------------------------------------------------|
| ID                | Sequential number of the op in the file                 |
| Date              | Date of the op in YYYY-MM-DD format.                    |
| Op Name           | Name of the op without the "Operation" prefix           |
| Map               | Name of the map                                         |
| Zeus              | Name of the op creator                                  |
| N Players         | Number of actually attending players (`0` for unknown)  |
| N Signed Up       | Number of signed-up players (including tentative)       |
| Faction           | Name of the player faction                              |
| Op Type           | Type of the op (infantry, armoured, etc.)               |
