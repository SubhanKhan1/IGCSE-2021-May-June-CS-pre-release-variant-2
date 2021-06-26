nine=480
eleven=480
thirteen=480
fifteen=480
ten=480
twelve=480
fourteen=480
sixteen=480
nine_money=0
eleven_money=0
thirteen_money=0
fifteen_money=0
ten_money=0
twelve_money=0
fourteen_money=0
sixteen_money=0
screen_1 = "The train leaving times are 9:00/11:00/13:00/15:00"
screen_2 = "The train returning times are 10:00/12:00/14:00/16:00"
screen_3 = "9:00 tickets left:"
screen_4 = "10:00 tickets left:"
screen_5 = "11:00 tickets left:"
screen_6 = "12:00 tickets left:"
screen_7 = "13:00 tickets left:"
screen_8 = "14:00 tickets left:"
screen_9 = "15:00 tickets left:"
screen_10 = "16:00 tickets left:"
print(screen_1)
print(screen_2)
print(screen_3)
print(nine)
print(screen_4)
print(ten)
print(screen_5)
print(eleven)
print(screen_6)
print(twelve)
print(screen_7)
print(thirteen)
print(screen_8)
print(fourteen)
print(screen_9)
print(fifteen)
print(screen_10)
print(sixteen)
status=input("Do you want a ticket?(y/n)")
while status != "y" and status != "n":
    print("Error.")
    status=input("Do you want a ticket?(y/n)")
while status=="y":
    num_of_tickets=int(input("How many passengers are there?(Between 1 and 80 inclusively)"))
    if num_of_tickets >= 1 and num_of_tickets <= 80:
        print("")
    else:
        print("Error.")
        continue
    leaving_time=int(input("What leaving time do you want?(9/11/13/15)"))
    while leaving_time != 9 and leaving_time != 11 and leaving_time != 13 and leaving_time != 15:
        print("Error.")
        leaving_time=int(input("What leaving time do you want?(9/11/13/15)"))
    return_time=int(input("What return time do you want?(10/12/14/16)"))
    while return_time != 10 and return_time != 12 and return_time != 14 and return_time != 16:
        print("Error.")
        return_time=int(input("What return time do you want?(10/12/14/16)"))
    if leaving_time == 9 and nine >= num_of_tickets:
        if return_time == 10 and ten >= num_of_tickets:
            nine -= num_of_tickets
            ten -= num_of_tickets
            if num_of_tickets < 10:
                nine_money += 25 * num_of_tickets
                ten_money += 25 * num_of_tickets
            else:
                nine_money += (25 * num_of_tickets) - (25 * ((num_of_tickets - (num_of_tickets % 10)) / 10))
                ten_money += (25 * num_of_tickets) - (25 * ((num_of_tickets - (num_of_tickets % 10)) / 10))
        elif return_time == 12 and twelve >= num_of_tickets:
            nine -= num_of_tickets
            twelve -= num_of_tickets
            if num_of_tickets < 10:
                nine_money += 25 * num_of_tickets
                twelve_money += 25 * num_of_tickets
            else:
                nine_money += (25 * num_of_tickets) - (25 * ((num_of_tickets - (num_of_tickets % 10)) / 10))
                twelve_money += (25 * num_of_tickets) - (25 * ((num_of_tickets - (num_of_tickets % 10)) / 10))
        elif return_time == 14 and fourteen >= num_of_tickets:
            nine -= num_of_tickets
            fourteen -= num_of_tickets
            if num_of_tickets < 10:
                nine_money += 25 * num_of_tickets
                fourteen_money += 25 * num_of_tickets
            else:
                nine_money += (25 * num_of_tickets) - (25 * ((num_of_tickets - (num_of_tickets % 10)) / 10))
                fourteen_money += (25 * num_of_tickets) - (25 * ((num_of_tickets - (num_of_tickets % 10)) / 10))
        elif return_time == 16 and sixteen >= num_of_tickets:
            nine -= num_of_tickets
            sixteen -= num_of_tickets
            if num_of_tickets < 10:
                nine_money += 25 * num_of_tickets
                sixteen_money += 25 * num_of_tickets
            else:
                nine_money += (25 * num_of_tickets) - (25 * ((num_of_tickets - (num_of_tickets % 10)) / 10))
                sixteen_money += (25 * num_of_tickets) - (25 * ((num_of_tickets - (num_of_tickets % 10)) / 10))
        else:
            print("Error.")
            continue
    elif leaving_time == 11 and eleven >= num_of_tickets:
        if return_time == 12 and twelve >= num_of_tickets:
            eleven -= num_of_tickets
            twelve -= num_of_tickets
            if num_of_tickets < 10:
                eleven_money +=25 * num_of_tickets
                twelve_money += 25 * num_of_tickets
            else:
                eleven_money += (25 * num_of_tickets) - (25 * ((num_of_tickets - (num_of_tickets % 10)) / 10))
                twelve_money += (25 * num_of_tickets) - (25 * ((num_of_tickets - (num_of_tickets % 10)) / 10))
        elif return_time == 14 and fourteen >= num_of_tickets:
            eleven -= num_of_tickets
            fourteen -= num_of_tickets
            if num_of_tickets < 10:
                eleven_money += 25 * num_of_tickets
                fourteen_money += 25 * num_of_tickets
            else:
                eleven_money += (25 * num_of_tickets) - (25 * ((num_of_tickets - (num_of_tickets % 10)) / 10))
                fourteen_money += (25 * num_of_tickets) - (25 * ((num_of_tickets - (num_of_tickets % 10)) / 10))
        elif return_time == 16 and sixteen >= num_of_tickets:
            eleven -= num_of_tickets
            sixteen -= num_of_tickets
            if num_of_tickets < 10:
                eleven_money += 25 * num_of_tickets
                sixteen_money += 25 * num_of_tickets
            else:
                eleven_money += (25 * num_of_tickets) - (25 * ((num_of_tickets - (num_of_tickets % 10)) / 10))
                sixteen_money += (25 * num_of_tickets) - (25 * ((num_of_tickets - (num_of_tickets % 10)) / 10))
        else:
            print("Error.")
            continue
    elif leaving_time == 13 and thirteen >= num_of_tickets:
        if return_time == 14 and fourteen >= num_of_tickets:
            thirteen -= num_of_tickets
            fourteen -= num_of_tickets
            if num_of_tickets < 10:
                thirteen_money += 25 * num_of_tickets
                fourteen_money += 25 * num_of_tickets
            else:
                thirteen_money += (25 * num_of_tickets) - (25 * ((num_of_tickets - (num_of_tickets % 10)) / 10))
                fourteen_money += (25 * num_of_tickets) - (25 * ((num_of_tickets - (num_of_tickets % 10)) / 10))
        elif return_time == 16 and sixteen >= num_of_tickets:
            thirteen -= num_of_tickets
            sixteen -= num_of_tickets
            if num_of_tickets < 10:
                thirteen_money += 25 * num_of_tickets
                sixteen_money += 25 * num_of_tickets
            else:
                thirteen_money += (25 * num_of_tickets) - (25 * ((num_of_tickets - (num_of_tickets % 10)) / 10))
                sixteen_money += (25 * num_of_tickets) - (25 * ((num_of_tickets - (num_of_tickets % 10)) / 10))
        else:
            print("Error.")
            continue
    elif leaving_time == 15 and fifteen >= num_of_tickets:
        if return_time == 16 and sixteen >= num_of_tickets:
            fifteen -= num_of_tickets
            sixteen -= num_of_tickets
            if num_of_tickets < 10:
                fifteen_money += 25 * num_of_tickets
                sixteen_money += 25 * num_of_tickets
            else:
                fifteen_money += (25 * num_of_tickets) - (25 * ((num_of_tickets - (num_of_tickets % 10)) / 10))
                sixteen_money += (25 * num_of_tickets) - (25 * ((num_of_tickets - (num_of_tickets % 10)) / 10))
        else:
            print("Error.")
            continue
    else:
        continue
    print(screen_1)
    print(screen_2)
    print(screen_3)
    if nine > 0:
        print(nine)
    else:
        print("Closed")
    print(screen_4)
    if ten > 0:
        print(ten)
    else:
        print("Closed")
    print(screen_5)
    if eleven > 0:
        print(eleven)
    else:
        print("Closed")
    print(screen_6)
    if twelve > 0:
        print(twelve)
    else:
        print("Closed")
    print(screen_7)
    if thirteen > 0:
        print(thirteen)
    else:
        print("Closed")
    print(screen_8)
    if fourteen > 0:
        print(fourteen)
    else:
        print("Closed")
    print(screen_9)
    if fifteen > 0:
        print(fifteen)
    else:
        print("Closed")
    print(screen_10)
    if sixteen > 0:
        print(sixteen)
    else:
        print("Closed")
    status=input("Do you want a ticket?(y/n)")
