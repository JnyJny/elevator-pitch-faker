# -*- coding: utf-8 -*-

import pytest
import sys
from pathlib import Path
from faker import Faker

localpath = Path(__file__).absolute().parent.joinpath('..')

sys.path.insert(0, localpath)

from src.elevator_pitch import ElevatorPitchProvider  # noqa


@pytest.fixture(scope='module')
def fake():
    fixture = Faker()
    fixture.add_provider(ElevatorPitchProvider)
    return fixture
