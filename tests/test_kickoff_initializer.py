import os
import pytest
from kickoff.kickoff_initializer import KickOffInitializer


@pytest.fixture
def kickoff_initializer(tmpdir):
    test_root_folder = tmpdir.mkdir("test_kickoff_initializer")
    return KickOffInitializer(str(test_root_folder))


def test_initialization(kickoff_initializer):
    kickoff_initializer.initialize()

    assert os.path.exists(kickoff_initializer.root_folder)
    assert os.path.exists(os.path.join(kickoff_initializer.root_folder, "Images"))
    assert os.path.exists(os.path.join(kickoff_initializer.root_folder, "Notes"))
    assert os.path.exists(os.path.join(kickoff_initializer.root_folder, "Others"))
    assert os.path.exists(os.path.join(kickoff_initializer.root_folder, ".gitignore"))
    assert os.path.exists(os.path.join(kickoff_initializer.root_folder, "LICENSE"))
    assert os.path.exists(os.path.join(kickoff_initializer.root_folder, "README.md"))

    assert os.path.exists(
        os.path.join(kickoff_initializer.root_folder, "Images", "README.md")
    )
    assert os.path.exists(
        os.path.join(kickoff_initializer.root_folder, "Notes", "README.md")
    )
    assert os.path.exists(
        os.path.join(kickoff_initializer.root_folder, "Others", "README.md")
    )
