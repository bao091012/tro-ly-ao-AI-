/* ============================================================
   AI ASSISTANT — script.js
   Full functionality: Theme, Navigation, 6 Tools, Toast
   ============================================================ */

'use strict';

// ── UTILS ────────────────────────────────────────────────────
const $ = id => document.getElementById(id);
const $$ = sel => document.querySelectorAll(sel);

function escapeHtml(str) {
  return String(str)
    .replace(/&/g,'&amp;')
    .replace(/</g,'&lt;')
    .replace(/>/g,'&gt;')
    .replace(/"/g,'&quot;')
    .replace(/'/g,'&#039;');
}

function showToast(msg, duration = 2800) {
  const t = $('toast');
  t.textContent = msg;
  t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), duration);
}

function setLoading(btnId, on) {
  const btn = $(btnId);
  if (!btn) return;
  btn.disabled = on;
  if (on) btn.classList.add('loading');
  else btn.classList.remove('loading');
}

function renderAlert(type, msg) {
  const icons = { success:'fa-circle-check', error:'fa-circle-xmark', warning:'fa-triangle-exclamation', info:'fa-circle-info' };
  return `<div class="alert alert-${type}"><i class="fa-solid ${icons[type]||'fa-info'}"></i><span>${msg}</span></div>`;
}

function renderSkeleton(rows = 1) {
  return Array.from({length: rows}, () =>
    `<div class="skeleton" style="height:56px;margin-bottom:10px;border-radius:14px;"></div>`
  ).join('');
}

// ── THEME ────────────────────────────────────────────────────
const Theme = {
  KEY: 'ai-theme',
  current() { return localStorage.getItem(this.KEY) || 'light'; },
  apply(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem(this.KEY, theme);
    $('themeLabel').textContent = theme === 'light' ? 'Tối' : 'Sáng';
  },
  toggle() {
    const next = this.current() === 'light' ? 'dark' : 'light';
    this.apply(next);
    showToast(next === 'dark' ? '🌙 Đã bật chế độ tối' : '☀️ Đã bật chế độ sáng');
  },
  init() {
    this.apply(this.current());
    $('themeToggle').addEventListener('click', () => this.toggle());
  }
};

// ── SIDEBAR ──────────────────────────────────────────────────
const Sidebar = {
  init() {
    $('sidebarToggle').addEventListener('click', () => {
      document.querySelector('.sidebar').classList.toggle('open');
    });
    // Close on outside click (mobile)
    document.addEventListener('click', e => {
      const sidebar = document.querySelector('.sidebar');
      if (window.innerWidth <= 900 &&
          !sidebar.contains(e.target) &&
          !$('sidebarToggle').contains(e.target)) {
        sidebar.classList.remove('open');
      }
    });
  }
};

// ── NAVIGATION ───────────────────────────────────────────────
const Nav = {
  pages: { home: 'Tổng Quan', tools: 'Công Cụ', settings: 'Cài Đặt' },

  goTo(pageId) {
    $$('.page').forEach(p => p.classList.remove('active'));
    $$('.nav-item[data-page]').forEach(n => n.classList.remove('active'));

    const page = $(`page-${pageId}`);
    if (page) page.classList.add('active');

    const navLink = document.querySelector(`.nav-item[data-page="${pageId}"]`);
    if (navLink) navLink.classList.add('active');

    $('breadcrumbCurrent').textContent = this.pages[pageId] || pageId;

    if (window.innerWidth <= 900)
      document.querySelector('.sidebar').classList.remove('open');
  },

  openTool(toolId) {
    this.goTo('tools');
    Tabs.switchTo(toolId);
    // Highlight sidebar tool link
    $$('.nav-item.tool-link').forEach(l => l.classList.remove('active'));
    const link = document.querySelector(`.nav-item[data-tool="${toolId}"]`);
    if (link) link.classList.add('active');
  },

  init() {
    // Page nav
    $$('.nav-item[data-page]').forEach(link => {
      link.addEventListener('click', e => {
        e.preventDefault();
        this.goTo(link.dataset.page);
      });
    });

    // Sidebar tool links
    $$('.nav-item.tool-link').forEach(link => {
      link.addEventListener('click', e => {
        e.preventDefault();
        this.openTool(link.dataset.tool);
      });
    });

    // Stat cards on home
    $$('[data-tool-open]').forEach(card => {
      card.addEventListener('click', () => this.openTool(card.dataset.toolOpen));
    });
  }
};

