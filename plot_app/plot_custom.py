# File created by Leonardo Cencetti on 1/29/21
def custom_plots(plots):
    text_height = 20
    for i in range(len(plots)):
        try:
            plots[i].output_backend = 'svg'
            for j in range(len(plots[i].renderers)):
                plots[i].renderers[j].glyph.line_width = plots[i].renderers[j].nonselection_glyph.line_width = 1.2

            plots[i].xaxis.axis_label_text_font_size = \
                plots[i].yaxis.axis_label_text_font_size = \
                plots[i].xaxis.major_label_text_font_size = \
                plots[i].yaxis.major_label_text_font_size = \
                plots[i].legend.label_text_font_size = \
                plots[i].legend.title_text_font_size = \
                plots[i].title.text_font_size = '{}px'.format(text_height)
            plots[i].xaxis.major_label_standoff = \
                plots[i].xaxis.axis_label_standoff = \
                plots[i].yaxis.major_label_standoff = \
                plots[i].yaxis.axis_label_standoff = round((2 * text_height + 49) / 15)
        except:
            pass
    return plots