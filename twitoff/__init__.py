#!/usr/bin/env python
"""
Entry point for the TwitOff Flask Web Application.
"""

from .app import create_app

APP = create_app()