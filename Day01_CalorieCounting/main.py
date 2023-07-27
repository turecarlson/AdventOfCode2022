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
    print("elf carrying most caloires total:", max(total_cal_per_elf))

    # PART 2 - find total total calories of top 3 elves

    # sort list of total calories per elf
    total_cal_per_elf.sort()
    top_three = total_cal_per_elf[-3:]
    total_top_three = 0
    for calories in top_three:
        total_top_three += calories
    print("total calories for top three elves:", total_top_three)
if __name__ == '__main__':
    main()
