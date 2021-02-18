# Exercise 4-09: Close the tag, please!

import re

html_tags = ['<body>Welcome to our course! It would be an awesome experience</body>',
             '<article>To be a data scientist, you need to have knowledge in statistics and mathematics</article>',
             '<nav>About me Links Contact me!']

for string in html_tags:
    # Complete the regex and find if it matches a closed HTML tags
    match_tag = re.match(r"<(.+?)>.*?</\1>", string)

    if match_tag:
        # If it matches print the first group capture
        print("Your tag {} is closed".format(match_tag.group(1)))
    else:
        # If it doesn't match capture only the tag
        notmatch_tag = re.match(r"<(.+?)>", string)
        # Print the first group capture
        print("Close your {} tag!".format(notmatch_tag.group(1)))
