import pytest
from app import mainApp
from flask import Flask

@pytest.fixture
def app():
    return mainApp
