# import re
# from urllib.parse import urlparse

# # info_url = r"https://jsoc1.stanford.edu/data/aia/synoptic/"
# # baseurl = info_url + r"%Y/%m/%d/H%H00/AIA%Y%m%d_%H%M_.....fits"
# # extractor = pattern = info_url + r"%Y/%m/%d/H%H00/AIA%Y%m%d_%H%M_{}.fits"

# # Assuming you have the necessary imports and setup
# extractor = r"https://jsoc1.stanford.edu/data/aia/synoptic/(\d{4})/(\d{2})/(\d{2})/H(\d{2})00/AIA(?P<year>\d{4})(?P<month>\d{2})(?P<day>\d{2})_(?P<hour>\d{2})(?P<minute>\d{2})_(?P<wavelength>\d{4})\.fits"
# print(extractor)
# # Example URL
# url = "https://jsoc1.stanford.edu/data/aia/synoptic/2023/10/11/H0300/AIA20231011_0300_1234.fits"

# # Parse the URL using regex
# matches = re.match(extractor, url)

# # Check if there's a match and extract named groups
# if matches:
#     exdict = matches.groupdict()  # This will give you a dictionary of named groups
#     print("Match found! Extracted values:", exdict)
# else:
#     print("No match found.")


import re

url = 'https://jsoc1.stanford.edu/data/aia/synoptic/2023/10/11/H0000/AIA20231011_0000_0094.fits'
regex = r'https://jsoc1.stanford.edu/data/aia/synoptic/\d{4}/\d{2}/\d{2}/H\d{2}00/AIA\d{8}_\d{4}_\d+\.fits'

if re.match(regex, url):
    print("Match!")
else:
    print("No match.")