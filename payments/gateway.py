"""Talks to the card gateway to authorize payments.

The gateway usually answers in 1 to 3 seconds.
"""

GATEWAY_TIMEOUT_SECONDS = 4
MAX_RETRIES = 3
BACKOFF_SECONDS = 0.5


def authorize(card_token: str, amount_cents: int) -> bool:
    """Ask the card gateway to authorize a payment, retrying with backoff."""
    raise NotImplementedError("Demo service: the gateway call is not part of the course.")