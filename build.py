#!/usr/bin/env python3
"""Build isene.org: Markdown posts and pages to plain HTML in _site/.

    python3 build.py

Posts live in _posts/YYYY-MM-DD-Title.md and keep Jekyll's addresses,
/YYYY/MM/Title.html. Pages are the *.md files at the top with a
permalink. template.html is the frame around every page. Everything
else that is not excluded below is copied as it is.
"""
import datetime
import html
import os
import pathlib
import re
import shutil
import sys
from email.utils import format_datetime

import yaml
from markdown_it import MarkdownIt
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name
from pygments.util import ClassNotFound

TITLE = "Geir's Everything"
DESCRIPTION = "Philosophy - Sciences - Geekery - Art - Life - Coaching - Fun < Simplify Everything"
URL = "https://isene.org"
COPYRIGHT = "Geir Isene"
# On the front page, years before this one start folded; a click on the year opens it.
FOLD_BEFORE = 2025

ROOT = pathlib.Path(__file__).resolve().parent
OUT = ROOT / "_site"
TEMPLATE = (ROOT / "template.html").read_text()
# Not copied to the site: sources, tooling, and old files nothing links to.
SKIP = {"build.py", "template.html", "README.md", "LICENSE", "lib", "stats"}

YOUTUBE = ('<div class="youtube-wrapper">\n  <iframe src="https://www.youtube.com/embed/{}" '
           'allowfullscreen></iframe>\n</div>')
GISCUS = """<a id="comments"></a>
<script src="https://giscus.app/client.js"
        data-repo="isene/isene.github.io"
        data-repo-id="MDEwOlJlcG9zaXRvcnkxNDM2NjUwNjU="
        data-category="General"
        data-category-id="DIC_kwDOCJAnqc4C5Y-d"
        data-mapping="pathname"
        data-strict="0"
        data-reactions-enabled="1"
        data-emit-metadata="0"
        data-input-position="top"
        data-theme="preferred_color_scheme"
        data-lang="en"
        crossorigin="anonymous"
        async>
</script>"""


def code_block(code, lang, attrs):
    """Code the way Jekyll's Rouge wrote it, so the stylesheet still fits."""
    try:
        body = highlight(code, get_lexer_by_name(lang), HtmlFormatter(nowrap=True)) if lang else None
    except ClassNotFound:
        body = None
    body = body or html.escape(code)
    cls = f"language-{lang} highlighter-rouge" if lang else "highlighter-rouge"
    return f'<div class="{cls}"><div class="highlight"><pre class="highlight"><code>{body}</code></pre></div></div>\n'


# Kramdown reads Markdown inside inline tags such as <b> on a line of their
# own; CommonMark passes such a line through raw. Drop that one rule.
_blocks = sys.modules["markdown_it.rules_block.html_block"].HTML_SEQUENCES
_blocks.pop()
# Media tags stay raw blocks, as in Kramdown; wrapping them in <p> breaks players.
_blocks.append((re.compile(r"^</?(video|audio|source|picture|svg|canvas|object|embed)(?=[\s/>]|$)", re.I),
                re.compile(r"^$"), True))
MD = MarkdownIt("commonmark", {"html": True, "typographer": True})
MD.enable(["table", "strikethrough", "smartquotes"])
MD.add_render_rule("fence", lambda self, tokens, idx, options, env: code_block(
    tokens[idx].content, tokens[idx].info.strip().split(" ")[0], None))


def typography(state):
    """Kramdown's typography: dashes, ellipsis, and every straight quote curled."""
    for tok in state.tokens:
        if tok.type != "inline":
            continue
        prev = " "
        for ch in tok.children or []:
            if ch.type == "text":
                s = ch.content.replace("---", "\u2014").replace("--", "\u2013").replace("...", "\u2026")
                out = []
                for c in s:
                    if c in "\"'":
                        opening = prev.isspace() or prev in "([{\u2014\u2013-"
                        c = ("\u201c" if opening else "\u201d") if c == '"' else ("\u2018" if opening else "\u2019")
                    out.append(c)
                    prev = c
                ch.content = "".join(out)
            elif ch.type in ("softbreak", "hardbreak"):
                prev = " "
            elif ch.type == "code_inline":
                prev = ch.content[-1:] or prev


