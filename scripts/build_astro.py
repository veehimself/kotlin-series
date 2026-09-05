#!/usr/bin/env python3
"""
Build the 5 lesson .astro files from the extracted body content.
Each .astro file wraps the body in <LessonLayout> and adds a
page-specific <style> block for styles NOT in global.css.
"""
from pathlib import Path

BODY_DIR = Path('/workspace/extract-tmp')
OUT_DIR  = Path('/workspace/kotlin-series-astro/src/pages')
OUT_DIR.mkdir(parents=True, exist_ok=True)

# -----------------------------------------------------------------------------
# Page-specific style blocks (everything not already in global.css)
# -----------------------------------------------------------------------------

STYLES_01 = """
  /* ==== Page-specific: ceremony reduction table ==== */
  .reduce { background: var(--bg-card); border: 1px solid var(--line); border-radius: var(--r-xl); padding: var(--space-8); margin: 40px 0; }
  .reduce-title { text-align: center; color: var(--ink-soft); font-size: 13px; font-weight: 600; letter-spacing: 0.12em; text-transform: uppercase; margin-bottom: 24px; }
  .reduce-table { width: 100%; border-collapse: collapse; font-size: 14.5px; }
  .reduce-table th { text-align: left; padding: 12px 16px; color: var(--ink-soft); font-size: 11px; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; border-bottom: 2px solid var(--line); }
  .reduce-table td { padding: 14px 16px; border-bottom: 1px solid var(--line-soft); color: var(--ink-mid); vertical-align: top; }
  .reduce-table tr:last-child td { border-bottom: none; }
  .reduce-table .feat { font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 13px; color: var(--primary); font-weight: 600; white-space: nowrap; }
  .reduce-table .gone { color: #b06367; text-decoration: line-through; font-style: italic; }
  .reduce-table .kept { color: var(--accent); font-weight: 600; }

  /* ==== Page-specific: ranges visualization ==== */
  .ranges { background: var(--bg-card); border: 1px solid var(--line); border-radius: var(--r-xl); padding: var(--space-8); margin: 32px 0; }
  .range-row { display: grid; grid-template-columns: 160px 1fr 200px; gap: var(--space-4); align-items: center; padding: 14px 0; }
  .range-row + .range-row { border-top: 1px dashed var(--line); }
  @media (max-width: 720px) { .range-row { grid-template-columns: 1fr; gap: 8px; } }
  .range-syntax { font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 14px; font-weight: 600; color: var(--primary); }
  .range-viz { display: flex; align-items: center; gap: 4px; overflow-x: auto; }
  .range-cell { width: 28px; height: 28px; border: 1px solid var(--line); border-radius: 6px; display: flex; align-items: center; justify-content: center; font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 12px; color: var(--ink-soft); background: white; }
  .range-cell.in { background: var(--primary); color: white; border-color: var(--primary); font-weight: 600; }
  .range-cell.edge { background: var(--accent); color: white; border-color: var(--accent); font-weight: 600; }
  .range-desc { font-size: 13.5px; color: var(--ink-mid); }

  /* ==== Page-specific: function signature visual ==== */
  .sig-viz { background: var(--bg-card); border: 1px solid var(--line); border-radius: var(--r-xl); padding: var(--space-8); margin: 32px 0; }
  .sig-def { background: #1a1f2b; color: #e6e6e6; font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 14px; border-radius: 12px; padding: 16px 20px; margin: 12px 0 20px; overflow-x: auto; }
  .sig-def .k { color: var(--code-keyword); }
  .sig-def .fn { color: var(--code-fn); }
  .sig-def .t { color: var(--code-type); }
  .sig-def .v { color: #ff5370; }
  .sig-def .df { color: var(--accent); }
  .sig-def .c { color: var(--code-comment); font-style: italic; }
  .calls { display: grid; grid-template-columns: 1fr; gap: 8px; }
  .call-row { display: grid; grid-template-columns: 1fr 80px; gap: 12px; align-items: center; padding: 10px 14px; background: #fbfaf6; border: 1px solid var(--line-soft); border-radius: 8px; }
  .call-row .call-code { font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 13px; color: var(--ink); }
  .call-row .call-result { font-size: 12px; color: var(--ink-soft); font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; }
""".strip()

