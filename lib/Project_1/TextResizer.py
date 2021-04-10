#https://stackoverflow.com/a/44797574/4663086
#slighly improved to take into account width

import matplotlib.pyplot as plt

class TextResizer():
    def __init__(self, texts, fig=None):
        if not fig: fig = plt.gcf()
        self.fig=fig
        self.texts = texts
        self.fontsizes = [t.get_fontsize() for t in self.texts]
        self.windowwidth, self.windowheight = fig.get_size_inches()*fig.dpi

    def __call__(self, event=None):
        scaleh = event.height / self.windowheight
        scalew = event.width / self.windowwidth
        for i in range(len(self.texts)):
            newsize = self.fontsizes[i]*min(scaleh, scalew)
            self.texts[i].set_fontsize(newsize)