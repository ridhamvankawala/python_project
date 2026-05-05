courier={
    "t101":"dispatch",
    "t102":"in transit",
    "t103":"delivered"
    }
trackid=input("enter traking id:")
if trackid in courier:
    print("Status:",courier[trackid])
else:
    print("Tracking id not found!")
