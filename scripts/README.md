# Data Analysis Scripts

The `scripts` directory contains data analysis scripts designed to operate on the op statistics data.

The scripts are designed as filters. They open an op data file, produce the results, and write the results to the standard output. Any errors are written to the standard error output.

General usage:
```console
python filter-script.py OP_DATA_FILE
```
