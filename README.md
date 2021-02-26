# ffmpeg

Python script for batch processing video files using ffmpeg.

Uses the default command: 

ffmpeg -i <input_file.ext> <output_file.ext> 

Drop this script in the directory containing the videos you wish to process. 

When executed, it will hash all the original files in the directory using sha1, and prompt
you for the input / output file extensions.  

After processing, it will hash all the contents of the directory once again and output two 
text files containing all the associated hash values. 
