# pylint: disable=line-too-long
"""This import needs for reading csv files"""
import pandas as pd

# https://www.cryptodatadownload.com/data/bitstamp/

# Read the csv file and store it in the data variable
data = pd.read_csv("Bitstamp_BTCUSD_1h.csv")  # Bitstamp_BTCUSD_d.csv
btcPriceCloseList = data['close'].tolist()

LINE_COUNT = 10
TOLERANCE_PERCENTAGE = 0.05

print(f"Line Count: {LINE_COUNT}")
print(f"Tolerance Percentage: {TOLERANCE_PERCENTAGE}")
print("--------------------------------------------------------")


def get_price_change(index):
    """This function calculates the percentage difference between two prices"""
    return f'{100 * (btcPriceCloseList[index + 1] - btcPriceCloseList[index]) / btcPriceCloseList[index]:.2f}'


for currentIndex in range(len(btcPriceCloseList)):
    priceChangeList = []
    indexPriceList = []

    # Detect current index price change list
    for line in range(currentIndex, currentIndex + LINE_COUNT + 1):
        if line + 1 == len(btcPriceCloseList):
            break
        priceChange = get_price_change(line)
        priceChangeList.append(priceChange)
        indexPriceList.append(btcPriceCloseList[line])

    for loopIndex in range(currentIndex):
        sampleRate: int = 0
        detectedPriceChangeList = []
        detectedPriceList = []

        for line, value in enumerate(priceChangeList):
            priceChange = get_price_change(loopIndex + line)
            detectedPriceList.append(btcPriceCloseList[loopIndex + line])

            if float(value) - TOLERANCE_PERCENTAGE < float(priceChange) < float(value) + TOLERANCE_PERCENTAGE:
                detectedPriceChangeList.append(priceChange)
                sampleRate += 1

                if sampleRate == LINE_COUNT:
                    expectedPriceChange = get_price_change(loopIndex + line + 1)
                    detectedPriceChangeList.append(expectedPriceChange)
                    detectedPriceList.append(btcPriceCloseList[loopIndex + line + 1])

                    print(f"CurrentIndex: {currentIndex} DetectedIndex: {loopIndex + 2}")
                    print(f"Index price percentage list: {priceChangeList}")
                    print(f"Detected price percentage list: {detectedPriceChangeList}")
                    print(f"Index Price list: {indexPriceList}")
                    print(f"Detected Price list: {detectedPriceList}")
                    print(
                        f"Real Price percent: {priceChangeList[LINE_COUNT]} Expected Price percent: {expectedPriceChange}")
                    print("--------------------------------------------------------")
            else:
                break
