# ASCII Terminal Video Player

A lightweight CLI tool that captures video files or live camera feeds and renders them in real time as vectorized ASCII art inside your terminal.

## Features

* **High Performance**: Vectorized frame processing using NumPy to eliminate frame drops and lag.
* **Aspect Ratio Correction**: Automatically compensates for terminal character height ratios to prevent distortion.
* **Flexible Input**: Plays local video files (`.mp4`, `.mkv`, etc.) or streams directly from webcams.
* **Flicker-Free Rendering**: Uses ANSI escape sequences for smooth cursor repositions without clearing the buffer.

## Requirements
* OpenCV
* NumPy

> [!NOTE]
> I am using `uv` as Package Manager for this project

## Quick Start

```bash
# Clone the repository
git clone https://github.com/abhinavvv-hub/Ascii-Video-Art.git
cd Ascii-Video-Art

# Create and activate virtual environment
uv venv
source .venv/bin/activate

# Install dependencies
uv pip install -r requirements.txt
```