STYLES_02 = """
  /* ==== Page-specific: impossible states map ==== */
  .map { background: var(--bg-card); border: 1px solid var(--line); border-radius: var(--r-xl); padding: var(--space-8); margin: 40px 0; }
  .map-title { text-align: center; color: var(--ink-soft); font-size: 13px; font-weight: 600; letter-spacing: 0.12em; text-transform: uppercase; margin-bottom: 24px; }
  .map-table { width: 100%; border-collapse: collapse; font-size: 14.5px; }
  .map-table th { text-align: left; padding: 12px 16px; color: var(--ink-soft); font-size: 11px; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; border-bottom: 2px solid var(--line); }
  .map-table td { padding: 14px 16px; border-bottom: 1px solid var(--line-soft); color: var(--ink-mid); vertical-align: top; }
  .map-table tr:last-child td { border-bottom: none; }
  .map-table .feat { font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 13px; color: var(--primary); font-weight: 600; white-space: nowrap; }
  .map-table .stops { color: var(--ink); font-style: italic; }
  .map-table .lvl { font-size: 12px; color: var(--ink-soft); text-transform: uppercase; letter-spacing: 0.08em; font-weight: 600; }
  .map-table .lvl.syn { color: var(--ink-soft); }
  .map-table .lvl.model { color: var(--primary); font-weight: 700; }

  /* ==== Page-specific: null-safety big section divider ==== */
  .big-section { margin: 80px 0 0; padding: 36px; background: linear-gradient(135deg, #ebe3ee 0%, #f5e6d3 100%); border: 1px solid var(--line); border-radius: var(--r-2xl); }
  .big-section .tag { display: inline-block; color: var(--primary); background: white; font-size: 12px; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; padding: 6px 14px; border-radius: 20px; margin-bottom: 16px; }
  .big-section h2 { margin-top: 0; font-size: 40px; }
  .big-section p { font-size: 17px; color: var(--ink-mid); max-width: 680px; }

  /* ==== Page-specific: null-safety flow rows ==== */
  .ns-flow { display: grid; grid-template-columns: 1fr; gap: var(--space-4); margin: 24px 0; }
  .ns-row { display: grid; grid-template-columns: 180px 1fr; gap: 20px; align-items: stretch; background: var(--bg-card); border: 1px solid var(--line); border-radius: var(--r-lg); padding: 20px 24px; }
  @media (max-width: 720px) { .ns-row { grid-template-columns: 1fr; } }
  .ns-op { display: flex; flex-direction: column; justify-content: center; padding-right: 20px; border-right: 1px solid var(--line-soft); }
  @media (max-width: 720px) { .ns-op { border-right: none; border-bottom: 1px solid var(--line-soft); padding-right: 0; padding-bottom: 12px; } }
  .ns-op .op-name { font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 22px; font-weight: 600; color: var(--primary); }
  .ns-op .op-when { font-size: 12px; color: var(--ink-soft); margin-top: 4px; }
  .ns-body { display: flex; flex-direction: column; gap: 8px; justify-content: center; }
  .ns-body p { margin: 0; font-size: 14.5px; color: var(--ink-mid); }
  .ns-body .code { margin: 0; font-size: 13px; padding: 14px 18px; }
  .ns-row.safe { border-left: 3px solid #6f8b6f; }
  .ns-row.danger { border-left: 3px solid #b06367; }
  .ns-row.bridge { border-left: 3px solid var(--accent); }

  /* ==== Page-specific: smart cast timeline ==== */
  .smartcast { background: var(--bg-card); border: 1px solid var(--line); border-radius: var(--r-xl); padding: var(--space-8); margin: 32px 0; }
  .sc-step { display: grid; grid-template-columns: 100px 1fr; gap: var(--space-4); padding: 12px 0; align-items: center; }
  .sc-step + .sc-step { border-top: 1px dashed var(--line); }
  .sc-step .sc-line-num { font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 12px; color: var(--ink-soft); text-align: right; }
  .sc-step .sc-type { font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 12px; display: inline-block; padding: 2px 8px; border-radius: 4px; margin-right: 8px; }
  .sc-step .sc-type.nullable { background: #f0d8d8; color: #b06367; }
  .sc-step .sc-type.nonnull { background: #dde6dd; color: #6f8b6f; }
  .sc-step .sc-desc { font-size: 14px; color: var(--ink-mid); }
  .sc-step .sc-desc code { font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 12.5px; background: var(--line-soft); color: var(--primary); padding: 1px 5px; border-radius: 3px; }
""".strip()

