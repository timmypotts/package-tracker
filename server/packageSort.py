def packageSort(array):
    def getStatus(package):
        return package.get("statuscode")

    def getExpected(package):
        return package.get("expected")

    def getDelivery(package):
        return package.get("deliverdate")

    output = []
    categories = {}
    categories["unknown"] = []
    categories["attempt"] = []
    categories["exception"] = []
    categories["transit"] = []
    categories["accepted"] = []
    categories["notinsystem"] = []
    categories["delivered"] = []
    for package in array:
        if getStatus(package) == "DE":
            categories["delivered"].append(package)
        elif getStatus(package) == "IT":
            categories["transit"].append(package)
        elif getStatus(package) == "AC":
            categories["accepted"].append(package)
        elif getStatus(package) == "EX":
            categories["exception"].append(package)
        elif getStatus(package) == "AT":
            categories["attempt"].append(package)
        elif getStatus(package) == "NY":
            categories["notinsystem"].append(package)
        elif getStatus(package) == "UN":
            categories["unknown"].append(package)
        else:
            pass

    categories["delivered"].sort(key=getDelivery, reverse=True)
    categories["transit"].sort(key=getExpected, reverse=True)
    categories["accepted"].sort(key=getExpected, reverse=True)
    categories["exception"].sort(key=getExpected, reverse=True)
    categories["attempt"].sort(key=getExpected, reverse=True)

    for category in categories:
        for i in categories[category]:
            output.append(i)
    
    return(output)

    