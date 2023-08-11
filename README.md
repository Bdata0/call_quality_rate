# Call Quality Rate

Performing Call Quality Rate (CQR) evaluation on customer call transcripts.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Description

This project aims to evaluate the Call Quality Rate (CQR) of customer call transcripts based on emotional responsiveness, effectiveness of problem-solving, professionalism, and awareness.

## Features

- Transcribe audio recordings into text using the Vosk model.
- Perform diarization to distinguish speakers using pyannote.audio.
- Analyze sentiment of text using the SentenceTransformer model.
- Export results to Google Sheets using the Google Sheets API.
- Visualize results using a Streamlit web app.

## Getting Started

### Prerequisites

- Docker: Install [Docker](https://www.docker.com/get-started) for containerization.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Bdata0/call_quality_rate.git
   cd call_quality_rate
   ```

2. Build the Docker container:

    ```bash
    docker build -t call_quality_rate .
    ```

### Usage

1. Place your audio file (in MP3 format) in the root directory.

2. Run the Docker container:

    ```bash
    docker run -it -v $(pwd):/app call_quality_rate
    ```

3. Follow the instructions in the terminal to analyze the call transcript and view the results using the Streamlit web app.

### Project Structure

The project follows a structured organization based on Domain-Driven Design (DDD) principles.

```css
# project/
├── app.py
├── domain/
│   ├── __init__.py
│   ├── transcription/
│   │   ├── __init__.py
│   │   ├── models/
│   │   │   ├── vosk-model-ru-0.42.zip
│   │   │   └── ...
│   │   ├── transcription.py
│   │   └── ...
│   ├── diarization/
│   │   ├── __init__.py
│   │   ├── diarization.py
│   │   └── ...
│   ├── sentiment_analysis/
│   │   ├── __init__.py
│   │   ├── sentiment_analysis.py
│   │   └── ...
│   ├── google_sheets/
│   │   ├── __init__.py
│   │   ├── google_sheets.py
│   │   └── ...
├── tests/
│   ├── __init__.py
│   ├── test_transcription.py
│   ├── test_diarization.py
│   ├── test_sentiment_analysis.py
│   ├── test_google_sheets.py
│   └── ...
├── Dockerfile
├── requirements.txt
└── ...
```

### Contributing

Contributions are welcome! Please follow these guidelines when contributing:
    *Fork the repository.
    *Create a new branch for your feature or bug fix.
    *Make your changes and commit with descriptive messages.
    *Submit a pull request.

### License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Bdata0/call_quality_rate/blob/main/LICENSE) file.
