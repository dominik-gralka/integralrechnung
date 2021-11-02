from manim import *
from manim.utils import scale

class Linear(Scene):
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

        graph2_area = ax2.get_area(graph2, opacity=0.5)

        #dot_1 = Dot(ax2.i2gp(graph2.t_min, graph2))
        #dot_2 = Dot(ax2.i2gp(graph2.t_max, graph2))

        graph2_lab = MathTex("f(x)=0,75x").scale(0.8).to_corner(LEFT, buff=2)
        graph2_lab2 = MathTex("f(x)=\int_{1}^{3}", "0,75x", "\,dx").next_to(graph2_lab, DOWN, buff=0.8)
        graph2_lab2.set_color_by_tex("0,75x", YELLOW)

        line_1 = ax2.get_vertical_line(ax2.input_to_graph_point(1, graph2), color=YELLOW)
        line_2 = ax2.get_vertical_line(ax2.input_to_graph_point(4, graph2), color=YELLOW)

        lines = VGroup(line_1, line_2)

        riemann = ax2.get_riemann_rectangles(graph=graph2, dx=1, color=BLUE, fill_opacity=0.5, x_range=(1,4))
        riemann2 = ax2.get_riemann_rectangles(graph=graph2, dx=0.5, color=BLUE, fill_opacity=0.5, x_range=(1,4))

        flaeche = MathTex("A=(0,75*1)+(1,5*1)+(2,25*1)").next_to(graph2_lab, DOWN).scale(0.5)
        flaeche2 = MathTex("A=4,5cm").next_to(graph2_lab, DOWN).scale(0.8)
        flaeche3 = MathTex("A=5,25cm").next_to(graph2_lab, DOWN).scale(0.8)

        graph_group = VGroup(graph2_lab, flaeche)

        dot1 = Dot(ax2.c2p(1,1.2,0))
        dot2 = Dot(ax2.c2p(2,1.2,0))
        dot3 = Dot(ax2.c2p(1.5,1.2,0))
        line_3 = Line(dot1.get_center(), dot2.get_center())
        line_4 = Line(dot1.get_center(), dot3.get_center())
        brace1 = Brace(line_3, color=YELLOW).rotate(PI).set_stroke(width=2)
        brace1_text = brace1.get_tex("dx").set_color(YELLOW).set_stroke(width=2).shift(UP*0.5)
        brace2 = Brace(line_4, color=YELLOW).rotate(PI).set_stroke(width=2)
        brace2_text = brace2.get_tex("dx").set_color(YELLOW).set_stroke(width=2).shift(UP*0.5)

        group = VGroup(ax2, graph2, lines, graph_group, brace1, riemann, brace1_text)

        dx = MathTex("\lim_{dx\\to\infty}").scale(2)

        leibniz = MathTex("I=\int_","{x_1}","^{x_2}","f(x)","dx")
        #leibniz[1].set_color(YELLOW)
        lrec1 = SurroundingRectangle(leibniz[2], buff=.1)
        lrec2 = SurroundingRectangle(leibniz[1], buff=.1)
        lrec3 = SurroundingRectangle(leibniz[3], buff=.1)
        lrec4 = SurroundingRectangle(leibniz[4], buff=.1)
        #leibniz2 = MathTex()

        self.play(Write(ax2))
        self.play(Create(graph2, run_time=2), Create(graph2_lab))
        self.play(FadeIn(graph2_area))
        self.play(FadeOut(graph2_area))
        self.wait(1)
        self.play(Write(lines, run_time=2))
        self.wait(7)
        self.play(Write(riemann))
        self.wait(4)
        self.play(Create(flaeche), graph_group.animate.shift(UP*0.5))
        self.wait()
        self.play(Transform(flaeche, flaeche2))
        self.wait(11)
        self.play(Write(brace1), Write(brace1_text))
        self.wait(7)
        self.play(Transform(riemann, riemann2), Transform(brace1, brace2), Transform(brace1_text, brace2_text), Transform(flaeche, flaeche3))
        self.wait(10)
        self.play(ReplacementTransform(group, dx))
        self.wait(27)
        self.play(ReplacementTransform(dx, leibniz))
        self.wait(3)
        self.play(Create(lrec1))
        self.wait()
        self.play(ReplacementTransform(lrec1, lrec2))
        self.wait(2)
        self.play(ReplacementTransform(lrec2, lrec3))
        self.wait(1)
        self.play(ReplacementTransform(lrec3, lrec4))
        self.play(Unwrite(lrec4))
        self.wait(2)
        self.play(Unwrite(leibniz))
        self.wait()

        #self.play(Create(graph2_lab2), graph_group.animate.shift(UP))