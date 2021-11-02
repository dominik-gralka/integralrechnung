from typing_extensions import runtime
from manim import *
import numpy as np

class GraphAreaPlot(Scene):
    def construct(self):

        ax = Axes(
            x_range=[0, 4],
            y_range=[0, 6],
            x_axis_config={
                "numbers_to_include": np.arange(0,5),
            },
            y_axis_config={
                "numbers_to_include": np.arange(0,6),
            },
            tips=False,
        )

        labels = ax.get_axis_labels()

        curve_1 = ax.get_graph(lambda x: 4 * x - x ** 2, x_range=[0, 4], color=BLUE_C)
        rectangle = ax.get_riemann_rectangles(
            graph=curve_1,
            x_range=[1,2],
            dx=1,
            show_signed_area=False,
            color=(MAROON_A, RED_B, PURPLE_D),
        )
        #line_1 = ax.get_vertical_line(ax.input_to_graph_point(2, curve_1), color=YELLOW)
        #line_2 = ax.get_vertical_line(ax.i2gp(3, curve_1), color=YELLOW)

        self.play(FadeIn(ax, labels))
        self.play(Create(curve_1, runtime=4))
        self.wait()
        self.wait()