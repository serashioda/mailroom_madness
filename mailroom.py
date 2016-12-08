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
        sort these donors
    quit_prompt()


def donation_prompt(person):
    """Prompt and return an integer from user"""
    value = input('How much did you donate?')
    if value == 'quit'
        quit()
    else
        int(value)
        return value


if __name__ == '__main__':
    initial_prompt()
