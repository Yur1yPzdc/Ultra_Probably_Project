# Python file for constructing animations and images used within .pptx file

from manim import *
import math
import numpy as np
import itertools as it
from fractions import Fraction

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
        #end

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
        #end

class v2_slide4_text2(Scene): #DONE #V2 # анимка с изменяющимися распределениями
    def construct(self):
        
        self.camera.background_color='#1E1E1E' # задник теперь сливается с поверпоинтом

        #fig = FullScreenRectangle(color='#1E1E1E').set_fill('#1E1E1E', opacity=1.0)

        text1 = Text('Интересным способом \nпредставить систему \nотзывов будет \n«Совокупность \nбросков кубика»', 
        font='Times New Roman', font_size=36, t2s={'«Совокупность \nбросков кубика»': ITALIC}, 
        t2c={'«Совокупность \nбросков кубика»': YELLOW})

        k = 0.6
        Dice1 = SVGMobject(file_name='media/v2_slide4_Dices/Dice1.svg', height=0.5).shift(LEFT*2.5*k+DOWN)
        Dice2 = SVGMobject(file_name='media/v2_slide4_Dices/Dice2.svg', height=0.5).shift(LEFT*1.5*k+DOWN)
        Dice3 = SVGMobject(file_name='media/v2_slide4_Dices/Dice3.svg', height=0.5).shift(LEFT*.5*k+DOWN)
        Dice4 = SVGMobject(file_name='media/v2_slide4_Dices/Dice4.svg', height=0.5).shift(RIGHT*.5*k+DOWN)
        Dice5 = SVGMobject(file_name='media/v2_slide4_Dices/Dice5.svg', height=0.5).shift(RIGHT*1.5*k+DOWN)

        Dice_Group = VGroup(Dice1, Dice2, Dice3, Dice4, Dice5)

        D_Values = [[0.0001, 0.0001, 0.0001, 0.0001, 0.0001],[1/5, 1/5, 1/5, 1/5, 1/5], [60/137, 30/137, 20/137, 15/137, 12/137], 
        [18/47, 18/194, 2/47, 18/194, 18/47], [1/8, 3/16, 3/8, 3/16, 1/8]]

        Dice_Graph = BarChart(
            values=D_Values[0], bar_names=None, 
            bar_colors=[YELLOW_E, '#EECA30', YELLOW_D, '#FADC5A', '#FFEE6F', '#FFFF84'],
            y_length=2, y_range=[0, 0.5, 0.5], x_length=3, bar_fill_opacity=0.9, 
        ).shift(UP*0.4+LEFT*0.3)

        Dice_Graph_Labels = Dice_Graph.get_axis_labels(
            Tex("Value", color=GRAY_A).scale(0.7), 
                        Tex("Probability", color=GRAY_A).scale(0.7))


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
        #end

