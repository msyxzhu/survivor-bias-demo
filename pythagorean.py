from manim import *

class PythagoreanTheorem(Scene):
    def construct(self):
        # Title
        title = Text("勾股定理", font_size=72, color=WHITE, font="Noto Sans SC")
        subtitle = Text("a² + b² = c²", font_size=48, color=YELLOW)
        subtitle.next_to(title, DOWN, buff=0.5)
        self.play(Write(title), run_time=1)
        self.play(FadeIn(subtitle, shift=UP*0.3), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(subtitle))

        # Draw right triangle
        a_len = 3  # vertical
        b_len = 4  # horizontal
        c_len = 5  # hypotenuse

        A = ORIGIN + LEFT * 2 + DOWN * 1.5
        B = A + RIGHT * b_len
        C = A + UP * a_len

        triangle = Polygon(A, B, C, color=WHITE, stroke_width=3)

        # Labels
        a_label = MathTex("a=3", color=BLUE).next_to(Line(A, C), LEFT, buff=0.3)
        b_label = MathTex("b=4", color=GREEN).next_to(Line(A, B), DOWN, buff=0.3)
        c_label = MathTex("c=5", color=RED).next_to(Line(B, C), RIGHT, buff=0.3).shift(UP*0.5)

        # Right angle mark
        right_angle = RightAngle(Line(A, B), Line(A, C), length=0.3, color=YELLOW)

        self.play(Create(triangle), run_time=1.5)
        self.play(Create(right_angle), run_time=0.5)
        self.play(
            Write(a_label),
            Write(b_label),
            Write(c_label),
            run_time=1
        )
        self.wait(1)

        # Draw squares on each side
        # Square on side a (left side, vertical)
        sq_a = Square(side_length=a_len, color=BLUE, fill_opacity=0.3, fill_color=BLUE)
        sq_a.next_to(Line(A, C), LEFT, buff=0)

        # Square on side b (bottom)
        sq_b = Square(side_length=b_len, color=GREEN, fill_opacity=0.3, fill_color=GREEN)
        sq_b.next_to(Line(A, B), DOWN, buff=0)

        # Square on hypotenuse c
        # Need to rotate it to align with the hypotenuse
        hyp_direction = normalize(B - C)
        hyp_perp = np.array([-hyp_direction[1], hyp_direction[0], 0])
        sq_c_corners = [B, C, C + hyp_perp * c_len, B + hyp_perp * c_len]
        sq_c = Polygon(*sq_c_corners, color=RED, fill_opacity=0.3, fill_color=RED)

        # Area labels
        area_a = MathTex("a^2 = 9", color=BLUE, font_size=36)
        area_a.move_to(sq_a.get_center())
        area_b = MathTex("b^2 = 16", color=GREEN, font_size=36)
        area_b.move_to(sq_b.get_center())
        area_c = MathTex("c^2 = 25", color=RED, font_size=36)
        area_c.move_to(sq_c.get_center())

        # Animate squares appearing
        self.play(DrawBorderThenFill(sq_a), run_time=1)
        self.play(Write(area_a), run_time=0.5)
        self.wait(0.5)

        self.play(DrawBorderThenFill(sq_b), run_time=1)
        self.play(Write(area_b), run_time=0.5)
        self.wait(0.5)

        self.play(DrawBorderThenFill(sq_c), run_time=1)
        self.play(Write(area_c), run_time=0.5)
        self.wait(1)

        # Show the equation
        equation = MathTex("a^2", "+", "b^2", "=", "c^2", font_size=72)
        equation[0].set_color(BLUE)
        equation[2].set_color(GREEN)
        equation[4].set_color(RED)
        equation.to_edge(UP, buff=0.5)

        self.play(Write(equation), run_time=1.5)
        self.wait(0.5)

        # Numerical verification
        num_eq = MathTex("9", "+", "16", "=", "25", font_size=64)
        num_eq[0].set_color(BLUE)
        num_eq[2].set_color(GREEN)
        num_eq[4].set_color(RED)
        num_eq.next_to(equation, DOWN, buff=0.5)

        self.play(TransformFromCopy(area_a, num_eq[0]),
                  Write(num_eq[1]),
                  TransformFromCopy(area_b, num_eq[2]),
                  Write(num_eq[3]),
                  TransformFromCopy(area_c, num_eq[4]),
                  run_time=2)
        self.wait(2)

        # Highlight: the two smaller squares equal the big one
        flash_a = sq_a.copy().set_fill(BLUE, opacity=0.6)
        flash_b = sq_b.copy().set_fill(GREEN, opacity=0.6)
        flash_c = sq_c.copy().set_fill(RED, opacity=0.6)

        self.play(
            flash_a.animate.set_fill(opacity=0.8),
            flash_b.animate.set_fill(opacity=0.8),
            run_time=0.5
        )
        self.play(
            flash_a.animate.set_fill(opacity=0.3),
            flash_b.animate.set_fill(opacity=0.3),
            flash_c.animate.set_fill(opacity=0.8),
            run_time=0.5
        )
        self.play(flash_c.animate.set_fill(opacity=0.3), run_time=0.5)
        self.wait(1)

        # Clean up and show final message
        self.play(*[FadeOut(m) for m in [sq_a, sq_b, sq_c, area_a, area_b, area_c,
                                          flash_a, flash_b, flash_c, num_eq,
                                          triangle, right_angle, a_label, b_label, c_label]])

        # Final text
        final = Text("直角三角形两直角边的平方和\n等于斜边的平方", font_size=48, color=WHITE, font="Noto Sans SC")
        final.next_to(equation, DOWN, buff=1)
        self.play(Write(final), run_time=1.5)
        self.wait(2)

        self.play(FadeOut(equation), FadeOut(final))

        # Ending
        end = Text("勾股定理 · 数学之美", font_size=56, color=YELLOW, font="Noto Sans SC")
        self.play(Write(end), run_time=1)
        self.wait(2)
        self.play(FadeOut(end))
