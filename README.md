# Python CSV Column Remover Script
A Python script that allows you to remove specified columns from CSV files.


## Optional Arguments

**-f** : File name of file with columns to remove (file must have one word per line). Look at sample_file.txt as example.

**-r** : Recursively search for files starting from current directory. By default it will search currently directory only.

**-w** : Wildcard for which files to use. Default: "\*.csv". Files must be in CSV format!

**-e** : Drop all empty columns.

**-l** : Drop last column if empty and has no column name.

**NOTE:** CSV files are edited inplace!


**TODO:**

Handle CSV files with no headers
