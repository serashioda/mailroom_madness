"""Psuedo code to create email and report from a list of donors."""
import io


def initial_prompt():
    """Prompt the user for their choice"""
    prompt = input('Select from the following options: ' 'Create report', 'Send thank you', 'Quit')
    if prompt == 'quit':
        quit()
    elif prompt == 'create report': 
        create_report()
    elif prompt == 'send thank you':
        donor_list()
    else:
        print('Not a valid selection')
        initial_prompt()


def quit_prompt():
    """Bring up prompt to quit the program"""
    prompt = input('Quit?')
    if prompt == 'quit':
        quit()
    else:
        print('Not a valid selection.')
        quit_prompt()


def donor_list_prompt():
    """Prompt user for a name or to view donor list."""
    prompt = input('Type donor name or list to see a list of donors')
    if prompt == 'list':
        name_list()
    else:
        update_donations(prompt)


def name_list():
    "Return a list of donors and print their names."
    donors = donor_list("return a list")
    print('List of donors:')
    for name in donors:
        print(name[0])
    donor_list_prompt()

def create_report():
    """Return and print ordered list of donor stats."""
    donors = donor_list
    sorted_donors = sorted_list
    print('Your report:')
    for donor in sorted_donor:
        line = ('{0} has donated a total of ${1} in {2} donations at ${3} per '
                'donation.'.format(donor[0], donor[1], donor[2], donor[3]))
        print(line)
    quit_prompt()


def donation_prompt(person):
    """Prompt and return an integer from user"""
    value = input('How much did {name} donate? Type quit to quit'.format(person))
    if value == 'quit'
        quit()
    else
        int(value)
        return value


def update_donations(person):
    """Update donor values."""

def generate_text(donors):
    """Return list of donors."""

def write_file(text):
    """Write donor list to .txt file."""

def generate_email(person, donations):
    """Generate email for donor."""

def donor_calc(donations, value):
    """Return donation values."""

def read_donors():
    """Return donor txt file."""

def donor_list(readfile, choice):
    """Return list or dictionary depending on user choice."""

def sorted_list(first):
    """Return sorted list of donors from biggest donations to smallest donations."""

if __name__ == '__main__':
    initial_prompt()
