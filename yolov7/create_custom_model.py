import hubconf


# helper function to create a custom model outside of the yolov7 repository
def get_custom_model(custom_weights_path):
    model = hubconf.custom(path_or_model=custom_weights_path)
    return model


