# Youtube Comments Extractor

This is a simple script to extract all the comments and replies from Youtube video.

Clone the repository or download it.
```bash
git clone https://github.com/eduardoseity/youtube-comments-extractor.git
```

Install requirements.
```bash
pip install -r requirements.txt
```

Run `./src/YoutubeCommentsExtractor.py` with arguments.

First argument: video URL in **double quotes**<br>
Second argument: output file (csv format)

```bash
python ./src/YoutubeCommentsExtractor.py "https://www.youtube.com/watch?v=3G_oOVjqA8k" extracted_comments.csv
```

A file named `extracted_comments.csv` will be created with the fields below:
* commentId: The identification of the comment
* author: The author of the comment
* text: The text of the comment
* reply: True if the comment is a reply
---
<small>https://www.linkedin.com/in/eduardo-seity-iseri-15908224</small>
