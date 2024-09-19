# from ._utils import TUSIMPLE_ROOT

dataset = dict(
    name='TuSimple',
    image_set='train',  # Only set for training. Testing will override this value by --state.
    root='/home/anamaly/TUSimple',
    padding_mask=False
)
