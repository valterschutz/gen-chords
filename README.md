# gen-chords

`gen-chords` is a Python program that generates PNG images of musical chords based on specified parameters such as clef type, root note range, and chord intervals. The program uses the [pymusictheory](https://github.com/valterschutz/pymusictheory) library to handle musical theory concepts and MuseScore to render the chords into images.

## Motivation

Page 18 of Jeremy Siskind's [Jazz Piano Fundamentals (Book 1)](https://jeremysiskind.com/product/jazz-piano-fundamentals-book-1/) instructs the reader to generate flashcards for all major, minor, and dominant seventh chords in the F clef. This program allows you to generate those images with a single command. To create flashcards from the images, use a flashcard program like [Anki](https://apps.ankiweb.net/).

If you don't care about generating your own chord images, you can simply download the `assets` folder, which contains all seventh chords in the range E2–E3 on the F clef.


## Features

- Generate seventh chords (major, minor, dominant) in different clefs (e.g., G clef, F clef).
- Specify a range of root notes to generate chords for.
- Outputs PNG images of the generated chords, organized into subfolders by chord type.

## Requirements

- Python 3.13 or higher
- MuseScore installed and available in the system's PATH

## Installation

1. Install [uv](https://docs.astral.sh/uv/)

2. Clone the repository:
   ```bash
   git clone <repository-url>
   cd gen-chords
   ```

3. Install the required Python dependencies using `uv`:
   ```bash
   uv sync
   ```

4. Ensure [MuseScore](https://musescore.org/en/download) is installed and accessible via the `mscore` command.

## Usage

Run the program with the following arguments:

```bash
uv run main.py --clef <clef> --root_range <root1,root2> --folder_path <output_folder>
```

### Arguments

- `--clef`: The clef type to use for the generated chords. Choices: `G`, `F`.
- `--root_range`: The range of root notes to generate chords for, in the format `root1,root2` (e.g., `E2,E3`).
- `--folder_path`: The path to the folder where the generated images will be saved. Each chord type will be saved in a separate subfolder.

### Example

To generate chords in the G clef for root notes ranging from `C4` to `C5` and save them in the `output` folder:

```bash
uv run main.py --clef G --root_range C4,C5 --folder_path output
```

## How It Works

1. **Chord Generation**: The program calculates all possible root notes within the specified range and generates chords by stacking intervals on top of each root.
2. **MusicXML Creation**: For each chord, a MusicXML representation is created.
3. **Image Rendering**: The MusicXML is passed to MuseScore to generate a PNG image of the chord.

## Supported Chord Types

The program currently supports the following chord types:

- **Major Seventh**: Root, Major Third, Perfect Fifth, Major Seventh
- **Dominant Seventh**: Root, Major Third, Perfect Fifth, Minor Seventh
- **Minor Seventh**: Root, Minor Third, Perfect Fifth, Minor Seventh

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the program.
