class Star_cinema:
    __hall_list = []

    def entry_hall(self, hall_name):
        self.__hall_list.append(hall_name)

class Hall(Star_cinema):
    def __init__(self, rows, cols, hall_no):
        super().__init__()
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

        # self.entry_hall(self.hall_no)
        # self.entry_hall((self.hall_no, self.show_list, self.seats))
        self.entry_hall((self.rows, self.cols, self.hall_no))
        

    def entry_show(self, id, movie_name, time):
        show = (id, movie_name, time)
        self.show_list.append(show)
        self.seats[id] = []
        for seat in range(self.rows):
            row = []
            for seat in range(self.cols):
                row.append(0) # 0 means the seat is free
            self.seats[id].append(row)

    def book_seats(self, id, seat):
        if id in self.seats:
            for (r, c) in seat:
                if 0 <= r < self.rows and 0 <= c < self.cols:
                    if self.seats[id][r][c] == 1:
                        print('This seat is already booked!')
                    elif self.seats[id][r][c] == 0:
                        self.seats[id][r][c] = 1
                        print('Congrets, seat successfully booked for you.')
                else:
                    print('Envalid seat number (row & col)')
        else:
            print('Show ID didn\'t found! Please enter correct Show ID.')



    def view_show_list(self):
        for sh in self.show_list:
            print(f'Movie Name: {sh[1]} <--> Show ID: {sh[0]} <--> Time: {sh[2]}')

    def view_available_seats(self, id):
        if id in self.seats:
            for seat in self.seats[id]:
                print(seat)
        else:
            print('Show ID didn\'t found! Please enter correct Show ID.')


"""---------- Replica System ----------"""
star = Hall(10, 10, 10)
st = Hall(10, 10, 154)
st = Hall(10, 10, 4453)

star.entry_show(1, 'jawan', '7 sept, 2023')
star.entry_show(2, 'pathaan', '25 jan, 2023')
star.entry_show(3, 'Tiger 3', '13 nov, 2023')
star.entry_show(4, 'War', '2 oct, 2019')
star.entry_show(5, 'RRR', '15 Aug, 2022')
star.entry_show(6, '2.0', '10 feb, 2018')

while True:
    print('----------------------------------------')
    print('\n\tWelcome to Our Star Cineplex !')
    
    print('1. View all show today')
    print('2. View available seats')
    print('3. Book Ticket')
    print('4. Exit')

    option = int(input('Enter Option: '))

    if option == 1:
        print('----------')
        star.view_show_list()
        print('----------')

    elif option == 2:
        print('----------')
        id = int(input('Enter Show ID: '))
        print(f'-------- Available seats for Show ID: {id} --------')
        star.view_available_seats(id)
        print('----------')
    elif option == 3:
        print('----------')
        id = int(input('Enter Show ID: '))
        tickets = int(input('Number of tickets: '))
        for i in range(tickets):
            row = int(input(f'Enter seat Row for ticket {i + 1} out of {tickets}: '))
            col = int(input('Enter seat Col: '))
            star.book_seats(id,[(row - 1, col - 1)])
        print('----------')

    elif option == 4:
        break