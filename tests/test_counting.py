from micro.counting import count_objects
import numpy as np

def test_count_zero_objects():
    img = np.array(
            [[ 0., 0., 0., 0., 0.],
             [ 0., 0., 0., 0., 0.],
             [ 0., 0., 0., 0., 0.],
             [ 0., 0., 0., 0., 0.]], dtype=np.int32)
    assert(count_objects(img) == 0)