STYLES_03 = """
  /* ==== Page-specific: the spectrum diagram ==== */
  .spectrum { margin: 40px 0 64px; padding: var(--space-8) var(--space-6); background: var(--bg-card); border: 1px solid var(--line); border-radius: var(--r-xl); }
  .spectrum-label { text-align: center; color: var(--ink-soft); font-size: 13px; font-weight: 600; letter-spacing: 0.12em; text-transform: uppercase; margin-bottom: 28px; }
  .spectrum-row { display: grid; grid-template-columns: 1fr; gap: 0; position: relative; }
  .spectrum-bar { height: 6px; background: linear-gradient(90deg, var(--accent) 0%, var(--primary) 100%); border-radius: 3px; margin: 32px 60px 56px; position: relative; }
  .spectrum-bar::before, .spectrum-bar::after { content: ""; position: absolute; top: 50%; transform: translateY(-50%); width: 14px; height: 14px; border-radius: 50%; background: var(--bg); border: 3px solid var(--primary); }
  .spectrum-bar::before { left: -7px; }
  .spectrum-bar::after { right: -7px; border-color: var(--accent); }
  .spectrum-ticks { display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; position: relative; }
  .tick { text-align: center; position: relative; padding-top: 20px; }
  .tick::before { content: ""; position: absolute; top: 0; left: 50%; transform: translateX(-50%); width: 2px; height: 14px; background: var(--line); }
  .tick-name { font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 14px; font-weight: 600; color: var(--ink); margin-bottom: 4px; }
  .tick-sub { font-size: 12px; color: var(--ink-soft); }
  .spectrum-anchors { display: flex; justify-content: space-between; color: var(--ink-soft); font-size: 12px; margin-top: 8px; padding: 0 60px; }

  /* ==== Page-specific: tool cards ==== */
  .tool { background: var(--bg-card); border: 1px solid var(--line); border-radius: var(--r-xl); padding: var(--space-8); margin: 24px 0; box-shadow: 0 2px 8px rgba(0,0,0,0.03); }
  .tool-head { display: flex; align-items: center; gap: var(--space-4); margin-bottom: 8px; }
  .tool-icon { width: 48px; height: 48px; border-radius: 12px; display: flex; align-items: center; justify-content: center; color: white; }
  .tool-tagline { font-size: 15px; color: var(--ink-mid); margin: 0 0 20px 64px; }
  .tool-promise { background: var(--primary-soft); border-left: 3px solid var(--primary); padding: 12px 16px; border-radius: 0 8px 8px 0; margin: 16px 0 20px 64px; font-size: 14.5px; color: var(--ink-mid); }
  .tool-promise strong { color: var(--primary); }
  .vs { display: grid; grid-template-columns: 1fr 1fr; gap: var(--space-4); margin: 20px 0 0 64px; }
  .vs-col { background: #fbfaf6; border: 1px solid var(--line-soft); border-radius: 12px; padding: 16px 18px; }
  .vs-col.allow { border-top: 3px solid var(--primary); }
  .vs-col.deny { border-top: 3px solid #b06367; }
  .vs-label { font-size: 11px; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 8px; }
  .vs-col.allow .vs-label { color: var(--primary); }
  .vs-col.deny .vs-label { color: #b06367; }
  .vs-col ul { margin: 0; padding-left: 18px; }
  .vs-col li { font-size: 14px; line-height: 1.7; color: var(--ink-mid); }
  @media (max-width: 640px) { .vs { grid-template-columns: 1fr; margin-left: 0; } .tool-promise { margin-left: 0; } .tool-tagline { margin-left: 0; } }

  /* ==== Page-specific: big example ==== */
  .big-example { background: var(--bg-card); border: 1px solid var(--line); border-radius: var(--r-xl); padding: var(--space-8); margin: 32px 0; }
  .big-example-head { display: flex; align-items: center; gap: 12px; margin-bottom: 8px; }
  .big-example-head h3 { margin: 0; }
  .big-example-desc { color: var(--ink-soft); font-size: 14px; margin: 0 0 20px; }
  .annotate { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin: 24px 0; }
  @media (max-width: 720px) { .annotate { grid-template-columns: 1fr; } }
  .annotate-list { background: #fbfaf6; border: 1px solid var(--line-soft); border-radius: 12px; padding: 18px 22px; }
  .annotate-list h4 { font-family: "Outfit", sans-serif; font-weight: 600; font-size: 14px; margin: 0 0 12px; color: var(--primary); }
  .annotate-list ul { margin: 0; padding-left: 18px; }
  .annotate-list li { font-size: 14px; line-height: 1.7; color: var(--ink-mid); }
  .annotate-list li code { font-size: 0.85em; }

  /* ==== Page-specific: connection puzzle ==== */
  .puzzle { margin: 40px 0; padding: var(--space-8); background: var(--bg-card); border: 1px solid var(--line); border-radius: var(--r-xl); }
  .puzzle-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 14px; margin-top: 20px; }
  @media (max-width: 640px) { .puzzle-grid { grid-template-columns: 1fr; } }
  .puzzle-cell { display: flex; gap: 12px; padding: 14px 16px; border: 1px solid var(--line-soft); border-radius: 12px; background: #fbfaf6; }
  .puzzle-cell .dot { flex-shrink: 0; width: 10px; height: 10px; border-radius: 50%; margin-top: 8px; }
  .puzzle-cell[data-t="object"] .dot { background: #c97b3f; }
  .puzzle-cell[data-t="enum"] .dot { background: #d49a3f; }
  .puzzle-cell[data-t="data"] .dot { background: var(--primary); }
  .puzzle-cell[data-t="sealed"] .dot { background: #4a8e7c; }
  .puzzle-cell .txt { font-size: 14px; line-height: 1.55; color: var(--ink-mid); }
  .puzzle-cell .txt strong { color: var(--ink); }
""".strip()

