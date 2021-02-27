#!/usr/bin/env python3

import subprocess, hashlib, os


def encode_all_nix(in_file, out_ext):
    process = f'for i in *{in_file}; do ffmpeg -i "$i" "${{i%.*}}{out_ext}" ; done'
    subprocess.call(process, shell = True)
    return

def encode_all_win(in_file, out_ext):
    cwd = os.getcwd()
    for video in os.listdir(cwd):
            files = os.path.join(cwd, video)
            if os.path.isfile(video):
                output_file = os.path.join(cwd, video + out_ext)
                os.system(f"ffmpeg -i {video} {output_file} ")

def input_hash (in_file):
    print("All the input files have been hashed using the sha1 checksum ")
    print('')
    cwd = os.getcwd()                   #gets current directory
    filenames = []
    for video in os.listdir(cwd):
        with open(video, 'rb') as getsha1:
            data = getsha1.read()
        checksum = hashlib.sha1(data).hexdigest()
        filenames.append(os.path.join(checksum, video))
    with open("Original_hash.txt", "w+") as output:
        output.writelines([name + "\n" for name in filenames])
    output.close()

def output_hash (out_ext):
    print("All the input and output files have been hashed using the sha1 checksum ")
    print('')
    cwd = os.getcwd()                   #gets current directory
    filenames = []
    for video in os.listdir(cwd):
        with open(video, 'rb') as getsha1:
            data = getsha1.read()
        checksum = hashlib.sha1(data).hexdigest()
        filenames.append(os.path.join(checksum, video))
    with open("Output_hash.txt", "w+") as output:
        output.writelines([name + "\n" for name in filenames])
    output.close()

print('')
print(''' \t*************** WARNING ********************

This is not a "forensically sound" process.  This is strictly a down
and dirty method of transcoding all the files in this directory with ffmpeg to
produce a "working copy" of the original.

It is possible that you could drop some frames and /or lose data contained
in the original videos using this method.

\t*************** WARNING ******************** \n''')


print(' \r')
print ("What is your Operating System? ")
User_Sys = int(input("Enter 1. for Windows    OR    2. for Linux / MAC \n "))
print('')
print("NOTE!:  If you are using a Linux or MAC system.....\n")
print("Answers to the next two questions are CASE sensitive. \n")

print("Press ENTER or RETURN to continue ")
input(">>> ")

# in_file = input("What is the input file extension [CASE Sensitive] (.mov, .MOV etc): \n")
# out_ext = input("What is the output file extension: (.mp4, .avi etc) \n")

if User_Sys == 1:
    in_file = input("What is the input file extension? (.mov, .avi etc): \n")
    out_ext = input("What is the output file extension? (.mp4, .mkv etc) \n")
    print("OK, running ffmpeg for Windows: ")
    input_hash(in_file)
    encode_all_win(in_file, out_ext)
    cleanup = "powershell.exe", "Remove-Item", f"Original_hash.txt{out_ext}"
    subprocess.run(cleanup, shell=True)
    output_hash(out_ext)


elif User_Sys == 2:
    in_file = input("What is the input file extension? (.mov, .avi etc): \n")
    out_ext = input("What is the output file extension? (.mp4, .mkv etc) \n")
    print("OK, running ffmpeg for Linux / Mac: ")
    input_hash(in_file)
    encode_all_nix(in_file, out_ext)
    #cleanup = f"rm " "Original_hash.txt{out_ext}"
    #subprocess.run(cleanup, shell=True)
    output_hash(out_ext)


print("Done! \n")
print("""Verify that you have an 'Original_hash.txt' file and 'Output_hash.txt'
file in the directory with all your transcoded video files. \n""")