// ── TABS ─────────────────────────────────────────────────────
const Tabs = {
  switchTo(tabId) {
    $$('.tab-btn').forEach(b => b.classList.remove('active'));
    $$('.tab-panel').forEach(p => p.classList.remove('active'));

    const btn = document.querySelector(`.tab-btn[data-tab="${tabId}"]`);
    const panel = $(`tab-${tabId}`);
    if (btn) btn.classList.add('active');
    if (panel) panel.classList.add('active');
  },

  init() {
    $$('.tab-btn').forEach(btn => {
      btn.addEventListener('click', () => this.switchTo(btn.dataset.tab));
    });
  }
};

// ── API KEYS ─────────────────────────────────────────────────
const Keys = {
  get google()  { return localStorage.getItem('ai-google-key')  || 'AQ.Ab8RN6LasT9VWVMeub7XXB4VPt0v9X5qQAjEKOBMBLSNGxqIZA'; },
  get weather() { return localStorage.getItem('ai-weather-key') || '614859b889a9e5d051c60d45643f2de6'; },

  save() {
    const g = $('googleApiKey').value.trim();
    const w = $('weatherApiKey').value.trim();
    if (g) localStorage.setItem('ai-google-key', g);
    if (w) localStorage.setItem('ai-weather-key', w);
    $('googleStatus').innerHTML  = g ? '<span class="status-success">✅ Đã lưu</span>' : '';
    $('weatherKeyStatus').innerHTML = w ? '<span class="status-success">✅ Đã lưu</span>' : '';
    showToast('✅ Đã lưu cài đặt API Keys');
  },

  load() {
    const g = this.google;
    const w = this.weather;
    if (g) { $('googleApiKey').value = g;  $('googleStatus').innerHTML = '<span class="status-success">✅ Đã kích hoạt</span>'; }
    if (w) { $('weatherApiKey').value = w; $('weatherKeyStatus').innerHTML = '<span class="status-success">✅ Đã kích hoạt</span>'; }
  },

  init() {
    this.load();
    $('saveKeysBtn').addEventListener('click', () => this.save());
    $('googleApiKey').addEventListener('change', () => this.save());
    $('weatherApiKey').addEventListener('change', () => this.save());
  }
};

// ── CALCULATOR ───────────────────────────────────────────────
const Calculator = {
  evaluate(expr) {
    // Replace common math names
    let safe = expr
      .replace(/sqrt/g,  'Math.sqrt')
      .replace(/cbrt/g,  'Math.cbrt')
      .replace(/abs/g,   'Math.abs')
      .replace(/sin/g,   'Math.sin')
      .replace(/cos/g,   'Math.cos')
      .replace(/tan/g,   'Math.tan')
      .replace(/log/g,   'Math.log10')
      .replace(/ln/g,    'Math.log')
      .replace(/pow/g,   'Math.pow')
      .replace(/PI/g,    'Math.PI')
      .replace(/E(?![a-z])/g, 'Math.E')
      .replace(/floor/g, 'Math.floor')
      .replace(/ceil/g,  'Math.ceil')
      .replace(/round/g, 'Math.round');

    // Validate: only allow safe chars after replacement
    if (/[a-zA-Z]/.test(safe.replace(/Math\.[a-zA-Z]+/g, ''))) {
      throw new Error('Biểu thức chứa ký tự không hợp lệ');
    }
    // eslint-disable-next-line no-eval
    const result = eval(safe);
    if (typeof result !== 'number') throw new Error('Kết quả không phải số');
    if (!isFinite(result)) throw new Error('Kết quả không xác định (chia cho 0?)');
    return result;
  },

  render(expr, result) {
    const formatted = Number.isInteger(result) ? result : parseFloat(result.toFixed(10));
    $('calcResult').innerHTML = `
      <div class="result-block">
        <div class="calc-result-box">
          <div class="calc-expr">Biểu thức: <span>${escapeHtml(expr)}</span></div>
          <div class="calc-eq">=</div>
          <div class="calc-answer">${formatted}</div>
        </div>
      </div>`;
  },

  run() {
    const expr = $('calcInput').value.trim();
    if (!expr) { $('calcResult').innerHTML = renderAlert('warning', 'Vui lòng nhập biểu thức'); return; }
    try {
      const result = this.evaluate(expr);
      this.render(expr, result);
    } catch (err) {
      $('calcResult').innerHTML = renderAlert('error', `❌ ${err.message}`);
    }
  },

  init() {
    $('calcBtn').addEventListener('click', () => this.run());
    $('calcInput').addEventListener('keydown', e => { if (e.key === 'Enter') this.run(); });
    $$('.example-calc').forEach(chip => {
      chip.addEventListener('click', () => {
        $('calcInput').value = chip.dataset.v;
        this.run();
      });
    });
  }
};

