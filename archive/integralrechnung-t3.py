from os import waitpid
from typing_extensions import runtime
from manim import *

class Integralrechnung(Scene):
    def construct(self):

        # Beginning Scene 1

        ax = Axes(
            x_range=[-5, 5],
            y_range=[-5, 5],
            x_length=8,
            y_length=8,
            axis_config={"color": WHITE},
        )

        aufleiten = Text("Aufleiten")

        graph = ax.get_graph(lambda x: 5 * x** 2, color=WHITE,x_range=[-1,1])

        plane = VGroup(ax, graph)
        plane.scale(0.5).to_corner(UP, buff=0.8)

        intro=Text("Integralrechnung")
        eq1 = MathTex(
            "f(x)=", "5", "x^", "{2}"
            )
        eq2 = MathTex(
            "f(x)=", "5", "x^", "{2+1}"
        )
        eq3 = MathTex(
            "f(x)=", "5", "x^", "{3}"
        )
        eq3.set_color_by_tex("{3}", color=YELLOW)
        eq4 = MathTex(
            "f(x)=", "\\frac{5}{3}", "x^", "{3}"
        )
        eq4.set_color_by_tex("^{3}", color=YELLOW)

        eq4_lab = Text("Durch die neue Hochzahl teilen").next_to(eq4, DOWN*2, buff=0.2).set_color(YELLOW).scale(0.5)

        eq5 = MathTex(
            "F(x)=", "\\frac{5}{3}", "x^", "{3} + k"
        )

        eq_group = VGroup(eq1, eq2, eq3, eq4, eq4_lab, eq5)
        eq_group.to_corner(DOWN, buff=0.8)

        framebox1 = SurroundingRectangle(eq3[1], buff=.1)
        framebox2 = SurroundingRectangle(eq1[3], buff=.1)
        framebox3 = SurroundingRectangle(eq5, buff=.3)

        scene_1= VGroup(plane, eq_group)

        self.play(Write(intro))
        self.wait(7)
        self.play(Transform(intro, Text("Stammfunktion bilden")))
        self.wait()
        self.play(FadeIn(aufleiten.to_corner(LEFT + UP, buff=0.8)))
        self.play(ReplacementTransform(intro, eq1))
        self.play(Write(ax, run_time=2))
        self.play(Create(graph))
        self.play(Create(framebox2))
        self.wait()
        self.play(ReplacementTransform(eq1, eq2), Transform(framebox2, SurroundingRectangle(eq2[3], buff=.1)), Transform(graph, ax.get_graph(lambda x: 5 * x** 3, color=WHITE,x_range=[-1,1])))
        self.wait(2)
        self.play(Uncreate(framebox2))
        self.play(ReplacementTransform(eq2, eq3))
        self.play(Create(framebox1))
        self.wait(2)
        self.play(Write(eq4_lab, run_time=1))
        self.play(ReplacementTransform(eq3, eq4), Transform(framebox1, SurroundingRectangle(eq4[1], buff=.1)), Transform(graph, ax.get_graph(lambda x: 5/3 * x** 3, color=WHITE,x_range=[-1.45,1.45])))
        self.play(Uncreate(framebox1))
        self.wait(2)
        self.play(Unwrite(eq4_lab, run_time=1), ReplacementTransform(eq4, eq5), Create(framebox3))
        self.wait(2)
        self.play(Uncreate(plane), Uncreate(eq5), Uncreate(framebox3), Uncreate(aufleiten), Uncreate(graph))
        self.wait()

        # Beginning Scene 2

        integrieren = Text("Integrieren")

        ax2 = Axes(
            x_range=[0, 5],
            y_range=[0, 5],
            x_length=5,
            y_length=5,
            axis_config={"color": WHITE},
            x_axis_config={
                "numbers_to_include": np.arange(0,5),
            },
            y_axis_config={
                "numbers_to_include": np.arange(0,5),
            },
        ).to_corner(RIGHT, buff=2)

        graph2 = ax2.get_graph(lambda x: 0.75 * x, x_range=[0,4])

        #dot_1 = Dot(ax2.i2gp(graph2.t_min, graph2))
        #dot_2 = Dot(ax2.i2gp(graph2.t_max, graph2))

        graph2_lab = MathTex("f(x)=0,75x").scale(0.8).to_corner(LEFT, buff=2)
        graph2_lab2 = MathTex("f(x)=\int_{1}^{3}", "0,75x", "\,dx").next_to(graph2_lab, DOWN, buff=0.8)
        graph2_lab2.set_color_by_tex("0,75x", YELLOW)

        graph_group = VGroup(graph2_lab, graph2_lab2)


        self.play(Create(ax2))
        self.play(Create(graph2, run_time=2), Create(graph2_lab))
        self.wait()
        self.play(Create(graph2_lab2), graph_group.animate.shift(UP))

        #rectangle = ax2.get_riemann_rectangles(
        #    graph=graph2,
        #    x_range=[0,3],
        #    dx=1,
        #    show_signed_area=False,
        #    color=(BLUE, GREEN),
        #    fill_opacity=1
        #)
#
        #i = 1
#
        #while i > 0.1:
        #    self.play(Transform(
        #        rectangle,
        #    rectangle = ax2.get_riemann_rectangles(
        #        graph=graph2,
        #        x_range=[0,3],
        #        dx=i-0.1,
        #        show_signed_area=False,
        #        color=(BLUE, GREEN),
        #        fill_opacity=1
        #    ),
        #))
        #i = i-0.5