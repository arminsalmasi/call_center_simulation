"""Free-threading / GIL checks."""

import sys

import pytest


@pytest.mark.skipif(
    not hasattr(sys, "_is_gil_enabled"),
    reason="sys._is_gil_enabled requires Python 3.13+",
)
def test_gil_disabled_on_freethreaded_build():
    import sysconfig

    if not sysconfig.get_config_var("Py_GIL_DISABLED"):
        pytest.skip("Interpreter was not built with free-threading")
    assert sys._is_gil_enabled() is False
