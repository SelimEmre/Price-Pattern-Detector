from pandas import *

# Read the csv file and store it in the data variable
data = read_csv("Bitstamp_BTCUSD_d.csv")
list = data['close'].tolist()

lineCount = 6
tolerancePercentage = 0.30
successPercentList = []
searchLoopCount = 0

print("Line Count: " + str(lineCount) + " Tolerance Percentage: " + str(tolerancePercentage))
print("--------------------------------------------------------")

def getPriceChange(index):
    return "{:.2f}".format(100 * (list[index + 1] - list[index]) / list[index])

for currentIndex, item in enumerate(list):

    priceChangeList = []
    indexPriceList = []
    searchLoopCount = 0

    # Detect current index price change list
    for x in range(currentIndex, currentIndex + lineCount + 1):
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

                if sampleRate == lineCount:
                    expectedPriceChange = getPriceChange(searchLoopCount + x + 1)
                    detectedPriceChangeList.append(expectedPriceChange)

                    detectedPriceList.append(list[searchLoopCount + x + 1])

                    print("Current Index: " + str(currentIndex) + " Detected Index: " + str(searchLoopCount+2))
                    print("Index price percentage list: " + str(priceChangeList))
                    print("Detected price percentage list: " + str(detectedPriceChangeList))
                    print("Index Price list: " + str(indexPriceList))
                    print("Detected Price list: " + str(detectedPriceList))

                    print("Real Price percent: " + priceChangeList[lineCount] + " Expected Price percent: " + expectedPriceChange)
                    print("--------------------------------------------------------")
            else:
                break

        searchLoopCount += 1