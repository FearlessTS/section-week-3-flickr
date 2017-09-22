import json

with open('sample_diction.json') as f:
    diction_string = f.read()

flickr_response = json.loads(diction_string)
photo_diction = flickr_response['photo']


class Photo:
    def __init__(self, photo):
        self.author = photo['owner']['username']

        self.tags = []
        for photo_tag in photo['tags']['tag']:
            self.tags.append(photo_tag['_content'])

        self.id = photo['id']
        self.title = photo['title']['_content']
        self.datetaken = photo['dates']['taken']
        self.url = photo['urls']['url'][0]['_content']

    def __str__(self):
        return '{0} by {1}'.format(self.title, self.author)

    def __repr__(self):
        return ('title: {0}' + '\n'
            + 'author: {1}' + '\n'
            + 'id: {2}' + '\n'
            + 'datetaken: {3}' + '\n'
            + 'tags: {4}' + '\n'
            + 'url: {5}').format(self.title, self.author, self.id, self.datetaken, self.tags, self.url)

    def __contains__(self, tag_name):
        return tag_name in self.tags


p = Photo(photo_diction)
print(p.tags)
print("__str__", str(p))
print("__repr__", repr(p))
print("tag \"nature\" contained? ", ('nature' in p))
print("tag \"morning\" contained? ", ('morning' in p))

