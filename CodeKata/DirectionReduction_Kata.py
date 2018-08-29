def dirReduc(arr):
    OriginalRoute = ("".join(arr))
    RouteWithoutNS = OriginalRoute.replace("NORTHSOUTH", "")
    RouteWithoutSN = RouteWithoutNS.replace("SOUTHNORTH", "")
    RouteWithoutWE = RouteWithoutSN.replace("WESTEAST", "")
    RouteWithoutEW = RouteWithoutWE.replace("EASTWEST", "")
    RouteWithoutSN2 = RouteWithoutEW.replace("SOUTHNORTH", "")
    C1 = RouteWithoutSN2.replace("WEST", "WEST,")
    C2 = C1.replace("NORTH", "NORTH,")
    C3 = C2.replace("SOUTH", "SOUTH,")
    C4 = C3.replace("EAST", "EAST,")
    FinalRoute = C4.split(",")
    FinalRoute.pop()
    return FinalRoute

print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))  # Should equal ['WEST']
print(dirReduc(["NORTH", "WEST", "SOUTH", "EAST"]))  # Should equal <self>
print(dirReduc(['NORTH', 'EAST', 'NORTH', 'SOUTH']))  # Should equal ['NORTH', 'EAST']
