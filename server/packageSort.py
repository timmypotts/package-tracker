

testarray = [
        {
            "courier": "USPS",
            "deliverdate": "Fri, 26 Mar 2021 20:53:00 GMT",
            "expected": None,
            "id": 4,
            "item": "the killing",
            "shipdate": "Tue, 23 Mar 2021 02:33:00 GMT",
            "status": "Delivered",
            "tracking": "9205590109401292312659",
            "user": "9f3396bc-461a-47ff-9d5f-39ed1bece91f",
            "statuscode" : "DE"
        },
        {
            "courier": "USPS",
            "deliverdate": "Tue, 30 Mar 2021 16:38:00 GMT",
            "expected": None,
            "id": 5,
            "item": "punch drunk",
            "shipdate": "Sun, 28 Mar 2021 02:48:00 GMT",
            "status": "Delivered",
            "tracking": "9200190109401293876331",
            "user": "9f3396bc-461a-47ff-9d5f-39ed1bece91f",
            "statuscode" : "DE"
        },
        {
            "courier": "USPS",
            "deliverdate": "Mon, 19 Apr 2021 17:18:00 GMT",
            "expected": None,
            "id": 6,
            "item": "bong joon ho",
            "shipdate": "Fri, 16 Apr 2021 00:16:00 GMT",
            "status": "Delivered",
            "tracking": "9200190109401299509929",
            "user": "9f3396bc-461a-47ff-9d5f-39ed1bece91f",
            "statuscode" : "DE"
        },
        {
            "courier": "UPS",
            "deliverdate": None,
            "expected": "Thu, 22 Apr 2021 07:00:00 GMT",
            "id": 8,
            "item": "blah",
            "shipdate": None,
            "status": "Accepted",
            "tracking": "1Z300WE80341573512",
            "user": "9f3396bc-461a-47ff-9d5f-39ed1bece91f",
            "statuscode" : "AC"
        }
    ]

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

    