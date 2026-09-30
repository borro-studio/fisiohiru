(() => {
  const root = document.documentElement;
  // idioma
  const setLang = l => {
    root.lang = l;
    document.querySelectorAll('.lang button').forEach(b => b.setAttribute('aria-pressed', b.dataset.lang === l));
    try { localStorage.setItem('hiru-lang', l); } catch (e) {}
  };
  let saved = null; try { saved = localStorage.getItem('hiru-lang'); } catch (e) {}
  if (saved) setLang(saved);
  document.querySelectorAll('.lang button').forEach(b => b.addEventListener('click', () => setLang(b.dataset.lang)));

  // menú móvil
  const nav = document.getElementById('nav'), mb = document.getElementById('menuBtn');
  mb.addEventListener('click', () => { const o = nav.classList.toggle('open'); mb.setAttribute('aria-expanded', o); });
  document.querySelectorAll('#navLinks a').forEach(a => a.addEventListener('click', () => { nav.classList.remove('open'); mb.setAttribute('aria-expanded', false); }));

  // borde nav al hacer scroll
  const sentinel = document.createElement('div'); sentinel.style.cssText = 'position:absolute;top:8px;height:1px;width:1px';
  document.body.prepend(sentinel);
  new IntersectionObserver(([e]) => nav.classList.toggle('scrolled', !e.isIntersecting)).observe(sentinel);

  // servicios: acordeón + imagen
  const items = [...document.querySelectorAll('.svc-item')], pics = [...document.querySelectorAll('.svc-media img')];
  const fine = matchMedia('(hover:hover) and (min-width:901px)');
  const activate = (it, toggle) => {
    const was = it.classList.contains('active');
    items.forEach(o => { o.classList.remove('active'); o.querySelector('.svc-head').setAttribute('aria-expanded', 'false'); });
    if (toggle && was && !fine.matches) return;
    it.classList.add('active'); it.querySelector('.svc-head').setAttribute('aria-expanded', 'true');
    pics.forEach(p => p.classList.toggle('on', p.dataset.key === it.dataset.img));
  };
  items.forEach(it => {
    it.querySelector('.svc-head').addEventListener('click', () => activate(it, true));
    it.addEventListener('mouseenter', () => { if (fine.matches) activate(it); });
  });

  // páginas de servicio: índice lateral activo
  const tocLinks = [...document.querySelectorAll('.toc a[href^="#"]')];
  if (tocLinks.length) {
    const map = new Map(tocLinks.map(a => [a.getAttribute('href').slice(1), a]));
    const setOn = id => { tocLinks.forEach(a => a.classList.toggle('on', a === map.get(id))); const a = map.get(id); if (a && innerWidth <= 900) a.closest('ul').scrollTo({ left: a.offsetLeft - 16, behavior: 'smooth' }); };
    const secs = [...document.querySelectorAll('.svc-sec')];
    const pick = () => { const cur = secs.filter(x => x.getBoundingClientRect().top < innerHeight * .4).pop() || secs[0]; setOn(cur.id); };
    const so = new IntersectionObserver(pick, { rootMargin: '0px 0px -60% 0px' });
    secs.forEach(x => so.observe(x));
    pick();
  }

  // mapa: se carga solo si el usuario lo pide (sin cookies de terceros por defecto)
  const ml = document.getElementById('mapLoad');
  if (ml) ml.addEventListener('click', () => {
    const f = document.createElement('iframe');
    f.title = 'Mapa'; f.referrerPolicy = 'no-referrer-when-downgrade';
    f.src = 'https://www.google.com/maps/embed?origin=mfe&pb=!1m2!2m1!1sPlazaola+kalea+4,+20230+Legazpi';
    document.getElementById('map').replaceChildren(f);
  });

  // reveal
  const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), { threshold: .15, rootMargin: '0px 0px -40px 0px' });
  document.querySelectorAll('.rv').forEach(el => io.observe(el));
})();
