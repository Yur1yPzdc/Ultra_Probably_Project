# Python file for constructing animations and images, used within .pptx file

from manim import *
import math
import numpy as np

class LikeDislike_4(Scene): #DONE #V1
    def construct(self):

        fig = FullScreenRectangle(color='#1E1E1E')
        fig.set_fill('#1E1E1E', opacity=1.0)
        txt21 = Tex(r'$_{105}$', color=GREEN).shift(LEFT*1.3+DOWN*.25).shift(RIGHT*.5)
        txt22 = Tex(r'$_{17}$', color=RED).shift(RIGHT*0.55+DOWN*.1).shift(DOWN*.1)
        txt11 = Text(text='👍', color=GREEN, font='Times New Roman').shift(LEFT*2).shift(RIGHT*.5)
        txt12 = Text(text='👎', color=RED, font='Times New Roman', font_size=(DEFAULT_FONT_SIZE-10)).shift(DOWN*.1)
        self.play(DrawBorderThenFill(fig), Write(txt22), Write(txt21), Write(txt11), Write(txt12))
        self.wait(5)

class v1_slide5_text1(Scene): #DONE #V1
    def construct(self):
        fig = FullScreenRectangle(color='#1E1E1E').set_fill('#1E1E1E', opacity=1.0)

        starttext = Text('Логичным рассуждением\n'
        'будет предположение о\n'
        'наличии константного\n'
        'отношения данных,\n'
        'при их числе стремящемся\n'
        'к бесконечности.',
        font='Times New Roman')

        trans_tex1 = MathTex(r'\lim\limits_{N_i \to \infty} \bigg(\frac{\phantom{N}_{\phantom{1}}}{\phantom{N}_{\phantom{2}}}\bigg)').shift(LEFT*1.5).scale(1.5).shift(DOWN)
        trans_text3 = Text('N', color=GREEN, font='Times New Roman', font_size=DEFAULT_FONT_SIZE+5, t2s={'N': ITALIC}).shift(LEFT*0.65+UP*0.5).shift(DOWN)
        trans_text4 = Text('N', color=RED, font='Times New Roman', font_size=DEFAULT_FONT_SIZE+5, t2s={'N': ITALIC}).shift(LEFT*0.65+DOWN*0.5).shift(DOWN)
        trans_tex2 = MathTex(r'= const').shift(RIGHT*2).scale(1.5)
        trans_text1 = Text(text='👍', color=GREEN, font='Times New Roman', font_size=(DEFAULT_FONT_SIZE-25)).shift(UP*0.5+LEFT*0.15+DOWN*0.1).shift(DOWN)
        trans_text2 = Text(text='👎', color=RED, font='Times New Roman', font_size=(DEFAULT_FONT_SIZE-25)).shift(DOWN*0.55+LEFT*0.15+DOWN*0.1).shift(DOWN)
        #trans2_tex1 = MathTex(r'= P', tex_to_color_map={'= ': WHITE, 'P': YELLOW}).shift(RIGHT*2).scale(1.5)

        trans_group1 = VGroup(trans_tex1, trans_tex2, trans_text1, trans_text2, trans_text3, trans_text4).shift(UP)
        #trans_group2 = VGroup(trans_tex1, trans2_tex1, trans_text1, trans_text2, trans_text3, trans_text4).shift(UP)

        self.add(fig)
        self.play(Write(starttext))
        self.wait(1)
        self.play(Transform(starttext, trans_group1))
        self.wait(1)
        #self.play(FadeOut(trans_group1))
        #self.play(Transform(trans_group1, trans_group2))
        #self.wait(1)

class v2_slide4_text2(Scene): #DONE #V2
    def construct(self):
        
        self.camera.background_color='#1E1E1E'

        #fig = FullScreenRectangle(color='#1E1E1E').set_fill('#1E1E1E', opacity=1.0)

        text1 = Text('Интересным способом \nпредставить систему \nотзывов будет \n«Совокупность \nбросков кубика»', 
        font='Times New Roman', font_size=36, t2s={'«Совокупность \nбросков кубика»': ITALIC}, 
        t2c={'«Совокупность \nбросков кубика»': YELLOW}
        )

        k = 0.6
        Dice1 = SVGMobject(file_name='media/v2_slide4_Dices/Dice1.svg', height=0.5).shift(LEFT*2.5*k+DOWN)
        Dice2 = SVGMobject(file_name='media/v2_slide4_Dices/Dice2.svg', height=0.5).shift(LEFT*1.5*k+DOWN)
        Dice3 = SVGMobject(file_name='media/v2_slide4_Dices/Dice3.svg', height=0.5).shift(LEFT*.5*k+DOWN)
        Dice4 = SVGMobject(file_name='media/v2_slide4_Dices/Dice4.svg', height=0.5).shift(RIGHT*.5*k+DOWN)
        Dice5 = SVGMobject(file_name='media/v2_slide4_Dices/Dice5.svg', height=0.5).shift(RIGHT*1.5*k+DOWN)

        Dice_Group = VGroup(Dice1, Dice2, Dice3, Dice4, Dice5)

        D_Values = [[0.0001, 0.0001, 0.0001, 0.0001, 0.0001],[1/5, 1/5, 1/5, 1/5, 1/5], [60/137, 30/137, 20/137, 15/137, 12/137], 
        [18/47, 18/194, 2/47, 18/194, 18/47], [1/8, 3/16, 3/8, 3/16, 1/8], 
        ]

        Dice_Graph = BarChart(
            values=D_Values[0], bar_names=None, 
            bar_colors=[YELLOW_E, '#EECA30', YELLOW_D, '#FADC5A', '#FFEE6F', '#FFFF84'],
            y_length=2, y_range=[0, 0.5, 0.5], x_length=3, bar_fill_opacity=0.9, 
        ).shift(UP*0.4+LEFT*0.3)

        Dice_Graph_Labels = Dice_Graph.get_axis_labels(
            Tex("Value", color=GRAY_A).scale(0.7), 
                        Tex("Probability", color=GRAY_A).scale(0.7)
        )



        self.play(Write(text1)) #ACTUAL
        self.wait(0.5)
        self.play(Transform(text1, VGroup(Dice_Group, Dice_Graph, Dice_Graph_Labels))) #ACTUAL

        #self.add(Dice_Group) #DEBUG
        #self.add(Dice_Graph, Dice_Graph_Labels) #DEBUG

        self.play(Dice_Graph.animate.change_bar_values(D_Values[1]), run_time=1, rate_func=ease_in_out_sine)
        self.wait(0.5)
        self.play(Dice_Graph.animate.change_bar_values(D_Values[2]), run_time=1, rate_func=ease_in_out_sine)
        self.wait(0.5)
        self.play(Dice_Graph.animate.change_bar_values(D_Values[3]), run_time=1, rate_func=ease_in_out_sine)
        self.wait(0.5)
        self.play(Dice_Graph.animate.change_bar_values(D_Values[4]), run_time=1, rate_func=ease_in_out_sine)
        self.wait(0.5)
        self.play(Dice_Graph.animate.change_bar_values(D_Values[1]), run_time=1, rate_func=ease_in_out_sine)

        self.wait(1)