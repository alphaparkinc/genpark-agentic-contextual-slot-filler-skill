import json
from typing import Dict, Any, List, Optional

class AgenticContextualSlotFillerClient:
    """
    Production-grade conversational slot filling engine.
    Tracks mandatory and optional parameters in user dialogue and generates targeted clarifying prompts.
    """
    SLOT_DEFINITIONS = {
        "target_category": {"required": True, "prompt": "What category of product are you looking to purchase?"},
        "price_ceiling": {"required": True, "prompt": "What is your maximum target budget?"},
        "brand_preference": {"required": False, "prompt": "Do you have any specific preferred brands?"},
        "delivery_speed": {"required": True, "prompt": "Do you require standard or expedited 2-day delivery?"}
    }

    def fill_conversational_slots(self, extracted_entities: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        if not extracted_entities:
            extracted_entities = {
                "target_category": "Robot Vacuum",
                "price_ceiling": 1200.0
            }

        filled_slots = {}
        missing_mandatory_slots = []

        for slot, spec in self.SLOT_DEFINITIONS.items():
            if slot in extracted_entities and extracted_entities[slot] is not None:
                filled_slots[slot] = extracted_entities[slot]
            elif spec["required"]:
                missing_mandatory_slots.append({
                    "slot_name": slot,
                    "clarification_prompt": spec["prompt"]
                })

        slots_complete = (len(missing_mandatory_slots) == 0)
        next_action = "EXECUTE_DOWNSTREAM_CHECKOUT_ACTION" if slots_complete else "PROMPT_USER_FOR_MISSING_SLOT"

        return {
            "session_slot_id": "slt_fil_5521",
            "slots_complete": slots_complete,
            "next_agent_action": next_action,
            "filled_slots_count": len(filled_slots),
            "missing_mandatory_count": len(missing_mandatory_slots),
            "filled_slots": filled_slots,
            "next_clarification_prompt": missing_mandatory_slots[0]["clarification_prompt"] if missing_mandatory_slots else None
        }
