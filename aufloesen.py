from manim import *

class Aufloesen(Scene):
    def construct(self):

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

        graph2_area = ax2.get_area(graph2, opacity=0.5, x_range=(1,4))

        graph_group = VGroup(ax2, graph2, graph2_area)

        area = Tex("Flächeninhalt: ","5,625cm").to_corner(LEFT, buff=1).scale(1)
        area[1].set_color(YELLOW)

        leibniz = MathTex("I=\int_{1}^{4}0,75x dx=[F(x)]_","{1}^{4}")
        leibniz2 = MathTex("F(","4",")-F(","1",")").shift(DOWN)
        leibniz3 = MathTex("F(","4",")-F(","1",")=\\frac{45}{8}=","5,625").shift(DOWN)
        leibniz2[1].set_color(YELLOW)
        leibniz2[3].set_color(YELLOW)
        leibniz3[1].set_color(YELLOW)
        leibniz3[3].set_color(YELLOW)

        rect1 = SurroundingRectangle(leibniz3[5], buff=.1)
        rect2 = SurroundingRectangle(leibniz2[1], buff=.1)
        rect3 = SurroundingRectangle(leibniz2[3], buff=.1)

        leibniz_group = VGroup(leibniz2, rect1, leibniz)

        self.play(Write(leibniz))
        self.wait()
        self.play(leibniz.animate.shift(UP))
        self.play(leibniz[1].animate.set_color(YELLOW))
        self.play(Write(leibniz2))
        self.wait(2)
        self.play(Create(rect2))
        self.wait()
        self.play(ReplacementTransform(rect2, rect3))
        self.wait(3)
        self.play(Uncreate(rect3))
        self.play(Transform(leibniz2, leibniz3))
        self.play(Create(rect1))
        self.wait(2)
        self.play(ReplacementTransform(leibniz_group, graph_group), Write(area))
        self.wait(6)
        self.play(Uncreate(leibniz_group), Uncreate(graph_group), FadeOut(area))
        self.wait()