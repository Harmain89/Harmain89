from PIL import Image
import os
import subprocess

input_path = 'assets/assetsseries-ai-voice-agent.gif'
temp_path = 'assets/temp_compressed.gif'
output_path = 'assets/assetsseries-ai-voice-agent.gif'

print('Opening original GIF...')
gif = Image.open(input_path)
orig_size = os.path.getsize(input_path)
print(f'Original size: {orig_size / (1024*1024):.2f} MB')

# Extract frames, taking every 3rd or 4th frame to reduce frame count from 301 to ~75 frames
# While keeping original 1000x562 resolution!
frames = []
durations = []

step = 4  # every 4th frame gives ~75 frames
for i in range(0, gif.n_frames, step):
    gif.seek(i)
    # Convert each frame to P mode with adaptive palette (64 colors for clean sharp UI)
    frame = gif.convert('RGB').convert('P', palette=Image.Palette.ADAPTIVE, colors=64)
    frames.append(frame)
    durations.append(100) # 100ms = 10 fps, smooth playback

print(f'Reduced to {len(frames)} frames at resolution {frames[0].size}')

# Save with PIL optimize
frames[0].save(
    temp_path,
    save_all=True,
    append_images=frames[1:],
    duration=100,
    loop=0,
    optimize=True
)

temp_size = os.path.getsize(temp_path)
print(f'PIL compressed size: {temp_size / 1024:.1f} KB ({temp_size / (1024*1024):.2f} MB)')

# Apply gifsicle -O3 --lossy=80 if gifsicle is available
gifsicle_exe = r'C:\Users\HP 440 G6\AppData\Local\npm-cache\_npx\b753d9a83bd1e962\node_modules\gifsicle\vendor\gifsicle.exe'
if os.path.exists(gifsicle_exe):
    opt_path = 'assets/temp_opt.gif'
    cmd = [gifsicle_exe, '-O3', '--lossy=80', temp_path, '-o', opt_path]
    subprocess.run(cmd)
    if os.path.exists(opt_path):
        opt_size = os.path.getsize(opt_path)
        print(f'Gifsicle optimized size: {opt_size / 1024:.1f} KB ({opt_size / (1024*1024):.2f} MB)')
        os.replace(opt_path, output_path)
        if os.path.exists(temp_path):
            os.remove(temp_path)
else:
    os.replace(temp_path, output_path)

final_size = os.path.getsize(output_path)
print(f'FINAL COMPRESSED SIZE: {final_size / 1024:.1f} KB ({final_size / (1024*1024):.2f} MB)')
