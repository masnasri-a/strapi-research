import feedparser

data = feedparser.parse('data.xml')
posts = []
 
for entry in data['entries']:
    print(entry['content'][0]['value'])

print(posts)