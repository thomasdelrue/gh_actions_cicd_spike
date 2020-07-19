import pytest
import requests

from redshirt import something


def test_func_a():
    assert 1 == something.func_a(0)


class MockResponse:
    @staticmethod
    def json():
        return {'uuid': 'stub_uuid'}


def test_get_uuid(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, 'get', mock_get)

    assert 'stub_uuid' == something.get_uuid()
