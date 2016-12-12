"""Psuedo code to create email and report from a list of donors."""
import io

donors = []


class Donor:
    """Stores donor info."""

    first_name = ""
    last_name = ""
    donations = []
    total_amount = 0


def initial_prompt():
    """Prompt the user for their choice."""
    while True:
        prompt = input('Select from the following options: Create report, Send thank you, Quit: ')
        if prompt == 'quit':
            quit_prompt()
        elif prompt == 'create report':
            create_report()
        elif prompt == 'send thank you':
            send_thanks()
        else:
            print('Not a valid selection')


def quit_prompt():
    """Bring up prompt to quit the program."""
    prompt = input('Type \'Quit\' to confirm, otherwise type \'Go back\'').lower()
    if prompt == 'quit':
        quit()

def send_thanks():
    donor = Donor()
    donor.first_name = 'list'
    while donor.first_name == 'list':
        donor.first_name = input('Type first name of the donor OR type \'list\' to see a list of donors: ')
        if donor.first_name == 'list':
            name_list()
    donor.last_name = input('Type the last name of the donor: ')
    amount = 0
    while amount == 0:
        userInput = input('Enter donation amount: ')
        try:
            amount = int(userInput)
        except ValueError:
            print('Invalid input. Enter a number: ')
    d = get_donor(donor)
    d.donations.append(amount)
    d.total_amount += amount
    generate_email(d)

def get_donor(donor):
    """Checks if inputted donor already exists in the system."""
    for d in donors:
        if d.first_name == donor.first_name and d.last_name == donor.last_name:
            return d
    donors.append(donor)
    return donor


def name_list():
    """returns list of all donor names."""
    for d in donors:
        print("{0} {1}".format(d.first_name, d.last_name))

def create_report():
    """Return and print ordered list of donor stats."""
    print('Your report:')
    for donor in donors:
        avg = donor.total_amount/len(donor.donations)
        line = ('{0} {1} has donated a total of ${2} in {3} donations at ${4} per donation.'.format(donor.first_name, donor.last_name, donor.total_amount, len(donor.donations), avg))
        print(line)

# def generate_text(donors):
#     """Return list of donors."""
#     people = list(donors.keys())
#     text_string = ' '
#     for donor in people:
#         values = donors[donor]
#         temp_val = ('{0}:{1} {2}'
#                     '{3}\n'.format(donor, values[0], values[1], values[2]))
#         text_string = text_string + temp_val
#         return text_string

def generate_email(donor):
    """Generate email for donor."""
    print('\nWell met {0} {1}!,\n We would like to thank you for your donation of ${2}.'.format(donor.first_name, donor.last_name, donor.donations[-1]))

if __name__ == '__main__':
    initial_prompt()
