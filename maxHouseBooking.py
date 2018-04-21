def maxHouseBooking(bookings):
    prevMax = 0
    currMax = 0
    
    for i in bookings:
        tmp = currMax
        currMax = max(currMax, prevMax + i)
        prevMax = tmp
        
    return currMax