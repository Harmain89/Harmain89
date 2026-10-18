import math
import os
from PIL import Image, ImageDraw

def cubic_bezier(p0, p1, p2, p3, t):
    x = (1 - t)**3 * p0[0] + 3 * (1 - t)**2 * t * p1[0] + 3 * (1 - t) * t**2 * p2[0] + t**3 * p3[0]
    y = (1 - t)**3 * p0[1] + 3 * (1 - t)**2 * t * p1[1] + 3 * (1 - t) * t**2 * p2[1] + t**3 * p3[1]
    return (x, y)

def sample_path(points, num_samples=100):
    # points can be 2 points (linear) or 4 points (cubic bezier)
    samples = []
    if len(points) == 2:
        p0, p1 = points
        for i in range(num_samples):
            t = i / (num_samples - 1)
            samples.append((p0[0] + t * (p1[0] - p0[0]), p0[1] + t * (p1[1] - p0[1])))
    elif len(points) == 4:
        p0, p1, p2, p3 = points
        for i in range(num_samples):
            t = i / (num_samples - 1)
            samples.append(cubic_bezier(p0, p1, p2, p3, t))
    return samples

# Paths definition
paths = [
    # 1. Webhook -> Validate
    sample_path([(178, 437), (268, 437)], 40),
    # 2. Validate -> Is Valid?
    sample_path([(333, 437), (414, 437)], 40),
    # 3. Is Valid? -> Build AI Prompt (true)
    sample_path([(476, 428), (515, 428), (525, 437), (565, 437)], 50),
    # 4. Build AI Prompt -> OpenAI
    sample_path([(630, 437), (710, 437)], 40),
    # 5. OpenAI -> Parse Decision
    sample_path([(854, 437), (904, 437)], 30),
    # 6. Parse Decision -> Is Human Escalation?
    sample_path([(969, 437), (1050, 437)], 40),
    # 7. Human Escalation (true) -> Discord Alert
    sample_path([(1112, 426), (1154, 426), (1154, 291), (1196, 291)], 60),
    # 8. Discord Alert -> Admin Email
    sample_path([(1260, 291), (1350, 291)], 40),
    # 9. Admin Email -> Client Email
    sample_path([(1416, 291), (1495, 291)], 40),
    # 10. Client Email -> Format Final Response
    sample_path([(1561, 291), (1610, 291), (1610, 437), (1649, 437)], 60),
    # 11. Human Escalation (false) -> Is Hot Lead?
    sample_path([(1112, 448), (1155, 448), (1155, 495), (1198, 495)], 50),
    # 12. Is Hot Lead? (true) -> Hot Lead Email
    sample_path([(1262, 485), (1307, 485), (1307, 437), (1352, 437)], 50),
    # 13. Hot Lead Email -> Hot Lead Discord Alert
    sample_path([(1416, 437), (1456, 437), (1456, 377), (1496, 377)], 50),
    # 14. Hot Lead Discord Alert -> Format Final Response
    sample_path([(1559, 377), (1604, 377), (1604, 437), (1649, 437)], 60),
    # 15. Is Hot Lead? (false) -> Is Warm Lead?
    sample_path([(1262, 505), (1306, 505), (1306, 571), (1351, 571)], 50),
    # 16. Is Warm Lead? (true) -> Warm Lead Email
    sample_path([(1417, 560), (1457, 560), (1457, 514), (1497, 514)], 50),
    # 17. Warm Lead Email -> Format Final Response
    sample_path([(1560, 514), (1605, 514), (1605, 437), (1649, 437)], 60),
    # 18. Is Warm Lead? (false) -> Nurture Lead Email
    sample_path([(1417, 582), (1457, 582), (1457, 632), (1498, 632)], 50),
    # 19. Nurture Lead Email -> Format Final Response
    sample_path([(1561, 632), (1605, 632), (1605, 437), (1649, 437)], 60),
    # 20. Format Final Response -> Respond 200 Success
    sample_path([(1714, 437), (1795, 437)], 40),
]

