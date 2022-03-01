import pytest
from shapely import geometry
import numpy as np
from twoaxistracking import layout


@pytest.fixture
def rectangular_geometry():
    collector_geometry = geometry.box(-2, -1, 2, 1)
    total_collector_area = collector_geometry.area
    min_tracker_spacing = layout._calculate_min_tracker_spacing(collector_geometry)
    return collector_geometry, total_collector_area, min_tracker_spacing


@pytest.fixture
def square_field_layout():
    # Corresponds to GCR 0.125 with the rectangular_geometry
    X = np.array([-8, 0, 8, -8, 8, -8, 0, 8])
    Y = np.array([-8, -8, -8, 0, 0, 8, 8, 8])
    tracker_distance = (X**2 + Y**2)**0.5
    relative_azimuth = np.array([225, 180, 135, 270, 90, 315, 0, 45])
    Z = np.zeros(8)
    relative_slope = np.zeros(8)
    return X, Y, Z, tracker_distance, relative_azimuth, relative_slope


def assert_isinstance(obj, klass):
    assert isinstance(obj, klass), f'got {type(obj)}, expected {klass}'
