from manim import *
from manim.utils import scale


class Count(Animation):
    def __init__(self, number: DecimalNumber, start: float, end: float, **kwargs) -> None:
        # Pass number as the mobject of the animation
        super().__init__(number,  **kwargs)
        # Set start and end
        self.start = start
        self.end = end

    def interpolate_mobject(self, alpha: float) -> None:
        # Set value of DecimalNumber according to alpha
        value = self.start + (alpha * (self.end - self.start))
        self.mobject.set_value(value)

class Konstante(Scene):
    def construct(self):

        eq1 = MathTex("f(x)=5").shift(RIGHT*1.25)
        eq2 = MathTex("F(x)= 5x + ").shift(DOWN + RIGHT*1.5)

        number = DecimalNumber(num_decimal_places=0).set_color(WHITE).next_to(eq2, RIGHT)
        number.add_updater(lambda number: number)

        #x_var = Variable(start, 'x', num_decimal_places=0).next_to(eq2, RIGHT)

        #self.add(x_var)
        #self.play(x_var.tracker.animate.set_value(360), run_time=2, rate_func=linear)
        #self.wait(0.1)

        konstante = Tex("k").scale(5)
        definitionsbereich = MathTex("\mathbb{D}_F : k \in \mathbb{R}").to_corner(LEFT + DOWN, buff=1.5)

        eq_group = VGroup(eq1, eq2, number).shift(UP*0.5)

        group = VGroup(konstante, definitionsbereich, eq_group)

        self.play(Write(konstante, run_time=2))
        self.wait()
        self.play(konstante.animate.to_corner(LEFT, buff=2))
        self.wait(1)
        self.play(Write(eq1))
        self.wait(4)
        self.play(Write(eq2), Write(number))
        self.play(Count(number, 0, 10), run_time=1, rate_func=linear)
        self.wait()
        self.play(Count(number, 10, 17), run_time=1, rate_func=linear)
        self.wait(3)
        self.play(Write(definitionsbereich))
        self.wait(10)
        self.play(Unwrite(group))
        self.wait()

        