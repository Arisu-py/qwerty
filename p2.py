# formatirovanie filov
import argparse


def format_text_block(frame_height, frame_width, file_name):
    try:
        with open(file_name) as in_file:
            lines = in_file.readlines()
        out_line = []
        first_list = [line if (len(line) == 1 and line.find('\n') != -1) else line.replace('\n', '') for line in lines]
        for line in ''.join(first_list).split('\n'):
            for i in range(0, len(line), frame_width):
                out_line.append(line[i:i + frame_width])
            else:
                out_line.append('')
        return '\n'.join(out_line[:frame_height])
    except Exception as text:
        return text


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--frame-height', type=int)
    parser.add_argument('--frame-width', type=int)
    parser.add_argument('filename', type=str)
    args = parser.parse_args()
    print(format_text_block(args.frame_height, args.frame_width, args.filename))
