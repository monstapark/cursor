#!/usr/bin/env python3
"""
Generate advertisement video for AIR POS System
- Resolution: 1280x720
- Format: MP4
- Animation: Fade transitions only
- Duration: Short clip (~10-15 seconds)
"""

from moviepy import (
    TextClip, CompositeVideoClip,
    ColorClip, concatenate_videoclips, vfx
)
import os

# Video settings
WIDTH = 1280
HEIGHT = 720
DURATION_PER_SLIDE = 2.5  # seconds per slide
FADE_DURATION = 0.5  # fade in/out duration
FPS = 24
# Convert hex colors to RGB tuples
BG_COLOR = (26, 26, 46)  # Dark blue background #1a1a2e
TEXT_COLOR = (255, 255, 255)  # White text #ffffff
ACCENT_COLOR = (0, 212, 255)  # Cyan accent #00d4ff

def create_text_slide(text, subtext=None, duration=DURATION_PER_SLIDE, fontsize=80, subfontsize=50):
    """Create a text slide with fade animation"""
    # Main text
    txt_clip = TextClip(
        text=text,
        font_size=fontsize,
        color=TEXT_COLOR,
        method='caption',
        size=(int(WIDTH * 0.9), None),
        text_align='center'
    ).with_position('center').with_duration(duration).with_effects([vfx.FadeIn(FADE_DURATION), vfx.FadeOut(FADE_DURATION)])
    
    clips = [txt_clip]
    
    # Add subtext if provided
    if subtext:
        sub_txt_clip = TextClip(
            text=subtext,
            font_size=subfontsize,
            color=ACCENT_COLOR,
            method='caption',
            size=(int(WIDTH * 0.85), None),
            text_align='center'
        ).with_position(('center', HEIGHT * 0.6)).with_duration(duration).with_effects([vfx.FadeIn(FADE_DURATION), vfx.FadeOut(FADE_DURATION)])
        clips.append(sub_txt_clip)
    
    # Create background
    bg = ColorClip(size=(WIDTH, HEIGHT), color=BG_COLOR).with_duration(duration)
    
    # Composite all clips
    return CompositeVideoClip([bg] + clips)

def create_logo_slide(text, duration=DURATION_PER_SLIDE):
    """Create a slide with large logo text"""
    txt_clip = TextClip(
        text=text,
        font_size=120,
        color=ACCENT_COLOR,
        method='caption',
        size=(int(WIDTH * 0.9), None),
        text_align='center'
    ).with_position('center').with_duration(duration).with_effects([vfx.FadeIn(FADE_DURATION), vfx.FadeOut(FADE_DURATION)])
    
    bg = ColorClip(size=(WIDTH, HEIGHT), color=BG_COLOR).with_duration(duration)
    return CompositeVideoClip([bg, txt_clip])

def main():
    print("Creating AIR POS System advertisement video...")
    
    # Create slides
    slides = [
        create_logo_slide("AIR", duration=2.0),
        create_text_slide(
            "AI Integrated Retail",
            "POS System",
            duration=2.5
        ),
        create_text_slide(
            "Smart Management",
            "Intelligent inventory & analytics",
            duration=2.5
        ),
        create_text_slide(
            "Better Customer Experience",
            "Faster checkout, personalized service",
            duration=2.5
        ),
        create_text_slide(
            "AIR POS",
            "The future of retail",
            duration=2.0
        ),
    ]
    
    # Concatenate all slides
    print("Compositing video clips...")
    final_video = concatenate_videoclips(slides, method="compose")
    
    # Set FPS
    final_video = final_video.with_fps(FPS)
    
    # Write video file
    output_file = "air_pos_ad.mp4"
    print(f"Rendering video to {output_file}...")
    print("This may take a moment...")
    
    final_video.write_videofile(
        output_file,
        fps=FPS,
        codec='libx264',
        audio=False,
        preset='medium',
        bitrate='5000k'
    )
    
    print(f"\n✓ Video created successfully: {output_file}")
    print(f"  Resolution: {WIDTH}x{HEIGHT}")
    print(f"  Duration: {final_video.duration:.1f} seconds")
    print(f"  Format: MP4")

if __name__ == "__main__":
    main()
