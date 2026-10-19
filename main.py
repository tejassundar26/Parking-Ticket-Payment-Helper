def calculate_change(paid , price):
    change = paid -  price
    return change

ticket_price = 30

print("======PARKING TICKET PAYMENT HELPER======")
print("This parking ticket costs {ticket price}units.")
print("Accepted coins: 1 , 10 , 20 , 30 \n")

total_inserted = 0
coins_inserted = 0

while True:
    coin = int(input("Insert a coin (1 , 10 , 20 or 30): "))

    if coin != 1 and coin != 10 and coin != 20 and coin != 30:
        print("Invalid coin , try again! ")
        continue

    total_inserted += coin
    coins_inserted += 1
    print("Inserted {coin}. Total so far {total_inserted}")

    if total_inserted >= ticket_price:
        print("Enough  money inserted!!!\n")
        break

    change_due = calculate_change(total_inserted , ticket_price)

    if change_due == 0:
        pass
    else:
        print("Here is your desired change: {change_due} units")


    print("---------PAYMENT SUMMARY--------")
    print("Ticket Price:",ticket_price)
    print("Number of coins inserted:", coins_inserted)
    print("Total Paid:",total_inserted)
    print("Change Given:",change_due)
    print("Parking Ticket Payment officially and successfully completed!")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

    




    




