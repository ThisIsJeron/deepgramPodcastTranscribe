# Deepgram Podcast Transcribe

## Overview

This project takes output from Deepgram API, then processes a transcript text file, combining consecutive lines spoken by the same speaker into a single line of text. The result is saved in a new file with a consolidated view of the transcript, where each speaker’s contributions are aggregated together.

## Requirements

- Python 3.x

## Installation

1. **Clone the Repository (Optional):**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment (Optional but Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **No additional dependencies are required for this script.**

## Usage

1. **Prepare `transcript.txt`:**
   - Ensure `transcript.txt` is in the same directory as `combine_transcripts.py`.
   - The file should contain text in the format:
     ```
     [Speaker:0] <text>
     [Speaker:1] <text>
     ```

2. **Run the Script:**
   ```bash
   python combine_transcripts.py
   ```

3. **Check `output.txt`:**
   - After running the script, `output.txt` will be created or overwritten with the combined transcript.

## Example

Given `transcript.txt`:

```
[Speaker:0] to talk to you
[Speaker:0] for a long time. So I'm really looking forward to it. You said something that caught me right away when we were discussing
[Speaker:0] various issues just before we started. You said you're were up till four in the morning. Yeah. So actually, little... More like five in the morning, but Okay we got
[Speaker:1] the
[Speaker:1] the X ai data center,
[Speaker:1] or supercomputer center
[Speaker:1] training
[Speaker:1] from
```

The output in `output.txt` will be:

```
[Speaker:0] to talk to you for a long time. So I'm really looking forward to it. You said something that caught me right away when we were discussing various issues just before we started. You said you're were up till four in the morning. Yeah. So actually, little... More like five in the morning, but Okay we got
[Speaker:1] the the X ai data center, or supercomputer center training from
```

## Troubleshooting

- **File Not Found:** Ensure `transcript.txt` is in the same directory as the script.
- **Permission Errors:** Check file permissions and ensure you have write access to the directory.
