import pandas as pd

# Standardizes a timezone string (ex: PST) to UTC format (0-24)
def to_utc(timezone):
    timezone = timezone.upper()

    # If the timezone begins with GMT, convert it to UTC format (0-24)
    if timezone.startswith('GMT'):
        timezone = timezone.replace('GMT', '')
        timezone = int(timezone)
        if timezone < 0:
            timezone = 24 + timezone
        return timezone

    # Otherwise, convert using the timezone dictionary
    if timezone == 'UTC':
        return '0'
    elif timezone == 'EST':
        return '5'
    elif timezone == 'CST':
        return '6'
    elif timezone == 'MST':
        return '7'
    elif timezone == 'PST' or timezone == 'PDT' or timezone == 'PT' or 'PACIFIC' in timezone:
        return '8'
    elif timezone == 'AKST':
        return '9'
    elif timezone == 'HST':
        return '10'
    elif timezone == 'AST':
        return '11'
    elif timezone == 'NST':
        return '12'
    elif timezone == 'CET':
        return '13'
    elif timezone == 'EET':
        return '14'
    elif timezone == 'MSK':
        return '15'
    elif timezone == 'IST':
        return '16'
    elif timezone == 'JST':
        return '17'
    elif timezone == 'GMT':
        return '18'
    elif timezone == 'BST':
        return '19'
    elif timezone == 'CEST':
        return '20'
    elif timezone == 'EEST':
        return '21'
    elif timezone == 'MSK':
        return '22'
    elif timezone == 'IST':
        return '23'
    elif timezone == 'JST':
        return '24'
    else:
        return timezone

# Flattens a language response
# Ex: mandarin -> CHINESE
# Ex: English -> ENGLISH
# Ex: Chinese -> CHINESE
def lang_flatten(language):
    language = language.upper()
    if 'CHINESE' in language:
        return 'CHINESE'
    elif 'MANDARIN' in language:
        return 'CHINESE'
    elif 'ENGLISH' in language:
        return 'ENGLISH'
    elif 'SPANISH' in language:
        return 'SPANISH'
    elif 'FRENCH' in language:
        return 'FRENCH'
    elif 'KOREAN' in language:
        return 'KOREAN'
    elif 'JAPANESE' in language:
        return 'JAPANESE'
    elif 'ARABIC' in language:
        return 'ARABIC'
    else:
        return language

# Read responses from .csv file
responses = pd.read_csv('responses.csv')

# Data Cleaning
## Timezone Standardization
responses['# UTC OFFSET'] = responses['What timezone are you in?'].apply(to_utc)

## Language Flattening
# For the purposes of group formation, Mandarin == Chinese
responses['# LANGUAGE'] = responses['What is your native language? (you may list more than one, or if multiple, a preferred language)'].apply(lang_flatten)

# Export to .csv file
responses.to_csv('responses_new.csv', index=False)

