# Spherical Phase Space

[![Demo video](https://vumbnail.com/1181644304.jpg)](https://vimeo.com/1181644304?fl=tl&fe=ec)

An interactive 3D visualisation system that maps the harmonic content of Schoenberg's Op. 19 _Sechs kleine Klavierstücke_ onto a sphere, using the Discrete Fourier Transform (DFT) of pitch-class sets. Chords are represented as points on the sphere's surface according to their phase-space coordinates, and K-means clustering identifies harmonic regions and movement patterns across the piece.

This project was developed as part of the master's thesis *"A Sintaxe Harmonica Atonal no Espaco de Fourier: Para Uma Representacao Esferica das Fases"* (Atonal Harmonic Syntax in the Fourier Space: Towards a Spherical Representation of Phases) at the [University of Porto](https://www.doi.org/10.34626/w4hp-0458), 2020.

> **Thesis author:** Samuel Pereira
> **Supervisor:** Gilberto Bernardes
> **Programme:** MSc in Multimedia — Interactive Music and Sound Design

## Overview

The system follows a three-stage pipeline:

1. **Harmonic analysis** — A MusicXML score is parsed into chroma vectors, and the DFT extracts magnitude and phase information for each chord (components 1–6, corresponding to the six interval classes).
2. **Clustering** — Phase coordinates from a chosen pair of DFT components are projected onto a sphere and clustered with K-means to identify harmonic regions.
3. **Interactive visualisation** — A Processing (Python mode) sketch renders the sphere in 3D, allowing the user to step through the chord progression with arrow keys while hearing each chord and observing real-time analytical overlays (cluster counters, transition paths, movement patterns).

## Repository structure

```
spherical-phase-space/
├── analysis/                       # Python 3 analysis scripts
│   ├── phaseSpace_main.py          # Entry point: XML → FFT → phases
│   ├── phaseSpace_utilities.py     # Core functions (parsing, FFT, plotting)
│   ├── kmeans.py                   # K-means clustering entry point
│   └── kmeans_utilities.py         # Clustering helper functions
│
├── scores/                         # MusicXML input scores
│   ├── skk_III.xml                 # Schoenberg Op. 19, Mvt. III
│   ├── skk_V.xml                   # Schoenberg Op. 19, Mvt. V
│   ├── cs_I.xml                    # Additional analysis score
│   ├── asd.xml                     # Additional analysis score
│   ├── qwe.xml                     # Additional analysis score
│   └── material.xml                # Compositional material
│
├── visualization/                  # Processing sketch (Python mode)
│   └── spherical_phase_space/
│       ├── spherical_phase_space.pyde  # Main sketch file
│       ├── draw_utilities.py           # 3D drawing functions
│       ├── sps_utilities.py            # Sphere maths & data I/O
│       ├── midi_utilities.py           # MIDI list parser
│       ├── sketch.properties           # Processing config
│       ├── data/                       # Audio samples (see below)
│       │   └── .gitkeep
│       ├── phases_skk_III_4_5.txt      # Pre-computed phase data
│       ├── phases_cs_4_5.txt
│       ├── phases_cs_2_5.txt
│       ├── cluster_center_III_movement.txt
│       ├── labels_III_movement.txt
│       └── midi_list_III_movement.txt
│
├── LICENSE                         # MIT (source code)
├── LICENSE-DATA                    # CC BY-NC 4.0 (scores & data)
├── CITATION.cff                    # Machine-readable citation metadata
├── requirements.txt                # Python dependencies
└── .gitignore
```

## Prerequisites

| Dependency | Version | Purpose |
|---|---|---|
| [Python](https://www.python.org/) | 3.7+ | Analysis scripts |
| [Processing](https://processing.org/) | 3.x with [Python mode](https://py.processing.org/) | 3D visualisation |
| [music21](https://web.mit.edu/music21/) | 6.x–7.x | MusicXML parsing |
| [SciPy](https://scipy.org/) | ≥ 1.4 | FFT computation |
| [NumPy](https://numpy.org/) | ≥ 1.18 | Numerical operations |
| [matplotlib](https://matplotlib.org/) | ≥ 3.1 | 2D phase-space plots |
| [scikit-learn](https://scikit-learn.org/) | ≥ 0.22 | K-means clustering |

The Processing sketch additionally requires the **Sound** and **PeasyCam** libraries (installable from Processing's Library Manager).

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/USERNAME/spherical-phase-space.git
cd spherical-phase-space
```

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure music21

The analysis scripts use music21's corpus mechanism to locate MusicXML files. Point it at the `scores/` directory:

```python
import music21
us = music21.environment.UserSettings()
us['localCorpusPath'] = '/absolute/path/to/spherical-phase-space/scores'
```

Alternatively, you can pass the full file path directly when calling the analysis functions.

### 4. Audio samples (for the visualisation)

The interactive visualisation plays back each chord using individual WAV samples mapped to MIDI note numbers 24–108. These files are not included in the repository due to their size (~190 MB).

To set up audio playback, place WAV files named `24.wav` through `108.wav` in `visualization/spherical_phase_space/data/`. Any General MIDI piano sample set covering that range will work. If you do not need audio playback, the visualisation will still run but the `SoundFile` calls will fail silently.

### 5. Install Processing libraries

Open Processing, go to **Sketch → Import Library → Add Library** and install:

- **Sound** (The Processing Foundation)
- **PeasyCam** (Jonathan Feinberg)

## Usage

### Running the harmonic analysis

```bash
cd analysis
python phaseSpace_main.py
```

Edit `phaseSpace_main.py` to change the score being analysed (the `sheet_music_reader()` call) and to uncomment the desired plotting functions. Output phase files can be exported by uncommenting `ps.phases_exporter(...)`.

### Running K-means clustering

```bash
cd analysis
python kmeans.py
```

Edit `kmeans.py` to change the input phase file and the number of clusters. Cluster centres and labels can be exported by uncommenting the exporter calls.

### Running the 3D visualisation

Open `visualization/spherical_phase_space/spherical_phase_space.pyde` in Processing (with Python mode enabled). Ensure the required `.txt` data files are present in the sketch folder, then press **Run**.

**Controls:**

| Key | Action |
|---|---|
| `↑` (Up arrow) | Advance to the next chord |
| `↓` (Down arrow) | Go back to the previous chord |
| Mouse click | Replay the current chord |
| Mouse drag | Rotate the 3D view (PeasyCam) |
| Scroll wheel | Zoom in/out |

**HUD overlays** (displayed during playback):

- **Software name & phase-space label** — top-left
- **Path representation** — triangle diagram showing inter-cluster transition frequency
- **Cluster counter** — top-right, counts chords per cluster
- **Cluster sequence** — recent sequence of cluster transitions (without consecutive repetitions)
- **Movement patterns** — most frequent three-cluster transition patterns

## How it works

1. A MusicXML score is parsed into a sequence of chords, each reduced to a 12-dimensional chroma vector (binary pitch-class set).
2. The DFT of each chroma vector yields six complex coefficients (components 1–6), normalised by the DC component (component 0). Each coefficient's **phase** encodes the "centre of gravity" of the pitch-class set with respect to one of the six interval classes.
3. A pair of phase components (e.g. φ₄, φ₅) is selected and mapped to spherical coordinates (longitude, latitude), placing each chord as a point on the surface of a sphere.
4. K-means clustering groups these points into harmonic regions. The cluster centres, labels, and MIDI note lists are saved as text files.
5. The Processing sketch reads these files, renders the sphere, and lets the user step through the piece interactively while observing the analytical overlays.

This approach builds on the DFT-based pitch-class set analysis formalised by Yust (2015) and extends it into a three-dimensional spherical representation.

## Citation

If you use this software or data in your research, please cite the associated thesis:

> Pereira, S. (2020). *A Sintaxe Harmonica Atonal no Espaco de Fourier: Para Uma Representacao Esferica das Fases*. Master's thesis. University of Porto. https://www.doi.org/10.34626/w4hp-0458.

A machine-readable citation file is provided in [`CITATION.cff`](CITATION.cff).

## Licence

- **Source code** is released under the [MIT License](LICENSE).
- **Scores, data files, and non-code assets** are released under [CC BY-NC 4.0](LICENSE-DATA).

## Acknowledgements

This work was carried out at the University of Porto under the supervision of Gilberto Bernardes, within the MSc in Multimedia programme (Interactive Music and Sound Design specialisation).
