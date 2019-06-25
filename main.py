def declare_variables(variables, macro):

    @macro
    def summary(url):
        return f'<a class="card" href="{url}">{url}</a>'
