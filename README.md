# gen-chords

`gen-chords` is a collection of Python programs that
1. Generate PNG images of musical chords based on specified parameters such as clef type, root note range, and chord intervals.
2. Produce an [Anki](https://apps.ankiweb.net/) package for spaced repetition.

The program uses
- The [pymusictheory](https://github.com/valterschutz/pymusictheory) library to handle musical theory concepts.
- [MuseScore](https://musescore.org/en/download) to render the chords into images.
- [genanki](https://github.com/kerrickstaley/genanki) to create the [Anki](https://apps.ankiweb.net/) package.

## Motivation

Page 18 of Jeremy Siskind's [Jazz Piano Fundamentals (Book 1)](https://jeremysiskind.com/product/jazz-piano-fundamentals-book-1/) instructs the reader to generate flashcards for all major, minor, and dominant seventh chords in the F clef.

If you don't care about generating your own chord images and flashcards, you can simply download the `assets` folder, which contains images of all seventh chords in the range E2–E3 on the F clef, and also a corresponding Anki package (`chord_images.apkg`).


## Features

- Generate seventh chords (major, minor, dominant) in different clefs (e.g., G clef, F clef).
- Specify a range of root notes to generate chords for.
- Outputs PNG images of the generated chords, organized into subfolders by chord type.
- Takes the folder of PNG images as input and generates an Anki package from it.

## Requirements

- Python 3.13 or higher
- [MuseScore](https://musescore.org/en/download) installed and available in the system's PATH

## Installation

1. Install [uv](https://docs.astral.sh/uv/)

2. Clone the repository:
   ```bash
   git clone <repository-url>
   cd gen-chords
   ```

3. Install the required Python dependencies using [uv](https://docs.astral.sh/uv/):
   ```bash
   uv sync
   ```

4. Ensure [MuseScore](https://musescore.org/en/download) is installed and accessible via the `mscore` command.

## Usage

### Generating chord images

Run the `gen_chord_images` program with the following arguments:

```bash
uv run gen_chord_images.py --clef <clef> --root_range <root1,root2> --folder_path <output_folder>
```

#### Arguments

- `--clef`: The clef type to use for the generated chords. Choices: `G`, `F`.
- `--root_range`: The range of root notes to generate chords for, in the format `root1,root2` (e.g., `E2,E3`).
- `--folder_path`: The path to the folder where the generated images will be saved. Each chord type will be saved in a separate subfolder.

#### Example

To generate chords in the F clef for root notes ranging from `E2` to `E3` and save them in the `assets` folder:

```bash
uv run gen_chord_images.py --clef F --root_range E2,E3 --folder_path assets
```

### Creating an Anki package

Run the `gen_anki_pkg` program with the following arguments:

```bash
uv run gen_anki_pkg.py --folder_path <input_folder> --pkg_path <output_file>
```

#### Arguments

- `--folder_path`: The path to the folder containing the generated chord images. The same folder that `gen_chord_images` created.
- `--pkg_path`: The path to the output [Anki](https://apps.ankiweb.net/) package file (e.g., `output.apkg`).

#### Example

To create an [Anki](https://apps.ankiweb.net/) package from the chord images in the `assets` folder and save it as `assets/chord_images.apkg`:

```bash
uv run gen_anki_pkg.py --folder_path assets --pkg_path assets/chord_images.apkg
```

## How It Works

1. **Chord Generation**: The program calculates all possible root notes within the specified range and generates chords by stacking intervals on top of each root.
2. **MusicXML Creation**: For each chord, a MusicXML representation is created.
3. **Image Rendering**: The MusicXML is passed to [MuseScore](https://musescore.org/en/download) to generate a PNG image of the chord.
4. **Anki Package Creation**: The program takes the folder of generated chord images, organizes them into [Anki](https://apps.ankiweb.net/) notes, and creates an [Anki](https://apps.ankiweb.net/) package (`.apkg`) file. Each note contains a chord image and its corresponding name.

## Supported Chord Types

The program currently supports the following chord types:

- **Major Seventh**: Root, Major Third, Perfect Fifth, Major Seventh
- **Dominant Seventh**: Root, Major Third, Perfect Fifth, Minor Seventh
- **Minor Seventh**: Root, Minor Third, Perfect Fifth, Minor Seventh

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the program.
