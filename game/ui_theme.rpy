# Resolution-independent panels: text and controls stay live, not baked into art.
init -10 python:
    class WarmPanel(renpy.Displayable):
        def __init__(self, fill="#211a15ed", border="#a6885666", **kwargs):
            super(WarmPanel, self).__init__(**kwargs)
            self.fill = fill
            self.border = border

        def render(self, width, height, st, at):
            width, height = max(1, int(width)), max(1, int(height))
            result = renpy.Render(width, height)
            canvas = result.canvas()
            canvas.rect(self.fill, (0, 0, width, height))
            if width > 20 and height > 20:
                canvas.rect(self.border, (1, 1, width - 2, height - 2), 1)
                for x, sx in ((7, 1), (width - 8, -1)):
                    for y, sy in ((7, 1), (height - 8, -1)):
                        canvas.line(self.border, (x, y), (x + sx * 16, y), 1)
                        canvas.line(self.border, (x, y), (x, y + sy * 16), 1)
            return result

    def ui_panel(fill="#211a15ed", border="#a6885666"):
        return WarmPanel(fill, border)

    class MapPin(renpy.Displayable):
        def __init__(self, locked=False, selected=False, **kwargs):
            super(MapPin, self).__init__(**kwargs)
            self.locked = locked
            self.selected = selected

        def render(self, width, height, st, at):
            result = renpy.Render(52, 64)
            canvas = result.canvas()
            edge = "#958775" if self.locked else "#edc781"
            fill = "#554a3d" if self.locked else ("#a77c38" if self.selected else "#3b2c1c")
            canvas.polygon(edge, [(7, 31), (26, 62), (45, 31)])
            canvas.circle(edge, (26, 25), 24)
            canvas.circle(fill, (26, 25), 20)
            canvas.circle(edge, (26, 25), 10, 2)
            if self.locked:
                canvas.line(edge, (20, 25), (32, 25), 3)
            else:
                canvas.circle(edge, (26, 25), 4)
            return result
