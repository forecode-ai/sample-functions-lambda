"""Refund eligibility: called by the payments API through API Gateway."""

import json

REFUND_WINDOW_DAYS = 30


def eligible(days_since_purchase: int, used: bool) -> bool:
    return days_since_purchase <= REFUND_WINDOW_DAYS and not used


def handler(event: dict, _context: object) -> dict:
    body = json.loads(event.get("body") or "{}")
    ok = eligible(int(body.get("days", 0)), bool(body.get("used", False)))
    return {"statusCode": 200, "body": json.dumps({"eligible": ok})}
