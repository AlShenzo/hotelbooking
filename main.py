import pandas
import pandas as pd

df = pd.read_csv('hotels.csv', dtype={'id':str})
df_cards= pandas.read_csv('cards.csv', dtype = str).to_dict(orient = 'records')

class Hotel:
    def __init__(self,hotel_id):
        self.hotel_id=hotel_id
        self.name = df.loc[df['id'] == self.hotel_id, 'name'].squeeze()


    def book(self):
        """ Book a hotel by changing its availability to no"""
        df.loc[df['id'] == self.hotel_id, 'available'] ='no'
        df.to_csv('hotels.csv', index=False)

    def available(self):
        """Check if the hotel is available"""
        availability = df.loc[df['id'] == self.hotel_id, 'available'].squeeze()
        if availability == "yes":
            return True
        else:
            return False

class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object
        pass
    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are your booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}
        
"""
        return content


class CreditCard:
    def __init__(self, number):
        self.number = number


    def validate(self,expiration, holder, cvc):
        card_data = {'number':self.number,
                     'expiration':expiration,
                     'holder':holder,
                     'cvc':cvc}
        if card_data in df_cards:
            return True
        else:
            return False

class SecureCreditCard:


print(df)
hotel_ID = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_ID)

if hotel.available():
    credit_card = CreditCard(number = "1234")
    if credit_card.validate(expiration = "12/26", holder = 'JOHN SMITH', cvc='123'):
        hotel.book()
        name = input("Enter your name: ")
        reservation_ticket = ReservationTicket(customer_name = name, hotel_object= hotel)
        print(reservation_ticket.generate())
    else:
        print('There was a problem with your payment')
else:
    print("Hotel is not free")

