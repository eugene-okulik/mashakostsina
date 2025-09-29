import pytest


def pytest_configure(config):
    """Регистрирует пользовательские маркеры для pytest"""
    config.addinivalue_line("markers", "medium: marks tests as medium priority")
    config.addinivalue_line("markers", "critical: marks tests as critical priority")