MD.core.ruler.push("typography", typography)


def read(path):
    """Front matter and body of a source file."""
    text = path.read_text(encoding="utf-8")
    if text.startswith("---"):
        _, fm, body = text.split("---", 2)
        return yaml.safe_load(fm) or {}, body
    return {}, text


def liquid(body, meta):
    """The few Jekyll tags the posts and pages use."""
    body = re.sub(r"{%\s*include youtube\.html id=['\"]([^'\"]+)['\"]\s*%}",
                  lambda m: "\n\n" + YOUTUBE.format(m.group(1)) + "\n\n", body)
    body = re.sub(r"{{\s*site\.url\s*}}", URL, body)
    body = re.sub(r"{{\s*\"([^\"]+)\"\s*\|\s*absolute_url\s*}}", lambda m: URL + m.group(1), body)

    def loop(m):
        var, key, inner = m.groups()
        return "\n".join(re.sub(r"{{\s*" + var + r"\.(\w+)\s*}}", lambda f: str(item.get(f.group(1), "")),
                                inner).strip() for item in meta.get(key) or [])
    body = re.sub(r"{%\s*for (\w+) in page\.(\w+)\s*%}(.*?){%\s*endfor\s*%}", loop, body, flags=re.S)
    if "{%" in body or "{{" in body:
        print("  left unconverted:", re.findall(r"{[{%].{0,40}", body)[:2])
    return body


def heading_id(text, used):
    """Heading ids as Kramdown made them, so old #links still work."""
    s = re.sub(r"^[^a-zA-Z]+", "", text)
    s = re.sub(r"[^a-zA-Z0-9 -]", "", s).replace(" ", "-").lower() or "section"
    if s in used:
        used[s] += 1
        return f"{s}-{used[s]}"
    used[s] = 0
    return s


_TAGS = r"center|div|p|table|figure|blockquote|h[1-6]|ul|ol|section|details|iframe|video|audio"
BLOCK_LINE = re.compile(r"^((?:<(" + _TAGS + r")\b[^\n]*)?</(" + _TAGS + r")>)[ \t]*\n(?=[^\n])", re.M | re.I)


def markdown(body, meta):
    # A block tag closed on its own line ends the block in Kramdown;
    # CommonMark needs a blank line after it.
    out = MD.render(BLOCK_LINE.sub(r"\1\n\n", liquid(body, meta)))
    used = {}

    def add_id(m):
        text = html.unescape(re.sub(r"<[^>]+>", "", m.group(3)))
        return f'<h{m.group(1)}{m.group(2)} id="{heading_id(text, used)}">{m.group(3)}</h{m.group(1)}>'
    return re.sub(r"<h([1-6])((?:(?!\bid=)[^>])*)>(.*?)</h\1>", add_id, out, flags=re.S)


def plain(html_text):
    return html.unescape(re.sub(r"<[^>]+>", "", html_text))


def esc(s):
    """Text between tags: only & < > need escaping."""
    return html.escape(str(s), quote=False)


def attr(s):
    return html.escape(str(s), quote=True)


class Post:
    def __init__(self, path):
        self.meta, body = read(path)
        m = re.match(r"(\d{4})-(\d{2})-(\d{2})-(.+)\.md$", path.name)
        self.date = datetime.datetime(int(m[1]), int(m[2]), int(m[3]), tzinfo=datetime.timezone.utc)
        self.slug = m[4]
        self.url = f"/{m[1]}/{m[2]}/{self.slug}.html"
        self.title = str(self.meta.get("title", self.slug))
        self.tags = [str(t) for t in self.meta.get("tags") or []]
        self.image = self.meta.get("image")
        self.html = markdown(body, self.meta)
        self.key = (self.date, path.name)


def date_long(d):
    return f"{d.day} {d:%B %Y}"


