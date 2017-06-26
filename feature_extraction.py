import tempfile
import matlab.engine
import h5py


def random_sample(input_files, central_crop_fraction, samples_per_image, num_workers):
    eng = matlab.engine.start_matlab()
    with tempfile.NamedTemporaryFile('w+b', suffix='.h5') as output_file:
        eng.sample_sid(input_files,
                       output_file.name,
                       central_crop_fraction,
                       samples_per_image,
                       num_workers,
                       nargout=0)
        with h5py.File(output_file.name, 'r') as f:
            features = f['/features'].value
    return features


def dense_sample(input_files, fp, central_crop_fraction, stride=1, num_workers=8):
    eng = matlab.engine.start_matlab()
    eng.dense_sid(input_files,
                  fp,
                  central_crop_fraction,
                  stride,
                  num_workers,
                  nargout=0)
