from requests_html import HTMLSession


def declare_variables(variables, macro):
    @macro
    def summary(url):
        return f'<a class="card" href="{url}" data-card-description="0">{url}</a>'

    @macro
    def refer(url):
        print(f"Request... {url}")

        res = HTMLSession().get(url)
        title = res.html.find("title")[0].text

        if "github.com" in url:
            return f"""<div>
            <img src="https://cdn.svgporn.com/logos/github-icon.svg" width=20 class="inline-image"/>
            <a href={url} class="inline-image">{title or url}</a>
            </div>"""
        elif "qiita.com" in url:
            return f"""<div>
            <img src="https://pbs.twimg.com/profile_images/1542801560/Qiita.png" width=20 class="inline-image"/>
            <a href={url} class="inline-image">{title or url}</a>
            </div>"""
        else:
            return f"""<div>
            <a href={url} class="inline-image">🔗 {title or url}</a>
            </div>"""

    @macro
    def link(url):
        print(f"Request... {url}")

        res = HTMLSession().get(url)
        title = res.html.find("title")[0].text

        descriptions = (
            res.html.search('name="description" content="{}"')
            or res.html.search('property=og:title content="{}"')
            or res.html.search('property="og:title" content="{}"')
        )
        description = descriptions[0] if descriptions else ""

        image_urls = res.html.search(
            'property=og:image content="{}"'
        ) or res.html.search('property="og:image" content="{}"')
        image_url = image_urls[0] if image_urls else ""
        return f"""<div>
        <img src={image_url} width=30 class="link"/>
        <a href={url} class="link">{title or url}</a>
        <div>{description}</div>
        </div>"""
