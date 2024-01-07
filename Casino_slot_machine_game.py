import random;
# slot machine rows and colums  matrix .
ROWS = 3
COLS = 3
# symbols in slot machine .
symbol_count = {
    "A":8,
    "B":8,
    "C":8,
    "D":8
}
# bet multiplier eg: A = bet * 5 times
symbol_values = {
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []      
    for _ in range(cols):
        column=[]
        current_symbols = all_symbols.copy()
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)  
    return columns

# columns are layed out as rows so we need to rotate it horizontally (transposing operation)

def print_slot_machine(columns):
        for row in range(len(columns[0])):
            for i , column in enumerate(columns):
                #if else condition to print pipe operator at the end of the column or not
                if i != len(columns)-1:  
                    print(column[row],end=" | ")
                else:
                    print(column[row],end=" ")
            print()



def check_winnings(columns,lines,bet,values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol]*bet
            winning_lines.append(line+1)
    return winnings ,winning_lines

    


MAX_LINES = 3
MAX_BET = 500
MIN_BET = 10

def deposit():
    while True:
        amount = input("enter your amount to deposite: ")
        if amount.isdigit():
            amount = int(amount)
            if amount >= 500 :
                break
            else:
                print("amount must be greater than 500")
        else:
            print("enter a valid deposit amount")
    
    return amount

def get_number_of_line():
    while True:
        lines = input("enter the number of lines to bet on (1- " + str(MAX_LINES)+")? : ")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= 3 :
                break
            else:
                print("enter the number of lines to bet on (1-3)")
        else:
            print("enter a valid number of lines to bet on!")
    
    return lines

def get_bet():
    while True:
        amount = input("enter amount to be bet: ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET<= amount <= MAX_BET :
                break
            else:
                print("enter the minimum "+str(MIN_BET)+": ")
        else:
            print("enter a valid amount to bet on !")
    
    return amount

def spin(balance):
    lines = get_number_of_line()
    while True:
        bet = get_bet()
        total_bet= bet * lines
        if total_bet > balance:
            print(f"you do not have sufficient balance to bet, your current balance is ${balance} ")
        else:
            break
    print(f"you are betting ${bet} on {lines} lines.total bet is equal to : ${total_bet}")


    slots =get_slot_machine_spin(ROWS,COLS,symbol_count)   
    print_slot_machine(slots)
    winnings,winning_line = check_winnings(slots,lines,bet,symbol_values)
    print(f"you won ${winnings}")
    print(f"you won on lines: {winning_line}")
    
    return winnings-total_bet



def main():
    balance = deposit()
    while True:
        print(f"current balance is : ${balance}")
        answer = input("press enter the play (q to Quit)")
        if answer.lower() ==  "q":
            break
        
        balance += spin(balance)

    print(f"you left with balance : ${balance}")

main()

