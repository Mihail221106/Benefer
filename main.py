class SiteBuilder:

    def __init__(self):
        self.code = [['<!DOCTYPE html>\n'], '<html>\n', "\t<head>\n", '\t\t<style>\n', '\t\t</style>\n',
                     '\t\t<meta charset = "utf-8">\n', '\t</head>\n',
                     '\t<body>\n', '\t</body>\n', '</html>\n']
        self.prev = []
        self.ind_class = 0

    def icon(self, icon):
        self.code = self.code[:self.code.index('\t</head>\n')] + [
            f'\t\t<link rel = "icon" href = "{icon}" type = "image/x-icon">\n'] + \
                    self.code[self.code.index('\t</head>\n'):]

    def page_name(self, title):
        self.code = self.code[:self.code.index('\t</head>\n')] + ['\t\t<title>', title, '</title>\n'] + \
                    self.code[self.code.index('\t</head>\n'):]

    def paragraph(self, text, font_size, x, y, width, color, font):
        s = [f'<p  style = "font-size:{font_size[0]}{font_size[1]}; \
            color:{color}; font:"{font}">\n', f'{text} \n', '</p>\n']
        for i in range(0, len(s)):
            s[i] = '\t\t\t' + s[i]

        s = [f'\t\t<div class="c{self.ind_class}" style = "position:absolute; left:{x[0]}{x[1]}; top:{y[0]}{y[1]}; \
             width:{width[0]}{width[1]};">\n'] + s + ['\t\t</div>\n']
        self.prev.append(s)
        self.code = self.code[0:self.code.index('\t</body>\n')] + s + self.code[self.code.index('\t</body>\n'):]
        self.ind_class += 1

    def image(self, src, width, height, x, y, title='picture', alt='picture', label='', lab_size=[16, 'pt'],
              lab_font="Times New Roman"):
        s = ['<figure>\n', f'\t<img src = "{src}" ' + f'title = "{title}" ' + f'alt = "{alt}" ' +
             f'width=100% height=100%>\n']
        s = s + [f'\t<figcaption style = "font-size:{lab_size[0]}{lab_size[1]}; font:"{lab_font}"; ">\n',
                 f'\t<i>{label}</i></figcaption>\n']
        s = s + [f'</figure>\n']
        for i in range(0, len(s)):
            s[i] = '\t\t\t' + s[i] + '\n'

        open_fig = f'\t\t<figure class="c{self.ind_class}" style = "position:absolute; left:{x[0]}{x[1]}; \
                   top:{y[0]}{y[1]}; width:{width[0]}{width[1]}; height:{height[0]}{height[1]} ">\n '

        s[0] = open_fig

        self.prev.append(s)

        self.code = self.code[0:self.code.index('\t</body>\n')] + s + self.code[self.code.index('\t</body>\n'):]
        self.ind_class += 1

    def save(self, html):
        with open(f'{html}.html', 'w', encoding='UTF-8') as file:
            for cod in self.code:
                if type(cod) == f'class ' + "'" + 'list' + "'" + '>':
                    file.writelines(cod)
                else:
                    file.writelines(cod)


    def undo(self):
        if self.ind_class == 0:
            return
        self.ind_class -= 1
        for text in self.code:
            if text.find(f'class="c{self.ind_class}"') != -1:
                i = self.code.index(text)
                del self.code[i]
                del self.code[i]
                del self.code[i]
                del self.code[i]
                del self.code[i]
        if len(self.prev) != 0:
            self.prev.pop(-1)

    def swap(self, step_index, index):
        step = self.prev[step_index]
        del self.prev[step_index]
        self.prev = self.prev[0:index] + [step] + self.prev[index:]


sb = SiteBuilder()
sb.page_name('Paaaaage')
sb.icon('icon.png')
sb.paragraph(text='fdfasgdfafaggadgdagdagdgdg', font_size=[16, 'pt'], x=[10, 'vw'], y=[10, 'vh'], width=[90, 'vw'],
             color='black', font='Times New Roman')
sb.image(src='L1.jpg', width=[50, 'vw'], height=[60, 'vh'], x=[20, 'vw'], y=[10, 'vh'], label='fds')
sb.swap(1, 0)
sb.save('site')