class v2_slide6_table(Scene): #V2 # В бездне # Видимо больше не надо
    def construct(self):
        self.camera.background_color = '#1d1d1d'

        Dice1 = SVGMobject(file_name='media/v2_slide4_Dices/Dice1.svg', height=0.8)
        Dice2 = SVGMobject(file_name='media/v2_slide4_Dices/Dice2.svg', height=0.8)
        Dice3 = SVGMobject(file_name='media/v2_slide4_Dices/Dice3.svg', height=0.8)
        Dice4 = SVGMobject(file_name='media/v2_slide4_Dices/Dice4.svg', height=0.8)
        Dice5 = SVGMobject(file_name='media/v2_slide4_Dices/Dice5.svg', height=0.8)

        """Dices_Horisontal = VGroup(Dice1.copy().shift(k*RIGHT), Dice2.copy().shift(2*k*RIGHT),
        Dice3.copy().shift(3*k*RIGHT), Dice4.copy().shift(4*k*RIGHT), Dice5.copy().shift(5*k*RIGHT))

        Dices_Vertical = VGroup(Dice1.copy().shift(k*DOWN), Dice2.copy().shift(2*k*DOWN),
        Dice3.copy().shift(3*k*DOWN), Dice4.copy().shift(4*k*DOWN), Dice5.copy().shift(5*k*DOWN))

        Dice_Table_Dices = VGroup(Dices_Vertical, Dices_Horisontal).center()"""

        Dice_Table = Table(
            table=[['2', '3', '4', '5', '6'], ['3', '4', '5', '6', '7'], ['4', '5', '6', '7', '8'], ['5', '6', '7', '8', '9'], ['6', '7', '8', '9', '10']],
            row_labels=[Dice1.copy(), Dice2.copy(),
                        Dice3.copy(), Dice4.copy(), Dice5.copy()],
            col_labels=[Dice1.copy(), Dice2.copy(),
                        Dice3.copy(), Dice4.copy(), Dice5.copy()],
            line_config={'stroke_width': 3, "color": GRAY_A}
        ).scale(0.5)

        Dice_Pair_1_2 = VGroup(Dice1.copy().scale(0.75), Dice2.copy().scale(0.75))

        self.play(Create(Dice_Table))
        #end

class v2_slide6_animated_bars(Scene): #DONE #V2 # преобразование таблицы значений в диаграмму, но не совсем в диаграмму
    def construct(self):
        self.camera.background_color='#1e1e1e'

        k = 0.7
        kostil_1 = [['2', '3', '4', '5', '6'], ['3', '4', '5', '6', '7'], ['4', '5', '6', '7', '8'], ['5', '6', '7', '8', '9'], ['6', '7', '8', '9', '10']]
        kostil_2 = {'10': RED, '2': RED, '3': ORANGE, '9': ORANGE, '4': YELLOW_D, '8': YELLOW_D, '5': YELLOW, '7': YELLOW, '6': GREEN}

        values_table = [ # ввели значения в память
            Text(kostil_1[i][j], color=kostil_2[kostil_1[i][j]], font_size=36, font='Times New Roman').shift(UP*(5-i)*k + RIGHT*j*k) 
            for i in range(5) for j in range(5)]
        
        for i in values_table:
            self.play(Write(i), run_time=1/25) # отрисовали значения

        self.wait(1)

        for idx in range(9):
            indexes = [i for i in it.combinations_with_replacement(range(idx + 1), 2) if sum(i) == idx and all(k not in i for k in [5, 6, 7, 8, 9])]
            indexes.extend([i[::-1] for i in indexes.copy() if i != i[::-1]])
            # херня, которая работает. находим "индексы" элементов, расположенных по диагонали

            temp = []
            for i in indexes:
                temp.append(values_table[i[1]+5*i[0]].copy())
            group_from = VGroup(*temp)

            rect_k = 0.5
            curr_color = rgb_to_color([(172-idx*(172-73)/8)/255, (234-idx*(234-168)/8)/255, (215-idx*(215-143)/8)/255])
            bg_color = rgb_to_color([(172-(idx+5)*(172-73)/8)/255, (234-(idx+5)*(234-168)/8)/255, (215-(idx+5)*(215-143)/8)/255])

            rect = Rectangle(height=(len(temp))*(rect_k/2), width=rect_k, color=curr_color).shift(rect_k*LEFT*2.5+rect_k*RIGHT*idx+(rect_k/2)*UP*(len(temp)-1)/2+DOWN).set_fill(bg_color, opacity=0.8)
            kostil_stroka = r'\frac{' + f'{len(temp)}' + r'}{25}'
            prob = MathTex(kostil_stroka, tex_to_color_map={kostil_stroka: curr_color}).scale(rect_k).move_to(rect)
            
            if len(temp) < 3: # условие, чтоб текст помещало не внутрь слишком низкого столбика
                prob.shift((rect_k/4)*UP*len(temp)+UP*(0.75*rect_k))
            
            group_to = VGroup(rect, prob)

            self.play(Transform(group_from, group_to))

        self.play(Create(Rectangle(width=4.75, height=1.5).shift(DOWN*0.5+RIGHT*0.75))) # обвели столбики
        
        self.wait(1)
        #end

