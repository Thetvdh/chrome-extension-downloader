import requests
import re
import hashlib

chrome_url_pattern = re.compile("https?:\/\/chrome.google.com\/webstore\/.+?\/([a-z]{32})(?=[\/#?]|$)")

chrome_new_url_pattern = re.compile("^https?:\/\/chromewebstore.google.com\/detail\/.+?\/([a-z]{32})(?=[\/#?]|$)")

version = "118.0.5993.117"  # Chrome version
nacl_arch = "x86-64"  # System architecture
# Example URL
# https://chrome.google.com/webstore/detail/high-contrast/djcfdncoelnlbldjfhinnjlhdjlikmph
extension_url = input("Enter URL: ")
result = chrome_url_pattern.search(extension_url)

if not result:
    result = chrome_new_url_pattern.search(extension_url)

file_name = f'{extension_url.split("/")[5]}.crx'


url = f"https://clients2.google.com/service/update2/crx?response=redirect&prodversion={version}&acceptformat=crx2,crx3&x=id%3D{result[1]}%26uc&nacl_arch={nacl_arch}"

with open(f"{file_name}", "wb") as file:
    file.write(requests.get(url).content)
    print(f"Extension written to {file_name}")

with open(file_name, "rb") as file:
    print("Extension hash:", end=" ")
    print(hashlib.sha256(file.read()).hexdigest())
