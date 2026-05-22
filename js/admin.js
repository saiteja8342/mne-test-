/* ============================================
   MOTIONNODEEDITS — Admin Panel JS
   ============================================ */

const ADMIN_PASS = 'mne2024';

function initAuth() {
  const auth = sessionStorage.getItem('mne_admin_auth');
  const loginDiv = document.getElementById('adminLogin');
  const contentDiv = document.getElementById('adminContent');
  
  if (auth === 'true') {
    if (loginDiv) loginDiv.style.display = 'none';
    if (contentDiv) contentDiv.style.display = 'block';
    return true;
  } else {
    if (loginDiv) loginDiv.style.display = 'block';
    if (contentDiv) contentDiv.style.display = 'none';
    return false;
  }
}

function loginAdmin() {
  const pwdInput = document.getElementById('adminPwd');
  if (pwdInput.value === ADMIN_PASS) {
    sessionStorage.setItem('mne_admin_auth', 'true');
    initAuth();
    // Initialize admin panel content
    renderCategoryList();
    populateCategoryDropdown();
    renderAdminList();
  } else {
    alert('Incorrect password');
    pwdInput.value = '';
  }
}

function extractYouTubeId(url) {
  const match = url.match(/(?:youtu\.be\/|youtube\.com\/(?:watch\?v=|embed\/|shorts\/))([a-zA-Z0-9_-]{11})/);
  return match ? match[1] : url.length === 11 ? url : null;
}

// ── Category Management ──
const DEFAULT_CATEGORIES = [
  { slug: 'ai-ads', label: 'AI Ads' },
  { slug: 'ai-reels', label: 'AI Reels' },
  { slug: 'ai-avatar', label: 'AI Avatar Videos' },
  { slug: 'real-estate', label: 'Real Estate' },
  { slug: 'post-production', label: 'Post Production' }
];

function getCategories() {
  const saved = localStorage.getItem('mne_categories');
  return saved ? JSON.parse(saved) : DEFAULT_CATEGORIES;
}

function saveCategories(cats) {
  localStorage.setItem('mne_categories', JSON.stringify(cats));
}

function slugify(text) {
  return text.toLowerCase().trim().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '');
}

function populateCategoryDropdown() {
  const select = document.getElementById('addCategory');
  if (!select) return;
  const cats = getCategories();
  select.innerHTML = '';
  cats.forEach(c => {
    const opt = document.createElement('option');
    opt.value = c.slug;
    opt.textContent = c.label;
    select.appendChild(opt);
  });
}

function renderCategoryList() {
  const list = document.getElementById('categoryList');
  if (!list) return;
  const cats = getCategories();
  const portfolio = getPortfolio();
  list.innerHTML = '';

  if (cats.length === 0) {
    list.innerHTML = '<p style="color:var(--text-muted);font-size:0.85rem;">No categories yet. Add one above.</p>';
    return;
  }

  cats.forEach((cat, i) => {
    const count = portfolio.filter(v => v.category === cat.slug).length;
    const row = document.createElement('div');
    row.className = 'cat-row';
    row.innerHTML = `
      <span class="cat-slug">${cat.slug}</span>
      <span class="cat-label">${cat.label}</span>
      <span class="cat-count">${count} video${count !== 1 ? 's' : ''}</span>
      <div class="cat-actions">
        <button onclick="renameCategory(${i})" class="admin-btn admin-btn-edit">Rename</button>
        <button onclick="deleteCategory(${i})" class="admin-btn admin-btn-delete">Delete</button>
      </div>
    `;
    list.appendChild(row);
  });
}

function addCategory() {
  const nameInput = document.getElementById('newCatName');
  const name = nameInput.value.trim();
  if (!name) { alert('Please enter a category name.'); return; }

  const slug = slugify(name);
  const cats = getCategories();

  if (cats.some(c => c.slug === slug)) {
    alert('A category with this slug already exists: ' + slug);
    return;
  }

  cats.push({ slug, label: name });
  saveCategories(cats);
  nameInput.value = '';
  document.getElementById('newCatSlug').value = '';
  renderCategoryList();
  populateCategoryDropdown();
  showToast('Category "' + name + '" added');
}

