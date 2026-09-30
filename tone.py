MIN_VELOCITY = 0
MAX_VELOCITY = 127

MIN_SUSTAIN = 1
MAX_SUSTAIN = 10000000

MIN_NOTE = 0
MAX_NOTE = 96

OCTAVE_SIZE = 12
NOTES = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]


class Note:

    @staticmethod
    def validate_range(value:int, min_val:int, max_val:int):
        if value < min_val or value > max_val:
            raise ValueError(f"Note value '{value}' must be between {min_val} and {max_val}")

    def get_readable_note(self):
        octave = self.note // 12
        note = self.note % 12
        return NOTES[note] + str(octave)

    def __init__(self,
                 note: int, # 0-87 notes
                 velocity: int, # 0-127
                 sustain: int): # milliseconds 1-...
        try:
            Note.validate_range(note, MIN_NOTE, MAX_NOTE)
            Note.validate_range(velocity, MIN_VELOCITY, MAX_VELOCITY)
            Note.validate_range(sustain, MIN_SUSTAIN, MAX_SUSTAIN)
        except ValueError as e:
            print(e)
            exit(1)

        self.note = note
        self.velocity = velocity
        self.sustain = sustain


notes = [
    Note(0, 4, 1000),
    Note(1, 4, 1000),
    Note(2, 4, 1000),
    Note(3, 4, 1000),
    Note(4, 4, 1000),
    Note(5, 4, 1000),
    Note(6, 4, 1000),
    Note(7, 4, 1000),
    Note(23, 4, 1000),
]


