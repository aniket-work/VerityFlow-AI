import os
from PIL import Image, ImageDraw, ImageFont
import time

# Constants
WIDTH, HEIGHT = 1200, 800
FPS = 10
FRAME_DURATION = 100/1000  # seconds
VENV_PATH = "./venv/bin/python"

# Fonts - Using standard system fonts for portability
try:
    MONO_FONT = ImageFont.truetype("/System/Library/Fonts/Courier.ttc", 20)
    SANS_FONT = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 24)
    BOLD_FONT = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 32)
except:
    MONO_FONT = ImageFont.load_default()
    SANS_FONT = ImageFont.load_default()
    BOLD_FONT = ImageFont.load_default()

def create_terminal_frame(text_lines, cursor_on=True):
    img = Image.new('RGB', (WIDTH, HEIGHT), (30, 30, 30))
    draw = ImageDraw.Draw(img)
    
    # Mac Window Controls
    draw.ellipse([20, 20, 35, 35], fill=(255, 95, 87)) # Red
    draw.ellipse([45, 20, 60, 35], fill=(255, 189, 46)) # Yellow
    draw.ellipse([70, 20, 85, 35], fill=(39, 201, 63)) # Green
    
    # Title Bar
    draw.text((WIDTH//2 - 100, 18), "zsh — VerityFlow-AI — 80x24", fill=(180, 180, 180), font=SANS_FONT)
    
    # Terminal Content
    y = 60
    for line in text_lines:
        draw.text((30, y), line, fill=(230, 230, 230), font=MONO_FONT)
        y += 30
        
    if cursor_on:
        last_line_width = draw.textlength(text_lines[-1], font=MONO_FONT)
        draw.rectangle([30 + last_line_width, y - 30, 30 + last_line_width + 10, y - 5], fill=(200, 200, 200))
        
    return img

def create_ui_frame(results_data):
    img = Image.new('RGB', (WIDTH, HEIGHT), (240, 245, 250))
    draw = ImageDraw.Draw(img)
    
    # Header
    draw.rectangle([0, 0, WIDTH, 80], fill=(74, 144, 226))
    draw.text((40, 20), "VerityFlow-AI: Truth Dashboard", fill=(255, 255, 255), font=BOLD_FONT)
    
    # Summary Card
    draw.rounded_rectangle([50, 120, WIDTH-50, 300], radius=15, fill=(255, 255, 255), outline=(200, 200, 200), width=1)
    draw.text((80, 140), "Executive Summary", fill=(50, 50, 50), font=BOLD_FONT)
    draw.text((80, 190), "Autonomous swarm has validated 3 core claims regarding 'Synthetic Media in 2026 Elections'.", fill=(80, 80, 80), font=SANS_FONT)
    draw.text((80, 230), "Overall Credibility Score: 42% (Warning: High Bias Detected)", fill=(200, 50, 50), font=SANS_FONT)
    
    # Table Results
    y = 350
    headers = ["Claim", "Status", "Confidence", "Bias Source"]
    col_widths = [400, 150, 150, 250]
    
    x = 80
    for i, h in enumerate(headers):
        draw.text((x, y), h, fill=(100, 100, 100), font=BOLD_FONT)
        x += col_widths[i]
        
    y += 50
    for row in results_data:
        x = 80
        for i, val in enumerate(row):
            color = (50, 50, 50)
            if val == "DEBUNKED": color = (200, 50, 50)
            if val == "VERIFIED": color = (50, 150, 50)
            draw.text((x, y), str(val), fill=color, font=SANS_FONT)
            x += col_widths[i]
        y += 40
        draw.line([80, y-10, WIDTH-80, y-10], fill=(220, 220, 220))
        
    return img

def generate_gif():
    frames = []
    
    # Part 1: Terminal Typing
    terminal_lines = ["$ ", "$ python main.py", "--- VerityFlow-AI: Starting Swarm ---"]
    command = "python main.py"
    current_line = "$ "
    
    # Typing command
    for char in command:
        current_line += char
        frames.append(create_terminal_frame([current_line]))
        
    # Running
    frames.append(create_terminal_frame([current_line, "--- VerityFlow-AI: Starting Swarm ---"]))
    frames.append(create_terminal_frame([current_line, "--- VerityFlow-AI: Starting Swarm ---", "[Lead] Identifying core claims..."]))
    frames.append(create_terminal_frame([current_line, "--- VerityFlow-AI: Starting Swarm ---", "[Lead] Identifying core claims...", "[Analyst] Searching global news archives..."]))
    frames.append(create_terminal_frame([current_line, "--- VerityFlow-AI: Starting Swarm ---", "[Lead] Identifying core claims...", "[Analyst] Searching global news archives...", "[Auditor] Auditing sentiment markers..."]))
    
    # ASCII Table Output
    ascii_table = [
        "+--------------------------------+------------+------------+",
        "| Claim                          | Status     | Bias       |",
        "+--------------------------------+------------+------------+",
        "| AI Video in Swing States       | DEBUNKED   | Extreme    |",
        "| Deepfake Audio Leaks           | VERIFIED   | Moderate   |",
        "| Automated Bot Swarms           | VERIFIED   | High       |",
        "+--------------------------------+------------+------------+",
    ]
    for i in range(len(ascii_table)):
        frames.append(create_terminal_frame(terminal_lines[2:] + ascii_table[:i+1]))
        
    # Hold terminal
    for _ in range(20): frames.append(frames[-1])
    
    # Transition to UI
    ui_data = [
        ["AI Video in Swing States", "DEBUNKED", "98%", "Hyper-Partisan PAC"],
        ["Deepfake Audio Leaks", "VERIFIED", "89%", "State-Sponsored"],
        ["Automated Bot Swarms", "VERIFIED", "94%", "Undisclosed Ad-Tech"],
    ]
    ui_frame = create_ui_frame(ui_data)
    for _ in range(40): frames.append(ui_frame)
    
    # Save with Optimized Palette
    print("--- Saving Optimized GIF ---")
    OUTPUT = "images/title-animation.gif"
    os.makedirs("images", exist_ok=True)
    
    # Generate global palette from sample frames (MANDATORY)
    sample = Image.new("RGB", (WIDTH, HEIGHT * 3))
    sample.paste(frames[0], (0,0))
    sample.paste(frames[len(frames)//2], (0,HEIGHT))
    sample.paste(frames[-1], (0,HEIGHT*2))
    palette = sample.quantize(colors=256, method=2)
    
    # Convert all frames to P-mode using global palette (No Dither)
    final_frames = [f.quantize(palette=palette, dither=Image.Dither.NONE) for f in frames]
    final_frames[0].save(OUTPUT, save_all=True, append_images=final_frames[1:], optimize=True, loop=0, duration=100)
    print(f"GIF generated successfully at {OUTPUT}")

if __name__ == "__main__":
    generate_gif()
