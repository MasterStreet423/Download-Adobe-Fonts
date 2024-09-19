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

Install the required dependencies using pip:
```bash
pip install -r requirements.txt
```
Install Playwright and set up the browser environment:
```bash
playwright install
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
python adobe_font_scraper.py
```
Input either the direct URL of the Adobe Fonts page or the font name.

The script will scrape and download all font variations (weights, styles) for that font family.

The downloaded fonts will be saved in the fonts/ directory with proper subfolders for each font.

## Example
### Input:
```bash
Escriba la URL o el nombre de la fuente de Adobe: proxima nova
```
### Output:
```make
Descargando: Proxima Nova Regular
Descargando: Proxima Nova Bold
Descargando: Proxima Nova Light
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
├── adobe_font_scraper.py       # Main script
├── requirements.txt            # Python package dependencies
└── fonts/                      # Directory where downloaded fonts will be stored
```
## Requirements
- Python 3.7+
- Playwright: Used to automate browser interaction.
- FontTools: Used for manipulating fonts.
- Requests: For making HTTP requests to download fonts.

Install the requirements with:

```bash
pip install -r requirements.txt
```

## Important Notes

- **Adobe Fonts URL Format**: Ensure that the URL provided is a valid Adobe Fonts URL. If a font name is used, ensure it is accurate as it is converted into a URL format to match Adobe Fonts conventions.

- **Font Modification**: The script modifies the font name metadata fields (Full Name, Family Name, PostScript Name) before saving the .otf files.

- **Fonts Limit**: If the font family has multiple variations, the script will attempt to download all available variations.

## Contributions
Feel free to fork this repository and make pull requests if you'd like to contribute improvements or fixes. If you encounter any issues, please open an issue on the GitHub repository.
