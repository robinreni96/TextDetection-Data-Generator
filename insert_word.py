import os
from PIL import Image, ImageFont, ImageDraw, ImageEnhance
import random
import csv
import argparse
from tqdm import tqdm
import shutil

def parse_arguments():
    """
        Parse the command line arguments of the program.
    """

    parser = argparse.ArgumentParser(
        description="Generate synthetic text data for text detection."
    )
    parser.add_argument(
        "--output_dir", type=str, nargs="?", help="The output directory", default="dataset/"
    )
    parser.add_argument(
        "-i",
        "--input_file",
        type=str,
        nargs="?",
        help="When set, this argument uses a specified text file as source for the text"
    )

    parser.add_argument(
        "-b",
        "--background",
        type=str,
        nargs="?",
        help="Define what kind of background color to use.",
        default="white",
    )

    parser.add_argument(
        "-fd",
        "--font_dir",
        type=str,
        nargs="?",
        help="Define a font directory to be used",
        default="fonts/"
    )

    parser.add_argument(
        "-np",
        "--num_pages",
        type=int,
        nargs="?",
        help="Define how many pages of text data need to be generated",
        default=10,
    )

    parser.add_argument(
        "-w",
        "--width",
        type=int,
        nargs="?",
        help="width of the page",
        default=600,
    )

    parser.add_argument(
        "--height",
        type=int,
        nargs="?",
        help="height of the page",
        default=800,
    )

    return parser.parse_args()


def main():
    """
    Generate the dateset
    """

    # Argument parsing
    args = parse_arguments()

    # words file
    text_file = args.input_file

    #fonts file
    fonts_file = args.font_dir

    # read all the words as list
    with open(text_file) as f:
        lines = f.read().splitlines()

    # Fixed font sizes
    font_sizes= [15,18,20,12,22,30,25]

    # List of fonts available
    fonts= os.listdir(os.path.join(os.getcwd(),fonts_file))


    #Define No of Pages want to create dataset
    Pages = args.num_pages

    if os.path.isdir(args.output_dir):
        shutil.rmtree(args.output_dir)
        os.mkdir(args.output_dir)
    else:
        os.mkdir(args.output_dir)

    with open('ground_truth.csv','w') as csvfile:
        filewriter = csv.writer(csvfile,delimiter=',')
        filewriter.writerow(["filename", "text", "xmin", "xmax", "ymin", "ymax", "class"])
        for page in tqdm(range(1,Pages)):
            file_name = args.output_dir +"page-"+str(page)+".jpg"
            # create a image template with white background w * h
            im = Image.new('RGB', (args.width, args.height), args.background)
            draw = ImageDraw.Draw(im)
            # setting up the y axis distribution
            for i in range(20,801,50):
                font_choice = fonts_file+random.choice(fonts)
                size = random.choice(font_sizes)
                Font = ImageFont.truetype(font_choice,size)
                horiz=10
                for j in range (10,601,100):
                    string=random.choice(lines)
                    size=Font.getsize(string)
                    draw.text((horiz,i), string , fill=(0,0,0), font=Font)
                    #draw.rectangle([horiz,i,horiz+size[0],i+size[1]],outline="blue")
                    file_n = file_name.split("/")
                    filewriter.writerow([file_n[1],string,horiz,i,horiz+size[0],i+size[1],"Text"])
                    horiz+=size[0]+5
                    if horiz + 200 > 600:
                        break
            im.save(file_name)

if __name__ == "__main__":
    main()