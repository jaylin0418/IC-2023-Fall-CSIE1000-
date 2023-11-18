import argparse

def get_args():
    # TODO: Add --input_dir, --output_dir argument
    #*************add your code here*************
    #usage like this:  python3 main.py --input_dir input_dir_path --output_dir output_dir_path
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir', 
                        type=str, 
                        required=True,
                        help='Path to the input directory.')
    parser.add_argument('--output_dir', 
                        type=str, 
                        required=True,
                        help='Path to the output directory.')
    args = parser.parse_args()
    return args
    #*************end your code here************* 
