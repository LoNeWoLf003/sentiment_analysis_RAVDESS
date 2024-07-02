import pathlib
import os

working_dir_path = pathlib.Path().absolute()

TRAINING_FILES_PATH = os.path.join(str(working_dir_path), 'features')
SAVE_DIR_PATH = os.path.join(str(working_dir_path), 'dataset_features')
#MODEL_DIR_PATH = os.path.join(str(working_dir_path), 'model')
TESS_ORIGINAL_FOLDER_PATH = os.path.join(str(working_dir_path), 'TESS_Toronto_emotional_speech_set_data')
#EXAMPLES_PATH = os.path.join(str(working_dir_path), 'examples')