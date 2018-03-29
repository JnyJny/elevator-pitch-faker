#!/usr/bin/env python3

from faker import Faker

from src.elevator_pitch import ElevatorPitchProvider

fake = Faker()

fake.add_provider(ElevatorPitchProvider)

print(fake.elevator_pitch())
