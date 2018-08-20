# Whatanipy
### Whatanime.ga Python wrapper.

### Example
```py
In [1]: import whatanime
   ...: whatclass = whatanime.whatanime('API KEY')
   ...: import base64
   ...: with open('working!!.jpg', 'rb') as f:
   ...:    base = base64.standard_b64encode(f.read())
   ...: whatclass.search(base)
   ...: whatclass.simple()
Out[2]: 
{'status': 200,
 'native_title': 'Working!!',
 'english_title': 'Wagnaria!!',
 'synonyms': 'Working!!',
 'nsfw': False,
 'duration': (785.58, 785.58, 786.5),
 'episode': 13,
 'similarity': 0.96,
 'similarity_percent': '96.0%',
 'simple_string': 'Working!! - 13: [13:06s]',
 'thumbnail_url': 'https://whatanime.ga/thumbnail.php?anilist_id=6956&file=%5BKTXP%26SD%5D%5BWorking%21%21%5D%5B13%5D%5BGB%5D%5BAVC_AAC%5D%28EF85C6F6%29.mp4&t=785.58&token=EPfGknf5vCnfaPRH6iwTJw ',
 'preview_url': 'https://whatanime.ga/preview.php?anilist_id=6956&file=%5BKTXP%26SD%5D%5BWorking%21%21%5D%5B13%5D%5BGB%5D%5BAVC_AAC%5D%28EF85C6F6%29.mp4&t=785.58&token=EPfGknf5vCnfaPRH6iwTJw '}
In [1]: whatclass.me()
Out[3]: 
{'status': 200,
 'reason': '',
 'user_id': 1050,
 'email': 'Noyou!@raysmail.com',
 'quota': 10,
 'quota_ttl': 60}
```
