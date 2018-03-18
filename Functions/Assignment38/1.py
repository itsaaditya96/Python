def compare(phoenix_to_slc, phoenix_to_tampa):
    if phoenix_to_slc > phoenix_to_tampa:
        print("SLC is far from Phoenix compared to Tampa, Florida")
    elif(phoenix_to_slc < phoenix_to_tampa):
        print("Tampa, Florida is far from Phoenix compared to SLC")
    else:
        print("Both locations are equidistance from Phoneix")

compare (1790, 506)