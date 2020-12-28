# Stress relief exercises and coping mechanisms.
exercises = ['Meditate', 'Do one of those exercises in your notes app', 'Take a power nap. 10 minutes will change your outlook.']
wisdom = ['Don\'t quit. You\'ll wish you hadn\'t quit.', 'Exercise and meditation are key.']

# Opening message for me -- tuple because it shouldn't change during run-time
MESSAGE = ('\t\t\tM\tE\tS\tS\tA\tG\tE\n\t\t\tStress, anxiety, and loneliness are temporary things. \n\t\t\tI wasn\'t mature because I was in martial arts, I was mature because I was responsible, \n\t\t\tsober, and wanted to change.')

# print all of the exercises
def list_exercises():
    for i in range(len(exercises)):
        print('{}. {}'.format(i+1, exercises[i]))

# print some wisdom
def list_wisdom():
    for i in range(len(wisdom)):
        print('{}. {}'.format(i+1, wisdom[i]))

# main method
if __name__ == "__main__":
    # print the main message
    print(MESSAGE)

    # What's needed more?
    response = int(input('What do you need? 1) exercises or 2) wisdom? '))

    if response == 1:
        list_exercises()
    elif response == 2:
        list_wisdom()
    else:
        print('Oops. Do you want either of those? That answer doesn\'t work.')


