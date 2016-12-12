"""Code to create email and report from a list of donors."""
donors = []


class Donor:
    """Stores donor info."""

    first_name = ""
    last_name = ""
    donations = 0
    total_amount = 0

    @classmethod
    def create(cls, first_name, last_name, donations, total_amount):
        """Create an instance of Donor for testing."""
        d = Donor()
        d.first_name = first_name
        d.last_name = last_name
        d.donations = donations
        d.total_amount = total_amount
        return d


def initial_prompt():
    """Prompt the user for their choice."""
    while True:
        prompt = input('Select from the following options: Create report, Send thank you, Quit: ')
        if prompt == 'quit':
            quit_prompt()
        elif prompt == 'create report':
            create_report(donors)
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
    """Check if donor exists in system and otherwise prompts for input to add full name and amount."""
    donor = Donor()
    donor.first_name = 'list'
    while donor.first_name == 'list':
        donor.first_name = input('Type first name of the donor OR type \'list\' to see a list of donors: ')
        if donor.first_name == 'list':
            name_list(donors)
    donor.last_name = input('Type the last name of the donor: ')
    amount = 0
    while amount == 0:
        user_input = input('Enter donation amount: ')
        try:
            amount = int(user_input)
        except ValueError:
            print('Invalid input. Enter a number: ')
    d = get_donor(donor, donors)
    d.donations += 1
    d.total_amount += amount
    generate_email(d, amount)


def get_donor(donor, donors):
    """Check if inputted donor already exists in the system."""
    for d in donors:
        if d.first_name == donor.first_name and d.last_name == donor.last_name:
            return d
    donors.append(donor)
    return donor


def name_list(donors):
    """Return list of all donor names."""
    for d in donors:
        print("{0} {1}".format(d.first_name, d.last_name))


def create_report(donor_list):
    """Return and print ordered list of donor stats."""
    print('Your report:')
    donor_list.sort(key=lambda x: x.total_amount)
    print('FIRST\t\tLAST\t\tTOTAL\tCOUNT\tAVG')
    for donor in donor_list:
        avg = donor.total_amount / donor.donations
        line = ('{0}\t\t{1}\t\t${2}\t{3}\t${4}'.format(donor.first_name, donor.last_name, donor.total_amount, donor.donations, avg))
        print(line)


def generate_email(donor, amount):
    """Generate email for donor."""
    print('\nWell met {0} {1}!,\n We would like to thank you for your donation of ${2}.'.format(donor.first_name, donor.last_name, amount))


if __name__ == '__main__':
    initial_prompt()
