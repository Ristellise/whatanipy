import requests
import human_time_formatter.human_time_formatter as humanise
import urllib.parse

class WhatAnime:
    def __init__(self, key):
        """
        Whatanime initialisation.
        :param key: your Whatanime.ga key
        """
        self.key = key
        self.data = None
        self.request = None

    def me(self):
        """
        Get's your Quota, Email and user_id.
        user_id, email, quota and quota_ttl will not be present if status code is not 200!
        :return:
            {'status': 200,
             'reason': '',
             'user_id': 1050,
             'email': 'yourmail@whatamail.wat',
             'quota': 10,
             'quota_ttl': 60}
        """
        request = requests.request("GET", f'https://whatanime.ga/api/me?token={self.key}')
        if request.status_code != 200:
            return {'status': request.status_code, 'reason': request.text}
        else:
            return {'status': 200, 'reason': "", **request.json()}

    def thumbnail_url(self, item=None, index=0):
        if item is None:
            item = self.data['docs'][index]
        return f"https://whatanime.ga/thumbnail.php{self.previewnail_params(item)}"

    @staticmethod
    def previewnail_params(item):
        return f"?anilist_id={item['anilist_id']}" \
               f"&file={urllib.parse.quote_plus(item['filename'])}" \
               f"&t={item['at']}" \
               f"&token={item['tokenthumb']} "

    def preview_url(self, item=None, index=0):
        if item is None:
            item = self.data['docs'][index]
        return f"https://whatanime.ga/preview.php{self.previewnail_params(item)}"

    @staticmethod
    def _mal_string(mal):
        return f"https://myanimelist.net/anime/{mal}/"

    def search(self, bb64, anilist_filter=None):
        data = {'image': bb64}
        if anilist_filter is not None:
            data['filter'] = anilist_filter
        self.request = requests.request("POST", f'https://whatanime.ga/api/search?token={self.key}',
                                        data=data)

        is_empty = True if self.request.json().get('docs', []) == [] else False
        if not is_empty:
            self.data = self.request.json()
            return {'status': 200, 'reason': ''}

        else:
            return {'status': self.request.status_code, 'reason': self.request.text}

    def simple(self, docs_index=0):
        """
            Simple Dict.
            :param docs_index: Index of the searched images.
            :return:
        """
        if docs_index > len(self.data['docs']):
            return {
                'status': 400,
                'reason': "docs_index out of range of total docs received."
            }
        item = self.data['docs'][docs_index]
        if self.data:
            return {
                'status': 200,
                'native_title': item['title_native'],
                'english_title': item['title_english'],
                'synonyms': item['title_native'],
                'nsfw': item['is_adult'],
                'duration': (item['from'], item['at'], item['to']),
                'episode': item['episode'],
                'similarity': item['similarity'],
                'similarity_percent': f"{item['similarity']*100}%",
                'simple_string': f"{item['title_native']} - {item['episode']}: "
                                 f"[{humanise.format_seconds(item['at'])}]",
                'thumbnail_url': self.thumbnail_url(item),
                'preview_url': self.preview_url(item)
            }
        else:
            return {
                'status': 404,
                'reason': "Not found"
            }

    def raw(self, docs_index=0):
        if docs_index > len(self.data['docs']):
            return {
                'status': 400,
                'reason': "docs_index out of range of total docs received."
            }
        return self.data['docs'][docs_index]
