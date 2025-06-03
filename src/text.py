from enum import Enum


class Text(Enum):
    """Text constants for the URL Shortener application."""

    # Error
    ERROR = "An error occurred. Please try again later."
    INVALID_URL = "The provided URL is invalid. Please enter a valid URL."
    NO_URL_PROVIDED = "No URL provided."

    # Buttons
    TITLE = "URL SHORTENER :link:"
    URL_BUTTON = "Shorten URL"
    QR_CODE_BUTTON = "Generate QR Code"
    ENTER_MESSAGE = "Enter URL here:"
