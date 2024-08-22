import subprocess

def compress_mp4(input_file, output_file):
    # ffmpeg command to compress mp4 without losing quality
    command = [
        'ffmpeg',
        '-i', input_file,              # input file
        '-vcodec', 'libx264',          # video codec
        '-crf', '18',                  # constant rate factor (lower is better quality)
        '-preset', 'slow',             # encoding speed (slower is better compression)
        '-c:a', 'copy',                # copy audio stream
        output_file                    # output file
    ]
    
    # Run the command
    subprocess.run(command, check=True)

# Example usage
input_file = 'input_video.mp4'
output_file = 'compressed_video.mp4'
compress_mp4(input_file, output_file)

print(f"Compression completed. Compressed file saved as {output_file}.")
