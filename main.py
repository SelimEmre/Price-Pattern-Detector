from pandas import *

# Read the csv file and store it in the data variable
data = read_csv("Bitstamp_BTCUSD_d.csv")
list = data['close'].tolist()

howManyColumn = 6
tolerancePercentage = 0.32
successPercentList = []
searchLoopCount = 0

def getPriceChange(index):
    return "{:.2f}".format(100 * (list[index + 1] - list[index]) / list[index])

for currentIndex, item in enumerate(list):

    priceChangeList = []
    indexPriceList = []
    searchLoopCount = 0

    # Detect current index price change list
    for x in range(currentIndex, currentIndex + howManyColumn + 1):
        if x + 1 == len(list):
            break
        priceChange = getPriceChange(x)
        priceChangeList.append(priceChange)
        indexPriceList.append(list[x])

    for a, b in zip(list[::1], list[1::1]):
        if searchLoopCount == currentIndex:
            break
        sampleRate = 0
        detectedPriceChangeList = []
        detectedPriceList = []

        for x in range(0, len(priceChangeList)):
            priceChange = getPriceChange(searchLoopCount + x)
            detectedPriceList.append(list[searchLoopCount + x])

            if float(priceChangeList[x]) - tolerancePercentage < float(priceChange) < float(priceChangeList[x]) + tolerancePercentage:
                detectedPriceChangeList.append(priceChange)
                sampleRate += 1

                if sampleRate == howManyColumn:
                    expectedPriceChange = getPriceChange(searchLoopCount + x + 1)
                    detectedPriceChangeList.append(expectedPriceChange)

                    detectedPriceList.append(list[searchLoopCount + x + 1])

                    print("--------------------------------------------------------")
                    print("sampleRate: " + str(howManyColumn) + " searchLoopCount: " + str(searchLoopCount+2) + " index: " + str(currentIndex))
                    print("percentage list: " + str(priceChangeList) + " detected price list: " + str(detectedPriceChangeList))
                    print("detectedPricelist:" + str(detectedPriceList))
                    print("IndexPricelist:" + str(indexPriceList))

                    print("Real Price percent: " + priceChangeList[howManyColumn] + " Expected Price percent: " + expectedPriceChange)
                    print("--------------------------------------------------------")
            else:
                break

        searchLoopCount += 1