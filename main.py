import os
import subprocess
import textwrap

from pymusictheory import Chord, Interval, NoteAlteration, NoteInOctave


def chord_to_musicxml(chord: Chord) -> str:
    """
    Generate MusicXML for the chord based on its notes.
    """

    template_xml = textwrap.dedent("""\
        <?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 3.1 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
        <score-partwise version="3.1">
        <part-list>
            <score-part id="P1">
            <part-name>Music</part-name>
            </score-part>
        </part-list>
        <part id="P1">
            <measure number="1">
            <attributes>
                <divisions>1</divisions>
                <key>
                <fifths>0</fifths>
                </key>
                <clef>
                <sign>G</sign>
                <line>2</line>
                </clef>
            </attributes>

            {}

            </measure>
        </part>
        </score-partwise>
    """)

    chord_xml = ""

    for i, note_in_octave in enumerate(chord):
        chord_xml += textwrap.indent(
            textwrap.dedent(f"""
            <note>
                {"<chord/>" if i != 0 else ""}
                <pitch>
                <step>{note_in_octave.letter}</step>
                <alter>{int(note_in_octave.alteration)}</alter>
                <octave>{note_in_octave.octave}</octave>
                </pitch>
                <duration>4</duration>
                <type>whole</type>
            </note>
        """),
            " " * 4,
        )

    # Insert chord xml into template
    musicxml = template_xml.format(chord_xml)

    return musicxml


def musicxml_to_png(musicxml: str, path: str) -> None:
    """
    Generate an image at `path` containing the specified musicxml.
    """

    # Write xml to temporary file
    with open("temp.xml", "w") as file:
        file.write(musicxml)
    print("MusicXML file 'temp.xml' has been generated.")

    # Run `mscore` command to generate png image
    try:
        subprocess.run(["mscore", "temp.xml", "-o", path, "-T", "50"], check=True)
        print(f"MuseScore has generated {path}.")
    except subprocess.CalledProcessError as e:
        print(f"Error generating image: {e}")
    except FileNotFoundError:
        print("MuseScore is not installed or not found in PATH.")


def main():
    chord = Chord(
        {
            NoteInOctave.from_str("C4"),
            NoteInOctave.from_str("E4"),
            NoteInOctave.from_str("G#4"),
        }
    )

    # We will generate all chords with the root between these notes, not including the end root. We will only consider roots with no accidental or a single accidental.
    start_root = NoteInOctave.from_str("C4")
    end_root = NoteInOctave.from_str("C5")

    # Find all possible notes between the specified roots, with possible *single* alterations (natural/sharp/flat)
    roots_with_duplicates: list[set[NoteInOctave]] = []
    current_note_position = start_root.absolute_semitone_offset
    while current_note_position != end_root.absolute_semitone_offset:
        # Ignore notes with double alterations (double sharp/flat)
        root_candidates = {
            note
            for note in NoteInOctave.from_absolute_semitone_offset(
                current_note_position
            )
            if note.alteration
            in (NoteAlteration.NATURAL, NoteAlteration.SHARP, NoteAlteration.FLAT)
        }
        roots_with_duplicates.append(root_candidates)
        current_note_position += 1
    roots: set[NoteInOctave] = set.union(*roots_with_duplicates)

    sorted_roots = sorted(roots)

    # For each root, construct a major chord
    chords = [
        Chord({root, root + Interval.MAJOR_THIRD, root + Interval.PERFECT_FIFTH})
        for root in sorted_roots
    ]

    musicxmls = [chord_to_musicxml(chord) for chord in chords]

    # Create "chords" directory if not present
    os.makedirs("chords", exist_ok=True)

    # Write each musicxml string to a file, with filename containing the notes
    for musicxml, chord in zip(musicxmls, chords):
        sorted_notes = sorted(chord)
        filename = "_".join((str(note) for note in sorted_notes))
        musicxml_to_png(musicxml, os.path.join("chords", f"{filename}.png"))
        print(f"Generated {filename}.png")


if __name__ == "__main__":
    main()