STYLES_04 = """
  /* ==== Page-specific: 2x2 matrix ==== */
  .matrix-wrap { margin: 40px 0; padding: var(--space-8); background: var(--bg-card); border: 1px solid var(--line); border-radius: var(--r-xl); }
  .matrix-title { text-align: center; color: var(--ink-soft); font-size: 13px; font-weight: 600; letter-spacing: 0.12em; text-transform: uppercase; margin-bottom: 24px; }
  .matrix { display: grid; grid-template-columns: 80px 1fr 1fr; grid-template-rows: auto 1fr 1fr; gap: 12px; max-width: 720px; margin: 0 auto; }
  .matrix-col-head, .matrix-row-head { display: flex; align-items: center; justify-content: center; text-align: center; color: var(--ink-soft); font-size: 12px; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; padding: 8px; }
  .matrix-cell { background: #fbfaf6; border: 1px solid var(--line-soft); border-radius: 14px; padding: 22px 20px; position: relative; transition: transform 0.2s, box-shadow 0.2s; }
  .matrix-cell:hover { transform: translateY(-2px); box-shadow: 0 6px 16px -4px rgba(0,0,0,0.08); }
  .matrix-cell .fn-name { font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 22px; font-weight: 600; color: var(--primary); margin-bottom: 4px; }
  .matrix-cell .fn-sub { font-size: 12.5px; color: var(--ink-soft); margin-bottom: 12px; }
  .matrix-cell .fn-ref { font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 12px; color: var(--ink-mid); }
  .matrix-cell .fn-ref .r-it { color: var(--accent); }
  .matrix-cell .fn-ref .r-this { color: var(--primary); }
  .matrix-cell .fn-ret { margin-top: 8px; font-size: 12px; color: var(--ink-soft); }
  .matrix-cell .fn-ret code { font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; background: var(--line-soft); color: var(--ink-mid); padding: 1px 6px; border-radius: 4px; font-size: 11px; }
  .matrix-cell.q1 { background: linear-gradient(135deg, #fbfaf6 0%, #f0e9da 100%); }
  .matrix-cell.q2 { background: linear-gradient(135deg, #fbfaf6 0%, var(--primary-soft) 100%); }
  .matrix-cell.q3 { background: linear-gradient(135deg, #fbfaf6 0%, #f3e4d4 100%); }
  .matrix-cell.q4 { background: linear-gradient(135deg, #fbfaf6 0%, #dde2f0 100%); }
  @media (max-width: 640px) { .matrix { grid-template-columns: 1fr; } .matrix-col-head, .matrix-row-head { display: none; } }

  /* ==== Page-specific: behavior-as-value diagram ==== */
  .bav { background: var(--bg-card); border: 1px solid var(--line); border-radius: var(--r-xl); padding: var(--space-8); margin: 40px 0; }
  .bav-row { display: grid; grid-template-columns: 1fr 60px 1fr 60px 1fr; gap: 12px; align-items: center; margin: 16px 0; }
  @media (max-width: 720px) { .bav-row { grid-template-columns: 1fr; gap: 8px; } .bav-row .arrow { transform: rotate(90deg); margin: 0 auto; } }
  .bav-box { background: #fbfaf6; border: 2px solid var(--line); border-radius: 12px; padding: 16px 18px; text-align: center; }
  .bav-box.data { border-color: #6f8b6f; background: #dde6dd; }
  .bav-box.fn { border-color: var(--accent); background: #f6dccc; }
  .bav-box.both { border-color: var(--primary); background: var(--primary-soft); }
  .bav-box .lbl { font-size: 11px; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 4px; }
  .bav-box.data .lbl { color: #6f8b6f; }
  .bav-box.fn .lbl { color: var(--accent); }
  .bav-box.both .lbl { color: var(--primary); }
  .bav-box .val { font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 15px; color: var(--ink); }
  .bav-arrow { display: flex; align-items: center; justify-content: center; color: var(--ink-soft); }
  .bav-caption { text-align: center; color: var(--ink-soft); font-size: 13px; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 16px; }

  /* ==== Page-specific: scope diagram ==== */
  .scope-diagram { background: var(--bg-card); border: 1px solid var(--line); border-radius: var(--r-xl); padding: var(--space-8); margin: 32px 0; }
  .scope-diagram h3 { margin-top: 0; }
  .scope-row { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 16px 0; }
  @media (max-width: 720px) { .scope-row { grid-template-columns: 1fr; } }
  .scope-box { border: 2px solid var(--line); border-radius: 12px; padding: 20px; background: #fbfaf6; position: relative; }
  .scope-box.outer { border-color: var(--primary); }
  .scope-box.inner { border-color: var(--accent); background: #fdf6e3; margin-left: 24px; }
  .scope-tag { position: absolute; top: -10px; left: 16px; background: var(--bg); padding: 0 8px; font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 11px; font-weight: 600; letter-spacing: 0.05em; }
  .scope-box.outer .scope-tag { color: var(--primary); }
  .scope-box.inner .scope-tag { color: var(--accent); }
  .scope-box p { margin: 0; font-size: 14px; color: var(--ink-mid); }
  .scope-box p code { font-size: 13px; }

  /* ==== Page-specific: unify panel ==== */
  .unify { background: linear-gradient(135deg, #ffffff 0%, #f3e4d4 100%); border: 1px solid var(--line); border-radius: var(--r-xl); padding: var(--space-8); margin: 40px 0; }
  .unify-row { display: grid; grid-template-columns: 1fr auto 1fr; gap: 20px; align-items: center; margin: 16px 0; }
  @media (max-width: 720px) { .unify-row { grid-template-columns: 1fr; } .unify-row .arrow { transform: rotate(90deg); margin: 0 auto; } }
  .unify-card { background: var(--bg-card); border: 1px solid var(--line); border-radius: 12px; padding: 18px 20px; }
  .unify-card-label { font-size: 11px; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; color: var(--ink-soft); margin-bottom: 8px; }
  .unify-card h4 { font-family: "DM Serif Display", Georgia, "Times New Roman", serif; font-weight: 400; font-size: 22px; margin: 0 0 4px; color: var(--ink); }
  .unify-card p { font-size: 14px; color: var(--ink-mid); margin: 0; }
  .arrow { width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; color: var(--accent); }

  /* ==== Page-specific: pair with margin (some compare blocks are indented) ==== */
  .pair { margin: 16px 0 0 64px; }
  @media (max-width: 720px) { .pair { grid-template-columns: 1fr; margin-left: 0; } }
""".strip()

