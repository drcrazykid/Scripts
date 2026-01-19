
sample_file = "./aoc3_sample.txt"
real_file = "./aoc3_real.txt"
with open(real_file,'r') as f:
    data = [l.strip() for l in f.readlines()]


def select_highest_num(sequence:str,forSecondNum = False):

    choosen_num = int(sequence[0])

    for num in sequence:
        if forSecondNum and int(num) > choosen_num:
            choosen_num = int(num)

        elif int(num) > choosen_num and not sequence.find(str(num)) == len(sequence)-1:
            choosen_num = int(num)

    place_in_sequence = sequence.find(str(choosen_num))

    # print(choosen_num,place_in_sequence)
    return [choosen_num, place_in_sequence] 

def select_second_num(sequence:str,starting_point:int):
    remaining_seq = sequence[1+starting_point:]
    # print(remaining_seq)
    second_value = select_highest_num(remaining_seq,True)[0]

    return second_value


# seq = "818181911112111"    
selected_joltages = []
for seq in data:
    output = select_highest_num(seq)

    first_choosen = output[0]
    second_chosen = select_second_num(seq,output[1])

    bank_joltage = str(first_choosen) + str(second_chosen)
    # print(bank_joltage)
    selected_joltages.append(int(bank_joltage))

sum = 0
for x in selected_joltages:
    sum = sum + x
print(sum)