class v2_slide8_convolution_demo(Scene): #DONE #V2
    def construct(self):
        self.camera.background_color='#1e1e1e'

        D_Values = [[0.0001, 0.0001, 0.0001, 0.0001, 0.0001],[1/5, 1/5, 1/5, 1/5, 1/5], [60/137, 30/137, 20/137, 15/137, 12/137], 
        [18/47, 18/194, 2/47, 18/194, 18/47], [1/8, 3/16, 3/8, 3/16, 1/8]]

        D_Values_str_LATEX = [[r'0', r'0', r'0', r'0', r'0'],
        [r'\frac{1}{5}', r'\frac{1}{5}', r'\frac{1}{5}', r'\frac{1}{5}', r'\frac{1}{5}'], 
        [r'\frac{60}{137}', r'\frac{30}{137}', r'\frac{20}{137}', r'\frac{15}{137}', r'\frac{12}{137}'], 
        [r'\frac{18}{47}', r'\frac{18}{194}', r'\frac{2}{47}', r'\frac{18}{194}', r'\frac{18}{47}'], 
        [r'\frac{1}{8}', r'\frac{3}{16}', r'\frac{3}{8}', r'\frac{3}{16}', r'\frac{1}{8}']]


        k = 0.6
        Dice1 = SVGMobject(file_name='media/v2_slide4_Dices/Dice1.svg', height=0.35)
        Dice2 = SVGMobject(file_name='media/v2_slide4_Dices/Dice2.svg', height=0.35)
        Dice3 = SVGMobject(file_name='media/v2_slide4_Dices/Dice3.svg', height=0.35)
        Dice4 = SVGMobject(file_name='media/v2_slide4_Dices/Dice4.svg', height=0.35)
        Dice5 = SVGMobject(file_name='media/v2_slide4_Dices/Dice5.svg', height=0.35)

        Dice_Group_A = VGroup(Dice1.copy().shift(LEFT*2.5*k+DOWN), 
        Dice2.copy().shift(LEFT*1.5*k+DOWN), 
        Dice3.copy().shift(LEFT*.5*k+DOWN), 
        Dice4.copy().shift(RIGHT*.5*k+DOWN), 
        Dice5.copy().shift(RIGHT*1.5*k+DOWN))

        Dice_Group_B = VGroup(Dice5.copy().shift(LEFT*2.5*k+DOWN), 
        Dice4.copy().shift(LEFT*1.5*k+DOWN), 
        Dice3.copy().shift(LEFT*.5*k+DOWN), 
        Dice2.copy().shift(RIGHT*.5*k+DOWN), 
        Dice1.copy().shift(RIGHT*1.5*k+DOWN))


        Bars_A_Gradient = [ rgb_to_color([0.925,  0.671,  0.757]),
                            rgb_to_color([0.866,  0.615,  0.696]),
                            rgb_to_color([0.806,  0.56,   0.635]),
                            rgb_to_color([0.746,  0.505,  0.574]),
                            rgb_to_color([0.687,  0.449,  0.513]),
                            rgb_to_color([0.627,  0.394,  0.452]),
                            rgb_to_color([0.567,  0.339,  0.391]),
                            rgb_to_color([0.508,  0.283,   0.33]),
                            rgb_to_color([0.448,  0.228,  0.269])]

        Bars_B_Gradient = [ rgb_to_color([0.675,  0.918,  0.843]),
                            rgb_to_color([0.621,  0.864,  0.791]),
                            rgb_to_color([0.567,  0.811,  0.739]),
                            rgb_to_color([0.514,  0.758,  0.686]),
                            rgb_to_color([0.46,   0.705,  0.634]),
                            rgb_to_color([0.407,  0.652,  0.582]),
                            rgb_to_color([0.353,  0.599,  0.529]),
                            rgb_to_color([0.299,  0.546,  0.477]),
                            rgb_to_color([0.246,  0.492,  0.425])]

        Bars_Finale_Gradient = [rgb_to_color([0.792,  0.639,  0.91 ]),
                                rgb_to_color([0.744,  0.596,  0.854]),
                                rgb_to_color([0.696,  0.554,  0.799]),
                                rgb_to_color([0.648,  0.511,  0.743]),
                                rgb_to_color([0.6,    0.468,  0.687]),
                                rgb_to_color([0.552,  0.425,  0.632]),
                                rgb_to_color([0.503,  0.383,  0.576]),
                                rgb_to_color([0.455,  0.34,   0.52 ]),
                                rgb_to_color([0.407,  0.297,  0.465]),
                                rgb_to_color([0.359,  0.254,  0.409]),
                                rgb_to_color([0.311,  0.211,  0.354])]

        Highlight_Color = WHITE


        bars_k = 1.5
        rects_A = []
        rects_B = []

        for iter in range(5):
            rectA = Rectangle(color=Bars_A_Gradient[3+iter], fill_color=Bars_A_Gradient[iter], width=0.3*bars_k, fill_opacity=0.9, height=D_Values[2][iter]*bars_k).shift(UP*bars_k*D_Values[2][iter]/2+iter*RIGHT*(0.3*bars_k+0.15))
            rectB = Rectangle(color=Bars_B_Gradient[3+iter], fill_color=Bars_B_Gradient[iter], width=0.3*bars_k, fill_opacity=0.9, height=D_Values[3][iter]*bars_k).shift(UP*bars_k*D_Values[3][iter]/2+iter*RIGHT*(0.3*bars_k+0.15))

            kostil_stroka_A = D_Values_str_LATEX[2][iter]
            kostil_stroka_B = D_Values_str_LATEX[3][iter]

            textA = MathTex(kostil_stroka_A, tex_to_color_map={kostil_stroka_A: Bars_A_Gradient[-iter-2]}).scale(bars_k*0.3)
            textB = MathTex(kostil_stroka_B, tex_to_color_map={kostil_stroka_B: Bars_B_Gradient[-iter-2]}).scale(bars_k*0.3)


            if str(iter) in '':
                textA.move_to(rectA)
            else:
                textA.move_to(rectA).shift(UP*(bars_k*D_Values[2][iter]/2+0.35))
            if str(iter) in '':
                textB.move_to(rectB)
            else:
                textB.move_to(rectB).shift(UP*(bars_k*D_Values[3][iter]/2+0.35))
            
            rects_A.append([rectA, textA])
            rects_B.append([rectB, textB])

        rects_A_Grouped = [VGroup(*i) for i in rects_A]
        rects_B_Grouped = [VGroup(*i) for i in rects_B]


        Dice_Bars_A = VGroup(*rects_A_Grouped,
            Axes(x_range=[0, 1], y_range=[0, 0.5, 0.5], x_length=2.1*bars_k, y_length=1*bars_k, y_axis_config={'include_numbers': True}, tips=False).shift(bars_k*UP*0.4875 + bars_k*RIGHT*0.8)
        ).shift(bars_k*LEFT*1+bars_k*DOWN*0.5)

        Dice_Bars_B = VGroup(*rects_B_Grouped,
            Axes(x_range=[0, 1], y_range=[0, 0.5, 0.5], x_length=2.1*bars_k, y_length=1*bars_k, y_axis_config={'include_numbers': True}, tips=False).shift(bars_k*UP*0.4875 + bars_k*RIGHT*0.8)
        ).shift(DOWN*bars_k*0.5+bars_k*LEFT*1)


        """Dice_Graph_A_Labels = Dice_Graph_A.get_axis_labels(
            Tex("Value", color=GRAY_A).scale(0.7), 
                        Tex("Probability", color=GRAY_A).scale(0.7)
        )

        Dice_Graph_B_Labels = Dice_Graph_B.get_axis_labels(
            Tex("Value", color=GRAY_A).scale(0.7), 
                        Tex("Probability", color=GRAY_A).scale(0.7)
        )"""

        group_A = VGroup(Dice_Group_A, Dice_Bars_A,).scale(0.8).shift(UP*2)#.rotate((math.pi))
        group_B = VGroup(Dice_Group_B, Dice_Bars_B,).scale(0.8).shift(LEFT*1.925+LEFT*0.5)

        #self.play(Create(group_A), Create(group_B))
        #self.wait(1)

        self.add(group_A, group_B) #DEBUG
        #self.play(Create(group_A), Create(group_B)) #ACTUAL

        for iter in range(9):
            
            self.play(group_B.animate.shift((0.321*bars_k)*RIGHT))

            self.wait(0.1)

            indexes = [i for i in it.combinations_with_replacement(range(iter + 1), 2) if sum(i) == iter and all(k not in i for k in [5, 6, 7, 8, 9])]
            indexes.extend([i[::-1] for i in indexes.copy() if i != i[::-1]])
            
            height = sum([D_Values[2][idx[0]]*D_Values[3][-idx[1]-1] for idx in indexes])
            bar_result = Rectangle(color=Bars_Finale_Gradient[2+iter], fill_color=Bars_Finale_Gradient[iter], width=0.3*bars_k, fill_opacity=0.9, height=height*bars_k).shift(UP*bars_k*height/2+iter*RIGHT*(0.3*bars_k+0.15)+DOWN*2+LEFT*1.8)
            
            actual_colors = [[rects_A[idx[0]][0].get_color() for idx in indexes], [rects_B[-(idx[1])-1][0].get_color() for idx in indexes]]

            self.play(*[rects_A_Grouped[idx[0]].animate.set_fill(Highlight_Color, 0.9) for idx in indexes], *[rects_B_Grouped[-idx[1]-1].animate.set_fill(Highlight_Color, 0.9) for idx in indexes], run_time=0.2)
            
            self.play(ReplacementTransform(VGroup(*[rects_A_Grouped[idx[0]].copy() for idx in indexes], *[rects_B_Grouped[-idx[1]-1].copy() for idx in indexes]), 
            target_mobject=VGroup(bar_result, MathTex(r'\frac{'+str(Fraction(height).limit_denominator(1000)).split('/')[0]+r'}{'+str(Fraction(height).limit_denominator(1000)).split('/')[1]+r'}', 
            tex_to_color_map={r'\frac{'+str(Fraction(height).limit_denominator(1000)).split('/')[0]+r'}{'+str(Fraction(height).limit_denominator(1000)).split('/')[1]+r'}': Bars_Finale_Gradient[2]}).scale(0.35*bars_k).move_to(bar_result).shift(UP*(height/2+0.4)))))

            self.play(*[rects_A_Grouped[indexes[idx][0]].animate.set_fill(actual_colors[0][idx], 0.9) for idx in range(len(indexes))], *[rects_B_Grouped[-indexes[idx][1]-1].animate.set_fill(actual_colors[1][idx], 0.9) for idx in range(len(indexes))], run_time=0.2)

            self.wait(0.2)


        self.play(group_B.animate.shift(2*(0.321*bars_k)*RIGHT+UP*2), Create(Rectangle(width=8, height=2.75).shift(DOWN*0.5+RIGHT*0.75).shift(0.9*DOWN+LEFT*2.6).shift(RIGHT*2.2)), 
        Create(Axes(x_range=[1, 11, 1], y_range=[0, 0.5, 0.5], x_length=4*bars_k, y_length=1.1*bars_k, 
        axis_config={'include_numbers': True, 'exclude_origin_tick': True, 'numbers_to_exclude': [1, 11]}, tips=False).shift(1.18*DOWN+LEFT*1.58).shift(RIGHT*2.2)))
        
        self.wait(1)            
        #end

