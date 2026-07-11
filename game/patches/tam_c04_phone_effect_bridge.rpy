# FILE: game/patches/tam_c04_phone_effect_bridge.rpy
# Optional effect buckets used by Chapter 04 phone content.

init 200 python:

    _tam_c04_original_phone_apply_effects = globals().get("phone_apply_effects")

    if callable(_tam_c04_original_phone_apply_effects):

        def phone_apply_effects(effects, *args, **kwargs):
            extended_add = {}
            relationship_contacts = []
            base_effects = effects

            if isinstance(effects, dict):
                extended_add = effects.get("tam_c04_extended_story_add", {})
                relationship_contacts = effects.get("relationship_contacts", [])
                base_effects = dict(effects)
                base_effects.pop("tam_c04_extended_story_add", None)
                base_effects.pop("relationship_contacts", None)

            result = _tam_c04_original_phone_apply_effects(
                base_effects,
                *args,
                **kwargs
            )

            if isinstance(extended_add, dict):
                for key, amount in extended_add.items():
                    tam_c04_add_extended_score(key, amount)

            if isinstance(relationship_contacts, dict):
                relationship_contacts = [relationship_contacts]

            if isinstance(relationship_contacts, (list, tuple)):
                for contact in relationship_contacts:
                    if not isinstance(contact, dict):
                        continue
                    pair_id = contact.get("pair_id")
                    period_id = contact.get("period_id")
                    if pair_id and period_id:
                        relationship_mark_contact(
                            pair_id,
                            period_id,
                            source=contact.get("source", "phone"),
                        )

            return result
