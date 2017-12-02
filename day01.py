#!python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":


    test_data = [
        "1122",
        "1111",
        "1234",
        "91212129"
    ]

    # Iterate through pairs each current-next pair + first and last
    for data in test_data:
        print("\n", data)

        identical_digit_pair_sum = 0
        length = len(data)
        for i in range(length):


            # If identical digit
            if data[i] == data[(i+1) % length]:
                print("HIT  ->",data[i] + data[(i+1) % length])
                identical_digit_pair_sum += int(data[i])
            else:
                print("MISS - ",data[i] + data[(i+1) % length])

        print("Sum = ", identical_digit_pair_sum)