#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

from mps_youtube import pafy


@pytest.mark.parametrize(
    "page, result, exp_res",
    [
        (1, 0, [0]),
        (0, 0, [0]),
        (2, 0, [0, 0]),
        (-1, 0, [0]),
        (1, 2, [2]),
        (3, 2, [2, 2, 2]),
    ],
)
def test_search_videos(monkeypatch, page, result, exp_res):
    monkeypatch.setattr(pafy.VideosSearch, "result", lambda _: {"result": [result]})
    assert pafy.search_videos("house", page) == exp_res
