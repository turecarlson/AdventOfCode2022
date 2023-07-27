fname = "./data.txt"

def main():
    # read file into list
    with open(fname, "r") as file:
        all_lines = file.readlines()
    
    # separate list by blank lines into array
    elves_lists = []
    temp_list = []
    for line in all_lines:
        if line == '\n':
            elves_lists.append(temp_list)
            temp_list = []
        else:
            number = int(line[:-1])
            temp_list.append(number)
    elves_lists.append(temp_list)

    # determine total calories in each list
    total_cal_per_elf = []
    for elf_list in elves_lists:
        total_calories = 0
        for item in elf_list:
            total_calories += item
        total_cal_per_elf.append(total_calories)

    # determine max value in total_cal_per_elf
    print(max(total_cal_per_elf))

if __name__ == '__main__':
    main()
