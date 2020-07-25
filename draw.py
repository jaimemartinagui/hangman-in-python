"""Module that uses the turtle library to draw the hangman."""

import turtle


class DrawHangMan():
    """Class for drawing functionalities."""
    
    def draw_hangman(self, t, lives):
        """Function that draws the hangman by parts."""

        if lives <= 6:
            self._draw_gallow(t)
            self._draw_head(t)
        if lives <= 5:
            t.fd(20)
        if lives <= 4:
            t.rt(45)
            t.fd(60)
        if lives <= 3:
            t.rt(180)
            t.fd(60)
            t.rt(90)
            t.fd(60)
        if lives <= 2:
            t.rt(180)
            t.fd(60)
            t.lt(135)
            t.fd(50)
        if lives <= 1:
            t.rt(30)
            t.fd(70)
        if lives == 0:
            t.rt(180)
            t.fd(70)
            t.rt(120)
            t.fd(70)

    def _draw_gallow(self, t):
        t.fd(60)
        t.rt(180)
        t.fd(30)
        t.rt(90)
        t.fd(220)
        t.rt(90)
        t.fd(70)
        t.rt(90)
        t.fd(30)

    def _draw_head(self, t):
        t.rt(90)
        t.circle(20)
        t.pu()
        t.lt(90)
        t.fd(40)
        t.pd()
