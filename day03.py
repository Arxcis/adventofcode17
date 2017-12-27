#!python3
# -*- coding: utf-8 -*-

#
# @author Jonas J. Solsvik
# @date 27.11.17
# @url https://adventofcode.com/2017/day/2
#

if __name__ == "__main__":

    # 0. Initial state
    target  = 50
    step    = 1
    value   = 0
    offset  = -1
    lap     = 0
    running = True
    right_turns        = 0
    manhattan_distance = 0

    # 1. Advance iterator to hit spiral target
    print("val", 
          "\t","st", 
          "\t","mid", 
          "\t","off",
          "\t", "offs", 
          "\t", "mdist",
          "\t", "rturn", 
          "\t", "lap")

    while running:
        for i in range(step * 2):

            # STOP - if we have found the target
            if value >= target:
                running = False
                break

            value  += 1
            offset += 1
            offset_step = offset % step
            mid = step // 2

            # If right turn
            if offset_step == 0: 
                right_turns += 1
                #print("TURNING!")

                # If new lap (every 4th right turn)
                if (right_turns + 2) % 4 == 0:
                    lap += 1
                    #print("LAPPING!")

            distance_mid       = abs(offset_step - mid)
            distance_center    = lap
            manhattan_distance = distance_mid + distance_center

            '''
            print(value, 
                  "\t",step, 
                  "\t",mid, 
                  "\t",offset,
                  "\t", offset_step,
                  "\t", manhattan_distance,
                  "\t", right_turns,
                  "\t", lap)'''

        #print("STEP UP!")
        step   +=  1
        offset  = -1
