import fontTools.ttLib
from playwright.sync_api import sync_playwright, Playwright,Route,Request
import fontTools
import re
import requests
import io
import os

IMAGE_404 = "https://afwebcdn.fonts.adobe.com/assets/svg/errors/404-28b2a4bef055b0727a82efb73e4c784ecc12b0c5e15652d318e256a3af1459a1.svg"

input_url_font = input("Escriba la URL o el nombre de la fuente de Adobe: ")
if "fonts.adobe.com" in input_url_font:
    URL_FONT = input_url_font
    if not input_url_font.startswith("https://"):
        URL_FONT = "https://" + input_url_font
else:
    URL_FONT = f"https://fonts.adobe.com/fonts/{input_url_font.lower().replace(' ','-')}"

pattern = re.compile(r".*m\?unicode.*")
fonts = []
font_names = []
fully_name = ""
font_count = 0
def process_font(route:Route, request:Request):
    global fonts
    if pattern.match(request.url):
        fonts.append(request.url)
    route.continue_()
    
def run(playwright: Playwright):
    global font_count, font_names
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.route("*/**", process_font)
    page.goto(URL_FONT, wait_until="load")
    # if not found
    if page.query_selector("img[src='https://afwebcdn.fonts.adobe.com/assets/svg/errors/404-28b2a4bef055b0727a82efb73e4c784ecc12b0c5e15652d318e256a3af1459a1.svg']"):
        print("Font not found")
        return

    list_fonts = page.query_selector_all('#fonts-section > div > ul > li .font-variation-card__variation-name')
    try:
        font_names = [x.inner_text() for x in list_fonts]
    except:
        print("Error getting font names")
    
    count_element = page.query_selector("#fonts-section > div > div > div.adobe-fonts-family__availability-summary > span")
    text = count_element.inner_text()
    font_count = int(text.split(" ")[0])
    page.close()
    
def download_font(url:str):
    global fonts, font_names, font_count
    # Identificadores de los campos de nombre
    ID_FULL_NAME = 4  # Nombre completo de la fuente
    ID_FAMILY_NAME = 1  # Nombre de la familia de la fuente
    ID_POSTSCRIPT_NAME = 6  # Nombre PostScript de la fuente
    name = get_name()
    for x in range(font_count):
        url = fonts[x]
        nuevo_nombre = font_names[x]
        print("Descargando: ", nuevo_nombre)
        r = requests.get(url)
        # font in otf
        font = fontTools.ttLib.TTFont(io.BytesIO(r.content))

        # Cambiar el nombre en la tabla 'name'
        for record in font['name'].names:
            if record.nameID in [ID_FULL_NAME, ID_FAMILY_NAME, ID_POSTSCRIPT_NAME]:
                record.string = nuevo_nombre.encode('utf-16-be')
        # save as otf
        os.makedirs("fonts", exist_ok=True)
        os.makedirs(f"fonts/{name}", exist_ok=True)
        font.save(f"fonts/{name}/{nuevo_nombre}.otf")
        
def get_name():
    global URL_FONT
    name = URL_FONT.split("/")[-1]
    return name.replace("-"," ").title()
with sync_playwright() as p:
    run(p)
    download_font(fonts)