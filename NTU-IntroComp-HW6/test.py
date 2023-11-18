import os
import filecmp
import argparse

def compare_output_with_answers(output_folder, answer_folder):
    output_files = [f for f in os.listdir(output_folder) if f.endswith(".txt")]
    answer_files = [f for f in os.listdir(answer_folder) if f.endswith(".txt")]

    for output_file in output_files:
        if output_file in answer_files:
            output_path = os.path.join(output_folder, output_file)
            answer_path = os.path.join(answer_folder, output_file)

            if filecmp.cmp(output_path, answer_path, shallow=False):
                print(f"{output_file}: Pass")
            else:
                print(f"{output_file}: Fail")
        else:
            print(f"{output_file} does not have a corresponding answer file.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compare output files with answer files.")
    parser.add_argument("--output_folder", type=str, help="Path to the output folder")
    parser.add_argument("--answer_folder", type=str, help="Path to the answer folder")
    args = parser.parse_args()

    compare_output_with_answers(args.output_folder, args.answer_folder)

