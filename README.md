# pyVideo

`pyVideo` is a simple Python script that generates a video with a background image or solid color and an audio track created from text using Google Text-to-Speech (gTTS). This project demonstrates how to combine text-to-speech and video creation using Python libraries.

## Purpose

The purpose of this project is to provide a basic example of how to create a video with an audio track generated from text. It can be used as a starting point for more complex video creation projects or for educational purposes to learn about text-to-speech and video processing in Python.

## Requirements

- Python 3.x
- gTTS
- moviepy
- os

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/pyVideo.git
    cd pyVideo
    ```

2. Install the required Python packages:
    ```sh
    pip install gTTS moviepy
    ```

## Usage

1. Place an image named `background.jpg` in the same directory as the script. If no image is provided, a solid blue background will be used.

2. Run the script:
    ```sh
    python pyVideo.py
    ```

3. The script will generate an audio file `hello_world.mp3` from the provided text and create a video `hello_world.mp4` with the audio and background image or solid color.

## Customization

- To change the text that is converted to speech, modify the `text` variable in the script.
- To change the language of the text-to-speech, modify the `language` variable in the script.
- To use a different background image, replace `background.jpg` with your desired image file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.