function renameCategory(index) {
  const cats = getCategories();
  const cat = cats[index];
  const newName = prompt('Rename category "' + cat.label + '":', cat.label);
  if (newName === null || newName.trim() === '') return;

  const newSlug = slugify(newName);
  const oldSlug = cat.slug;

  // Check for slug collision with a different category
  if (newSlug !== oldSlug && cats.some(c => c.slug === newSlug)) {
    alert('A category with slug "' + newSlug + '" already exists.');
    return;
  }

  // Update all portfolio videos with the old slug
  if (newSlug !== oldSlug) {
    const portfolio = getPortfolio();
    portfolio.forEach(v => { if (v.category === oldSlug) v.category = newSlug; });
    savePortfolio(portfolio);
  }

  cats[index] = { slug: newSlug, label: newName.trim() };
  saveCategories(cats);
  renderCategoryList();
  renderAdminList();
  populateCategoryDropdown();
  showToast('Category renamed to "' + newName.trim() + '"');
}

function deleteCategory(index) {
  const cats = getCategories();
  const cat = cats[index];
  const portfolio = getPortfolio();
  const count = portfolio.filter(v => v.category === cat.slug).length;

  let msg = 'Delete category "' + cat.label + '"?';
  if (count > 0) msg += '\n\nWarning: ' + count + ' video(s) use this category. They will become uncategorized.';

  if (!confirm(msg)) return;

  cats.splice(index, 1);
  saveCategories(cats);
  renderCategoryList();
  populateCategoryDropdown();
  showToast('Category "' + cat.label + '" deleted');
}

function getPortfolio() {
  const saved = localStorage.getItem('mne_portfolio');
  if (saved) return JSON.parse(saved);
  // Return defaults from main.js
  return [
    { id:'1', title:'Luxury Perfume AI Ad', category:'ai-ads', youtubeId:'dQw4w9WgXcQ', desc:'AI-generated luxury fragrance commercial' },
    { id:'2', title:'Coffee Morning', category:'ai-ads', youtubeId:'ScMzIvxBSi4', desc:'Premium AI coffee commercial' },
    { id:'3', title:'Sweet Delights', category:'ai-ads', youtubeId:'LXb3EKWsInQ', desc:'AI candy brand showcase' },
    { id:'4', title:'Urban Fashion Reel', category:'ai-reels', youtubeId:'2Vv-BfVoq4g', desc:'Hyper-edited AI fashion reel' },
    { id:'5', title:'Tech Product Launch', category:'ai-reels', youtubeId:'jNQXAC9IVRw', desc:'Futuristic product reveal' },
    { id:'6', title:'AI Avatar Presenter', category:'ai-avatar', youtubeId:'dQw4w9WgXcQ', desc:'AI avatar business presentation' },
    { id:'7', title:'Digital Human Host', category:'ai-avatar', youtubeId:'ScMzIvxBSi4', desc:'Realistic AI avatar hosting' },
    { id:'8', title:'Modern Villa Tour', category:'real-estate', youtubeId:'LXb3EKWsInQ', desc:'Cinematic real estate walkthrough' },
    { id:'9', title:'Skyline Penthouse', category:'real-estate', youtubeId:'2Vv-BfVoq4g', desc:'Luxury property showcase' },
    { id:'10', title:'Color Grading Reel', category:'post-production', youtubeId:'jNQXAC9IVRw', desc:'Professional color grading demo' },
    { id:'11', title:'VFX Breakdown', category:'post-production', youtubeId:'dQw4w9WgXcQ', desc:'Visual effects compositing' },
    { id:'12', title:'Neon Night Drive', category:'ai-ads', youtubeId:'ScMzIvxBSi4', desc:'Cinematic night automotive ad' },
  ];
}

function savePortfolio(data) {
  localStorage.setItem('mne_portfolio', JSON.stringify(data));
}

