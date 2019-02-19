"""
    This module provides some helpful functions and variables to parse commands from prompt
"""

from links import CONST_EMAILS, SOCIAL_MEDIA, CODING_MEDIA, BLOGS, SCHOOL
'''MAKE THE COMMANDS DICTIONARY CLASSWIDE OBJECT SO IT CAN BE ACCESSED BY OTHER MODULES'''

commands = {
            'twitter': SOCIAL_MEDIA[0],
            'instagram': SOCIAL_MEDIA[1],
            'github': CODING_MEDIA[0],
            'kaggle': CODING_MEDIA[1],
            'mail': CONST_EMAILS,  # all emails opened
            'mail0': CONST_EMAILS[0],
            'mail1': CONST_EMAILS[1],
            'mail2': CONST_EMAILS[2],
            'xkcd': BLOGS[0],  # xkcd main
            'blog': BLOGS[1],  # xkcd blog
            'school': SCHOOL[0],  # bxsci main website
            'sciencesurvey': SCHOOL[1]  # the science survey online newspaper
            }

input_commands = {
                "t" : 'twitter',
                "twitter" : 'twitter',
                'insta' : 'instagram',
                'instagram' : 'instagram',
                'i' : 'instagram',
                "g" : 'github',
                "git" : 'github',
                "github" : 'github',
                "k" : 'kaggle',
                "kaggle" : 'kaggle',
                "mail" : 'mail0',
                "mail0" : 'mail0',
                "mail1" : 'mail1',
                "mail2" : 'mail2',
                "email" : 'mail',
                "m" : 'mail',
                "xkcd" : 'xkcd',
                "x" : 'xkcd',
                "xk" : 'xkcd',
                "xkcd blog": 'blog',
                "x blog": 'blog',
                "xk blog": 'blog',
                "s" : 'school',
                "school" : 'school',
                "s news" : 'sciencesurvey',
                "school news" : 'sciencesurvey'
                }

def command_to_link(comm):
    return commands[comm.lower()]


def convert_to_command(comm):
    return input_commands[comm.lower()]
