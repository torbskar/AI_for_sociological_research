# Log Index

## Project: Structured AI Use in Sociological Research

| Date | Decision log | Author-input log | Key decisions |
|------|------|------|---------------|
| 2026-04-04 | 2026-04-04.md | 2026-04-04-author-input.md | Paper type; target journal; core distinction; file structure; logging convention; CSV format; three-stage screening protocol; naming convention; lit-screen skill; string A screened (309→211); string B exported |
| 2026-04-05 | 2026-04-05.md | 2026-04-05-author-input.md | OpenAlex replaces Scopus/WoS (legal); query authorship argument developed; target journal changed to Sociological Science; replication package fit identified; full pipeline run Steps 1–8: 1,133 records → 1,073 retained → 558 PDFs → 503 screened → 300 exported (50/subfolder); PIPELINE.md written; NotebookLM configs and report templates A/B/C written |
| 2026-04-06 | 2026-04-06.md | 2026-04-06-author-input.md | Pipeline bugs fixed (11 issues); v2 search strings (economics/psychology/String H/venue queries); re-run: 1,479 records → 1,407 retained → 851 new PDFs → 1,409 total on disk; download skip logic added |
| 2026-04-09 | 2026-04-09.md | 2026-04-09-author-input.md | 848 DOI-named PDFs renamed (594 already-named protected); 250 export files synced; NotebookLM notebooks B and C created and populated (50 sources each) |
| 2026-04-10 | 2026-04-10.md | 2026-04-10-author-input.md | Elicit search reviewed (27 sources); checklists-vs-pipelines gap identified as paper's structural position; three empirical anchors extracted (Zeng, Ludwig, Barrie); literature note and full working outline written |
| 2026-04-11 | 2026-04-11.md | 2026-04-11-author-input.md | PLOS ONE removed from venue queries; populate_upload_folders.py created; pipeline re-run (Theme C: 5→46 available papers); script portability fixes; NotebookLM reports assessed: A adequate, B inadequate (needs manual Q0 session), C adequate; MCP plugin found unreliable (all queries timeout) |
