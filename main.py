from urllib.parse import urljoin, urlsplit
from typing import Optional

from requests_html import HTMLSession


NO_FAVICON_IMG = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyRpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMy1jMDExIDY2LjE0NTY2MSwgMjAxMi8wMi8wNi0xNDo1NjoyNyAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENTNiAoTWFjaW50b3NoKSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDo0NTRGMzZFNTNBOTQxMUUzOUU0OUExMEE2NkE3QUNDMyIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDo0NTRGMzZFNjNBOTQxMUUzOUU0OUExMEE2NkE3QUNDMyI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOjQ1NEYzNkUzM0E5NDExRTM5RTQ5QTEwQTY2QTdBQ0MzIiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOjQ1NEYzNkU0M0E5NDExRTM5RTQ5QTEwQTY2QTdBQ0MzIi8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+pF18XQAAAUtJREFUeNqkkz1LA0EQhjdDQG0CaqOkFiEWNhG10cIrbSzTpAp4lY1cZeEPOOwDHljebxAiYilaiSDYapR0YiUW4jvwngzjLRYOPOzt3Hzszs40gpM8z9exDEAC2lSPwQgUWZZdW/uGcWxhGYIeVRPwAL7AJpihvgQpAr3/BKDzBeiCO3AAgysTXLPvmMS3utcgQsWQzs9g2zlrkhV30y59gvDO1bFP4fzmjNfAQvgtPfUVFqySlxrDG3Af6mXQZLVttoJH38JyDk7AfCRAIuapVPpwXOX3E5/vCCxGArTFKabBJYLsY/0AS6iJFnEKbIBHH0GYxcosK6z1mFMFgnyygfrOdizssJgkbu9PMJKqaBE5w3XsK3Xc/0J4tDISQNt31+wPzXepvk1uUi0YOyzUDJgW8hjsmVZO/xqmSnRoXsFydJj+M87fAgwAhBVmF6w0nW0AAAAASUVORK5CYII="


def get_meta(html: any, name: str) -> Optional[str]:
    e = html.find(f"meta[property='{name}']", first=True)
    return e.attrs.get("content") if e else None


def to_base_url(url: str) -> str:
    return f"{urlsplit(url).scheme}://{urlsplit(url).netloc}"


def get_favicon_url(html: any, url: str) -> str:
    icon_urls = html.find("link[rel='icon']") or html.find("link[rel='shortcut icon']")
    if not icon_urls:
        return f"{to_base_url(url)}/favicon.ico"

    href = icon_urls[0].attrs["href"]
    if "http" in href:
        return href

    base = html.find("base", first=True)
    base_url = base and base.attrs["href"]

    return f"{to_base_url(url)}{base_url}{href}" if base_url else urljoin(url, href)


def declare_variables(variables, macro):
    @macro
    def summary(url):
        return f'<a class="card" href="{url}" data-card-description="0">{url}</a>'

    @macro
    def refer(url):
        return "..."
        print(f"Request... {url}")

        res = HTMLSession.get(url)

        title = res.html.find("title")[0].text

        if "github.com" in url:
            return f"""<div>
            <img src="https://cdn.svgporn.com/logos/github-icon.svg" width=20 class="refer"/>
            <a href={url} class="refer">{title or url}</a>
            </div>"""
        elif "qiita.com" in url:
            return f"""<div>
            <img src="https://pbs.twimg.com/profile_images/1542801560/Qiita.png" width=20 class="refer"/>
            <a href={url} class="refer">{title or url}</a>
            </div>"""
        else:
            return f"""<div>
            <a href={url} class="refer">🔗 {title or url}</a>
            </div>"""

    @macro
    def link(url):
        print(f"Request... {url}")

        session = HTMLSession()
        res = session.get(url)

        site_name = get_meta(res.html, "og:site_name") or "No Site Name"
        title = (
            get_meta(res.html, "og:title")
            or res.html.find("title")[0].text
            or "No Title"
        )
        description = get_meta(res.html, "og:description") or "No Description"
        image_url = get_meta(res.html, "og:image") or ""
        favicon_url = get_favicon_url(res.html, url)
        icon_url = favicon_url if session.get(favicon_url).ok else NO_FAVICON_IMG
        print(f"ICON: {icon_url}")

        return f"""
        <div class="link-card">
            <div>
                <img src={icon_url} width=20 class="link-card-site-icon"/>
                <span class="link-card-site-name">{site_name}</span>
            </div>
            <div class="link-card-body">
                <div class="link-card-content">
                    <div>
                        <p class="link-card-title">{title or url}</p>
                    </div>
                    <div class="link-card-description">{description}</div>
                </div>
                <img src={image_url} class="link-card-image"/>
            </div>
            <a href={url}></a>
        </div>
        """.strip()