STYLES_05 = """
  /* ==== Page-specific: behavior-as-value diagram (functional) ==== */
  .bav { background: var(--bg-card); border: 1px solid var(--line); border-radius: var(--r-xl); padding: var(--space-8); margin: 40px 0; }
  .bav-row { display: grid; grid-template-columns: 1fr 60px 1fr 60px 1fr; gap: 12px; align-items: center; margin: 16px 0; }
  @media (max-width: 720px) { .bav-row { grid-template-columns: 1fr; gap: 8px; } .bav-row .arrow { transform: rotate(90deg); margin: 0 auto; } }
  .bav-box { background: #fbfaf6; border: 2px solid var(--line); border-radius: 12px; padding: 16px 18px; text-align: center; }
  .bav-box.data { border-color: #6f8b6f; background: #dfeae3; }
  .bav-box.fn { border-color: var(--accent); background: #f6dcd1; }
  .bav-box.both { border-color: var(--primary); background: #dde4ee; }
  .bav-box .lbl { font-size: 11px; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 4px; }
  .bav-box.data .lbl { color: #6f8b6f; }
  .bav-box.fn .lbl { color: var(--accent); }
  .bav-box.both .lbl { color: var(--primary); }
  .bav-box .val { font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 15px; color: var(--ink); }
  .bav-arrow { display: flex; align-items: center; justify-content: center; color: var(--ink-soft); }
  .bav-caption { text-align: center; color: var(--ink-soft); font-size: 13px; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 16px; }

  /* ==== Page-specific: shapes diagram (the 4 collection ops) ==== */
  .shapes { background: var(--bg-card); border: 1px solid var(--line); border-radius: var(--r-xl); padding: var(--space-8); margin: 40px 0; }
  .shapes-title { text-align: center; color: var(--ink-soft); font-size: 13px; font-weight: 600; letter-spacing: 0.12em; text-transform: uppercase; margin-bottom: 24px; }
  .shape-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; }
  @media (max-width: 720px) { .shape-grid { grid-template-columns: 1fr; } }
  .shape-card { border: 1px solid var(--line-soft); border-radius: 14px; padding: 20px; background: #fbfaf6; }
  .shape-name { font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 18px; font-weight: 600; color: var(--ink); margin-bottom: 4px; }
  .shape-shape { font-size: 13px; color: var(--ink-soft); font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; margin-bottom: 14px; }
  .shape-viz { display: flex; align-items: center; gap: 8px; padding: 12px; background: white; border: 1px dashed var(--line); border-radius: 8px; font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 12px; }
  .shape-viz .dot { width: 24px; height: 24px; border-radius: 50%; background: #6f8b6f; display: flex; align-items: center; justify-content: center; color: white; font-weight: 600; font-size: 11px; }
  .shape-viz .dot.out { background: var(--ink-soft); opacity: 0.3; text-decoration: line-through; }
  .shape-viz .arrow { color: var(--primary); }
  .shape-viz .bucket { background: var(--primary-soft); border: 1px solid var(--primary); border-radius: 6px; padding: 4px 8px; color: var(--primary); font-size: 11px; }
  .shape-viz .one { width: 32px; height: 32px; border-radius: 50%; background: var(--accent); color: white; display: flex; align-items: center; justify-content: center; font-weight: 600; font-size: 12px; }
  .shape-desc { margin-top: 12px; font-size: 13.5px; color: var(--ink-mid); line-height: 1.5; }
  .shape-desc code { font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 12px; background: var(--line-soft); color: var(--primary); padding: 1px 5px; border-radius: 3px; }

  /* ==== Page-specific: pipeline diagram ==== */
  .pipeline { background: var(--bg-card); border: 1px solid var(--line); border-radius: var(--r-xl); padding: var(--space-8); margin: 32px 0; }
  .pipe-step { display: grid; grid-template-columns: 56px 1fr; gap: var(--space-4); align-items: center; padding: 14px 0; }
  .pipe-step + .pipe-step { border-top: 1px dashed var(--line); }
  .pipe-step .step-num { width: 40px; height: 40px; border-radius: 50%; background: var(--primary-soft); color: var(--primary); display: flex; align-items: center; justify-content: center; font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; font-weight: 600; font-size: 14px; }
  .pipe-step .step-name { font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 15px; font-weight: 600; color: var(--ink); margin-bottom: 2px; }
  .pipe-step .step-desc { font-size: 13.5px; color: var(--ink-mid); }
  .pipe-step .step-returns { font-size: 12px; color: var(--ink-soft); font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; margin-top: 4px; }
  .pipe-step .step-returns code { background: var(--line-soft); color: var(--primary); padding: 1px 6px; border-radius: 3px; }

  /* ==== Page-specific: mental shift panel ==== */
  .shift { background: linear-gradient(135deg, #ffffff 0%, var(--primary-soft) 100%); border: 1px solid var(--line); border-radius: var(--r-xl); padding: var(--space-8); margin: 40px 0; }
  .shift-row { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 20px; }
  @media (max-width: 720px) { .shift-row { grid-template-columns: 1fr; } }
  .shift-col { background: var(--bg-card); border: 1px solid var(--line); border-radius: 14px; padding: 24px; }
  .shift-col h4 { font-family: "Outfit", sans-serif; font-size: 13px; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; margin: 0 0 8px; }
  .shift-col.imp h4 { color: #b06367; }
  .shift-col.func h4 { color: #6f8b6f; }
  .shift-col p { font-size: 14.5px; color: var(--ink-mid); margin: 0 0 12px; }
  .shift-col .code { margin: 0; font-size: 12.5px; }

  /* ==== Page-specific: tree-ans with bad/ok variants ==== */
  .tree-ans.bad { background: #f0d8d8; color: #b06367; }
  .tree-ans.ok { background: #dde6dd; color: #6f8b6f; }
""".strip()