# Key ports for pulsing rings
ports = [
    (178, 437), (268, 437), (333, 437), (414, 437), (476, 428), (565, 437),
    (630, 437), (710, 437), (854, 437), (904, 437), (969, 437), (1050, 437),
    (1112, 426), (1112, 448), (1196, 291), (1260, 291), (1350, 291), (1416, 291),
    (1495, 291), (1561, 291), (1198, 495), (1262, 485), (1262, 505), (1352, 437),
    (1416, 437), (1496, 377), (1559, 377), (1351, 571), (1417, 560), (1417, 582),
    (1497, 514), (1560, 514), (1498, 632), (1561, 632), (1649, 437), (1714, 437),
    (1795, 437), (1859, 437)
]

base_img_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'series-ai-lead-flow.png')
output_gif_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'series-ai-lead-flow.gif')

base_img = Image.open(base_img_path).convert('RGBA')
W, H = base_img.size

# We will generate 24 frames
num_frames = 24
frames = []

for f in range(num_frames):
    t_cycle = f / num_frames
    frame = base_img.copy()
    overlay = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    # 1. Draw glowing traveling pulses along each path
    for p_idx, path in enumerate(paths):
        # determine packet position
        # stagger speed slightly
        speed = 1.0 if p_idx < 6 or p_idx == 19 else 0.75
        phase = (t_cycle * speed + (p_idx * 0.13)) % 1.0
        idx = int(phase * (len(path) - 1))
        pt = path[idx]

        # color: green for main, purple for escalation, blue for openai/discord
        if p_idx in [6, 7, 8, 9]:
            core_color = (157, 114, 255, 255) # purple
            glow_color = (157, 114, 255, 80)
        elif p_idx in [3, 12]:
            core_color = (88, 166, 255, 255) # blue
            glow_color = (88, 166, 255, 80)
        elif p_idx in [14, 17, 18]:
            core_color = (227, 179, 65, 255) # amber
            glow_color = (227, 179, 65, 80)
        else:
            core_color = (0, 229, 153, 255) # green
            glow_color = (0, 229, 153, 80)

        # Draw outer glow
        gx, gy = pt
        draw.ellipse([gx - 9, gy - 9, gx + 9, gy + 9], fill=glow_color)
        draw.ellipse([gx - 5, gy - 5, gx + 5, gy + 5], fill=(core_color[0], core_color[1], core_color[2], 180))
        draw.ellipse([gx - 2.5, gy - 2.5, gx + 2.5, gy + 2.5], fill=(255, 255, 255, 255))

    # 2. Draw pulsing port rings
    pulse_val = math.sin(t_cycle * 2 * math.pi)
    port_r = 4 + 2 * (pulse_val * 0.5 + 0.5)
    for px, py in ports:
        draw.ellipse([px - port_r - 2, py - port_r - 2, px + port_r + 2, py + port_r + 2], outline=(0, 229, 153, 90), width=1)
        draw.ellipse([px - 3, py - 3, px + 3, py + 3], fill=(0, 229, 153, 200))

    # 3. Soft scanning beam line sweeping down
    scan_y = int(40 + (H - 80) * t_cycle)
    draw.line([(60, scan_y), (W - 60, scan_y)], fill=(0, 229, 153, 30), width=2)

    # Composite overlay on frame
    frame = Image.alpha_composite(frame, overlay)
    # Downscale smoothly to 1400px width for crisp rendering with lightweight GIF size
    target_w = 1400
    target_h = int(H * (target_w / W))
    frame_resized = frame.resize((target_w, target_h), Image.Resampling.LANCZOS)
    # Convert to adaptive palette
    frame_p = frame_resized.convert('P', palette=Image.Palette.ADAPTIVE, colors=128)
    frames.append(frame_p)

# Save as animated GIF
frames[0].save(
    output_gif_path,
    save_all=True,
    append_images=frames[1:],
    duration=65, # ~15 fps
    loop=0,
    optimize=True
)

file_size = os.path.getsize(output_gif_path)
print(f'Successfully generated {output_gif_path}')
print(f'Frames: {len(frames)}, Resolution: 1400x{target_h}, Size: {file_size / 1024:.1f} KB')
