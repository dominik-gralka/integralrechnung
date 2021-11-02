from manim import *

class Intro(Scene):
    def construct(self):
        
        integralrechnung = Tex("Integralrechnung")

        ax = Axes(
            x_range=[0, 5.5],
            y_range=[0, 6],
            x_axis_config={
                "numbers_to_include": np.arange(0,6),
            },
            y_axis_config={
                "numbers_to_include": np.arange(0,6),
            },
            tips=False,
        )
        graph = ax.get_graph(lambda x: 0.1 * (x - 2) ** 3 + 1)
        area = ax.get_area(graph, opacity=0.8)

        group = VGroup(ax, graph, area)

        self.play(Write(integralrechnung))
        self.wait(6) # 00:07
        self.play(ReplacementTransform(integralrechnung, graph), Write(ax), FadeIn(area))
        self.wait(10)
        self.play(Transform(group, Text("Stammfunktion bilden")))
        