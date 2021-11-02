from manim import *

class Two(ThreeDScene):
    def construct(self):
        #right = Text("Mr. Dybdhal")
        #self.add_fixed_in_frame_mobjects(right)
        #right.to_edge(UL).scale(0.6)

        self.set_camera_orientation(phi=0, theta=-90 * DEGREES)

        axes3 = ThreeDAxes(
            x_range=[0, 3, 1],
            x_length=4,
            y_range=[0, 7, 1],
            y_length=4,
            z_range=[-4, 4, 1],
            z_length=5,
        ).add_coordinates([0, 2], [0, 7])
        axis_labels = always_redraw(lambda: axes3.get_axis_labels(
            x_label="x", y_label="f(x)=x^{2}"))

        graph = always_redraw(lambda: axes3.get_graph(
            lambda x: x**2, x_range=[0, 2], color=GREEN_C))

        angle = ValueTracker(0)
        surface = always_redraw(
            lambda: ParametricSurface(
                lambda u, v: axes3.c2p(
                    v, v ** 2 * np.cos(u), v ** 2 * np.sin(u)
                ),
                u_range=[0, angle.get_value()],
                v_range=[0, 2],
                checkerboard_colors=[BLUE_B, BLUE_D],
            )
        )
        area = always_redraw(lambda: axes3.get_riemann_rectangles(
            graph=graph, x_range=[0, 2], dx=0.2))
        a = always_redraw(lambda: axes3.get_area(graph=graph, x_range=[
            0, 2], color=[GREEN_C], opacity=0.7))

        rect = Rectangle(color=GREEN_C, height=2, width=0.4).shift(
            RIGHT*2).shift(UP*1.5)
        rect_width = always_redraw(lambda: Tex(
            "{dx}").next_to(rect.get_bottom(), DOWN, buff=0.2))

        rect_height = always_redraw(lambda: MathTex(
            "x^{2}").next_to(rect.get_right(), buff=0.2))
        test = always_redraw(lambda: ParametricSurface(
            lambda u, v: axes3.c2p(
                v, np.cos(u), np.sin(u)),
            u_range=[0, 2*PI],
            v_range=[1, 1.2],
            color=GREEN_C,
            fill_color=GREEN_C,
            fill_opacity=1)
        )
        # disks = getCylinders(axes3, x_min=1.8, x_max=2, dx=0.2)

        self.add(axes3, axis_labels, surface, graph, a)
        self.play(FadeOut(surface), FadeOut(a))
        self.wait()
        self.play(Create(area))
        self.play(axes3.animate.shift(LEFT*3.4))
        self.wait()
        self.play(ReplacementTransform(area.copy(), rect))
        self.play(Write(rect_width), Write(rect_height))

        # self.play(FadeOut(area))
        self.move_camera(phi=60*DEGREES)
        self.wait()
        self.begin_ambient_camera_rotation(rate=0.05, about="theta")
        self.play(
            Rotating(
                VGroup(graph, area),
                axis=RIGHT,
                radians=2*PI,
                about_point=axes3.c2p(0, 0, 0),
                rate_func=linear,
                run_time=5,
            ),
            Create(test),
            run_time=5,
            rate_func=linear,
        )
        self.wait()
        self.stop_ambient_camera_rotation(about="theta")
        self.wait()
        # self.move_camera(phi=0, theta=-89 * DEGREES)

        self.play(angle.animate.set_value(2*PI))