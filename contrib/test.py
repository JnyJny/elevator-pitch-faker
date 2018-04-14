#!/usr/bin/env python3

from faker import Faker

from src.elevator_pitch import StoryPitchProvider

fake = Faker()

fake.add_provider(StoryPitchProvider)

print(fake.story_pitch())
