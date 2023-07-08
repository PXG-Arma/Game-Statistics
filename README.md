# PXG Game Statistics

Statistics data of Phoenix Group ops, and tools to analyze it.
For the purposes of improving member experience, accountability and, occasionally, boasting.


## Repo Structure

- `/data`: raw statistics data in plain text form
- `/scripts`: executable scripts for data analysis


## Data Format

Data is contained in plain text files and organized in columns. Column separator is the horizontal tab character, which allows easy import into any spreadsheet software. The first line of each file contains column headers.

The files are named by the following convention:
```text
{year}-{quarter}-{data type}.dat
```
