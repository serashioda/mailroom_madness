"""Psuedo code to create email and report from a list of donors."""
import io


def initial_prompt():
    """Prompt the user for their choice."""
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
    """Bring up prompt to quit the program."""
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
    """Return a list of donors and print their names."""
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


def donor_calc(donations, value):
    """Return donation values."""
    donations[0] = int(donations[0]) + value
    donations[1] = int(donations[1]) + 1
    donations[2] = int(donations[2]) / int(donations[1])
    return donations


def sorted_list(first):
    """Return sorted list of donors from biggest donations to smallest donations."""


def donation_prompt(person):
    """Prompt and return an integer from user."""
    value = input('How much did {0} donate? Type quit to quit'.format(person))
    if value == 'quit':
        quit()
    else:
        int(value)
    return value


def update_donations(person):
    """Update donor values."""
    donors = donor_list(read_donors(), 'dictionary')
    value = int(donation_prompt(person))
    if person in list(donors.keys()):
        donations = donors[person]
        new_donations = donor_calc(donations, value)
        donors.setdefault(person, new_donations)
    else:
        donors.setdefault(person, [value, 1, value])
    val = donors[person]
    write_file(generate_text(donors))
    generate_email(person, val[0])


def generate_text(donors):
    """Return list of donors."""
    people = list(donors.keys())
    text_string = ' '
    for donor in people:
        values = donors[donor]
        temp_val = ('{0}:{1} {2}'
                    '{3}\n'.format(donor, values[0], values[1], values[2]))
        text_string = text_string + temp_val
        return text_string



def write_file(text):
    """Write donor list to .txt file."""
    text_file = io.open('donors.txt', 'w')
    text_file.write(text)
    text_file.close()


def generate_email(person, donations):
    """Generate email for donor."""
    print('\nWell met {0}!,\n We would like to thank you for your donation of ${1}.'.format(person, donations))
    quit_prompt()


def read_donors():
    """Return donor txt file."""
    openfile = io.open('donors.txt')
    readfile = openfile.readlines()
    openfile.close()
    return readfile



def donor_list(readfile, choice):
    """Return list or dictionary depending on user choice."""


if __name__ == '__main__':
    initial_prompt()