// ── WEATHER ──────────────────────────────────────────────────
const Weather = {
  weatherKey() { return $('weatherApiKey')?.value.trim() || Keys.weather; },

  async fetch(city) {
    const key = this.weatherKey();
    if (!key) throw new Error('Chưa nhập OpenWeather API Key. Vào Cài Đặt để nhập.');
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${encodeURIComponent(city)}&appid=${key}&units=metric&lang=vi`;
    const res = await fetch(url);
    if (res.status === 401) throw new Error('API Key không hợp lệ');
    if (res.status === 404) throw new Error(`Không tìm thấy thành phố "${city}"`);
    if (!res.ok) throw new Error(`Lỗi máy chủ (${res.status})`);
    return res.json();
  },

  render(data) {
    const { name, main, weather, wind, clouds, sys } = data;
    const desc = weather[0]?.description || '';
    const icon = weather[0]?.icon || '';
    const iconUrl = icon ? `https://openweathermap.org/img/wn/${icon}@2x.png` : '';
    const feelsLike = main.feels_like?.toFixed(1);
    const country = sys?.country || '';

    $('weatherResult').innerHTML = `
      <div class="result-block">
        <div class="result-item" style="margin-bottom:12px;text-align:left;padding:20px 22px;display:flex;align-items:center;gap:16px;">
          ${iconUrl ? `<img src="${iconUrl}" alt="${escapeHtml(desc)}" width="64" height="64" style="flex-shrink:0;">` : ''}
          <div>
            <div style="font-size:1.25rem;font-weight:700;color:var(--txt-primary)">📍 ${escapeHtml(name)}${country ? ', '+country : ''}</div>
            <div style="font-size:1rem;color:var(--txt-secondary);margin-top:4px;text-transform:capitalize">${escapeHtml(desc)}</div>
          </div>
        </div>
        <div class="result-grid-4">
          <div class="result-item">
            <div class="result-item-label">🌡️ Nhiệt độ</div>
            <div class="result-item-value" style="color:var(--color-error)">${main.temp?.toFixed(1)}°C</div>
          </div>
          <div class="result-item">
            <div class="result-item-label">🤔 Cảm giác</div>
            <div class="result-item-value" style="color:var(--color-warning)">${feelsLike}°C</div>
          </div>
          <div class="result-item">
            <div class="result-item-label">💧 Độ ẩm</div>
            <div class="result-item-value" style="color:var(--color-accent)">${main.humidity}%</div>
          </div>
          <div class="result-item">
            <div class="result-item-label">💨 Gió</div>
            <div class="result-item-value" style="color:var(--color-primary)">${wind.speed?.toFixed(1)} m/s</div>
          </div>
        </div>
      </div>`;
  },

  async run(city) {
    city = city || $('weatherInput').value.trim();
    if (!city) { $('weatherResult').innerHTML = renderAlert('warning', 'Vui lòng nhập tên thành phố'); return; }
    $('weatherResult').innerHTML = renderSkeleton(1) + renderSkeleton(1);
    setLoading('weatherBtn', true);
    try {
      const data = await this.fetch(city);
      this.render(data);
    } catch (err) {
      $('weatherResult').innerHTML = renderAlert('error', err.message);
    } finally {
      setLoading('weatherBtn', false);
    }
  },

  init() {
    $('weatherBtn').addEventListener('click', () => this.run());
    $('weatherInput').addEventListener('keydown', e => { if (e.key === 'Enter') this.run(); });
    $$('.city-chip').forEach(chip => {
      chip.addEventListener('click', () => { $('weatherInput').value = chip.dataset.c; this.run(chip.dataset.c); });
    });
  }
};

