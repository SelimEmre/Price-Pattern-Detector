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
Daily BTC Results:
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

Hourly BTC Results:
Line Count: 10
Tolerance Percentage: 0.05
--------------------------------------------------------
CurrentIndex: 1001 DetectedIndex: 980
Index price percentage list: ['-0.06', '0.00', '0.04', '-0.12', '-0.05', '-0.03', '-0.13', '0.07', '0.07', '-0.12', '-0.04']
Detected price percentage list: ['-0.02', '-0.01', '0.08', '-0.07', '-0.07', '-0.02', '-0.15', '0.08', '0.08', '-0.07', '-0.05']
Index Price list: [16594.0, 16584.0, 16584.0, 16590.0, 16570.0, 16562.0, 16557.0, 16536.0, 16548.0, 16559.0, 16539.0]
Detected Price list: [16546.0, 16542.0, 16541.0, 16555.0, 16544.0, 16533.0, 16529.0, 16504.0, 16517.0, 16530.0, 16518.0]
Real Price percent: -0.04 Expected Price percent: -0.05
--------------------------------------------------------
CurrentIndex: 1002 DetectedIndex: 981
Index price percentage list: ['0.00', '0.04', '-0.12', '-0.05', '-0.03', '-0.13', '0.07', '0.07', '-0.12', '-0.04', '0.06']
Detected price percentage list: ['-0.01', '0.08', '-0.07', '-0.07', '-0.02', '-0.15', '0.08', '0.08', '-0.07', '-0.05', '0.08']
Index Price list: [16584.0, 16584.0, 16590.0, 16570.0, 16562.0, 16557.0, 16536.0, 16548.0, 16559.0, 16539.0, 16533.0]
Detected Price list: [16542.0, 16541.0, 16555.0, 16544.0, 16533.0, 16529.0, 16504.0, 16517.0, 16530.0, 16518.0, 16509.0]
Real Price percent: 0.06 Expected Price percent: 0.08
--------------------------------------------------------
CurrentIndex: 1003 DetectedIndex: 982
Index price percentage list: ['0.04', '-0.12', '-0.05', '-0.03', '-0.13', '0.07', '0.07', '-0.12', '-0.04', '0.06', '0.04']
Detected price percentage list: ['0.08', '-0.07', '-0.07', '-0.02', '-0.15', '0.08', '0.08', '-0.07', '-0.05', '0.08', '0.09']
Index Price list: [16584.0, 16590.0, 16570.0, 16562.0, 16557.0, 16536.0, 16548.0, 16559.0, 16539.0, 16533.0, 16543.0]
Detected Price list: [16541.0, 16555.0, 16544.0, 16533.0, 16529.0, 16504.0, 16517.0, 16530.0, 16518.0, 16509.0, 16522.0]
Real Price percent: 0.04 Expected Price percent: 0.09
--------------------------------------------------------
CurrentIndex: 2684 DetectedIndex: 1006
Index price percentage list: ['-0.07', '-0.02', '-0.05', '-0.12', '0.07', '0.04', '-0.09', '-0.02', '0.03', '0.05', '-0.16']
Detected price percentage list: ['-0.12', '-0.05', '-0.03', '-0.13', '0.07', '0.07', '-0.12', '-0.04', '0.06', '0.04', '0.12']
Index Price list: [19196.0, 19183.0, 19179.0, 19169.0, 19146.0, 19159.0, 19167.0, 19149.0, 19145.0, 19150.0, 19159.0]
Detected Price list: [16590.0, 16570.0, 16562.0, 16557.0, 16536.0, 16548.0, 16559.0, 16539.0, 16533.0, 16543.0, 16549.0]
Real Price percent: -0.16 Expected Price percent: 0.12
--------------------------------------------------------
CurrentIndex: 2823 DetectedIndex: 841
Index price percentage list: ['0.01', '0.03', '0.08', '-0.13', '-0.01', '0.04', '0.05', '-0.10', '0.07', '0.12', '-0.15']
Detected price percentage list: ['0.04', '0.01', '0.10', '-0.09', '0.02', '0.02', '0.08', '-0.06', '0.05', '0.14', '-0.14']
Index Price list: [19134.0, 19135.0, 19140.0, 19155.0, 19131.0, 19129.0, 19137.0, 19146.0, 19126.0, 19140.0, 19163.0]
Detected Price list: [16921.0, 16928.0, 16929.0, 16946.0, 16931.0, 16934.0, 16938.0, 16951.0, 16941.0, 16949.0, 16973.0]
Real Price percent: -0.15 Expected Price percent: -0.14
--------------------------------------------------------
CurrentIndex: 2824 DetectedIndex: 842
Index price percentage list: ['0.03', '0.08', '-0.13', '-0.01', '0.04', '0.05', '-0.10', '0.07', '0.12', '-0.15', '0.00']
Detected price percentage list: ['0.01', '0.10', '-0.09', '0.02', '0.02', '0.08', '-0.06', '0.05', '0.14', '-0.14', '0.04']
Index Price list: [19135.0, 19140.0, 19155.0, 19131.0, 19129.0, 19137.0, 19146.0, 19126.0, 19140.0, 19163.0, 19134.0]
Detected Price list: [16928.0, 16929.0, 16946.0, 16931.0, 16934.0, 16938.0, 16951.0, 16941.0, 16949.0, 16973.0, 16950.0]
Real Price percent: 0.00 Expected Price percent: 0.04
--------------------------------------------------------
CurrentIndex: 2825 DetectedIndex: 843
Index price percentage list: ['0.08', '-0.13', '-0.01', '0.04', '0.05', '-0.10', '0.07', '0.12', '-0.15', '0.00', '0.09']
Detected price percentage list: ['0.10', '-0.09', '0.02', '0.02', '0.08', '-0.06', '0.05', '0.14', '-0.14', '0.04', '-0.16']
Index Price list: [19140.0, 19155.0, 19131.0, 19129.0, 19137.0, 19146.0, 19126.0, 19140.0, 19163.0, 19134.0, 19134.0]
Detected Price list: [16929.0, 16946.0, 16931.0, 16934.0, 16938.0, 16951.0, 16941.0, 16949.0, 16973.0, 16950.0, 16957.0]
Real Price percent: 0.09 Expected Price percent: -0.16
--------------------------------------------------------
CurrentIndex: 37505 DetectedIndex: 819
Index price percentage list: ['0.01', '0.00', '-0.03', '0.01', '0.06', '-0.01', '0.02', '-0.09', '0.09', '-0.05', '-0.18']
Detected price percentage list: ['0.04', '-0.02', '-0.02', '-0.03', '0.01', '-0.06', '0.01', '-0.04', '0.13', '-0.05', '0.01']
Index Price list: [6306.99, 6307.36, 6307.48, 6305.59, 6306.06, 6309.54, 6309.03, 6310.0, 6304.62, 6310.34, 6307.01]
Detected Price list: [16944.0, 16950.0, 16946.0, 16942.0, 16937.0, 16938.0, 16928.0, 16929.0, 16923.0, 16945.0, 16937.0]
Real Price percent: -0.18 Expected Price percent: 0.01
--------------------------------------------------------
```
