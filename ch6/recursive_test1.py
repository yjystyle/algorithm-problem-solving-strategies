def pick(total_count, picked_list, to_pick_value):
    if to_pick_value ==0:
        print(picked_list)
        return
    smallest =  0 if not picked_list else picked_list[-1] +1
    for next in range(smallest, total_count):
        picked_list.append(next)
        pick(total_count, picked_list, to_pick_value-1)
        picked_list.pop()
    
b = []
pick(3, b, 2)