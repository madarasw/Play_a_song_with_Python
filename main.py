# I, Madara Wimalarathna wrote this code for a demonstration in my YouTube channel.
# https://www.youtube.com/watch?v=b5m8xynz8Rw&t=6s
# The idea behind this code is mine.
# I am happy if anyone finds this useful.
# Feel free to use this for any purpose.
# Kindly give credits to the original owner.

# This chord will play the song "Manike Mage Hithe".
# You will hear a repeating pattern, Melody and a Harmony when you run the code.
# Comments will guid you through the code.
# Refer to the README file to understand the input structure of the text files.

# Import scamp library and other useful packages
from scamp import *
import random

# Define constants
PLAY_TIME = 0.2
SMALL_PLAY_TIME = 0.0001

# Use scamp library to create a piano session
piano_session = Session()
piano = piano_session.new_part("piano")

# Create a dict to get the relevant pitch of a notation
pitch_dict = {
    "B": 71,
    "C": 72,
    "d": 73,
    "C": 74,
    "e": 75,
    "E": 76,
    "f": 77,
    "F": 78,
    "G": 79,
    "a": 80,
    "A": 81,
    "b": 82,
    }

# Create a list of pitches to specify the repeating background pattern
chords = [[73, 76, 80], [69, 73, 76], [71, 75, 78], [68, 71, 75]]


def read_content(file_name):
    """
    :param file_name: The name of the file to read
    :return: Content after removing spaces, "\n" and "|"
    """
    with open(file_name) as f:
        content = f.read()
        content = content.replace(' ', '')
        content = content.replace('\n', '')
        content = content.replace('|', '')
        return content


# Read the melody and harmony as a string and remove spaces, "\n" and "|"
melody = read_content("Manike_melody.txt")
harmony = read_content("Manike_harmony.txt")

piano_session.start_transcribing()

# Define variables to control the repeating background pattern
current_chord = 3
chord_note = 0

for n in range(0, len(melody)-1):
    # Reading notes one by one from the full string read from the file
    note_melody = melody[n]
    note_harmony = harmony[n]

    # Play the repeating background pattern
    piano.play_note(chords[current_chord % 4][chord_note % 3], 0.1, SMALL_PLAY_TIME)
    chord_note += 1
    if chord_note % 12 == 0:
        current_chord += 1

    # Skip a beat when there is no note to play
    if note_melody == '+' or note_melody == '-':
        wait(PLAY_TIME)
    else:
        # Play the melody and harmony. Random weight is given to each play to make the output natural
        if note_harmony != "+" and note_harmony != "-":
            piano.play_note(pitch_dict[note_harmony], random.randint(3, 5)/10, SMALL_PLAY_TIME)
        piano.play_note(pitch_dict[note_melody], random.randint(5, 9)/10, PLAY_TIME)


print("----------------------------------- END OF THE SONG -----------------------------------")

# End the piano session
piano_session.stop_transcribing()

























#
# from scamp import *
#
# s = Session()
# piano = s.new_part("piano")
#
# for i in (60, 64, 67):
#     piano.play_note(i, 1, 1)








# chords = [[85, 88, 92], [81, 85, 88], [83, 87, 90], [80, 83, 87]]
# chords = [[73, 76, 80], [69, 73, 76], [71, 75, 78], [68, 71, 75]]
# chords = [[61, 64, 68], [57, 61, 64], [59, 63, 66], [56, 59, 63]]
