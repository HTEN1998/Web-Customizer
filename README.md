# Web-Customizer

*This project is based on natural language processing werer use can customize  the given website by writing his needs in natural language.*
---

## Steps to use:
1. This project requires python and nltk library. So make sure you have both things are installed in your system.
2. Open the webpage 'index.html' in browser located in 'html_pages Folder'.
3. Exceute 'lang_processor.py' file and enter the changes you want to make in webpage 'index.html' and Run file in python IDLE.

---
## Working of web-cutomizer
- 'indexpage_writer.py' is file which write whole html codes. Their are few global variables who's values are taken from user's processed input sentences (which is in natural language) .
- 'lang_processor.py' is file which dose natural language processing by keyword extraction method. It sets values of global variables of 'indexpage_writer.py' after extracting keywords, and allow 'indexpage_writer.py' to write html file.

### Natural language Processing Algorithim

1. Remove stopwords from input sentences using nltk library.
2. Tokenize the sentence after filteration of stopwords from it and pass it to Stage 1 of natuaral language processing algorithim.
2. Stage 1 (tuple generator): This stage analysis each token and make  sets of 3 keywords. For this it uses 'corpus.json' from where algorithim comes to know which keyword belong to which category.

|1st keywords|2nd keyword|3rd keyword|
|----------|-----------|----------|
|indicate elements|indicate attributes|indicate values|
|website|title|Amazon|
|navigation bar|font color|Red|
|footer|text align|Left|

4. Stage 2 (tuple merger): After 1st gets finish their make some missing fields in each tuple/set of keywords. This stage files those blank/missing elements or attributes.
5. Stage 3 (tuple processor): This stage reads each set of keywords and make a meaning out of it and call appropriate variable form 'indexpage_writer.py' and sets its value.
'set = [navigation bar,fontcolor,Red] ====> variable navbar_font_color = "Red" '