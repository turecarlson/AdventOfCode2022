'''
Day 2: Rock Paper Scissors

a - opponentRock - 1
b - opponentPaper - 2
c - opponentScissors - 3

x - selfRock - 1
y - selfPaper - 2
c - selfScissors - 3

Draws
selfRock - opponentRock = 1 - 1 = 0
selfPaper - opponentPaper = 2 - 2 = 0
selfScissors - oppponentScissors = 3 - 3 = 0

Wins
selfRock - opponentScissors = 1 - 3 = -2
selfPaper - opponentRock = 2 - 1 = 1
selfScissors - opponentPaper = 3 - 2 = 1

Losses
selfRock - opponentPaper = 1 - 2 = -1
selfPaper - opponentScissors = 2 - 3 = -1
selfScissors - opponentRock = 3 - 1 = 2

(self - opponent) % 3 -> Win/Loss/Draw Category
Categories:
0 - draw
1 - win
2 - loss 
'''

def main():
    sum = 0
    line_num = 1
    input = []
    with open("./input") as file:
        input = file.readlines()
    
    for line in input:
        print(line_num)
        line_num += 1
        values = line.split(' ')
        self_char = values[1].strip('\n')
        opp_char = values[0]
        self_val = 0
        opp_val = 0

        match self_char:
            case 'X': # rock
                self_val = 1
            case 'Y': # paper
                self_val = 2
            case 'Z': # scissors
                self_val = 3
        match opp_char:
            case 'A': # rock
                opp_val = 1
            case 'B': # paper
                opp_val = 2
            case 'C': # scissors
                opp_val = 3

        '''
        result -see comment on ln 27
        0 - draw
        1 - win
        2 - loss
        '''
        result = (self_val - opp_val) % 3
        result_val = 0
        match result:
            case 0: # draw
                result_val = 3
            case 1: # win
                result_val = 6
            case 2: # loss
                result_val = 0
        matchTotal = result_val + self_val
        sum += matchTotal
            
        print("self_char: {}\nopp_char: {}".format(self_char, opp_char))
        print("Self: {}\nOpp: {}\nResult: {}".format(self_val, opp_val, result))
        print("RoundTotal:", (result_val + self_val), '\n')
    print('Total Score:', sum)

if __name__ == '__main__':
    main()