from manim import *

class Aufleiten(Scene):
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

            intro=Text("Stammfunktion bilden")
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

            self.add(intro)
            self.wait()
            self.play(FadeIn(aufleiten.to_corner(LEFT + UP, buff=0.8)))
            self.play(ReplacementTransform(intro, eq1))
            self.play(Write(ax, run_time=2))
            self.play(Create(graph))
            self.play(Create(framebox2))
            self.wait()
            self.play(ReplacementTransform(eq1, eq2), Transform(framebox2, SurroundingRectangle(eq2[3], buff=.1)), Transform(graph, ax.get_graph(lambda x: 5 * x** 3, color=WHITE,x_range=[-1,1])))
            self.wait()
            self.play(ReplacementTransform(eq2, eq4), Transform(framebox2, SurroundingRectangle(eq4[1], buff=.1)), Transform(graph, ax.get_graph(lambda x: 5/3 * x** 3, color=WHITE,x_range=[-1.45,1.45])), Write(eq4_lab, run_time=1))
            self.wait(2)
            self.play(Uncreate(framebox2), Unwrite(eq4_lab, run_time=1), ReplacementTransform(eq4, eq5), Create(framebox3))
            self.wait(10)
            self.play(Uncreate(plane), Uncreate(eq5), Uncreate(framebox3), Uncreate(aufleiten), Uncreate(graph))
            self.wait()