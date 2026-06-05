#!/bin/bash

# Navigate to the workspace
cd "/Users/vutukurisaiteja/Downloads/website ff"

# Ensure directories exist
mkdir -p assets/posters
mkdir -p temp_thumbs

FILES=(
  "assets/videos/ai-avatar-intro.mov"
  "assets/videos/ai-avatar-virtual.mov"
  "assets/videos/ai-coffee.mp4"
  "assets/videos/ai-hanuman.mp4"
  "assets/videos/ai-reel.mov"
  "assets/videos/ai-sweet.mp4"
  "assets/videos/showreel.mp4"
)

# Process each file
for file in "${FILES[@]}"; do
  if [ -f "$file" ]; then
    filename=$(basename -- "$file")
    name="${filename%.*}"

    echo "Processing $name..."

    # 1. Generate PNG thumbnail using qlmanage
    qlmanage -t -s 1000 -o temp_thumbs "$file" >/dev/null 2>&1
    
    png_file="temp_thumbs/${filename}.png"
    webp_file="assets/posters/${name}.webp"
    
    if [ "$name" == "showreel" ]; then
       webp_file="assets/posters/showreel-poster.webp"
    fi

    # 2. Convert PNG to WebP using sips
    if [ -f "$png_file" ]; then
      sips -s format webp "$png_file" --out "$webp_file" >/dev/null 2>&1
    fi

    # 3. Generate trimmed 6-second preview using avconvert
    mp4_file="assets/posters/${name}-preview.mp4"
    if [ "$name" == "showreel" ]; then
       mp4_file="assets/posters/showreel-hero.mp4"
    fi

    echo "Compressing $name to 6s MP4..."
    avconvert --source "$file" --output "$mp4_file" --duration 6 --preset PresetMediumQuality --replace >/dev/null 2>&1

    # 4. Generate fallback WebM (copying mp4 since we don't have webm encoder)
    webm_file="assets/posters/${name}-preview.webm"
    if [ "$name" == "showreel" ]; then
       webm_file="assets/posters/showreel-hero.webm"
    fi
    
    if [ -f "$mp4_file" ]; then
      cp "$mp4_file" "$webm_file"
    fi

  else
    echo "Source file $file not found!"
  fi
done

# Cleanup temp
rm -rf temp_thumbs

echo "Asset generation complete!"
