# Bible-it-Server
This is a search engine built using the the python flask framwork.  I allows for word searches, and question searches on the entire Holy Bible
content.

## Live URL
[Bibleit.co](https://www.bibleit.co/)

## Features
- Contains RESTful endpoints to return complete JSON for the NIV bible. 
- Searches for any word exact or inexact matches throughout the entire Holy Bible.
- Presents search results for matches in separate categories for exact and inexact.
-  Displays word definitions of matches and links to synomym words found in the bible.
-  Shows suggested questions for user's search bar input.

## Implementation
- Python 3.7.
- Built using Flask framework
- Client uses Bootstrap 4.0
- Uses FuzzyWuzzy library for string matching.
- SQLAlchemy ORM
- Uses NLP Spacy to retrieve text Part of Speech.
- Calls Meriam Webster's API to get definitions and Synonyms.


## WORD SEARCHES 
- Searches for any word exact or inexact matches throughout the entire Holy Bible.
- Presents search results for matches in separate categories for exact and inexact.

![image](https://user-images.githubusercontent.com/20021751/75855809-ecae7800-5da7-11ea-9f99-8c024c8b70b3.png)


## DICTIONARY

- Displays word definitions of matches and links to synomym words found in the bible.

![image](https://user-images.githubusercontent.com/20021751/75856079-765e4580-5da8-11ea-8e84-7f74f5b8b6e7.png)

## QUESTION SUGGESTIONS

-  Shows suggested questions for user's search bar input.

![image](https://user-images.githubusercontent.com/20021751/75856234-c806d000-5da8-11ea-87eb-55c172118fb1.png)