class v2_slide9_convolution_demo_lists(Scene): #DONE #V2
    def construct(self):
        self.camera.background_color = '#1e1e1e'

        expression_Left_1 = [
            MathTex(r'\{', tex_to_color_map={r'\{': WHITE}),
            MathTex(r'1', tex_to_color_map={r'1': WHITE}),
            MathTex(r', ', tex_to_color_map={r', ': WHITE}).shift(DOWN*0.25+LEFT*0.07),
            MathTex(r'2', tex_to_color_map={r'2': WHITE}),
            MathTex(r', ', tex_to_color_map={r', ': WHITE}).shift(DOWN*0.25+LEFT*0.07),
            MathTex(r'3', tex_to_color_map={r'3': WHITE}),
            MathTex(r'\}', tex_to_color_map={r'\}': WHITE})
        ]

        expression_Left_2 = [
            MathTex(r'\{', tex_to_color_map={r'\{': WHITE}),
            MathTex(r'4', tex_to_color_map={r'4': WHITE}),
            MathTex(r', ', tex_to_color_map={r', ': WHITE}).shift(DOWN*0.25+LEFT*0.07),
            MathTex(r'5', tex_to_color_map={r'5': WHITE}),
            MathTex(r', ', tex_to_color_map={r', ': WHITE}).shift(DOWN*0.25+LEFT*0.07),
            MathTex(r'6', tex_to_color_map={r'6': WHITE}),
            MathTex(r'\}', tex_to_color_map={r'\}': WHITE})
        ]

        expression_Right = [
            MathTex(r'\{', tex_to_color_map={r'\{': WHITE}),
            MathTex(r'4', tex_to_color_map={r'4': WHITE}),
            MathTex(r', ', tex_to_color_map={r', ': WHITE}).shift(DOWN*0.25+LEFT*0.07),
            MathTex(r'13', tex_to_color_map={r'13': WHITE}),
            MathTex(r', ', tex_to_color_map={r', ': WHITE}).shift(DOWN*0.25+LEFT*0.07),
            MathTex(r'28', tex_to_color_map={r'28': WHITE}),
            MathTex(r', ', tex_to_color_map={r', ': WHITE}).shift(DOWN*0.25+LEFT*0.07),
            MathTex(r'27', tex_to_color_map={r'27': WHITE}),
            MathTex(r', ', tex_to_color_map={r', ': WHITE}).shift(DOWN*0.25+LEFT*0.07),
            MathTex(r'18', tex_to_color_map={r'18': WHITE}),
            MathTex(r'\}', tex_to_color_map={r'\}': WHITE})
        ]

        start_group = VGroup(
            *[expression_Left_1[i].copy().shift(LEFT*2.5+RIGHT*i*0.3) for i in range(len(expression_Left_1))], 
            MathTex(r' \ast ', tex_to_color_map={r' \ast ': WHITE}).shift(LEFT*0.35), 
            *[expression_Left_2[i].copy().shift(RIGHT*i*0.3) for i in range(len(expression_Left_2))]
        )

        self.add(start_group)

        self.wait(0.5)

        anim_list_L = [ *[expression_Left_1[i].copy().shift(LEFT*1.05+RIGHT*i*0.3) for i in range(len(expression_Left_1))] ]

        anim_list_R = [ 
            expression_Left_2[0].copy().shift(LEFT*2.89+RIGHT*0*0.3+DOWN*0.7), 
            expression_Left_2[5].copy().shift(LEFT*2.89+RIGHT*1*0.3+DOWN*0.7),
            expression_Left_2[4].copy().shift(LEFT*2.89+RIGHT*4*0.3+DOWN*0.7),
            expression_Left_2[3].copy().shift(LEFT*2.89+RIGHT*3*0.3+DOWN*0.7),
            expression_Left_2[2].copy().shift(LEFT*2.89+RIGHT*2*0.3+DOWN*0.7),
            expression_Left_2[1].copy().shift(LEFT*2.89+RIGHT*5*0.3+DOWN*0.7),
            expression_Left_2[6].copy().shift(LEFT*2.89+RIGHT*6*0.3+DOWN*0.7)
        ]

        anim_group_L = VGroup(*anim_list_L)
        anim_group_R = VGroup(*anim_list_R)

        self.play(ReplacementTransform(start_group, VGroup(anim_group_L, anim_group_R)))

        anim_Finale = []

        for iter in range(5):
                    
            indexes = [i for i in it.combinations_with_replacement(range(iter + 1), 2) if sum(i) == iter and all(k not in i for k in [3, 4, 5, 6, 7, 8, 9])]
            indexes.extend([i[::-1] for i in indexes.copy() if i != i[::-1]])

            self.play(anim_group_R.animate.shift(0.6*RIGHT))

            if iter == 0:
                target = VGroup(expression_Right[0].copy().shift(LEFT*(1+iter)*0.3), expression_Right[1].copy(), expression_Right[2].copy().shift(RIGHT*(1+iter)*0.3)).shift(DOWN*2+LEFT*1.8)

            elif iter == 4:
                target = VGroup(expression_Right[-2].copy().shift(RIGHT*2*iter*0.4), expression_Right[-1].copy().shift(RIGHT*(2*iter+1)*0.4)).shift(DOWN*2+LEFT*1.8)
            
            else:
                target=VGroup(expression_Right[1+2*iter].copy().shift(RIGHT*2*iter*0.4), expression_Right[2+2*iter].copy().shift(RIGHT*(2*iter+1)*0.4)).shift(DOWN*2+LEFT*1.8)
            
            iter_list = [[*[anim_list_L[1+2*i[0]].copy() for i in indexes]], [*[anim_list_R[-(1+2*i[1])-1].copy() for i in indexes]]]

            kostil_stroka = ' + '.join([''.join([iter_list[0][i].get_tex_string() + r' \cdot ' + iter_list[1][i].get_tex_string()]) for i in range(len(indexes))])
            
            anim_mid_obj = MathTex(kostil_stroka, tex_to_color_map={kostil_stroka: WHITE}).shift(UP)

            anim_Finale.append(target)
            
            self.play(ReplacementTransform(VGroup(*[anim_list_L[1+2*i[0]].copy() for i in indexes], *[anim_list_R[-(1+2*i[1])-1].copy() for i in indexes]), 
            target_mobject=anim_mid_obj))

            self.wait(0.5*len(indexes))

            self.play(ReplacementTransform(anim_mid_obj, target_mobject=target))
        
        self.play(FadeOut(VGroup(anim_group_L, anim_group_R), shift=UP*0.5), VGroup(*anim_Finale).animate.shift(UP*2))

        self.wait(0.5)
        #end

