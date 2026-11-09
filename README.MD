# Adobe Fonts Scraper
This project allows users to download fonts from Adobe Fonts by providing either a direct Adobe Fonts URL or a font name. The tool scrapes the Adobe Fonts page, collects the font URLs, renames the fonts based on the names listed on the page, and downloads them in .otf format.

## Table of Contents
- [Installation](#installation)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Requirements](#requirements)
- [Important Notes](#important-notes)
- [Contributions](#contributions)

## Installation
Clone the repository or download the script files:
```bash
git clone https://github.com/masterstreet423/adobe-font-scraper.git
```

This project is managed with [uv](https://docs.astral.sh/uv/). Install the dependencies with:
```bash
uv sync
```
Install the Playwright browser:
```bash
uv run playwright install chromium
```
## How It Works
### The script operates by:

Taking user input for either an Adobe Fonts URL or the name of the font.
Navigating to the Adobe Fonts page.
Scraping the font URLs and font names from the page.
Downloading the fonts in .otf format.
Modifying font metadata to match the font names listed on Adobe Fonts.
Storing the fonts locally in a fonts/ directory.

## Usage
Run the script:
```bash
uv run adobe_font_scrapper.py
```
Input either the direct URL of the Adobe Fonts page or the font name.

The script will scrape and download all font variations (weights, styles) for that font family.

The downloaded fonts will be saved in the fonts/ directory with proper subfolders for each font.

## Example
### Input:
```bash
Enter the URL or name of the Adobe font: proxima nova
```
### Output:
```make
Downloading:  Proxima Nova Regular
Downloading:  Proxima Nova Bold
Downloading:  Proxima Nova Light
...
```
The fonts are stored in the following structure:

```
fonts/
├── Proxima Nova
│   ├── Proxima Nova Regular.otf
│   ├── Proxima Nova Bold.otf
│   └── Proxima Nova Light.otf
```
## File Structure
```
adobe_font_scraper/
├── adobe_font_scrapper.py      # Main script
├── pyproject.toml              # Project metadata and dependencies (used by uv)
└── fonts/                      # Directory where downloaded fonts will be stored
```
## Requirements
- [uv](https://docs.astral.sh/uv/) to manage the project and Python
- Python 3.14+
- Playwright: Used to automate browser interaction.
- FontTools: Used for manipulating fonts.
- Requests: For making HTTP requests to download fonts.

`uv sync` installs all of these from `pyproject.toml`.

## Important Notes

- **Adobe Fonts URL Format**: Ensure that the URL provided is a valid Adobe Fonts URL. If a font name is used, ensure it is accurate as it is converted into a URL format to match Adobe Fonts conventions.

- **Font Modification**: The script modifies the font name metadata fields (Full Name, Family Name, PostScript Name) before saving the .otf files.

- **Fonts Limit**: If the font family has multiple variations, the script will attempt to download all available variations.

## Contributions
Feel free to fork this repository and make pull requests if you'd like to contribute improvements or fixes. If you encounter any issues, please open an issue on the GitHub repository.
