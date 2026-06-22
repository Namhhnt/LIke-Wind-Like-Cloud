init -20 python:

    MM_ASSET_CACHE = {}

    def mm_loadable(path):
        return bool(path) and renpy.loadable(path)


    def mm_theme_asset(filename):
        return "gui/theme/%s" % filename


    def mm_missing_assets(paths):
        return [path for path in paths if not mm_loadable(path)]
