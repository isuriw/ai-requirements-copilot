extracted_items = [
    {
        "type": "requirement",
        "description": "Reports must be available by 8 am each business day.",
        "status": "proposed",
        "owner": None,
        "source": "Meeting note"
    },
    {
        "type": "preference",
        "description": "Retain the current report layout.",
        "status": "pending_approval",
        "owner": None,
        "source": "Meeting note"
    },
    {
        "type": "task",
        "description": "Confirm which existing reports are still required.",
        "status": "open",
        "owner": "Sarah",
        "due": "Friday",
        "source": "Meeting note"
    },
    {
        "type": "risk",
        "description": "AWS data may not be available early enough.",
        "status": "to_investigate",
        "owner": None,
        "source": "Meeting note"
    }
]

for item in extracted_items:
    print(f"{item['type'].upper()}: {item['description']}")