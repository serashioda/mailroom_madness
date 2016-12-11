# mailroom_madness

Program with a small command-line script to handle the task of sending manual thank-you-emails to donors

""" psuedo code for the above-stated program. """

donors = {'donors': '[individual donations]'}

def donor_list(prompt, validator=None):
    """ returns user input after prompt """
    user_select = prompt("Select option: select LIST for donor list of names and history of donation amounts. Select EXIT to exit out of system. /n

    Once a donor is selected, make a choice of either actions: 'Send a Thank You' or 'Create a Report'.)


""" data structure that holds list of donors, and history of donation amounts """


def user_choice():
    """ Once run, this script will prompt user choice: ‘Send a Thank You’ or ‘Create a Report’.


def thanks_or_no():
    """ If user selects ‘Send a Thank You’, prompt for a Full Name. """
    if____:
    thank_you = prompt("Please enter the donor's full name?")



    elif____:
    """ this handles option to fill out report instead of thank you """


    else:
    """ handles invalid/no input from user (from assignment example) """
        while reply is None:
          reply = ask_for_input(prompt)
          if there_is_a_validator:
            validate_the_reply
        return reply


<!-- def get_user_input(prompt, validator=None):
    """return the value input by a user prompted by `prompt`

    optionally, validate the input with a function `validator` which must
    take one argument, the input from the user and must return the input if
    valid, and None if not valid
    """
    reply = None
    while reply is None:
        reply = ask_for_input(prompt)
        if there_is_a_validator:
            validate_the_reply
    return reply -->
