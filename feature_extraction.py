import tempfile
import matlab.engine
import scipy.io


def random_sample(input_files, central_crop_fraction, samples_per_image):
    eng = matlab.engine.start_matlab()
    with tempfile.NamedTemporaryFile('w+b', suffix='.mat') as output_file:
        eng.sample_sid(input_files,
                       output_file.name,
                       central_crop_fraction,
                       samples_per_image,
                       nargout=0)
        features = scipy.io.loadmat(output_file.name)
    return features['features'][0]


def dense_sample(input_files, central_crop_fraction, stride=1):
    eng = matlab.engine.start_matlab()
    with tempfile.NamedTemporaryFile('w+b', suffix='.mat') as output_file:
        eng.dense_sid(input_files,
                      output_file.name,
                      central_crop_fraction,
                      stride,
                      nargout=0)
        features = scipy.io.loadmat(output_file.name)
    return features['features'][0]
