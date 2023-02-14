import pandas

# Read the csv file and store it in the data variable
data = pandas.read_csv("Bitstamp_BTCUSD_d.csv")
btcPriceCloseList = data['close'].tolist()

LINE_COUNT = 6
TOLERANCE_PERCENTAGE = 0.30

print("Line Count: " + str(LINE_COUNT))
print("Tolerance Percentage: " + str(TOLERANCE_PERCENTAGE))
print("--------------------------------------------------------")


def get_price_change(index):
    return "{:.2f}". \
        format(100 * (btcPriceCloseList[index + 1] -
                      btcPriceCloseList[index]) / btcPriceCloseList[index])


for currentIndex in range(0, len(btcPriceCloseList)):

    priceChangeList = []
    indexPriceList = []

    # Detect current index price change list
    for line in range(currentIndex, currentIndex + LINE_COUNT + 1):
        if line + 1 == len(btcPriceCloseList):
            break
        priceChange = get_price_change(line)
        priceChangeList.append(priceChange)
        indexPriceList.append(btcPriceCloseList[line])

    for loopIndex in range(0, len(btcPriceCloseList)):

        if loopIndex == currentIndex:
            break
        sampleRate = 0
        detectedPriceChangeList = []
        detectedPriceList = []

        for line, value in enumerate(priceChangeList):
            priceChange = get_price_change(loopIndex + line)
            detectedPriceList.append(btcPriceCloseList[loopIndex + line])

            if float(priceChangeList[line]) - TOLERANCE_PERCENTAGE < \
                    float(priceChange) < float(priceChangeList[line]) + TOLERANCE_PERCENTAGE:
                detectedPriceChangeList.append(priceChange)
                sampleRate += 1

                if sampleRate == LINE_COUNT:
                    expectedPriceChange = get_price_change(loopIndex + line + 1)
                    detectedPriceChangeList.append(expectedPriceChange)

                    detectedPriceList.append(btcPriceCloseList[loopIndex + line + 1])

                    print("CurrentIndex:{0} DetectedIndex:{1}".format(str(currentIndex), str(loopIndex + 2)))
                    print("Index price percentage list: " + str(priceChangeList))
                    print("Detected price percentage list: " + str(detectedPriceChangeList))
                    print("Index Price list: " + str(indexPriceList))
                    print("Detected Price list: " + str(detectedPriceList))

                    print("Real Price percent: " + priceChangeList[
                        LINE_COUNT] + " Expected Price percent: " + expectedPriceChange)
                    print("--------------------------------------------------------")
            else:
                break
