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
    prompt = input('Type 'Quit' to confirm, otherwise type 'Go back')
    if prompt == 'quit':
        quit()
    elif prompt == 'Go back'
        initial_prompt()
    else:
        print('Not a valid selection.')
        quit_prompt()


def donor_dict(donor):
    donors = donor_list
    dict = {}
    for donor in donors in enumerate():
        if index % 3
        dict[item] = a[index+1]
        return dict['first name', 'last name', 'total donations', 'average donation'] = 'donor[0]', 'donor[1]', 'donor[2]', 'donor[4]'
    my_dict = {}

dict = {}
a = [('sera', 'smith', 500), ('doge', 'shioda', 250), ('casey', 'Okane', 350)]

a = zip(first, last, amount)

for name, profession in a:
    professions_dict[name] = profession

a = [('sera', 'smith', 500), ('doge', 'shioda', 250), ('casey', 'Okane', 350)]
dict = {}
a = zip(first, last, amount)
print a

for name, profession in a:
    professions_dict[name] = profession

dict


    def create_dic(text):
    """Return {} with key value pairs"""
    first = text.split(' ')
    dic = {}
    for words in range(0, len(first) - 2):
        couple = "{0} {1}".format(first[words], first[words + 1])
        value = first[words + 2]
        dic.setdefault(couple, []).append(value)
    return dic


def donor_list_prompt():
    """Prompt user for a name or to view donor list."""
    prompt = input('Type a donor name or 'donors' to see a list of donors')
    if prompt == 'donors':
        name_list()
    else:
        update_donations(prompt)


def update_donations(donor):
    """Update donor values."""
    f_name, l_name, d_amount = prompt
    prompt = input('Enter: First Name, Last Name, Donation Amount').split
        return f_name, l_name, int(d_amount)
    for donor in donors
    donor.append(doner_list)


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
