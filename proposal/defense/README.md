# Proposal defense package

Revised 23 October 2026 after author review of the presentation.

- [Editable presentation](Mikhail_Dushkin_Proposal_Defense.pptx): 16 main slides,
  no hidden or backup slides. Full English narration is embedded in presenter notes.
- [Presentation PDF](Mikhail_Dushkin_Proposal_Defense.pdf): all 16 slides, exported
  locally through PowerPoint's printing renderer. Contains searchable text.
- [Presenter script](defense-preparation.md): derived from the embedded narration,
  1,139 words with planned allocations totalling 9:30. Actual timing requires rehearsal.
  No Q&A section. Source links are separated from spoken text in the notes.
- [Defense knowledge brief](defense-brief.html): standalone offline HTML with a Russian
  explanatory brief and a separate tab containing the exact full English speech
  extracted from the saved PowerPoint. No Q&A.
- [Production outline](../defense-outline.md): template mapping and content rationale.

Literature Review now starts with MAST, linking the practical failures to theory,
then introduces DABstep and existing systems. The content slides use smaller section
labels, consistent titles/body sizes, less bold, clearer spacing and editable diagrams.
The HTML brief is now delivered. It covers rationale, failure classification, mechanisms,
source summaries, benchmark access, controls, metrics, uncertainty, costs and limits.
Browser checks covered tab/keyboard navigation, anchors, responsive widths 320–1440 px
and exact equality of all 16 speech texts with the extracted PowerPoint notes. No
external assets or network requests are needed to read the brief; sources open as links.

## Source and verification scope

Retains the supplied university master/layout, cover, logos, palette and Microsoft
YaHei font family. The source template is unchanged. Typography and content placement
were revised at the author's request. Five native tables and editable diagrams remain.
The research design, mechanism names and comparison controls are unchanged.

The exact exported PPTX passed package, geometry, font and first-party import checks.
One table-expansion heuristic warning remains on slide 16; PowerPoint's native output
shows no corresponding overlap. The working copy was opened in native PowerPoint,
with the MAST slide and restored full notes inspected there. All 16 pages of its native
PDF export were rendered at 1600 × 900 and individually visually inspected for text
fit, spacing, table layout, connector direction, sources and template match. Native
rendering rather than a substituted-font office conversion supplies the delivered PDF.
A complete live slide-show rehearsal has not been performed.

All 16 notes parts contain the full intended narration, checked against the script.
Slide visibility and the MAST → DABstep → systems order were checked in the final file.
PDF page count, dimensions and searchable text were checked. Source claims retain the
existing dated literature checks; this revision adds no fresh ranking or full-paper
review. No experiments, performance findings, model/budget choice or Zotero sync claimed.
Author DOCX changes and supplied source files were preserved. No email, submission,
new supervisor approval or defense outcome is inferred.

## Provenance and delivery checksums

The slide/PDF production checks above describe the preceding task. The author has
since modified the local PPTX; this HTML task preserves those changes and the modified
DOCX. Speech was extracted from saved PPTX SHA-256
`97a65f940151f6ddd7f46b3c05e6e551811ea277110c0533c5bd7a250c5f1380`;
all speech text is unchanged from the preceding committed deck. The HTML captures a
fixed snapshot and does not auto-update when the presentation changes. Checksums below
identify the preceding presentation/PDF delivery, not the subsequent author-edited PPTX.

- `Mikhail_Dushkin_Proposal_Defense.pptx`: `debfbc0bd3265efd30dfb83f5bafc445023ab10ed57ea76c694ef0b8816452d1`
- `Mikhail_Dushkin_Proposal_Defense.pdf`: `0e3fecbae4464575cb05bfebc7c2658124039bc670058cf1a250752eb3f92a15`
