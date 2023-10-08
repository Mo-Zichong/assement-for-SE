class Room:
    def __init__(self, number, room_type, price):
        self.number = number
        self.room_type = room_type
        self.price = price
        self.is_available = True

class Customer:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class HotelRoomReservation:
    def __init__(self):
        self.rooms = []
        self.reservations = []

    def add_room(self, room):
        self.rooms.append(room)

    def check_available_rooms(self):
        available_rooms = []
        for room in self.rooms:
            if room.is_available:
                available_rooms.append(room)
        return available_rooms

    def make_reservation(self, room_number, customer_info):
        for room in self.rooms:
            if room.number == room_number and room.is_available:
                reservation_id = len(self.reservations) + 1
                reservation = {'id': reservation_id, 'room': room, 'customer': customer_info}
                self.reservations.append(reservation)
                room.is_available = False
                return reservation_id
        return None

    def cancel_reservation(self, reservation_id):
        for reservation in self.reservations:
            if reservation['id'] == reservation_id:
                room = reservation['room']
                room.is_available = True
                self.reservations.remove(reservation)
                return True
        return False

    def get_reservation(self, reservation_id):
        for reservation in self.reservations:
            if reservation['id'] == reservation_id:
                return reservation
        return None

# Example usage:
hotel = HotelRoomReservation()

# Add rooms to the hotel
room1 = Room('101', 'single', 100.0)
room2 = Room('102', 'double', 150.0)

hotel.add_room(room1)
hotel.add_room(room2)

# Check available rooms
available_rooms = hotel.check_available_rooms()
print("Available Rooms:")
for room in available_rooms:
    print("Room Number:", room.number)
    print("Room Type:", room.room_type)
    print("Price:", room.price)
    print()

# Make a reservation
customer_info = Customer('John Doe', 'johndoe@example.com', '1234567890')
reservation_id = hotel.make_reservation('101', customer_info)
if reservation_id:
    print("Reservation Successful!")
    print("Reservation ID:", reservation_id)
else:
    print("Invalid Room Number or Room Already Booked")

# Cancel a reservation
cancellation_result = hotel.cancel_reservation(reservation_id)
if cancellation_result:
    print("Reservation Cancelled Successfully!")
else:
    print("Invalid Reservation ID")