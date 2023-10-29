# Python file for constructing animations and images, used within .pptx file

from manim import *
import math

class LikeDislike_4(Scene):
    def construct(self):

        fig = FullScreenRectangle(color='#1E1E1E')
        fig.set_fill('#1E1E1E', opacity=1.0)
        txt21 = Tex(r'$_{105}$', color=GREEN).shift(LEFT*1.3+DOWN*.25).shift(RIGHT*.5)
        txt22 = Tex(r'$_{17}$', color=RED).shift(RIGHT*0.55+DOWN*.1).shift(DOWN*.1)
        txt11 = Text(text='👍', color=GREEN, font='Times New Roman').shift(LEFT*2).shift(RIGHT*.5)
        txt12 = Text(text='👎', color=RED, font='Times New Roman', font_size=(DEFAULT_FONT_SIZE-10)).shift(DOWN*.1)
        self.play(DrawBorderThenFill(fig), Write(txt22), Write(txt21), Write(txt11), Write(txt12))
        self.wait(5)

class Slide5_text1(Scene):
    def construct(self):
        fig = FullScreenRectangle(color='#1E1E1E').set_fill('#1E1E1E', opacity=1.0)

        starttext = Text('Логичным рассуждением\n'
        'будет предположение о\n'
        'наличии константного\n'
        'отношения данных,\n'
        'при их числе стремящемся\n'
        'к бесконечности.',
        font='Times New Roman')

        trans_tex1 = MathTex(r'\lim\limits_{N_i \to \infty} \bigg(\frac{\phantom{N}_{\phantom{1}}}{\phantom{N}_{\phantom{2}}}\bigg)').shift(LEFT*1.5).scale(1.5)
        trans_text3 = Text('N', color=GREEN, font='Times New Roman', font_size=DEFAULT_FONT_SIZE+5).shift(LEFT*0.65+UP*0.5)
        trans_text4 = Text('N', color=RED, font='Times New Roman', font_size=DEFAULT_FONT_SIZE+5).shift(LEFT*0.65+DOWN*0.5)
        trans_tex2 = MathTex(r'= const').shift(RIGHT*2).scale(1.5)
        trans_text1 = Text(text='👍', color=GREEN, font='Times New Roman', font_size=(DEFAULT_FONT_SIZE-25)).shift(UP*0.5+LEFT*0.15+DOWN*0.1)
        trans_text2 = Text(text='👎', color=RED, font='Times New Roman', font_size=(DEFAULT_FONT_SIZE-25)).shift(DOWN*0.55+LEFT*0.15+DOWN*0.1)

        trans_group = VGroup(trans_tex1, trans_tex2, trans_text1, trans_text2, trans_text3, trans_text4).shift(UP)

        self.add(fig)
        self.play(Write(starttext))
        self.wait(1)
        self.play(Transform(starttext, trans_group))
        self.wait(1)