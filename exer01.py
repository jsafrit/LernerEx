import datetime
from collections import namedtuple


PLACE = namedtuple('PLACE', 'city country')


def get_trip_input():
    user_info=input('Tell me where you went: ')
    while ',' not in user_info:
        if not user_info:
            print('Done')
            return None
        print('You must enter a  "City, Country" combination.')
        user_info = input('Tell me where you went: ')
    return user_info


def parse_trip(trip):
    city, country = trip.split(',', 1)
    return PLACE(city.strip(), country.strip())


if __name__ == '__main__':
    print(__file__, datetime.datetime.now().isoformat())

    ledger = dict()

    trip_string=get_trip_input()
    while trip_string:
        entry=parse_trip(trip_string)
        print(entry)
        ledger[entry]=ledger.get(entry, 0) + 1
        trip_string = get_trip_input()

    print(ledger)
    for destination in sorted(ledger.keys(), key=lambda x:x.country):
        if ledger[destination] > 1:
            print('{}, {}   {}'.format(destination.city, destination.country, ledger[destination]))
        else:
            print('{}, {}'.format(destination.city, destination.country))

