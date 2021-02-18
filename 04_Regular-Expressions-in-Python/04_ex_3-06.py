# Exercise 3-06: Everything clean

import pandas as pd

sentiment_analysis_dict = {'545': "Boredd. Colddd @blueKnight39 Internet keeps stuffing up. Save me! https://www.tellyourstory.com",
                           '546': "I had a horrible nightmare last night @anitaLopez98 @MyredHat31 which affected my sleep, now I'm really tired",
                           '547': "im lonely  keep me company @YourBestCompany! @foxRadio https://radio.foxnews.com 22 female, new york"}

sentiment_analysis = pd.Series(data=sentiment_analysis_dict, index=['545', '546', '547'])

# Import re module
import re

for tweet in sentiment_analysis:
    # Write regex to match http links and print out result
    # print(re.findall(r"https?\://\w+\.\w+\.\w+", tweet))
    print(re.findall(r"https?\://\S+", tweet))

    # Write regex to match user mentions and print out result
    print(re.findall(r"@\w+", tweet))
