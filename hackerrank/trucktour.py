def truckTour(petrolpumps):
    ln = len(petrolpumps)
    
    petrolpumps = [x - y for x, y in petrolpumps]
    
    for i in range(ln):
        sm = 0
        for j in range(ln):
            sm += petrolpumps[(i + j) % ln]
            if sm < 0:
                break
        else:
            return i
    return -1