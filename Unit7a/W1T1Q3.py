Outlet1Sales = [10, 12, 15, 10]
Outlet2Sales = [5, 8, 3, 6]
Outlet3Sales = [10, 12, 15, 10]
for i in range(0,4):
    Total = Outlet1Sales[i] + Outlet2Sales[i] + Outlet3Sales[i]
    print("Total for quarter " + str(i+1) + ": " + str(Total))