// ── TRANSLATOR ───────────────────────────────────────────────
const Translator = {
  langNames: {
    vi:'Tiếng Việt',
    en:'Tiếng Anh', fr:'Tiếng Pháp', es:'Tiếng Tây Ban Nha',
    de:'Tiếng Đức', ja:'Tiếng Nhật', zh:'Tiếng Trung',
    ko:'Tiếng Hàn', hi:'Tiếng Ấn Độ', pt:'Tiếng Bồ Đào Nha'
  },

  async fetch(text, targetCode) {
    const url = `https://api.mymemory.translated.net/get?q=${encodeURIComponent(text)}&langpair=vi|${targetCode}`;
    const res = await fetch(url);
    if (!res.ok) throw new Error(`Lỗi mạng (${res.status})`);
    const data = await res.json();
    if (data.responseStatus !== 200) throw new Error('Dịch thất bại, thử lại sau.');
    return data.responseData.translatedText;
  },

  async run() {
    const text = $('translateInput').value.trim();
    const targetCode = $('targetLang').value;
    const targetName = this.langNames[targetCode] || targetCode;

    if (!text) { $('translateResult').innerHTML = renderAlert('warning', 'Vui lòng nhập văn bản cần dịch'); return; }
    if (text.length > 500) { $('translateResult').innerHTML = renderAlert('warning', 'Văn bản quá dài (tối đa 500 ký tự)'); return; }

    $('translateResult').innerHTML = renderSkeleton(1);
    setLoading('translateBtn', true);
    try {
      const translated = await this.fetch(text, targetCode);
      $('translateResult').innerHTML = `
        <div class="result-block">
          <div class="translate-pair">
            <div class="translate-box">
              <div class="translate-box-label">🇻🇳 Tiếng Việt</div>
              <div class="translate-box-text">${escapeHtml(text)}</div>
            </div>
            <div class="translate-box output">
              <div class="translate-box-label">${escapeHtml(targetName)}</div>
              <div class="translate-box-text">${escapeHtml(translated)}</div>
            </div>
          </div>
        </div>`;
    } catch (err) {
      $('translateResult').innerHTML = renderAlert('error', err.message);
    } finally {
      setLoading('translateBtn', false);
    }
  },

  init() {
    $('translateBtn').addEventListener('click', () => this.run());
  }
};

// ── TIME ─────────────────────────────────────────────────────
const TimeModule = {
  days: ['Chủ Nhật','Thứ Hai','Thứ Ba','Thứ Tư','Thứ Năm','Thứ Sáu','Thứ Bảy'],

  run() {
    const now = new Date();
    const hh = String(now.getHours()).padStart(2,'0');
    const mm = String(now.getMinutes()).padStart(2,'0');
    const ss = String(now.getSeconds()).padStart(2,'0');
    const time = `${hh}:${mm}:${ss}`;
    const date = `${String(now.getDate()).padStart(2,'0')}/${String(now.getMonth()+1).padStart(2,'0')}/${now.getFullYear()}`;
    const day  = this.days[now.getDay()];
    const ts   = now.toLocaleString('vi-VN', { timeZone: 'Asia/Ho_Chi_Minh' });

    $('timeResult').innerHTML = `
      <div class="result-block">
        <div class="result-grid-3">
          <div class="result-item">
            <div class="result-item-label">⏰ Giờ</div>
            <div class="result-item-value" style="color:var(--color-primary)">${time}</div>
          </div>
          <div class="result-item">
            <div class="result-item-label">📅 Ngày</div>
            <div class="result-item-value" style="color:var(--color-accent)">${date}</div>
          </div>
          <div class="result-item">
            <div class="result-item-label">📆 Thứ</div>
            <div class="result-item-value" style="color:var(--color-success)">${day}</div>
          </div>
        </div>
        <div style="margin-top:12px;font-size:.8125rem;color:var(--txt-muted);text-align:center">
          Múi giờ: Việt Nam (UTC+7) — ${escapeHtml(ts)}
        </div>
      </div>`;
  },

  init() {
    $('timeBtn').addEventListener('click', () => this.run());
  }
};