def tag_links(tags):
    return ", ".join(f'<a href="/tags/#{attr(t)}">{esc(t)}</a>' for t in tags)


def head(title, url, description=None, tags=None, image=None):
    parts = [f"<title>{esc(title) + ' &#8211; ' if title else ''}{esc(TITLE)}</title>",
             f'<meta name="description" content="{attr(description or DESCRIPTION)}">']
    if tags:
        parts.append(f'<meta name="keywords" content="{attr(", ".join(tags))}">')
    if image:
        parts += [f'<meta property="og:image" content="{URL}{attr(image)}">',
                  '<meta name="twitter:card" content="summary_large_image">',
                  f'<meta name="twitter:image" content="{URL}{attr(image)}">']
    parts += ['<meta property="og:locale" content="en_US">',
              '<meta property="og:type" content="article">',
              f'<meta property="og:title" content="{attr(title or TITLE)}">',
              f'<meta property="og:description" content="{attr(description or DESCRIPTION)}">',
              f'<meta property="og:url" content="{URL}{url}">',
              f'<meta property="og:site_name" content="{attr(TITLE)}">',
              f'<link rel="canonical" href="{URL}{url}">']
    return "\n".join(parts)


def page(url, main, title=None, **meta):
    out = TEMPLATE.replace("{{head}}", head(title, url, **meta)).replace("{{main}}", main)
    path = OUT / url.lstrip("/")
    if url.endswith("/"):
        path = path / "index.html"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(out, encoding="utf-8")


def post_page(p, older, newer, by_tag):
    words = len(plain(p.html).split())
    meta = f'<time datetime="{p.date.isoformat()}">{date_long(p.date)}</time>'
    if p.tags:
        meta += " &nbsp;·&nbsp; " + tag_links(p.tags)
    meta += f" &nbsp;·&nbsp; {max(1, words // 200)} min"
    nav = (f'<a class="prev" href="{older.url}"><span>Older</span>{esc(older.title)}</a>' if older else "<span></span>")
    if newer:
        nav += f'\n      <a class="next" href="{newer.url}"><span>Newer</span>{esc(newer.title)}</a>'
    related = ""
    if p.tags:
        first = p.tags[0]
        rel = [q for q in by_tag[first] if q.date < p.date][:3]
        if rel:
            items = "".join(f'<li><time>{q.date:%b %Y}</time><a href="{q.url}">{esc(q.title)}</a></li>\n      '
                            for q in rel)
            related = (f'\n    <div class="related">\n      <h3 class="list-title">More on {esc(first)}</h3>\n'
                       f'      <ul class="post-list">\n      {items}</ul>\n    </div>')
    main = f"""<article>
    <h1>{esc(p.title)}</h1>
    <p class="post-meta">{meta}</p>
    <div class="entry-content">
      {p.html}
    </div>
    <nav class="post-nav">
      {nav}
    </nav>{related}
    <div class="post-footer">
      {GISCUS}
    </div>
  </article>"""
    page(p.url, main, p.title, tags=p.tags, image=p.image)


def thumb(p):
    if p.image:
        return p.image
    m = re.search(r'src="([^"]+)"', p.html)
    return m.group(1) if m else None


