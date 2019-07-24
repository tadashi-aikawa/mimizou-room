from datetime import timedelta
from urllib.parse import urljoin, urlsplit
from typing import Optional

import requests_cache


# Must install before importing HTMLSession
requests_cache.install_cache(
    cache_name="mimizou_room", backend="sqlite", expire_after=timedelta(weeks=1)
)
from requests_html import HTMLSession

from xml.sax.saxutils import escape

NO_FAVICON_IMG = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyRpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMy1jMDExIDY2LjE0NTY2MSwgMjAxMi8wMi8wNi0xNDo1NjoyNyAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENTNiAoTWFjaW50b3NoKSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDo0NTRGMzZFNTNBOTQxMUUzOUU0OUExMEE2NkE3QUNDMyIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDo0NTRGMzZFNjNBOTQxMUUzOUU0OUExMEE2NkE3QUNDMyI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOjQ1NEYzNkUzM0E5NDExRTM5RTQ5QTEwQTY2QTdBQ0MzIiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOjQ1NEYzNkU0M0E5NDExRTM5RTQ5QTEwQTY2QTdBQ0MzIi8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+pF18XQAAAUtJREFUeNqkkz1LA0EQhjdDQG0CaqOkFiEWNhG10cIrbSzTpAp4lY1cZeEPOOwDHljebxAiYilaiSDYapR0YiUW4jvwngzjLRYOPOzt3Hzszs40gpM8z9exDEAC2lSPwQgUWZZdW/uGcWxhGYIeVRPwAL7AJpihvgQpAr3/BKDzBeiCO3AAgysTXLPvmMS3utcgQsWQzs9g2zlrkhV30y59gvDO1bFP4fzmjNfAQvgtPfUVFqySlxrDG3Af6mXQZLVttoJH38JyDk7AfCRAIuapVPpwXOX3E5/vCCxGArTFKabBJYLsY/0AS6iJFnEKbIBHH0GYxcosK6z1mFMFgnyygfrOdizssJgkbu9PMJKqaBE5w3XsK3Xc/0J4tDISQNt31+wPzXepvk1uUi0YOyzUDJgW8hjsmVZO/xqmSnRoXsFydJj+M87fAgwAhBVmF6w0nW0AAAAASUVORK5CYII="


def get_meta_by_property(html: any, property: str) -> Optional[str]:
    e = html.find(f"meta[property='{property}']", first=True)
    return e.attrs.get("content") if e else None


def get_meta_by_name(html: any, name: str) -> Optional[str]:
    e = html.find(f"meta[name='{name}']", first=True)
    return e.attrs.get("content") if e else None


def get_src_by_id(html: any, id_: str) -> Optional[str]:
    e = html.find("#" + id_, first=True)
    return e.attrs.get("src") if e else None


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
        print(f"Create refer: {url}")

        session = HTMLSession()
        res = session.get(url)

        title = (
            get_meta_by_property(res.html, "og:title")
            or res.html.find("title")[0].text
            or url
        )
        favicon_url = get_favicon_url(res.html, url)
        icon_url = favicon_url if session.get(favicon_url).ok else NO_FAVICON_IMG

        return f"""
        <div class="refer">
            <img src={icon_url} class="refer-image"/>
            <a href={url}>{escape(title)}</a>
        </div>
        """.strip()

    @macro
    def link(url):
        print(f"Create link: {url}")

        session = HTMLSession()
        res = session.get(url)

        site_name = (
            get_meta_by_property(res.html, "og:site_name") or urlsplit(url).netloc
        )
        title = (
            get_meta_by_property(res.html, "og:title")
            or res.html.find("title")[0].text
            or url
        )
        description = (
            get_meta_by_property(res.html, "og:description")
            or get_meta_by_name(res.html, "description")
            or ""
        )
        image_url: Optional[str] = get_meta_by_property(
            res.html, "og:image"
        ) or get_src_by_id(res.html, "ebooksImgBlkFront")
        print(f"Image URL: {image_url}")
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
                        <p class="link-card-title">{escape(title)}</p>
                    </div>
                    <div class="link-card-description">{escape(description)}</div>
                </div>
                {f'<img src={image_url} class="link-card-image"/>' if image_url else ""}
            </div>
            <a href={url}></a>
        </div>
        """.strip()