train_times_strings = ["9:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00"]
train_times_variables = [nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen]
money_variables = [nine_money, ten_money, eleven_money, twelve_money, thirteen_money, fourteen_money, fifteen_money, sixteen_money]
total_passengers=0
total_money=0
least=480
print("")
print("")
print("")
print("")
print("Report for the day:")
print("")
print("")
for string in train_times_strings:
    print("The number passengers for the " + string + " train:")
    print(480 - train_times_variables[train_times_strings.index(string)])
    print("The sum of money for the " + string + " train")
    print(money_variables[train_times_strings.index(string)])
    total_passengers += 480 - train_times_variables[train_times_strings.index(string)]
    total_money += money_variables[train_times_strings.index(string)]
print("The total number of passengers for all trains:")
print(total_passengers)
print("The sum of money for all trains:")
print(total_money)
for variable in train_times_variables:
    if variable < least:
        least = variable
    else:
        continue
print("The train(s) times with the most passengers")
if train_times_variables[0] == least:
    print(train_times_strings[0])
else:
    print("")
if train_times_variables[1] == least:
    print(train_times_strings[1])
else:
    print("")
if train_times_variables[2] == least:
    print(train_times_strings[2])
else:
    print("")
if train_times_variables[3] == least:
    print(train_times_strings[3])
else:
    print("")
if train_times_variables[4] == least:
    print(train_times_strings[4])
else:
    print("")
if train_times_variables[5] == least:
    print(train_times_strings[5])
else:
    print("")
if train_times_variables[6] == least:
    print(train_times_strings[6])
else:
    print("")
if train_times_variables[7] == least:
    print(train_times_strings[7])
else:
    print("")


    

    









