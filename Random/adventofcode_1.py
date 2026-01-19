# advent of code

numbers = [x for x in range(100)]
start_pos = 50
zero_counter = 0
phrase = f"The dial starts by pointing at {start_pos}"
def move(current_pos,sequence):
    starting_pos = current_pos
    dist_to_move = int(sequence[1:])
    global zero_counter
    crossed_over = False
    if sequence[0] == "L":
        #move left
        while dist_to_move != 0:
            dist_to_move -= 1
            current_pos -= 1
            # print(dist_to_move,current_pos)
            if current_pos == 0:
                zero_counter +=1
            if current_pos < 0:
                current_pos = 99
        
        final_pos = current_pos
        
        return current_pos
    else:
        # move right
        while dist_to_move != 0:
            dist_to_move -= 1
            current_pos += 1
            if current_pos > 99:
                current_pos = 0
            if current_pos == 0:
                zero_counter +=1
        return current_pos
    
    print(dist_to_move)

print(phrase)

sample_data = "./sample.txt"
real_data = "./combo.txt"
with open(real_data,'r')as f:
    lines = f.readlines()
    mod_lines = [l.strip('\n') for l in lines]

print(mod_lines)

starting = True
for l in mod_lines:
    if starting:
        active_pos = move(start_pos,l)
        starting = False
    else:
        active_pos = move(active_pos,l)

print(f"Zero counter = {zero_counter}")

