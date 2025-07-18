# X-Ray Holography Simulation and Data Generation

X-ray Holography Data Generation simulates X-ray illumination interacting with synthetic objects to generate flexible training or evaluation datasets. It uses a parallel beam approximation and propagates the resulting wave field over a customizable distance. Users can configure various parameters via config files, including X-ray energy, geometry, detector resolution, and more. The framework randomly generates phantoms with user-defined ranges for size, shape, thickness, material properties, absorption, and phase shift, ensuring physically consistent synthetic data.

This project was integrated into the [**HoloWizard**](https://github.com/DESY-FS-PETRA/holowizard/) package as [**HoloForge**](https://github.com/DESY-FS-PETRA/holowizard/tree/main/holowizard/forge).

## How to use this Framework

The entire data generation is encapsulated in the class `DataGenerator` in `holly.generators` which offers the method `generate_data`, that can be used to generate data. Another more convenient way is through the command line by running the script

```{bash}
holly/scripts/generate_data.py
```

The script expects three positional and two optional arguments:

| Argument               | Description                                                      | Position |
|------------------------|------------------------------------------------------------------|----------|
| `num_samples`          | Number of data samples that should be generated.                 | 1        |
| `output`               | Output folder where the generated data is stored.                | 2        |
| `--config CONFIG`      | Path to the custom configuration file.                           | optional |
| `--override`           | Override the output folder if it already exists.                 | optional |


When a custom configuration file path is given, the script first looks in the directory `custom_configs`. Hence, the path to a configuration file can be relative to the folder `custom_configs`. If it was not found there, the relative path to the current working directoy is checked.

Since the command `python holly/generate_data.py` is, even without the argument list, quite long, there exists a wrapper `generate_data.sh` in the `project`'s root directory, that passes the parameters to the actual Python script.

**Example**: Generate 100 datasamples with a custom configuration and store them at `/gpfs/petra3/scratch/$USER/output`:

```{bash}
./generate_data.sh 100 /gpfs/petra3/scratch/$USER/output --config custom_configs/test_config.json
```
