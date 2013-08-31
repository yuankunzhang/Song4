# -*- coding: utf-8 -*-
import re
import markdown as md

from jinja2 import evalcontextfilter, Markup


def add_filters(app):

    @app.template_filter()
    @evalcontextfilter
    def nl2br(eval_ctx, stream):
        re_paragraph = re.compile(r'(?:\r\n|\r|\n){2,}')

        if stream is None:
            return

        outpur = u'\n\n'.join(u'<p>%s</p>' % p.replace(
            '\n', Markup('</p>\n<p>')) for p in re_paragraph.split(stream))

        if eval_ctx.autoescape:
            output = Markup(output)

        return output

    @app.template_filter()
    def markdown(stream):
        output = md.markdown(stream, ['tables', 'fenced_code'], safe_mode='remove')

        return Markup(output)

    @app.template_filter()
    def preview(html):
        PREVIEW_LEN = 150
        ellipsis = '<p>......</p>'

        if len(html) < PREVIEW_LEN:
            return html

        p_end_tag = html.find('</p>', PREVIEW_LEN)

        if p_end_tag != -1:
            html = html[:p_end_tag+4]

        return html + Markup(ellipsis)
