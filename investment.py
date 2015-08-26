def invest(amount, rate,time, investment):
    """Tracks the growing amount of an investment over time
            amount: initial investment amount
            rate: annual compounding rate
            time: total number of years to invest
            investment = amount invested at the start of each year"""

    total = amount
    year = 0

    print "principal amount:", amount
    print "annual rate of return:", rate

    for n in range (1, time + 1):
        year += 1
        total = total + total*rate + investment
        print "year {}: {}".format(year, total)
    

invest(100, .05, 8, 0)
invest(0, .07, 45, 730)