function renderAdminList() {
  const list = document.getElementById('adminVideoList');
  if (!list) return;
  const data = getPortfolio();
  list.innerHTML = '';
  data.forEach((v, i) => {
    const row = document.createElement('div');
    row.className = 'admin-video-row';
    row.innerHTML = `
      <img src="https://img.youtube.com/vi/${v.youtubeId}/mqdefault.jpg" alt="${v.title}" class="admin-thumb">
      <div class="admin-video-info">
        <strong>${v.title}</strong>
        <span class="admin-video-cat">${v.category}</span>
        <span class="admin-video-desc">${v.desc || ''}</span>
      </div>
      <div class="admin-video-actions">
        <button onclick="editVideo(${i})" class="admin-btn admin-btn-edit">Edit</button>
        <button onclick="deleteVideo(${i})" class="admin-btn admin-btn-delete">Delete</button>
        ${i > 0 ? `<button onclick="moveVideo(${i},-1)" class="admin-btn">↑</button>` : ''}
        ${i < data.length - 1 ? `<button onclick="moveVideo(${i},1)" class="admin-btn">↓</button>` : ''}
      </div>
    `;
    list.appendChild(row);
  });
}

function addVideo() {
  const url = document.getElementById('addUrl').value.trim();
  const title = document.getElementById('addTitle').value.trim();
  const category = document.getElementById('addCategory').value;
  const desc = document.getElementById('addDesc').value.trim();

  if (!url || !title) { alert('URL and title required'); return; }
  const youtubeId = extractYouTubeId(url);
  if (!youtubeId) { alert('Invalid YouTube URL'); return; }

  const data = getPortfolio();
  data.push({ id: Date.now().toString(), title, category, youtubeId, desc });
  savePortfolio(data);
  renderAdminList();

  document.getElementById('addUrl').value = '';
  document.getElementById('addTitle').value = '';
  document.getElementById('addDesc').value = '';
  showToast('Video added successfully');
}

function deleteVideo(index) {
  if (!confirm('Delete this video?')) return;
  const data = getPortfolio();
  data.splice(index, 1);
  savePortfolio(data);
  renderAdminList();
  showToast('Video deleted');
}

function editVideo(index) {
  const data = getPortfolio();
  const v = data[index];
  const cats = getCategories();
  
  const title = prompt('Title:', v.title);
  if (title === null) return;
  
  const desc = prompt('Description:', v.desc || '');
  if (desc === null) return;

  const url = prompt('YouTube URL or ID:', v.youtubeId);
  if (url === null) return;
  const youtubeId = extractYouTubeId(url) || v.youtubeId;

  const catList = cats.map((c, i) => `${i + 1}. ${c.label}`).join('\n');
  const catChoice = prompt(`Choose Category (number):\n${catList}`, cats.findIndex(c => c.slug === v.category) + 1);
  const selectedCat = cats[parseInt(catChoice) - 1];
  const category = selectedCat ? selectedCat.slug : v.category;

  data[index] = { ...v, title: title.trim() || v.title, desc: desc.trim(), youtubeId, category };
  savePortfolio(data);
  renderAdminList();
  showToast('Video updated');
}

function moveVideo(index, dir) {
  const data = getPortfolio();
  const newIndex = index + dir;
  if (newIndex < 0 || newIndex >= data.length) return;
  [data[index], data[newIndex]] = [data[newIndex], data[index]];
  savePortfolio(data);
  renderAdminList();
}

function resetPortfolio() {
  if (!confirm('Reset to default portfolio? This will remove all edits.')) return;
  localStorage.removeItem('mne_portfolio');
  renderAdminList();
  showToast('Portfolio reset to defaults');
}

function showToast(msg) {
  const toast = document.getElementById('adminToast');
  if (!toast) return;
  toast.textContent = msg;
  toast.classList.add('show');
  setTimeout(() => toast.classList.remove('show'), 3000);
}

document.addEventListener('DOMContentLoaded', () => {
  if (initAuth()) {
    renderCategoryList();
    populateCategoryDropdown();
    renderAdminList();
  }

  // Auto-generate slug as user types category name
  const catNameInput = document.getElementById('newCatName');
  const catSlugInput = document.getElementById('newCatSlug');
  if (catNameInput && catSlugInput) {
    catNameInput.addEventListener('input', () => {
      catSlugInput.value = slugify(catNameInput.value);
    });
  }
});