// ── SEARCH ───────────────────────────────────────────────────
const Search = {
  async fetch(query) {
    const url = `https://vi.wikipedia.org/w/api.php?action=query&format=json&list=search&srsearch=${encodeURIComponent(query)}&srlimit=5&utf8=1&origin=*`;
    const res = await fetch(url);
    if (!res.ok) throw new Error(`Lỗi mạng (${res.status})`);
    const data = await res.json();
    return data.query?.search || [];
  },

  cleanSnippet(html) {
    return html
      .replace(/<span[^>]*class="searchmatch"[^>]*>(.*?)<\/span>/gi, '$1')
      .replace(/<[^>]+>/g, '')
      .replace(/&quot;/g, '"')
      .replace(/&amp;/g, '&')
      .replace(/&lt;/g, '<')
      .replace(/&gt;/g, '>')
      .replace(/&#039;/g, "'")
      .trim();
  },

  render(query, results) {
    if (!results.length) {
      $('searchResult').innerHTML = `
        <div class="empty-state">
          <i class="fa-solid fa-magnifying-glass"></i>
          <p>Không tìm thấy kết quả cho "<strong>${escapeHtml(query)}</strong>"</p>
        </div>`;
      return;
    }

    const items = results.map((r, i) => {
      const snippet = this.cleanSnippet(r.snippet);
      const wikiUrl = `https://vi.wikipedia.org/wiki/${encodeURIComponent(r.title)}`;
      return `
        <details class="search-item" ${i === 0 ? 'open' : ''}>
          <summary>
            <i class="fa-solid fa-${i === 0 ? 'chevron-down' : 'chevron-right'}" style="font-size:.75rem;color:var(--txt-muted)"></i>
            ${escapeHtml(r.title)}
          </summary>
          <div class="search-item-body">
            <p>${escapeHtml(snippet)}${snippet.length >= 250 ? '…' : ''}</p>
            <a href="${wikiUrl}" target="_blank" rel="noopener" class="search-item-link">
              Đọc thêm trên Wikipedia <i class="fa-solid fa-arrow-up-right-from-square" style="font-size:.75rem"></i>
            </a>
          </div>
        </details>`;
    }).join('');

    $('searchResult').innerHTML = `
      <div class="result-block">
        <div style="font-size:.875rem;color:var(--txt-muted);margin-bottom:12px;">
          Tìm thấy ${results.length} kết quả cho "<strong>${escapeHtml(query)}</strong>" trên Wikipedia
        </div>
        ${items}
      </div>`;
  },

  async run(q) {
    const query = q || $('searchInput').value.trim();
    if (!query) { $('searchResult').innerHTML = renderAlert('warning', 'Vui lòng nhập từ khoá'); return; }
    $('searchResult').innerHTML = renderSkeleton(3);
    setLoading('searchBtn', true);
    try {
      const results = await this.fetch(query);
      this.render(query, results);
    } catch (err) {
      $('searchResult').innerHTML = renderAlert('error', err.message);
    } finally {
      setLoading('searchBtn', false);
    }
  },

  init() {
    $('searchBtn').addEventListener('click', () => this.run());
    $('searchInput').addEventListener('keydown', e => { if (e.key === 'Enter') this.run(); });
    $$('.search-chip').forEach(chip => {
      chip.addEventListener('click', () => { $('searchInput').value = chip.dataset.q; this.run(chip.dataset.q); });
    });
  }
};

// ── JSON FORMATTER ───────────────────────────────────────────
const JsonFormatter = {
  run() {
    const input = $('jsonInput').value.trim();
    if (!input) { $('jsonResult').innerHTML = renderAlert('warning', 'Vui lòng nhập JSON'); return; }
    try {
      const parsed = JSON.parse(input);
      const formatted = JSON.stringify(parsed, null, 2);
      const lines = formatted.split('\n').length;
      $('jsonResult').innerHTML = `
        <div class="result-block">
          ${renderAlert('success', `✅ JSON hợp lệ — ${lines} dòng`)}
          <div class="json-output-wrap">
            <pre>${escapeHtml(formatted)}</pre>
          </div>
          <div style="margin-top:10px">
            <button class="btn btn-outline" id="copyJsonBtn" style="font-size:.875rem">
              <i class="fa-solid fa-copy"></i> Sao Chép
            </button>
          </div>
        </div>`;
      $('copyJsonBtn').addEventListener('click', () => {
        navigator.clipboard.writeText(formatted)
          .then(() => showToast('✅ Đã sao chép JSON'))
          .catch(() => showToast('❌ Không thể sao chép'));
      });
    } catch (err) {
      $('jsonResult').innerHTML = renderAlert('error', `❌ JSON không hợp lệ: ${err.message}`);
    }
  },

  clear() {
    $('jsonInput').value = '';
    $('jsonResult').innerHTML = '';
  },

  init() {
    $('jsonFormatBtn').addEventListener('click', () => this.run());
    $('jsonClearBtn').addEventListener('click', () => this.clear());
    $$('.json-chip').forEach(chip => {
      chip.addEventListener('click', () => {
        $('jsonInput').value = chip.dataset.j;
        this.run();
      });
    });
  }
};

// ── SIDEBAR KEYS (inline) ────────────────────────────────────
const SidebarKeys = {
  updateStatus(statusId, value) {
    const el = $(statusId);
    if (!el) return;
    if (value) {
      el.textContent = '✅ Đã kích hoạt';
      el.className = 'sidebar-key-status ok';
    } else {
      el.textContent = 'Chưa nhập key';
      el.className = 'sidebar-key-status empty';
    }
  },

  save(inputId, storageKey, statusId) {
    const val = $(inputId)?.value.trim() || '';
    if (val) localStorage.setItem(storageKey, val);
    else localStorage.removeItem(storageKey);
    this.updateStatus(statusId, val);
    // Sync với Settings page
    const settingsInput = storageKey === 'ai-google-key' ? 'googleApiKey' : 'weatherApiKey';
    if ($(settingsInput)) $(settingsInput).value = val;
    if (val) showToast('✅ Đã lưu API Key');
  },

  load() {
    const g = localStorage.getItem('ai-google-key') || 'AQ.Ab8RN6LasT9VWVMeub7XXB4VPt0v9X5qQAjEKOBMBLSNGxqIZA';
    const w = localStorage.getItem('ai-weather-key') || '614859b889a9e5d051c60d45643f2de6';
    if ($('sidebarGoogleKey'))  { $('sidebarGoogleKey').value  = g; this.updateStatus('sidebarGoogleStatus', g); }
    if ($('sidebarWeatherKey')) { $('sidebarWeatherKey').value = w; this.updateStatus('sidebarWeatherStatus', w); }
  },

  init() {
    this.load();

    // Save on change/blur
    $('sidebarGoogleKey')?.addEventListener('change', () =>
      this.save('sidebarGoogleKey', 'ai-google-key', 'sidebarGoogleStatus'));
    $('sidebarWeatherKey')?.addEventListener('change', () =>
      this.save('sidebarWeatherKey', 'ai-weather-key', 'sidebarWeatherStatus'));

    // Save on Enter
    $('sidebarGoogleKey')?.addEventListener('keydown', e => {
      if (e.key === 'Enter') { e.target.blur(); this.save('sidebarGoogleKey', 'ai-google-key', 'sidebarGoogleStatus'); }
    });
    $('sidebarWeatherKey')?.addEventListener('keydown', e => {
      if (e.key === 'Enter') { e.target.blur(); this.save('sidebarWeatherKey', 'ai-weather-key', 'sidebarWeatherStatus'); }
    });

    // Show/hide toggle
    $$('.sidebar-key-toggle').forEach(btn => {
      btn.addEventListener('click', () => {
        const input = $(btn.dataset.target);
        if (!input) return;
        const isHidden = input.type === 'password';
        input.type = isHidden ? 'text' : 'password';
        btn.innerHTML = isHidden
          ? '<i class="fa-solid fa-eye-slash"></i>'
          : '<i class="fa-solid fa-eye"></i>';
      });
    });
  }
};


document.addEventListener('DOMContentLoaded', () => {
  Theme.init();
  Sidebar.init();
  Nav.init();
  Tabs.init();
  Keys.init();
  SidebarKeys.init();
  Calculator.init();
  Weather.init();
  Translator.init();
  TimeModule.init();
  Search.init();
  JsonFormatter.init();

  // Default page
  Nav.goTo('home');
});