class v2_slide16_center_mu(Scene): #DONE #V2
    def construct(self):

        self.camera.background_color = '#1e1e1e'

        D_Values = [2/37, 1/37, 4/37, 9/37, 21/37]

        k = 2/3
        Dice1 = SVGMobject(file_name='media/v2_slide4_Dices/Dice1.svg', height=0.35).shift(LEFT*2.5*k+DOWN)
        Dice2 = SVGMobject(file_name='media/v2_slide4_Dices/Dice2.svg', height=0.35).shift(LEFT*1.5*k+DOWN)
        Dice3 = SVGMobject(file_name='media/v2_slide4_Dices/Dice3.svg', height=0.35).shift(LEFT*.5*k+DOWN)
        Dice4 = SVGMobject(file_name='media/v2_slide4_Dices/Dice4.svg', height=0.35).shift(RIGHT*.5*k+DOWN)
        Dice5 = SVGMobject(file_name='media/v2_slide4_Dices/Dice5.svg', height=0.35).shift(RIGHT*1.5*k+DOWN)
        Dice_Group_1 = VGroup(Dice1.copy(), Dice2.copy(), Dice3.copy(), Dice4.copy(), Dice5.copy()).shift(DOWN*0.3)


        mu_value = sum(D_Values[i]*(i+1) for i in range(0, 5))

        Dotted_line = DashedLine(start=(0, 2, 0), end=(0, -2, 0), color=PURPLE_C, stroke_width=3).shift(LEFT*2+RIGHT*mu_value*2/3)
    
        Mu_text = MathTex(r'\mu_1').scale(0.7).next_to(Dotted_line, DOWN)

        Uptext = MathTex(r'\mu_1 = a_1+2a_2+3a_3+4a_4+5a_5').scale(0.7).shift(UP*3)


        Axes1 = Axes(x_range=(0, 6, 1), y_range=(0, 0.7, 0.5), x_length=4, y_length=2.8,
        tips=False, y_axis_config={"include_numbers":True}).shift(UP*0.4)

        Axes2_1 = NumberLine(x_range=[0, 6, 1], length=4, 
                include_tip=False, include_numbers=True, numbers_to_exclude=[6]).shift(DOWN)
        Axes2_2 = NumberLine(x_range=[0, 0.7, 0.5], length=2.8, rotation=90*DEGREES,
                include_tip=False, include_numbers=True, label_direction=LEFT, numbers_to_exclude=[0]).shift(LEFT*2+UP*0.4)
        

        bars_colors = [YELLOW_E, '#EECA30', YELLOW_D, '#FADC5A', '#FFEE6F', '#FFFF84']
        
        bars = [Rectangle(color=bars_colors[i], height=4*D_Values[i], width=2/3).set_fill(color=bars_colors[i], opacity=0.9).shift(RIGHT*i*2/3+UP*2*D_Values[i]) for i in range(5)]
        
        Bars = VGroup(*bars).shift(LEFT*(2-1/3-0.02)+DOWN*0.98)

        #bars_a_i_gradient = [YELLOW_E, '#EECA30', YELLOW_D, '#FADC5A', '#FFEE6F', '#FFFF84'].reverse()

        kostil_stroki = [r'a_'+f'{i+1}' for i in range(5)]

        bars_a_i_list = [MathTex(kostil_stroki[i]).next_to(bars[i], UP*0.5) for i in range(3)] + [MathTex(kostil_stroki[i]).move_to(bars[i]) for i in range(3, 5)]

        Bars_a_i = VGroup(*bars_a_i_list)


        self.play(Create(VGroup(Axes1, Bars, Dice_Group_1, Bars_a_i)))

        self.wait(1)

        self.play(FadeOut(Dice_Group_1, Axes1), FadeIn(Axes2_1, Axes2_2))

        self.wait(1)

        self.play(Create(VGroup(Dotted_line, Mu_text, Uptext)))

        self.wait(1)

        dict_values = {0:MathTex(r'-\mu_1').scale(0.5), 1:MathTex(r'1-\mu_1').scale(0.5), 2:MathTex(r'2-\mu_1').scale(0.5), 3:MathTex(r'3-\mu_1').scale(0.5), 4:MathTex(r'4-\mu_1').scale(0.5), 5:MathTex(r'5-\mu_1').scale(0.5)}

        self.play(
            Axes2_2.animate.shift(RIGHT*mu_value*2/3),
            Axes2_1.animate._original__init__(x_range=[0, 6, 1], length=4, include_tip=False, include_numbers=False).shift(DOWN).add_labels(dict_values=dict_values, direction=DOWN, font_size=24, buff=0.2),
            Mu_text.animate._original__init__(r'\mu_2=0').scale(0.7).next_to(Dotted_line, DOWN),
            Create(MathTex(r'\mu_2 = 0').scale(0.7).next_to(Uptext, DOWN).shift(LEFT*2))
        )

        self.wait(1)
        #end #наконецтоблять