import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import AgenticContextualSlotFillerClient

def main():
    client = AgenticContextualSlotFillerClient()
    res = client.fill_conversational_slots()
    print("=== Agentic Contextual Slot Filler Output ===")
    print(f"Slots Complete: {res['slots_complete']} | Next Action: {res['next_agent_action']}")
    print(f"Filled: {res['filled_slots_count']} | Missing Mandatory: {res['missing_mandatory_count']}")
    if res['next_clarification_prompt']:
        print(f"Targeted Clarification: '{res['next_clarification_prompt']}'")

if __name__ == '__main__':
    main()
