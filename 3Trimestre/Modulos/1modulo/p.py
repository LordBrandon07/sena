# def scales (C, D, E):
#     C = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
#     Db = ['C#, D#, F, F#, G#, A#, C']
#     D = ['D, E, F#, G, A, B, C#']
#     Eb = ['D#, F, F#, G#, A#, C, C#']
#     E = ['E, F#, G#, A, B, C#, D#']
#     F = ['F, G, A, Bb, C, D, E']
#     Gb = ['F#, G#, A#, B, C#, D#, F']
#     G = ['G, A, B, C, D, E, F#']
#     Ab = ['G#, A#, C, C#, D#, F, F#']
#     A = ['A, B, C#, D, E, F#, G#']
#     Bb = ['A#, C, D, D#, F, G, G#']
#     B = ['B, C#, D#, E, F#, G#, A#']

# Notes = ['C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B']

# pro = Notes[0, 5, 2, 6]



# print(C[0], C[5], C[2], C[6])


# def generate_major_scales():
#   major_scales = {
#       "C Major": ["C", "D", "E", "F", "G", "A", "B"],
#       "C# Major": ["C#", "D#", "F", "F#", "G#", "A#", "C"],
#       "D Major": ["D", "E", "F#", "G", "A", "B", "C#"],
#       "D# Major": ["D#", "F", "F#", "G#", "A#", "C", "C#"],
#       "E Major": ["E", "F#", "G#", "A", "B", "C#", "D#"],
#       "F Major": ["F", "G", "A", "Bb", "C", "D", "E"],
#       "F# Major": ["F#", "G#", "A#", "B", "C#", "D#", "F"],
#       "G Major": ["G", "A", "B", "C", "D", "E", "F#"],
#       "G# Major": ["G#", "A#", "C", "C#", "D#", "F", "F#"],
#       "A Major": ["A", "B", "C#", "D", "E", "F#", "G#"],
#       "A# Major": ["A#", "C", "D", "D#", "F", "G", "G#"],
#       "B Major": ["B", "C#", "D#", "E", "F#", "G#", "A#"],
#   }
#   return major_scales


# def generate_chord_progressions(scale):
#   major_scales = generate_major_scales()
#   scale_notes = major_scales.get(scale)
#   if not scale_notes:
#     return "Scale not found."
  
#   progressions = []
#   progressions.append([scale_notes[0], scale_notes[2], scale_notes[4]])
#   progressions.append([scale_notes[2], scale_notes[4], scale_notes[5]])
#   progressions.append([scale_notes[4], scale_notes[5], scale_notes[7]])
#   progressions.append([scale_notes[5], scale_notes[7], scale_notes[9]])
  
#   return progressions


# generate_chord_progressions("C Major")

# def generate_major_scales(major_scales):
#   major_scales = {}
#   major_scales["C Major"] = ["C", "D", "E", "F", "G", "A", "B"]
#   major_scales["C# Major"] = ["C#", "D#", "F", "F#", "G#", "A#", "C"]
#   major_scales["D Major"] = ["D", "E", "F#", "G", "A", "B", "C#"]
#   major_scales["D# Major"] = ["D#", "F", "G", "G#", "A#", "C", "D"]
#   major_scales["E Major"] = ["E", "F#", "G#", "A", "B", "C#", "D#"]
#   major_scales["F Major"] = ["F", "G", "A", "Bb", "C", "D", "E"]
#   major_scales["F# Major"] = ["F#", "G#", "A#", "B", "C#", "D#", "F"]
#   major_scales["G Major"] = ["G", "A", "B", "C", "D", "E", "F#"]
#   major_scales["G# Major"] = ["G#", "A#", "C", "C#", "D#", "F", "G"]
#   major_scales["A Major"] = ["A", "B", "C#", "D", "E", "F#", "G#"]
#   major_scales["A# Major"] = ["A#", "C", "D", "D#", "F", "G", "A"]
#   major_scales["B Major"] = ["B", "C#", "D#", "E", "F#", "G#", "A#"]
  
#   return major_scales

# print(generate_major_scales(1))




