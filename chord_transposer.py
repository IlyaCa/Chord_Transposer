""" Chord transposing module version 1.0 for musical chords
 Contains chord_transpose function that does the following:
  - takes a string with chords progression and a transposing value.
  - returns the transposed chord progression as a string.
 Here is an example of a typical chord progression with chord notes
 that is suitable for chord_transpose function:
 F/Bb C F/Bb C G#maj7 F/G G Cm Cm/B G#maj7 Fm7 Gm7 G7 Cm Csus2 C

 The function is using regular expressions' module for tracking chord notes
 and replacing them with transposed ones.

 The general idea of this function is that it is not sensitive to types of chords
 and any added steps. It literally can work with any types of chords. It picks only
 notes in text and replaces them with transposed ones.

 This module can run as a standalone program asking you to enter the chord
 progression and a transpose value after "@" on the same string.
"""

import re


def chord_transpose(my_chords: str, transp_value: int):
    """ 2 dictionaries below are used to convert chord notes into numbers and back.
    This is helpful for transposing them.
    The dictionary for reading contains some different names for the same chords.
    """
    chords_read = {'A': 1, 'Bb': 2, 'A#': 2, 'B': 3, 'H': 3, 'C': 4, 'C#': 5,
                   'Db': 5, 'D': 6, 'D#': 7, 'Eb': 7, 'E': 8,
                   'F': 9, 'F#': 10, 'Gb': 10, 'G': 11, 'G#': 12, 'Ab': 12}
    chords_write = {1: 'A', 2: 'Bb', 3: 'B', 4: 'C', 5: 'C#', 6: 'D', 7: 'Eb',
                    8: 'E', 9: 'F', 10: 'F#', 11: 'G',
                    12: 'G#'}
    """
    Below is a pattern for chord note.
    The chord note is the part of a chord name that is responsible for its tone.
    The chord note comprises a capital letter(A...H) and the optional # or b sign.
    """
    pattern = r'[A-H][b|#]?'

    # I am creating 3 separate lists:
    #   for matches (chord notes), for start indexes, 2 for end indexes.
    matches = []
    starts = []
    ends = []

    # re.finditer is an iterator that finds chord notes and puts them into my lists.
    for match in re.finditer(pattern, my_chords):
        matches.append(match.group())
        starts.append(match.start())
        ends.append(match.end())

    # Total number of chords.
    chords_num = len(matches)
    if chords_num == 0:
        return 'No chords found!'

    # Converting matches (found chord notes) into numbers.
    # This is needed to transpose them properly.
    num_matches = []
    for item in matches:
        num_matches.append(chords_read[item])

    # Transposing my chord progression in numeric state.
    for counter in range(chords_num):
        num_matches[counter] += transp_value
        if num_matches[counter] > 12:
            num_matches[counter] -= 12
        if num_matches[counter] < 1:
            num_matches[counter] += 12

    # Creating a list of transposed chord notes from the list of numbers.
    transposed_chord_notes = []
    for item in num_matches:
        transposed_chord_notes.append(chords_write[item])

    """
    Creating a final progression in a form of string that we are returning.
    It contains all transposed chord notes and all the rest comes
    intact from original progression.
    """
    output_progression = ''
    for num in range(chords_num):
        if num < (chords_num - 1):
            output_progression += (transposed_chord_notes[num] + my_chords[ends[num]:starts[num + 1]])
        else:
            output_progression += (transposed_chord_notes[num] + my_chords[ends[num]:])
    return output_progression


def interactive_transposer():
    print('Chord transposer v1.0')
    print('Please enter a chord progression followed by "@t" where "t" is transpose constant in semitones (-12...12).')
    print('Example: F/Bb C F/Bb C G#maj7 F/G G Cm Cm/B G#maj7 Fm7 Gm7 G7 Cm Csus2 C @-2')
    my_progr = input('>:')

    # Search pattern for transpose constant
    transp_pat = r'@-?\d\d?'
    transp_obj = re.search(transp_pat, my_progr)
    if transp_obj is not None:
        transp_str = transp_obj.group()
        at_index = transp_obj.start()
        transp_num = int(transp_str[1:])
        output_str = chord_transpose(my_progr[:at_index], transp_num)
        print('Transposed progression: ' + output_str)
    else:
        print('No transpose constant found!')
    return None


if __name__ == '__main__':
    interactive_transposer()