# -----------------------------------------------------------------------------
# Page metadata
# -----------------------------------------------------------------------------

PAGES = [
    {
        'slug': '01-syntax',
        'title': 'Kotlin syntax — the foundations',
        'description': 'val/var, types, control flow as expressions, ranges, loops, default and named arguments. The pieces that show up in every program.',
        'number': 1,
        'primary': '#2d3142',
        'accent': '#ef8354',
        'styles': STYLES_01,
    },
    {
        'slug': '02-classes-null-safety',
        'title': 'Classes & null safety',
        'description': 'Primary/secondary constructors, properties, visibility, and the null safety system: ?., ?:, smart casts, !!.',
        'number': 2,
        'primary': '#6b4e71',
        'accent': '#d4a574',
        'styles': STYLES_02,
    },
    {
        'slug': '03-data-modeling',
        'title': 'Modeling data in Kotlin',
        'description': 'data class, sealed class, enum class, object, and companion object — one spectrum from "exactly one value" to "any of N data shapes."',
        'number': 3,
        'primary': '#2f6f5e',
        'accent': '#c97b3f',
        'styles': STYLES_03,
    },
    {
        'slug': '04-scope-functions',
        'title': 'Extension & scope functions',
        'description': 'Extension functions as the engine, then let, apply, run, also, with on a 2×2: who is this and what does the block return.',
        'number': 4,
        'primary': '#2f6f5e',
        'accent': '#5b6cad',
        'styles': STYLES_04,
    },
    {
        'slug': '05-functional',
        'title': 'Functional Kotlin',
        'description': 'Lambdas, higher-order functions, and the collection ops (map, filter, reduce, groupBy) as pre-written HOFs.',
        'number': 5,
        'primary': '#3d5a80',
        'accent': '#e07a5f',
        'styles': STYLES_05,
    },
]

