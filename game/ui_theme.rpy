# Resolution-independent panels: text and controls stay live, not baked into art.
init -10 python:
    import math as _ui_math
    from functools import lru_cache as _ui_lru_cache

    def ui_is_compact():
        """Use larger landscape controls on touch devices and small PC windows."""
        return renpy.variant("small") or renpy.variant("touch") or renpy.get_physical_size()[0] <= 1000

    def ui_translate(text):
        # Translate fragments before concatenation/formatting; Text cannot find
        # a translation for the completed, data-dependent string afterwards.
        return renpy.translate_string(text)

    # Evaluate the curve per fragment, rather than approximating it with an
    # integer polygon. Coverage is softened in physical-pixel units at 720p too.
    renpy.register_shader("lwlc.glass_panel", variables="""
        uniform vec2 u_panel_size;
        uniform float u_panel_radius;
        uniform float u_panel_aa;
        uniform float u_panel_ornate;
        uniform vec4 u_panel_fill;
        uniform vec4 u_panel_border;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_functions="""
        float lwlc_round_distance(vec2 p, vec2 half_size, float radius) {
            vec2 q = abs(p) - half_size + vec2(radius);
            return length(max(q, vec2(0.0))) + min(max(q.x, q.y), 0.0) - radius;
        }
    """, fragment_300="""
        vec2 p = (v_tex_coord - vec2(0.5)) * u_panel_size;
        float d = lwlc_round_distance(p, u_panel_size * 0.5 - vec2(1.5), u_panel_radius);
        float aa = u_panel_aa;
        float coverage = 1.0 - smoothstep(-aa, aa, d);
        float rim = (1.0 - smoothstep(0.55, 0.55 + aa, abs(d + 0.8))) * coverage;
        float light = 0.78 + 0.22 * (1.0 - v_tex_coord.y) + 0.12 * (1.0 - v_tex_coord.x);
        vec3 gold = u_panel_border.rgb * light;
        float border_alpha = rim * u_panel_border.a;
        // A quiet, broad amber reflection, not a flat opaque brown rectangle.
        float reflection = pow(1.0 - v_tex_coord.x, 3.0) * (1.0 - v_tex_coord.y);
        vec3 fill = u_panel_fill.rgb + vec3(0.055, 0.039, 0.022) * reflection;
        float fill_alpha = coverage * u_panel_fill.a;
        vec4 base = vec4(fill * fill_alpha, fill_alpha);
        vec4 edge = vec4(gold * border_alpha, border_alpha);
        gl_FragColor = edge + base * (1.0 - edge.a);
        float inner = (1.0 - smoothstep(0.25, 0.25 + aa, abs(d + 7.0))) * u_panel_ornate * 0.23;
        vec4 inner_edge = vec4(gold * inner, inner);
        gl_FragColor = inner_edge + gl_FragColor * (1.0 - inner);
    """)

    class _UIScaledCanvas:
        """Supersample small line illustrations before filtered downscaling."""
        def __init__(self, canvas, scale=4):
            self.canvas, self.scale = canvas, scale

        def point(self, point):
            return tuple(int(round(v * self.scale)) for v in point)

        def line(self, color, a, b, width=1):
            self.canvas.line(color, self.point(a), self.point(b), max(1, int(width*self.scale)))

        def circle(self, color, center, radius, width=0):
            self.canvas.circle(color, self.point(center), int(radius*self.scale), int(width*self.scale))

        def polygon(self, color, points, width=0):
            self.canvas.polygon(color, [self.point(p) for p in points], int(width*self.scale))

        def rect(self, color, rect, width=0):
            self.canvas.rect(color, self.point(rect), int(width*self.scale))

    def _ui_round_rect(x, y, w, h, radius):
        radius = min(radius, w / 2.0, h / 2.0)
        points = []
        for cx, cy, start in ((x+w-radius, y+radius, -90), (x+w-radius, y+h-radius, 0), (x+radius, y+h-radius, 90), (x+radius, y+radius, 180)):
            for step in range(9):
                angle = _ui_math.radians(start + step * 11.25)
                points.append((int(cx + radius * _ui_math.cos(angle)), int(cy + radius * _ui_math.sin(angle))))
        return points

    def _ui_stroke(canvas, color, points, closed=True):
        for a, b in zip(points, points[1:] + ([points[0]] if closed else [])):
            canvas.line(color, a, b, 1)

    class WarmPanel(renpy.Displayable):
        def __init__(self, fill="#211a15cc", border="#b89a6b99", radius=18, ornate=False, **kwargs):
            super(WarmPanel, self).__init__(**kwargs)
            self.fill = fill
            self.border = border
            self.radius = radius
            self.ornate = ornate
            self._surface = None
            self._surface_size = None

        def visit(self):
            return [self._surface] if self._surface else []

        def render(self, width, height, st, at):
            width, height = max(1, int(width)), max(1, int(height))
            result = renpy.Render(width, height)
            physical_width = max(1, renpy.get_physical_size()[0])
            surface_size = (width, height, physical_width)
            if surface_size != self._surface_size:
                self._surface_size = surface_size
                self._surface = Transform(
                    Solid("#fff", xysize=(width, height)), mesh=True,
                    shader="lwlc.glass_panel",
                    u_panel_size=(float(width), float(height)),
                    u_panel_radius=float(min(self.radius, max(0, width/2.0-2), max(0, height/2.0-2))),
                    u_panel_aa=max(0.65, float(config.screen_width)/physical_width*0.7),
                    u_panel_ornate=float(self.ornate),
                    u_panel_fill=tuple(Color(self.fill).rgba),
                    u_panel_border=tuple(Color(self.border).rgba),
                )
            result.blit(renpy.render(self._surface, width, height, st, at), (0, 0))
            return result

    @renpy.pure
    @_ui_lru_cache(maxsize=192)
    def ui_panel(fill="#211a15cc", border="#b89a6b99", radius=18, ornate=False):
        return WarmPanel(fill, border, radius, ornate)

    class GoldDivider(renpy.Displayable):
        def render(self, width, height, st, at):
            width = max(1, int(width))
            high = renpy.Render(width*4, 18*4)
            c = _UIScaledCanvas(high.canvas())
            mid = width // 2
            c.line("#ba92566e", (0,9), (mid-14,9), 0.7)
            c.line("#ba92566e", (mid+14,9), (width,9), 0.7)
            c.polygon("#d8b77d", [(mid,2),(mid+2.5,7),(mid+9,9),(mid+2.5,11),(mid,16),(mid-2.5,11),(mid-9,9),(mid-2.5,7)])
            result = renpy.Render(width, 18)
            result.forward = renpy.display.matrix.Matrix2D(4, 0, 0, 4)
            result.reverse = renpy.display.matrix.Matrix2D(0.25, 0, 0, 0.25)
            result.blit(high, (0, 0))
            return result

    class GoldIcon(renpy.Displayable):
        """Small, consistent line-art medallions instead of unrelated font glyphs."""
        def __init__(self, kind="extras", muted=False, medallion=True, **kwargs):
            super(GoldIcon, self).__init__(**kwargs)
            self.kind, self.muted = kind, muted
            self.medallion = medallion
            self._disc = ui_panel("#564c4044" if muted else "#9c703f99", "#a89c8866" if muted else "#f2d6a6dd", radius=48) if medallion else None
            asset = {"characters": "person", "contacts": "person", "status": "person", "stories": "book", "library": "book", "music": "music", "cg": "gallery", "gallery": "gallery", "extras": "extras", "minigames": "gamepad", "settings": "settings", "start": "leaf"}.get(kind)
            self._icon = Transform(Image("gui/theme/refined/icon_" + asset + ".svg", oversample=4), matrixcolor=(SaturationMatrix(0.0)*BrightnessMatrix(-0.25) if muted else IdentityMatrix())) if asset else None

        def visit(self):
            # Stable children let prediction load icons before the first draw.
            return [child for child in (self._disc, self._icon) if child is not None]

        def render(self, width, height, st, at):
            if self._icon is not None:
                result = renpy.Render(96, 96)
                if self.medallion:
                    result.blit(renpy.render(self._disc, 96, 96, st, at), (0, 0))
                result.blit(renpy.render(self._icon, 96, 96, st, at), (0, 0))
                return result
            high = renpy.Render(384, 384)
            c = _UIScaledCanvas(high.canvas())
            ink = "#a99d87" if self.muted else "#f3d6a1"
            def line(a, b):
                c.line(ink, a, b, 2)
            kind = self.kind
            if kind == "continue":
                c.circle(ink, (48,48), 28, 2)
                line((48,27),(48,49));line((48,49),(64,57))
            elif kind == "settings":
                c.circle(ink,(48,48),20,2);c.circle(ink,(48,48),8,2)
                for angle in range(0,360,45):
                    a = _ui_math.radians(angle)
                    line((int(48+21*_ui_math.cos(a)),int(48+21*_ui_math.sin(a))), (int(48+31*_ui_math.cos(a)),int(48+31*_ui_math.sin(a))))
            elif kind == "back":
                line((72,48),(24,48));line((24,48),(42,30));line((24,48),(42,66))
            elif kind == "play":
                c.polygon(ink, [(35,25),(72,48),(35,71)])
            elif kind == "stop":
                c.rect(ink, (29,29,38,38))
            elif kind == "close":
                line((29,29),(67,67));line((67,29),(29,67))
            elif kind == "menu":
                for y in (30,48,66): line((26,y),(70,y))
            elif kind == "quit":
                _ui_stroke(c,ink,[(44,25),(25,25),(25,73),(44,73)],False)
                line((41,49),(75,49));line((63,37),(75,49));line((75,49),(63,61))
            elif kind == "start":
                _ui_stroke(c,ink,[(26,74),(31,49),(42,35),(72,22),(66,48),(53,60),(26,74)])
                line((23,80),(72,22));line((39,60),(36,42));line((48,49),(62,49))
            elif kind in ("characters", "contacts", "status"):
                c.circle(ink, (48,37), 11)
                c.polygon(ink, _ui_round_rect(28, 51, 40, 25, 12))
            elif kind in ("stories", "library"):
                _ui_stroke(c, ink, [(23,29),(43,32),(48,37),(53,32),(73,29),(73,65),(53,68),(48,73),(43,68),(23,65)])
                line((48,37),(48,70))
                line((29,38),(40,40)); line((56,40),(67,38))
            elif kind in ("messages", "social"):
                c.circle(ink, (48,44), 22, 2)
                _ui_stroke(c, ink, [(30,56),(26,72),(43,65)], False)
                for x in (38,48,58): c.circle(ink, (x,44), 2)
            elif kind == "music":
                line((43,30),(43,65)); line((67,25),(67,60)); line((43,30),(67,25))
                c.circle(ink,(35,65),9); c.circle(ink,(59,60),9)
            elif kind in ("cg", "gallery"):
                c.rect(ink,(24,27,48,43),2)
                c.circle(ink,(59,39),5)
                _ui_stroke(c,ink,[(26,64),(39,47),(51,59),(60,51),(70,64)],False)
            elif kind == "minigames":
                _ui_stroke(c,ink,[(29,36),(67,36),(76,64),(65,70),(56,59),(40,59),(31,70),(20,64)])
                line((30,48),(44,48));line((37,41),(37,55))
                c.circle(ink,(60,46),3);c.circle(ink,(67,54),3)
            elif kind == "mail":
                c.rect(ink,(23,32,50,34),2)
                line((23,32),(48,51));line((48,51),(73,32))
            elif kind == "building":
                c.rect(ink,(35,20,28,57),2)
                for x in (41,49,57):
                    for y in (28,38,48,58):
                        line((x,y),(x,y+4))
                line((27,78),(72,78));line((47,68),(47,77));line((55,68),(55,77))
            elif kind == "home":
                _ui_stroke(c,ink,[(22,46),(48,22),(75,46)],False)
                _ui_stroke(c,ink,[(29,42),(29,75),(67,75),(67,42)],False)
                _ui_stroke(c,ink,[(42,74),(42,54),(55,54),(55,74)],False)
            elif kind == "plane":
                c.polygon(ink,[(74,24),(76,29),(57,49),(69,70),(63,75),(47,59),(34,70),(34,78),(29,80),(25,68),(17,63),(20,58),(29,60),(41,47),(26,32),(31,27),(52,39)])
            elif kind == "cup":
                _ui_stroke(c,ink,[(24,42),(24,58),(29,68),(48,73),(63,66),(66,54),(66,42)])
                _ui_stroke(c,ink,[(67,44),(77,44),(78,56),(67,60)],False)
                line((21,78),(70,78));line((37,25),(37,34));line((49,23),(49,32))
            else:
                _ui_stroke(c,ink,[(32,25),(55,25),(67,37),(67,72),(32,72)])
                line((55,25),(55,38));line((55,38),(67,38))
                for y in (47,55,63):line((39,y),(59,y))
            illustration = renpy.Render(96, 96)
            illustration.forward = renpy.display.matrix.Matrix2D(4, 0, 0, 4)
            illustration.reverse = renpy.display.matrix.Matrix2D(0.25, 0, 0, 0.25)
            illustration.blit(high, (0, 0))
            result = renpy.Render(96, 96)
            if self.medallion:
                result.blit(renpy.render(self._disc, 96, 96, st, at), (0, 0))
            result.blit(illustration, (0, 0))
            return result

    class MapPin(renpy.Displayable):
        def __init__(self, locked=False, selected=False, kind="home", **kwargs):
            super(MapPin, self).__init__(**kwargs)
            self.locked = locked
            self.selected = selected
            self.kind = kind
            self._icon = Transform(ui_icon(kind, medallion=False), xysize=(136,136)) if not locked else None

        def visit(self):
            return [self._icon] if self._icon is not None else []

        def render(self, width, height, st, at):
            high = renpy.Render(208, 256)
            canvas = _UIScaledCanvas(high.canvas())
            edge = "#958775" if self.locked else "#edc781"
            fill = "#554a3d" if self.locked else ("#a77c38" if self.selected else "#3b2c1c")
            canvas.polygon(edge, [(7, 31), (26, 62), (45, 31)])
            canvas.circle(edge, (26, 25), 24)
            canvas.circle(fill, (26, 25), 20)
            result = renpy.Render(52, 64)
            result.forward = renpy.display.matrix.Matrix2D(4, 0, 0, 4)
            result.reverse = renpy.display.matrix.Matrix2D(0.25, 0, 0, 0.25)
            result.blit(high, (0, 0))
            if self.locked:
                canvas.line(edge, (20, 25), (32, 25), 3)
            else:
                icon = renpy.render(self._icon, 136, 136, st, at)
                high.blit(icon, (9*4, 8*4))
            return result

    # These decorations contain no animation or game state. Reuse identities
    # across screen reevaluations so Ren'Py can reuse their render trees.
    @renpy.pure
    @_ui_lru_cache(maxsize=64)
    def ui_icon(kind="extras", muted=False, medallion=True):
        return GoldIcon(kind, muted=muted, medallion=medallion)

    @renpy.pure
    @_ui_lru_cache(maxsize=32)
    def ui_map_pin(locked=False, selected=False, kind="home"):
        return MapPin(locked=locked, selected=selected, kind=kind)
