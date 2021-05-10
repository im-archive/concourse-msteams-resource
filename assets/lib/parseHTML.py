import html
import html2markdown
import re

class parseHTML:
  @classmethod
  def decode(cls, data: str):
    return html.unescape(data)

  @classmethod
  def asMarkdown(cls, html: str, ignoreIncompatibleTags: bool = True):
    res = html2markdown.convert(html)
    if ignoreIncompatibleTags == True:
      rx = '\<\/?[\s\w\-\=\'\"]*\/?\>'
      res = re.sub(rx, '', res)
    return res
