#!/bin/bash

# Navigate to the workspace
cd "/Users/vutukurisaiteja/Downloads/website ff"

# Create a posters directory
mkdir -p assets/posters

# Original files
FILES=(
  "assets/ai-avatar-intro.mov"
  "assets/ai-avatar-virtual.mov"
  "assets/ai-coffee.mp4"
  "assets/ai-hanuman.mp4"
  "assets/ai-reel.mov"
  "assets/ai-sweet.mp4"
)

for file in "${FILES[@]}"; do
  if [ -f "$file" ]; then
    filename=$(basename -- "$file")
    name="${filename%.*}"

    echo "Processing $name..."

    # Extract poster
    ffmpeg -y -i "$file" -vframes 1 -q:v 2 "assets/posters/$name.webp"

    # Create optimized preview (6 seconds, 720p, lower bitrate)
    # MP4
    ffmpeg -y -i "$file" -t 6 -vf "scale=-2:720" -c:v libx264 -crf 28 -preset fast -an "assets/posters/$name-preview.mp4"
    # WebM
    ffmpeg -y -i "$file" -t 6 -vf "scale=-2:720" -c:v libvpx-vp9 -crf 35 -b:v 1M -preset fast -an "assets/posters/$name-preview.webm"
  fi
done

# Hero video (showreel.mp4) optimization
if [ -f "assets/showreel.mp4" ]; then
  echo "Processing showreel..."
  # Poster
  ffmpeg -y -i "assets/showreel.mp4" -vframes 1 -q:v 2 "assets/posters/showreel-poster.webp"
  
  # Hero optimized version (10 seconds, 720p, muted)
  ffmpeg -y -i "assets/showreel.mp4" -t 10 -vf "scale=-2:720" -c:v libx264 -crf 28 -preset fast -an "assets/posters/showreel-hero.mp4"
  ffmpeg -y -i "assets/showreel.mp4" -t 10 -vf "scale=-2:720" -c:v libvpx-vp9 -crf 35 -b:v 1M -preset fast -an "assets/posters/showreel-hero.webm"
fi

echo "Done!"
