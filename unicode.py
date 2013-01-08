from lxml import etree
import urllib2
import codecs
import StringIO
from mako.template import Template

doc = urllib2.urlopen('http://news.ycombinator.com/')
print doc.info()
s = doc.read()
unicode_string = s.decode('utf-8')

e = etree.fromstring(unicode_string, etree.HTMLParser())

output_file = codecs.open('res.html', 'w', 'utf-8')
html_string_io = StringIO.StringIO()

myTemplate = Template(filename='template.html')

urls = []
entries = []

def process_subtexttr(tr_tag):
  strings = []
  entry = dict()
  for i in tr_tag.itertext():
    strings.append(i.decode('utf-8'))
  if len(strings) == 5:
    entry['timestamp'] = strings[-2].strip(' |')
  else:
    entry['timestamp'] = strings[-1].strip()
  anchors = tr_tag.xpath('td/a')
  if len(anchors) == 2:
    entry['comments_count'] = anchors[-1].text.decode('utf-8')
    entry['comments_url'] = anchors[-1].get('href').decode('utf-8')
  return entry


for i in e.xpath('//td/a'):
  if len(i.getparent().keys()) == 1 and i.getparent().values()[0] == 'title':
    if isinstance(i.text, str):
      u_s = i.text.decode('utf-8')
    else:
      u_s = i.text
    if u_s == u'More':
      continue

    entry = dict()
    entry['site'] = u''
    entry['comments_url'] = u''
    entry['comments_count'] = u''

    urls.append(u_s)
    
    entry['story_link'] = u_s
    entry['story_url'] = i.get('href').decode('utf-8')

    span_tag = i.getnext() #may be None if 'Ask HN'
    if not span_tag is None:
      entry['site'] = span_tag.text.decode('utf-8').strip()
    
      
     

    tr_subtext = i.getparent().getparent().getnext()
    if not tr_subtext is None:
      d = process_subtexttr(tr_subtext)
      entry['timestamp'] = d['timestamp']
      if 'comments_url' in d:
        entry['comments_url']  = d['comments_url']     
      if 'comments_count' in d:
        entry['comments_count']  = d['comments_count']
      
    
    #print entry
    entries.append(entry)

    html_string_io.write(u_s)
    html_string_io.write(str('<br/>').decode('utf-8')) 


render = myTemplate.render_unicode(rows=entries)
 
#output_file.write( html_string_io.getvalue() )
output_file.write( render )

html_string_io.close()

output_file.close()



