<b>Chord transposing module version 1.0 for musical chords. Originally written in Python 3.10 environment.</b>

Contains chord_transpose function that does the following:
  - takes a string with chords progression and a transposing value.
  - returns the transposed chord progression as a string.
Input chord progression must contain chord notes in capital letters followed when necessary by # or b. Non-capital letters are not considered as musical notes and are ignored. Here is an example of a typical chord progression with chord notes that is suitable for chord_transpose function: "F/Bb C F/Bb C G#maj7 F/G G Cm Cm/B G#maj7 Fm7 Gm7 G7 Cm Csus2 C".

The transpose value must be in semitones in a range from -12 to 12. For example it can be -2, 2, 4, or 0 (in this case the transposed progression will remain the same as the original).

The function is using regular expressions module for tracking chord notes and replacing them with transposed ones. The general idea of this function is that it is not sensitive to types of chords and any added steps. It literally can work with any types of chords. It picks only musical notes in a string and replaces them with transposed ones.

This module can run as a standalone program asking you to enter the chord progression and a transpose value after "@" on the same string. As an example, when entered "Bm A6 Gmaj7 Fsus4 F @-2" program returns "Am G6 Fmaj7 Ebsus4 Eb".
