import pandas as pd

# A Student
class Student:
    def __init__(self, response):
        self.name = response['What\'s your name?']
        self.timezone = response['# UTC OFFSET']
        self.language = response['# LANGUAGE']
        self.roles = [response['# ROLE 1'], response['# ROLE 2'], response['# ROLE 3']]

    def __str__(self):
        return self.name + ' (' + str(self.timezone) + ', ' + self.language + ', ' + str(self.roles) + ')'

# A Group
class Group:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add(self, student):
        self.students.append(student)

    def get_roles(self):
        return [student.roles for student in self.students]

    def get_languages(self):
        return [student.language for student in self.students]

    def get_mean_timezone(self):
        # If no students, return negative infinity
        if self.size() == 0:
            return float('inf')
        else:
            return sum([float(student.timezone) for student in self.students]) / len(self.students)

    def size(self):
        return len(self.students)

    def __str__(self):
        return 'Group ' + str(self.name) + ': ' + str([student.name for student in self.students])

# Standardizes a timezone response (ex: PST, Pacific Standard, Seattle) to UTC format (0-24)
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
    elif timezone == 'PST' or timezone == 'PDT' or timezone == 'PT' or timezone == 'PCT' or 'PACIFIC' in timezone or 'SEATTLE' in timezone or 'CALIFORNIA' in timezone or 'CUPERTINO' in timezone:
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
    elif timezone == 'GMT' or 'CHINA' in timezone or 'SHANGHAI' in timezone or 'BEIJING' in timezone:
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
        return '-1'

# Flattens a language response
# Ex: Mandarin -> CHINESE (the horror)
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

# Extracts roles from responses
def extract_roles(responses):
    # New column for roles
    responses['# ROLE 1'] = None
    responses['# ROLE 2'] = None
    responses['# ROLE 3'] = None

    # Extract roles from responses
    for i in range(len(responses)):
        student = responses.iloc[i]
        # Project Manager
        if (student['What roles interest you? [Project Manager]'] == 'First Choice'):
            responses.at[i, '# ROLE 1'] = 'Project Manager'
        elif (student['What roles interest you? [Project Manager]'] == 'Second Choice'):
            responses.at[i, '# ROLE 2'] = 'Project Manager'
        elif (student['What roles interest you? [Project Manager]'] == 'Third Choice'):
            responses.at[i, '# ROLE 3'] = 'Project Manager'

        # UI/UX Designer
        if (student['What roles interest you? [UI/UX Designer]'] == 'First Choice'):
            responses.at[i, '# ROLE 1'] = 'UI/UX Designer'
        elif (student['What roles interest you? [UI/UX Designer]'] == 'Second Choice'):
            responses.at[i, '# ROLE 2'] = 'UI/UX Designer'
        elif (student['What roles interest you? [UI/UX Designer]'] == 'Third Choice'):
            responses.at[i, '# ROLE 3'] = 'UI/UX Designer'

        # Backend Developer
        if (student['What roles interest you? [Backend Developer]'] == 'First Choice'):
            responses.at[i, '# ROLE 1'] = 'Backend Developer'
        elif (student['What roles interest you? [Backend Developer]'] == 'Second Choice'):
            responses.at[i, '# ROLE 2'] = 'Backend Developer'
        elif (student['What roles interest you? [Backend Developer]'] == 'Third Choice'):
            responses.at[i, '# ROLE 3'] = 'Backend Developer'

        # Public Relations and Marketing Rep
        if (student['What roles interest you? [Public Relations and Marketing Rep]'] == 'First Choice'):
            responses.at[i, '# ROLE 1'] = 'Public Relations and Marketing Rep'
        elif (student['What roles interest you? [Public Relations and Marketing Rep]'] == 'Second Choice'):
            responses.at[i, '# ROLE 2'] = 'Public Relations and Marketing Rep'
        elif (student['What roles interest you? [Public Relations and Marketing Rep]'] == 'Third Choice'):
            responses.at[i, '# ROLE 3'] = 'Public Relations and Marketing Rep'

        # Quality and DEI Officer
        if (student['What roles interest you? [Quality and DEI Officer]'] == 'First Choice'):
            responses.at[i, '# ROLE 1'] = 'Quality and DEI Officer'
        elif (student['What roles interest you? [Quality and DEI Officer]'] == 'Second Choice'):
            responses.at[i, '# ROLE 2'] = 'Quality and DEI Officer'
        elif (student['What roles interest you? [Quality and DEI Officer]'] == 'Third Choice'):
            responses.at[i, '# ROLE 3'] = 'Quality and DEI Officer'