def index_page(posts):
    latest = posts[0]
    meta = f'<time datetime="{latest.date.isoformat()}">{date_long(latest.date)}</time>'
    if latest.tags:
        meta += " &nbsp;·&nbsp; " + tag_links(latest.tags)
    out = [f"""<article class="latest">
  <h1><a href="{latest.url}">{esc(latest.title)}</a></h1>
  <p class="post-meta">{meta}</p>
  <div class="entry-content">
    {latest.html}
  </div>
  <p class="post-meta"><a href="{latest.url}#comments">Comments</a></p>
</article>

<h2 class="list-title">Recent</h2>
<ul class="teasers">"""]
    for p in posts[1:6]:
        words = plain(p.html).split()
        teaser = " ".join(words[:40]) + ("..." if len(words) > 40 else "")
        t = thumb(p)
        img = f'<a class="teaser-thumb" href="{p.url}"><img src="{attr(t)}" alt=""></a>' if t else ""
        out.append(f"""  <li class="teaser">
    {img}
    <div class="teaser-text">
      <h3><a href="{p.url}">{esc(p.title)}</a></h3>
      <p class="post-meta"><time datetime="{p.date.isoformat()}">{date_long(p.date)}</time></p>
      <p>{esc(teaser)}</p>
    </div>
  </li>""")
    out.append('</ul>\n\n<h2 class="list-title">All posts</h2>')
    year = None
    close = ""
    for p in posts[6:]:
        if p.date.year != year:
            out.append(close)
            year = p.date.year
            head = f'<h3 class="year">{year}</h3>'
            if year < FOLD_BEFORE:
                out.append(f'<details class="year-fold">\n<summary>{head}</summary>\n<ul class="post-list">')
                close = "</ul>\n</details>"
            else:
                out.append(f'{head}\n<ul class="post-list">')
                close = "</ul>"
        out.append(f'  <li><time>{p.date:%b} {p.date.day}</time><a href="{p.url}">{esc(p.title)}</a></li>')
    out.append(close)
    page("/", "\n".join(out))


def archive_page(posts):
    out = ['<article>\n    <h1 class="entry-title">\n        <a>Archives</a>\n    </h1>\n    <hr>\n</article>']
    year = None
    for p in posts:
        if p.date.year != year:
            if year:
                out.append("    </ul>\n</article>")
            ident = f' id="{p.date.year}-ref"' if year else ""
            year = p.date.year
            out.append(f'<article>\n    <h2{ident} class="year-heading">{year}</h2>\n    <ul>')
        out.append(f'        <li class="entry-title"><a href="{URL}{p.url}" title="{attr(p.title)}">{esc(p.title)}</a></li>')
    out.append("    </ul>\n</article>")
    page("/archives/", "\n".join(out), "Archives")


def tags_page(by_tag):
    names = sorted(by_tag)
    out = ['<article>\n    <h1 class="entry-title">\n        <a>Tags Archive</a>\n    </h1>\n    <hr>\n'
           '    <ul class="entry-meta inline-list">']
    for t in names:
        out.append(f'        <li><a href="#{attr(t)}" class="tag"><span class="term">{esc(t)}</span> '
                   f'<span class="count">({len(by_tag[t])})</span></a></li>')
    out.append("    </ul>\n</article>")
    for t in names:
        out.append(f'<article>\n    <h1 id="{attr(t)}" class="entry-title">{esc(t)}</h1>\n    <ul>')
        for p in by_tag[t]:
            out.append(f'        <li><a href="{URL}{p.url}" title="{attr(p.title)}">{esc(p.title)}   '
                       f'({p.date:%B %d, %Y})</a></li>')
        out.append("    </ul>\n</article>")
    page("/tags/", "\n".join(out), "Tags Archive")


