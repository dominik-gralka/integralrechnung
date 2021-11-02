from manim import *
from numpy import square

class Auto(Scene):
    def construct(self):

        ax = Axes(
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
        )

        graph = ax.get_graph(lambda x: 0.3 * x ** 2, x_range=[0,4])
        axis_labels = always_redraw(lambda: ax.get_axis_labels(
            x_label="t", y_label="v"))

        area = ax.get_area(graph, opacity=0.8, x_range=(0,3))

        graph_group = VGroup(ax, graph, axis_labels)

        eq = MathTex("I=\int_{0}^{3}0,3x^{2} dx=[F(x)]_","{0}^{3}").to_corner(LEFT, buff=1)
        eq2 = MathTex("F(3)-F(0)")
        eq3 = MathTex("F(3)-F(0)=","2,7cm")

        dot1 = Dot(ax.input_to_graph_point(0, graph), color=YELLOW)
        dot2 = Dot(ax.input_to_graph_point(1, graph), color=YELLOW)
        dot3 = Dot(ax.input_to_graph_point(2, graph), color=YELLOW)

        dots = VGroup(dot1, dot2, dot3)

        self.play(Create(ax), Write(axis_labels))
        self.play(Create(graph))
        self.wait(18)
        self.play(FadeIn(area))
        self.play(FadeOut(area))
        self.wait(4)
        self.play(graph_group.animate.scale(0.8), run_time=0.5)
        self.play(graph_group.animate.to_corner(RIGHT, buff=2), Write(eq))
        self.wait()
        self.play(eq.animate.shift(UP))

        eq2.next_to(eq, DOWN, buff=1)
        eq3.next_to(eq, DOWN, buff=1)
        rect1 = SurroundingRectangle(eq3[1], buff=.1)

        self.play(Write(eq2))
        self.wait()
        self.play(ReplacementTransform(eq2, eq3))
        self.wait()
        self.play(Create(rect1))
        self.play(Uncreate(rect1))
        self.wait(3)

        group = VGroup(eq, eq3, ax, axis_labels, graph)

        square = Square()
        square.set_fill(BLUE, opacity=0.5)

        triangle = Triangle().to_corner(LEFT, buff=2.5)
        triangle.set_fill(GREEN, opacity=0.5).set_stroke(GREEN_A).scale(1.3).shift(DOWN*0.2)

        circle = Circle().to_corner(RIGHT, buff=2.5)
        circle.set_fill(PINK, opacity=0.5)

        shapes = VGroup(square, triangle, circle)
        integral = MathTex("\int_")
        integral2 = Tex("Integralrechnung")

        self.play(ReplacementTransform(group, shapes))
        self.wait()
        self.play(square.animate.rotate(PI/2), triangle.animate.rotate(PI/2), circle.animate.rotate(PI/2))
        self.play(ReplacementTransform(shapes, integral))
        self.wait()
        self.play(FadeOut(integral), Write(integral2))
        self.wait(6)
        self.play(Unwrite(integral2))
        self.wait()