# Performs preprocessing on raw data
def preprocess(responses):
    # Data Cleaning
    ## Timezone Standardization
    responses['# UTC OFFSET'] = responses['What timezone are you in?'].apply(to_utc)

    ## Language Flattening
    responses['# LANGUAGE'] = responses['What is your native language? (you may list more than one, or if multiple, a preferred language)'].apply(lang_flatten)

    ## Role Extraction
    extract_roles(responses)

# Creates groups of students for a section
def create_section_groups(section, students):
    groups = []
    # Create groups
    for i in range(SECTION_TEAM_COUNT):
        groups.append(Group(str(section) + '-' + str(i + 1)))

    # For each student
    for i in range(len(students)):
        student = Student(students.iloc[i])
        # While the student isn't in a group
        matches = []
        added = False
        seek_role = 0
        for role in student.roles:
            # If we added the student to a group, break
            if added:
                break

            # For each group
            for group in groups:
                # If the group is full, skip
                if group.size() >= TEAM_SIZE_LIMIT:
                    continue

                # If the group doesn't contain the role
                if role not in group.get_roles():
                    # Add to matches
                    matches.append(group)

            # Save role matches
            role_matches = matches

            # For each match
            for match in matches:
                # If the match doesn't contain the student's desired language, remove it
                if student.language not in match.get_languages():
                    matches.remove(match)

            # Add the student to group with the closest average timezone to the student
            if len(matches) > 0:
                # Sort matches by timezone difference to student
                matches.sort(key=lambda x: abs(x.get_mean_timezone() - float(student.timezone)))

                # Add student to group
                matches[0].add(student)
                added = True
                break

            # If no matches were found, add to the first group with size < TEAM_SIZE_LIMIT
            if len(matches) == 0:
                for group in groups:
                    if group.size() < TEAM_SIZE_LIMIT:
                        group.add(student)
                        added = True
                        break

    # Create a Dataframe from the groups
    df = pd.DataFrame(columns=['# TEAM', '# STUDENT', '# LANGUAGE', '# TIMEZONE', '# ROLE 1', '# ROLE 2', '# ROLE 3'])
    for i in range(len(groups)):
        group = groups[i]
        for j in range(len(group.students)):
            student = group.students[j]
            df.loc[i * TEAM_SIZE_LIMIT + j] = [group.name, student.name, student.language, student.timezone, student.roles[0], student.roles[1], student.roles[2]]
        # Add blank rows to fill out the rest of the group
        for j in range(TEAM_SIZE_LIMIT - len(group.students)):
            df.loc[i * TEAM_SIZE_LIMIT + len(group.students) + j] = [group.name, '', '', '', '', '', '']
    return df

# Creates groups from a pre-processed response dataframe
def create_groups(responses):
    # Dataframe to store groups
    groups = pd.DataFrame()

    # Get a list of all sections
    sections = responses['I am in section'].unique()

    # For each section
    for section in sections:
        # Get the students in this section
        students = responses[responses['I am in section'] == section]

        # Create groups for this section
        section_groups = create_section_groups(section, students)

        # Add section groups to groups
        groups = pd.concat([section_groups, groups], axis=0)

    # Return groups
    return groups

# Prompt for .csv file
print('Please enter the name of the .csv file you would like to use:')
file_name = input()

# Prompt for # of groups per section
print('Please enter the number of groups per section:')
SECTION_TEAM_COUNT = int(input())

# Prompt for # of members per group
print('Please enter the number of members per group:')
TEAM_SIZE_LIMIT = int(input())

# Read responses from .csv file
responses = pd.read_csv(file_name)

# Preprocess responses
preprocess(responses)

# Export to .csv file
responses.to_csv('processed_' + file_name, index=False)

# Form groups
groups = create_groups(responses)
groups.to_csv('groups.csv', index=False)
print('Outputted groups to groups.csv')