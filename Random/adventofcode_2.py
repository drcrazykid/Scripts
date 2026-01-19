# day 2


day2_file_sample = "./id_sample.txt"
day2_real = "id_real.txt"

with open(day2_file_sample,'r') as f:
    line = f.readline()


sequences = line.split(",")
print(sequences)
invalid_ids = []
def convert_to_number_range(sequence):
    first = int(sequence.split('-')[0])
    last = int(sequence.split('-')[1])+1

    # print(f"starting: {first}\nlast: {last}")
    numbers = [n for n in range(first,last)]
    # print(numbers)
    return numbers

def identify_double(number):
    global invalid_ids
    n = str(number)
    if len(n) % 2 == 0:
        h = int(len(n) / 2)
        fh = n[:h]
        sh = n[h:]
        # print(f"Length: {len(n)}\nfirst-half: {fh}\nsec-half: {sh}")
        if fh == sh:
            invalid_ids.append(number)

def split_by(s,size):
    return [s[i:i+size] for i in range(0, len(s),size)]

def id_repition(number):
    global invalid_ids
    string_num = str(number)
    whole_size = len(string_num)
    c = 1

    while c <= whole_size:
        active_char = string_num[:c]
        active_list = split_by(string_num,c)
        # for i in range(len(active_list) -1):
        #     if active_list[i] and active_list[i+1] == active_char:
        #         invalid_ids.append(active_char)
        print(active_list)
        c += 1



    pass

for s in sequences:
    range_of_numbers = convert_to_number_range(s)
    for num in range_of_numbers:
        identify_double(num)
        id_repition(num)
print(invalid_ids)

sum = 0
for num in invalid_ids:
    sum +=num

print(sum)