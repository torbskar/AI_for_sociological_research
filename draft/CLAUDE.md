# CLAUDE.md — draft/

## Draft versioning procedure

Draft files follow a two-suffix naming convention that distinguishes author-edited versions from Claude-produced versions:

- `vN-draft.md` — produced by Claude (either initial draft or work continuing from a manualEdit file)
- `vN-draft - manualEdit.md` — saved by the author after making direct edits to a Claude draft

**Before making any structural or substantive changes to the draft**, check `draft/` for the most recent file:

1. If the most recent file is a `manualEdit` version (e.g. `v1-draft - manualEdit.md`): create a new copy with the next version number as `vN-draft.md` (e.g. `v2-draft.md`) and work on that copy. Do not edit the `manualEdit` file.
2. If the most recent file is a Claude version (e.g. `v2-draft.md`): continue editing it in place. Do not increment the version number unless the author explicitly requests it.

**Version number increments** only on two occasions: when the author asks for a new version, or when Claude is working from a `manualEdit` file (which signals that the author has made changes since the last Claude version).

The `manualEdit` suffix is the author's signal; Claude never creates `manualEdit` files.
