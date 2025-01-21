import pytest

mp = pytest.MonkeyPatch()
mp.setenv("ASSISTANT_ID", "dummy")
mp.setenv("OPENAI_API_KEY", "dummy")
