# BanglaLLM Research Lab — Landing Page Design

**Spec date:** 2026-04-22
**Target URL:** https://banglallm.github.io
**Repo:** github.com/banglallm/banglallm.github.io (new)

## 1. Purpose and audience

The lab needs a single shareable link that tells researchers, collaborators, students, funders, and press *what BanglaLLM is, what we've published, what we're building, and who we are* — in Bengali first, English on toggle.

The page is not marketing for Drishtikon and not a dashboard for the org's GitHub. It is the lab's public face: research, people, artifacts, and intent. If a reviewer clicks through from an arxiv paper, a professor from Twitter, or a prospective student from a Slack link, they should leave with a clear picture in under 60 seconds.

Reference aesthetic: [anthropic.com/research](https://www.anthropic.com/research) — single column, sans-serif, heavy whitespace, publications as a Date / Venue / Title table, no hero illustration, category tags for visual cueing. Adapted for Bengali typography and a bilingual toggle.

## 2. Principles

- **Bengali is the home language.** Page loads in Bengali. English is one click away. Neither version is a summary of the other — both are first-class.
- **Humanized prose, not brochure copy.** First-person plural ("আমরা" / "we"). No "cutting-edge", no "state-of-the-art", no "revolutionary". Paragraphs where paragraphs read better than bullets.
- **Content does the work.** Typography and whitespace carry the page. No gradients, no hero images, no decorative shapes. One restrained accent color for links and tags.
- **Cite exactly as published.** Paper titles, venues, and author orders must match arXiv / ACL Anthology character-for-character.
- **Never claim what isn't true.** TutorLM is in progress, not accepted. Say so plainly.

## 3. Architecture

### Stack
- **Jekyll** on GitHub Pages (native build, no CI needed).
- **Custom minimal theme** (not al-folio) — the academic-portfolio themes look too decorative for this; we want Anthropic-minimal.
- **Plain JS** for the language toggle (~30 lines), no framework.
- **Noto Sans Bengali** + **Inter** (or system-ui) via Google Fonts for Bengali + English respectively.
- **No build tools beyond Jekyll.** Push to `main`; Pages builds.

### File layout
```
banglallm.github.io/
├── _config.yml
├── _data/
│   ├── publications.yml       # one entry per paper, bn + en fields
│   ├── people.yml             # one entry per person, bn + en fields
│   ├── projects.yml           # research themes / repos to feature
│   └── site.yml               # hero copy, mission, contact, bn + en
├── _includes/
│   ├── header.html            # nav + language toggle
│   ├── footer.html
│   ├── publication.html       # renders one paper row
│   ├── person.html            # renders one person block
│   └── project.html           # renders one project card
├── _layouts/
│   └── default.html           # single layout; lang attr toggled via JS
├── assets/
│   ├── css/style.css
│   └── js/lang-toggle.js
├── index.html                 # the only page (single-page site)
├── CNAME                      # (optional, if custom domain later)
└── README.md
```

Data-driven: adding a paper = one YAML entry. No HTML edits for routine updates.

### Bilingual model
Every data entry carries both `bn` and `en` fields. The layout renders both, wrapping each in `<span data-lang="bn">` / `<span data-lang="en">`. CSS hides the inactive language. A toggle button flips a `data-active-lang` attribute on `<html>` and persists the choice to `localStorage`. Default is `bn`.

This avoids Jekyll's multilingual plugin complexity, avoids duplicate page builds, and lets search engines index both languages in the same URL.

## 4. Page sections (top to bottom)

1. **Header** — wordmark "BanglaLLM" (left), nav links (Publications · Models · People · GitHub · HuggingFace), language toggle "বাং / EN" (right). Sticky, thin border-bottom, nothing else.

2. **Hero** — one line: mission statement in Bengali (default) / English. Not a tagline, not a slogan — a sentence. Draft:
   > **BN:** বাংলা ভাষার জন্য উন্মুক্ত ভাষা-মডেল গবেষণা। আমরা মডেল, ডেটাসেট এবং বেঞ্চমার্ক তৈরি করি — যাতে বাংলা প্রথম শ্রেণির ভাষা হিসেবে বিবেচিত হয়, পরে যোগ করা একটি ভাষা নয়।
   > **EN:** Open language-model research for Bangla. We build models, datasets, and benchmarks so Bangla is treated as a first-class language — not an afterthought.

   A one-paragraph "about" follows (3–4 sentences, human voice, no buzzwords), framing why the lab exists and what "first-class" means in practice.

3. **Research themes** (4 cards, text only — no icons): *Foundation models for Bangla · Evaluation & benchmarks · Data infrastructure · Applied research (product-linked)*. Each card is a title + 2–3 sentences. These are themes, not lists of repos — repos live under each theme as sub-links.

4. **Publications** — a single table, newest first. Columns: **Year · Venue · Title · Authors**. Title links to arXiv (primary) and ACL Anthology (secondary, small). Authors: full co-author list as published, lab members in **bold**, others in regular weight. Venue tag uses the accent color. Entries to ship at launch:
   - **2025 · BLP @ IJCNLP-AACL** · *Read Between the Lines: A Benchmark for Uncovering Political Bias in Bangla News Articles* · Nusrat Jahan Lia, Shubhashis Roy Dipta, Abdullah Khan Zehady, Naymul Islam, Madhusodan Chakraborty, Abdullah Al Wasif. [arXiv:2510.03898](https://arxiv.org/abs/2510.03898) · [ACL Anthology](https://aclanthology.org/2025.banglalp-1.5/)
   - **2026 · LoResLM @ EACL** · *BanglaLlama: LLaMA for Bangla Language* · Abdullah Khan Zehady, Shubhashis Roy Dipta, Naymul Islam, Safi Al Mamun, Santu Karmaker. [arXiv:2410.21200](https://arxiv.org/abs/2410.21200)

   Below the published table, a small **In progress** subsection lists ongoing work as plain-text entries, no fake links:
   - *TutorLM* — building tutoring-oriented Bengali models. Preprint coming.

5. **Models & Datasets** — a compact grid linking to HuggingFace, grouped by family:
   - *BanglaLlama family* (Llama 3 / 3.1 / 3.2 base + instruct variants, 3B–11B)
   - *Bangla-s1k family* (test-time scaling adapted for Bengali; Qwen-2.5 3B/32B, QWQ-32B)
   - *Datasets* (bangla-alpaca-orca 172k, bangla-alpaca 52k, bangla_math 859k)

   Each item: name → HF link, size, one-line purpose. Total downloads shown in aggregate ("Over X downloads across 31 models") rather than per-model, to avoid stale numbers.

6. **Drishtikon** — a single callout section, two paragraphs. What it is, how it connects to the lab's research (built on BongLLaMA; the lab's bias work from *Read Between the Lines* feeds the platform's bias mapping). Link out to drishtikon.life. Framed as "research → product", not as promotion.

7. **People** — name, affiliation, one-sentence role. Photos optional, skip for v1. Lab members to list (per user directive 2026-04-22):
   - Abdullah Khan Zehady (Lead; Perspectivity)
   - Shubhashis Roy Dipta (PhD, UMBC)
   - Santu Karmaker (Assistant Professor, UCF — Bridge-AI Lab)
   - Naymul Islam
   - Safi Al Mamun
   - Nusrat Jahan Lia
   - Madhusodan Chakraborty

   Abdullah Al Wasif is omitted from the People section at the user's request. He remains in the *Read Between the Lines* author list in Publications (that list is the published paper's record; altering it would misrepresent the paper).

8. **Open source** — link to the GitHub org with a line per featured repo (bangla-llama, s1-bengali, BanglaDataManager, bd-newspaper-crawlers, lm-evaluation-harness fork, Open-Translator, youtube_bangla, OpenMAIC). Brief one-line purpose each.

9. **Join / Contact** — two sentences on what collaboration looks like, plus an email (to be confirmed: contact@banglallm? or redirect to Zehady's email?) and GitHub issues as the open-door channel.

10. **Footer** — tiny: copyright, MIT licensing note for content where applicable, link to the site's own source repo (so visitors know they can open a PR).

## 5. Language toggle — behavior spec

- Default language: `bn`. Set via `<html lang="bn" data-active-lang="bn">`.
- Toggle button shows the *other* language ("EN" when currently bn; "বাং" when currently en) — clicking it switches.
- CSS: `[data-active-lang="bn"] [data-lang="en"] { display: none; }` and vice versa. Block-level and inline elements both supported by using the selector on `[data-lang]` regardless of element type.
- Persistence: selection stored in `localStorage.banglallm_lang`. Read on page load; overrides the default.
- URL: no `?lang=` param in v1 — keep URLs clean. (Future: deep-link support if needed.)
- Accessibility: the toggle is a `<button>`, not a link. Announces "ভাষা পরিবর্তন করুন" / "Change language" via `aria-label`. `lang` attribute on `<html>` is updated on toggle so screen readers pronounce content correctly.

## 6. Visual design

- **Typography:**
  - Bengali: Noto Sans Bengali, 400/600/700. Larger base size (17px) than English because Bengali glyphs need more room to breathe.
  - English: Inter (400/600) with system-ui fallback. Base 16px.
  - Headings: same family as body, weight 600–700, not oversized.
- **Color:**
  - Background: `#fafaf9` (warm off-white) — not pure white, less clinical.
  - Text: `#1a1a1a`.
  - Accent: one muted color — proposing deep indigo `#3a3a7c` for links and venue tags. Subject to change after first render.
  - Borders: `#e5e5e5` for table dividers and thin rules.
- **Layout:**
  - Single column, max-width 720px, centered. Generous left/right padding on mobile.
  - Section spacing: 96px on desktop, 64px on mobile.
  - Publications table: borderless rows, thin bottom border per row.
- **Motion:** none except `prefers-reduced-motion`-safe link hover and a 120ms cross-fade on language toggle.
- **No dark mode in v1.** Can be added later with CSS custom properties; don't block launch on it.

## 7. Content writing voice

- Bengali: conversational-formal register. Think "academic article intro" not "news headline" or "government circular". No English loan-words where natural Bangla exists. Sentence-level translations, not word-level.
- English: plain, confident, no boilerplate. Short paragraphs. Active voice. No em-dash overuse. If the sentence could appear on a consulting firm's About page, rewrite it.
- A native Bengali speaker on the team (Naymul / Nusrat / Madhusodan) should review Bengali copy before launch — the draft Bengali in this spec is a starting point, not final text.

## 8. What's explicitly out of scope for v1

- Blog / news section (add in v2 when there's something to post).
- Search.
- Dark mode.
- Sitemap.xml / RSS feed (add with blog).
- Analytics (decide later — Plausible > GA if we add anything).
- Custom domain (can add CNAME later without rework).
- Multi-page routes; this is one `index.html` in v1.

## 9. Risks and open questions

- **Bengali copy quality.** The draft copy in this spec must be reviewed by a native speaker before launch. If that's blocked, we can launch English-only and enable Bengali after review.
- **Contact email.** Need to confirm: a shared `contact@banglallm` (requires email setup) or a personal email? Recommending a GitHub-issues-first policy plus one personal email.
- **Affiliations for Safi Al Mamun, Madhusodan Chakraborty.** Not public. Options: list as "Researcher" with no affiliation, or omit the affiliation field for those entries. Recommending the latter — no placeholder text.
- **HF download counts.** If we show aggregate numbers, who updates them? Recommending static "31+ models on HuggingFace" phrasing rather than a specific number that goes stale.
- **Photos in People section.** Skipped for v1 per "minimal" direction. Reconsider in v2 if team prefers.

## 10. Success criteria

A reader who knows nothing about us should, after 60 seconds on the page, be able to:
1. Explain what BanglaLLM is (one sentence).
2. Name at least two published papers.
3. Know where to find the models (HuggingFace).
4. Know one product/application the research powers (Drishtikon).
5. Know how to get in touch.

If a reader has to scroll twice to find the papers, the page has failed.
