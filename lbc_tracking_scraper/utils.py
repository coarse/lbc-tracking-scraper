"""Utility functions"""

import base64


def encode_tracking_number(
    tracking_number: str, template: str = "{}hashlbcexpress"
) -> str:
    """Encode tracking number for use of finding the tracking page

    Args:
        tracking_number (str): 14 digit tracking number
        template (str, optional): message template to be encoded. Defaults to "{}hashlbcexpress".

    Returns:
        str: base64 encoded string
    """
    message = template.format(tracking_number)
    return base64.b64encode(message.encode()).decode()


def get_tracking_url(tracking_number: str) -> str:
    """Get tracking page URL for a given tracking number

    Args:
        tracking_number (str): 14 digit tracking number

    Returns:
        str: tracking page URL
    """
    encoded_tracking_number = encode_tracking_number(tracking_number)
    url = f"https://www.lbcexpress.com/track/{encoded_tracking_number}"
    return url
