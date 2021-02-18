# Exercise 3-10: Finding files

import pandas as pd
import re

sentiment_analysis_dict = {'780': "AIshadowhunters.txt aaaaand back to my literature review. At least i have a friendly cup of coffee to keep me company",
                           '781': "ouMYTAXES.txt I am worried that I won't get my $900 even though I paid tax last year"}

sentiment_analysis = pd.Series(data=sentiment_analysis_dict, index=['780', '781'])

# Write a regex to match text file name
regex = r"^[aAeEiIoOuU]{2,3}\w+\.txt"

for text in sentiment_analysis:
    # Find all matches of the regex
    print(re.findall(regex, text))

    # Replace all matches with empty string
    print(re.sub(regex, "", text))

