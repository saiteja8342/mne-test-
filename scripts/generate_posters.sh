#!/bin/bash
cd "/Users/vutukurisaiteja/Downloads/website ff"
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

for file in "${FILES[@]}"; do
  filename=$(basename -- "$file")
  name="${filename%.*}"
  
  qlmanage -t -s 1000 -o temp_thumbs "$file" >/dev/null 2>&1
  png_file="temp_thumbs/${filename}.png"
  
  webp_file="assets/posters/${name}.webp"
  if [ "$name" == "showreel" ]; then
     webp_file="assets/posters/showreel-poster.webp"
  fi
  
  # Convert to jpg, then rename to webp
  if [ -f "$png_file" ]; then
    sips -s format jpeg "$png_file" --out "${webp_file}.jpg" >/dev/null 2>&1
    mv "${webp_file}.jpg" "$webp_file"
  fi
done

rm -rf temp_thumbs
echo "Done generating posters!"
