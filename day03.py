#!python3
# -*- coding: utf-8 -*-

# @author Jonas J. Solsvik
# @date 27.11.17
# @url https://adventofcode.com/2017/day/2


if __name__ == "__main__":

    # 0. Initial state
    target = 50
    step   = 1
    value  = 0
    offset = -1    
    running = True

    # 1. Advance iterator to hit spiral target
    print("val", 
          "\t","st", 
          "\t","mid", 
          "\t","off",
          "\t", "offs", 
          "\t", "mdist")
    while running:
        for i in range(step*2):
            if value < target:
                value += 1
                offset += 1
                offset_step = offset % step
                mid = step // 2

                # 
                # MANHATTAN DISTANCE
                #
                distance_center = 0
                distance_mid    = abs(offset_step - mid)
                

                manhattan_distance = mid + distance_mid

                print(value, 
                      "\t",step, 
                      "\t",mid, 
                      "\t",offset,
                      "\t", offset_step)
                      #\t", manhattan_distance)
            else:
                running = False
                break

        step += 1
        offset = -1

    # 2. Calculate Manhattan Distance(steps) to spiral center
    