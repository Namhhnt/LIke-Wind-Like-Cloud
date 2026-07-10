# FILE: game/patches/tam_c04_phone_effect_bridge.rpy
# Adds one optional effect bucket for Chapter 04 extended relationship scores.

init 200 python:

    _tam_c04_original_phone_apply_effects = globals().get("phone_apply_effects")

    if callable(_tam_c04_original_phone_apply_effects):

        def phone_apply_effects(effects, *args, **kwargs):
            extended_add = {}
            base_effects = effects

            if isinstance(effects, dict):
                extended_add = effects.get("tam_c04_extended_story_add", {})
                base_effects = dict(effects)
                base_effects.pop("tam_c04_extended_story_add", None)

            result = _tam_c04_original_phone_apply_effects(
                base_effects,
                *args,
                **kwargs
            )

            if isinstance(extended_add, dict):
                for key, amount in extended_add.items():
                    tam_c04_add_extended_score(key, amount)

            return result
