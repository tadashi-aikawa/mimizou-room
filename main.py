from requests_html import HTMLSession

def declare_variables(variables, macro):

    @macro
    def summary(url):
        return f'<a class="card" href="{url}" data-card-description="0">{url}</a>'

    @macro
    def refer(url):
        res = HTMLSession().get(url)
        title = res.html.find('title')[0].text
        return f'🔗 [{title or url}]({url})'
