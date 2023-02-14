# Price-Pattern-Detector
This script analyzes old price correlations from a historical CSV file. Main purpose is to predict future price movements.

## Explanations about this script
I am aware that this is just the beginning of the script. This phase is only a proof of concept. I would like to add some indicators for more accurate results. :)

## How to run this project
This script works on v3.6 python version. You just need to install `pandas` to your environment with as below:
```
pip install pandas
```

After that you just need to call:
```
python main.py
```

### Sample results:
```
Line Count: 6 Tolerance Percentage: 0.3
--------------------------------------------------------
Current Index: 597 Detected Index: 226
Index price percentage list: ['0.87', '-0.78', '-0.33', '0.52', '-0.33', '0.55', '-0.40']
Detected price percentage list: ['0.79', '-0.97', '-0.44', '0.81', '-0.45', '0.52', '-0.45']
Index Price list: [653.8, 659.51, 654.37, 652.22, 655.63, 653.44, 657.03]
Detected Price list: [277.23, 279.43, 276.73, 275.5, 277.73, 276.48, 277.93]
Real Price percent: -0.40 Expected Price percent: -0.45
--------------------------------------------------------
Current Index: 598 Detected Index: 227
Index price percentage list: ['-0.78', '-0.33', '0.52', '-0.33', '0.55', '-0.40', '-5.25']
Detected price percentage list: ['-0.97', '-0.44', '0.81', '-0.45', '0.52', '-0.45', '4.80']
Index Price list: [659.51, 654.37, 652.22, 655.63, 653.44, 657.03, 654.37]
Detected Price list: [279.43, 276.73, 275.5, 277.73, 276.48, 277.93, 276.67]
Real Price percent: -5.25 Expected Price percent: 4.80
--------------------------------------------------------
Current Index: 669 Detected Index: 483
Index price percentage list: ['-0.63', '0.63', '-0.10', '0.64', '0.04', '-0.14', '0.29']
Detected price percentage list: ['-0.56', '0.59', '-0.03', '0.92', '-0.05', '-0.08', '0.94']
Index Price list: [611.06, 607.18, 610.98, 610.34, 614.23, 614.48, 613.61]
Detected Price list: [415.4, 413.09, 415.51, 415.38, 419.19, 419.0, 418.65]
Real Price percent: 0.29 Expected Price percent: 0.94
--------------------------------------------------------
Current Index: 1415 Detected Index: 649
Index price percentage list: ['0.46', '0.01', '-0.11', '-0.20', '0.29', '-0.29', '0.20']
Detected price percentage list: ['0.53', '0.12', '0.03', '-0.44', '0.11', '-0.31', '0.66']
Index Price list: [6383.46, 6412.86, 6413.38, 6406.06, 6393.41, 6411.96, 6393.53]
Detected Price list: [603.8, 607.0, 607.73, 607.89, 605.21, 605.9, 604.04]
Real Price percent: 0.20 Expected Price percent: 0.66
--------------------------------------------------------
Current Index: 2864 Detected Index: 708
Index price percentage list: ['-0.57', '0.13', '-1.61', '-0.38', '0.51', '1.15', '-1.01']
Detected price percentage list: ['-0.82', '0.18', '-1.79', '-0.21', '0.45', '0.87', '3.82']
Index Price list: [19532.0, 19420.0, 19445.0, 19131.0, 19059.0, 19157.0, 19377.0]
Detected Price list: [720.44, 714.5, 715.82, 703.0, 701.51, 704.7, 710.82]
Real Price percent: -1.01 Expected Price percent: 3.82
--------------------------------------------------------
```
