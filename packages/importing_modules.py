# import packages.my_functions.os_functions as f
# print(f.work_dir)
# print(f.return_new_vegas())

# PIP -> PIP Installs Packages (Auto-acronym)

import requests

r = requests.get("https://www.bbc.co.uk")
print(r, type(r))

print(r.status_code)
# print(r.content)
