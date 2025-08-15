document.addEventListener('DOMContentLoaded', () => {
  const topicSel = document.getElementById('topic');
  const qInput   = document.getElementById('quality') || { value: 80 };
  const applyBtn = document.getElementById('apply');
  const urlOut   = document.getElementById('stream-url');

  // Ensure an <img> exists to render the MJPEG
  let img = document.getElementById('mjpeg-view');
  if (!img) {
    img = document.createElement('img');
    img.id = 'mjpeg-view';
    img.alt = 'Live camera';
    img.style.maxWidth = '100%';
    img.style.width = '640px';
    img.style.height = 'auto';
    // Try to place it in a container if present; else append to body
    const holder = document.getElementById('stream-container') || document.body;
    holder.appendChild(img);
  }

  function buildUrl() {
    const t = (topicSel && topicSel.value) ? topicSel.value : '/image_raw';
    const q = (qInput && qInput.value) ? qInput.value : 80;
    const u = `/stream?topic=${encodeURIComponent(t)}&type=mjpeg&quality=${encodeURIComponent(q)}`;
    if (urlOut) urlOut.textContent = u;
    // Bust any caching when changing params
    img.src = u + `&ts=${Date.now()}`;
  }

  if (applyBtn) applyBtn.addEventListener('click', (e) => { e.preventDefault(); buildUrl(); });
  if (topicSel) topicSel.addEventListener('change', buildUrl);

  // Auto-start once the page loads
  buildUrl();
});
