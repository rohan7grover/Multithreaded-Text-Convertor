# Multithreaded Text Convertor

This repository contains a Python script that converts lowercase text files to uppercase using multithreading. The purpose of this code is to analyze the time taken for conversion with different parameters, such as the number of files and the number of threads.

## How to Use

1. To create 20 random text files of 100 MB each, run the `fileCreator.py` script. The generated files will be stored in the `input` folder.
2. Run the `multithreading_code.py` script. The script will convert the text files to uppercase and store the results in the `output` folder.
3. The script will output a CSV file named `time_taken.csv` with the time taken for each combination of parameters.

## Parameters

The script analyzes the time taken with the following parameters:
- Number of files to convert (n): 10, 20
- Number of threads (t): 1, 2, 3, 4

## Results

The CSV file, `time_taken.csv`, contains the time taken (in seconds) for each combination of parameters. The results are shown below in the table:

| n  | t=1 | t=2 | t=3 | t=4 |
|----|-----|-----|-----|-----|
| 10 | 1.79| 1.09| 1.03| 1.03|
| 20 | 2.99| 1.97| 2.22| 2.06|