def feeds(posts, by_tag, now):
    x = html.escape
    rfc = format_datetime

    def rss(path, items, description, cats):
        body = "".join(f"""
    <item>
      <title>{x(p.title)}</title>
      <description>{x(p.html)}</description>
      <pubDate>{rfc(p.date)}</pubDate>
      <link>{URL}{p.url}</link>
      <guid>{URL}{p.url[:-5]}</guid>{"".join(f"<category>{x(t)}</category>" for t in (p.tags if cats else []))}
    </item>""" for p in items)
        (OUT / path).write_text(f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>{x(TITLE)}</title>
    <description>{x(description)}</description>
    <link>{URL}/</link>
    <atom:link href="{URL}/{path}" rel="self" type="application/rss+xml"/>
    <pubDate>{rfc(now)}</pubDate>
    <lastBuildDate>{rfc(now)}</lastBuildDate>{body}
  </channel>
</rss>
""", encoding="utf-8")

    rss("feed.xml", posts[:10], DESCRIPTION, True)
    rss("amar.rss.xml", by_tag.get("Amar RPG", []), TITLE, False)
    entries = "".join(f"""
 <entry>
   <title>{x(p.title)}</title>
   <link href="{URL}{p.url}"/>
   <updated>{p.date.isoformat()}</updated>
   <id>{URL}{p.url[:-5]}</id>
   <content type="html">{x(p.html)}</content>
 </entry>""" for p in posts[:20])
    (OUT / "atom.xml").write_text(f"""<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
 <title>{x(TITLE)}</title>
 <link href="{URL}/atom.xml" rel="self"/>
 <link href="{URL}"/>
 <updated>{now.isoformat()}</updated>
 <id>{URL}</id>
 <author><name>{x(COPYRIGHT)}</name></author>{entries}
</feed>
""", encoding="utf-8")


def redirect(old, new):
    target = URL + new
    path = OUT / old.strip("/") / "index.html"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"""<!DOCTYPE html>
<html lang="en-US">
  <meta charset="utf-8">
  <title>Redirecting&hellip;</title>
  <link rel="canonical" href="{target}">
  <script>location="{target}"</script>
  <meta http-equiv="refresh" content="0; url={target}">
  <meta name="robots" content="noindex">
  <h1>Redirecting&hellip;</h1>
  <a href="{target}">Click here if you are not redirected.</a>
</html>
""", encoding="utf-8")


def copy_static(done):
    for root, dirs, files in os.walk(ROOT):
        rel = pathlib.Path(root).relative_to(ROOT)
        dirs[:] = [d for d in dirs if not d.startswith(("_", ".")) and str(rel / d) not in SKIP]
        for f in files:
            src = pathlib.Path(root) / f
            relf = str(src.relative_to(ROOT))
            if f.startswith(("_", ".")) or relf in SKIP or relf in done:
                continue
            dst = OUT / relf
            if dst.exists() and dst.stat().st_mtime >= src.stat().st_mtime and dst.stat().st_size == src.stat().st_size:
                continue
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)


def main():
    now = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0)
    if OUT.exists():
        for f in OUT.rglob("*.html"):
            f.unlink()
    OUT.mkdir(exist_ok=True)
    posts = sorted((Post(p) for p in (ROOT / "_posts").glob("*.md")), key=lambda p: p.key, reverse=True)
    by_tag = {}
    for p in posts:
        for t in p.tags:
            by_tag.setdefault(t, []).append(p)
    for i, p in enumerate(posts):
        post_page(p, posts[i + 1] if i + 1 < len(posts) else None, posts[i - 1] if i else None, by_tag)
    index_page(posts)
    archive_page(posts)
    tags_page(by_tag)
    feeds(posts, by_tag, now)

    done = {"index.html", "archives/index.html", "tags/index.html", "feed.xml", "atom.xml", "amar.rss.xml"}
    urls = ["/", "/archives/", "/tags/"] + [p.url for p in posts]
    for src in sorted(ROOT.glob("*.md")):
        meta, body = read(src)
        if "permalink" not in meta:
            continue
        done.add(src.name)
        url = meta["permalink"]
        main_html = f"""<article>
    <h1>{esc(meta.get('title', ''))}</h1>
    <div class="entry-content">
      {markdown(body, meta)}
    </div>
  </article>"""
        page(url, main_html, meta.get("title"), description=meta.get("description"), image=meta.get("image"))
        if url != "/404.html":
            urls.append(url)
        for old in meta.get("redirect_from") or []:
            redirect(old, url)

    copy_static(done)

    pdfs = sorted("/" + str(f.relative_to(OUT)) for f in OUT.rglob("*.pdf"))
    (OUT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f"<url><loc>{URL}{html.escape(u)}</loc></url>\n" for u in urls + pdfs) + "</urlset>\n")
    (OUT / "robots.txt").write_text(f"Sitemap: {URL}/sitemap.xml\n")
    print(f"{len(posts)} posts, {len(urls)} pages, {len(by_tag)} tags -> {OUT}")


if __name__ == "__main__":
    main()
