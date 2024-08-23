import re


subscription_text_pattern = r"@(\w+) (\d+) days"


def parse_subscription_text(text: str):
    match = re.search(subscription_text_pattern, text.strip())
    if not match:
        raise WrongSubscriptionFormatException

    username: str = match.group(1)
    days: int = int(match.group(2))

    return username, days


class WrongSubscriptionFormatException:
    pass
