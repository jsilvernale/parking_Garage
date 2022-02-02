class Parking_Garage():

    def __init__(self, tickets, parking_space, current_ticket):
        self.tickets = tickets
        self.parking_space = parking_space
        self.current_ticket = current_ticket

    def takeTicket(self):
        price1 = input("Ok the fee for parking here is $5 and will be charged upon leaving the garage. Still want a ticket?  y/n ")
        if price1.lower() == 'y':
            self.tickets[0] - 1
            self.parking_space[0] - 1
        else:
            print("Ok then there is partking available on the street. Have a great day")
            y
            
    def payForParking(self):
        x = 1
        price2 = input("You owe $5. pay ")
        if price2.lower() == 'pay':
            self.current_ticket[x] = '$5'
            x += 1
            self.tickets[0] + 1
            self.parking_space[0] + 1
            Parking_Garage.leaveGarage(self)
        else:
            print("you have to pay before you can leave the garrage.")
            Parking_Garage.payForParking(self)

    def leaveGarage(self):
        print("Thank you for parking in my garage! Have yourself a fantastic day!")
        

    
my_24_hr_Garage = Parking_Garage([50], [50], {})

def Park():
    while True:
        print("Hello! welcome to my garage!")
        ticket = input("Are you parking in the garage today? y/n ")
        if ticket.lower() == 'y':
            my_24_hr_Garage.takeTicket()
        else:
            my_24_hr_Garage.leaveGarage()
        leaving = input("Hello again. Are you leaving? y/n")
        if leaving.lower() == 'y':
            my_24_hr_Garage.payForParking()
        else:
            print("ok then, continue to enjoy the luxury of parking in my garage!")
            

Park()