# -----------------------------------------------------------------------------
# Build each file
# -----------------------------------------------------------------------------

def escape_astro_braces(html: str) -> str:
    """
    Escape { and } in HTML text content so Astro doesn't interpret
    them as JSX expressions. We walk the string and only escape braces
    that appear in text content — not inside <script>, <style>, or
    attribute values that contain code.

    Heuristic: escape every { and } that appears OUTSIDE of:
      - <style>...</style> blocks
      - <script>...</script> blocks
      - <!-- ... --> comments
    This is conservative but safe for our use case (the body is just
    rendered HTML with embedded code samples).
    """
    import re
    # Strip out <style>...</style> blocks
    parts = re.split(r'(<style[^>]*>.*?</style>)', html, flags=re.DOTALL)
    out = []
    for i, part in enumerate(parts):
        if i % 2 == 1:
            # Inside a <style> block — leave braces alone
            out.append(part)
        else:
            # Outside <style> — escape braces in text and tag content
            # Skip attribute values that look like CSS (style="...") or JSON
            # For safety, just escape every { and } outside <style>
            # (we don't use <script> in the body, and the body has no
            # inline event handlers with {})
            out.append(part.replace('{', '&#123;').replace('}', '&#125;'))
    return ''.join(out)


for page in PAGES:
    body_path = BODY_DIR / f'{page["slug"]}.body.html'
    body = body_path.read_text(encoding='utf-8')
    # Escape braces so Astro doesn't treat them as JSX expressions
    body = escape_astro_braces(body)
    # Re-indent body by 2 spaces (since it'll be inside a <LessonLayout> in a 4-space indented template)
    indented = '\n'.join('  ' + line if line.strip() else line for line in body.split('\n'))

    out = f"""---
import LessonLayout from '../layouts/LessonLayout.astro';
---

<LessonLayout
  title={page['title']!r}
  description={page['description']!r}
  number={page['number']}
  primary={page['primary']!r}
  accent={page['accent']!r}
>
{indented}
</LessonLayout>

<style>
{page['styles']}
</style>
"""
    out_path = OUT_DIR / f'{page["slug"]}.astro'
    out_path.write_text(out, encoding='utf-8')
    print(f'wrote {out_path} ({out_path.stat().st_size:,} bytes)')
