import re

with open('js/app.js', 'r') as f:
    js = f.read()

# Replace initWorkCards logic
new_init = """  function initWorkCards() {
    function updatePlayBtn(card, isPlaying) {
      const iconPause = card.querySelector('.icon-pause');
      const iconPlay = card.querySelector('.icon-play');
      if (iconPause && iconPlay) {
        iconPause.style.display = isPlaying ? 'block' : 'none';
        iconPlay.style.display = isPlaying ? 'none' : 'block';
      }
    }

    document.querySelectorAll('.work-card').forEach(card => {
      const vid = card.querySelector('.wc-vid');
      if (!vid) return;

      // Autoplay on hover, pause on mouseout
      card.addEventListener('mouseenter', () => {
        if (vid.dataset.manualPause !== 'true') {
          vid.play().catch(() => {});
          updatePlayBtn(card, true);
        }
      });
      card.addEventListener('mouseleave', () => {
        vid.pause();
        updatePlayBtn(card, false);
      });

      const btnPlayPause = card.querySelector('.wc-btn-playpause');
      const btnMute = card.querySelector('.wc-btn-mute');

      if (btnPlayPause) {
        btnPlayPause.addEventListener('click', (e) => {
          e.preventDefault();
          e.stopPropagation();
          if (vid.paused) {
            vid.dataset.manualPause = 'false';
            vid.play().catch(() => {});
            updatePlayBtn(card, true);
          } else {
            vid.dataset.manualPause = 'true';
            vid.pause();
            updatePlayBtn(card, false);
          }
        });
      }

      if (btnMute) {
        btnMute.addEventListener('click', (e) => {
          e.preventDefault();
          e.stopPropagation();
          vid.muted = !vid.muted;
          const iconMuted = card.querySelector('.icon-muted');
          const iconUnmuted = card.querySelector('.icon-unmuted');
          if (vid.muted) {
            if(iconUnmuted) iconUnmuted.style.display = 'none';
            if(iconMuted) iconMuted.style.display = 'block';
          } else {
            if(iconMuted) iconMuted.style.display = 'none';
            if(iconUnmuted) iconUnmuted.style.display = 'block';
          }
        });
      }

      const btnFullscreen = card.querySelector('.wc-btn-fullscreen');
      if (btnFullscreen) {
        btnFullscreen.addEventListener('click', (e) => {
          e.preventDefault();
          e.stopPropagation();
          if (vid.requestFullscreen) {
            vid.requestFullscreen();
          } else if (vid.webkitRequestFullscreen) { /* Safari */
            vid.webkitRequestFullscreen();
          } else if (vid.msRequestFullscreen) { /* IE11 */
            vid.msRequestFullscreen();
          }
        });
      }
    });
  }"""

# Use regex to replace the function definition
js = re.sub(r'function initWorkCards\(\) \{[\s\S]*?\}\n\s*\}\n', new_init + '\n', js)
with open('js/app.js', 'w') as f:
    f.write(js)
print("Updated app.js")
