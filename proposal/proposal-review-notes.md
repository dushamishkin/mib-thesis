# Proposal review and document verification

## Local Word display cleanup — 14 October

The author closed Dushkin_Thesis_Proposal.docx and authorised removal of the grey
editable-region brackets/shading. Removed all 54 w:permStart/w:permEnd elements
from that external author copy. The only changed package part is document.xml;
comparison after removing exactly those elements confirms identical remaining XML.
All other parts, text, styles, numbering, hyperlinks and user edits are unchanged.
The repository DOCX is not replaced or changed by this external-file repair.

Before/after renders both have 16 pages. Every cleaned page was visually inspected;
15 images are pixel-identical, and the last differs only in the Chinese date-label
glyph rendering. Text extraction is identical. This is a bounded display cleanup,
not a correction of the author copy’s pre-existing list numbering.

Cleaned external author-copy SHA-256: `16d0ff5b3da728d93253848be5965eca42df45b0b42b1f83f1fcef7e886b7743`.

Input SHA-256: `08903b28b7685fe7ae283cdc526b4064b0f0afb254a390af223cdceefad9150e`.

## SQLDriller link repair — 14 October

Replaced the unavailable IPADS PDF URL with the working
[coauthor-hosted PDF](https://haoran-ding.github.io/assets/pdf/sqldriller.pdf), reached
from [Haoran Ding’s publications](https://haoran-ding.github.io/). PDF title, author list,
28-page extent and DOI 10.1145/3725271 match reference [10]. This verifies the replacement
link and identity, not a new full-paper reading. Markdown source and both active reading
cards use the same URL. Generated BibTeX was not edited.

The author saved and closed Word before the local edit. Only one hyperlink target in
word/_rels/document.xml.rels changed; every other local package part is byte-identical
to the saved author version. All 16 local rendered pages were inspected; pre-existing
Word list numbering continues across some sections and is outside this link-only edit.
The author’s local cover/reference/schedule and Word formatting changes are preserved
and remain uncommitted; the publication includes only the hyperlink correction against
the previously committed DOCX. Local Word content consequently differs from Markdown.

Published link-only DOCX SHA-256: `92bd1c96fc98ac45d2ce374641fc50c20bf5117a78d63f0cb4de107f4bc5a4f3`.

Local author-edited DOCX after link repair SHA-256: `08903b28b7685fe7ae283cdc526b4064b0f0afb254a390af223cdceefad9150e`.

Current Markdown SHA-256: `0f05d983831ffc07e6227aeff25e8a6f2b132525bd1b9267cff55f829ad35ec0`.

## Prior formatting verification — before the author’s subsequent Word edits

Updated 14 October 2026. The author completed narrative review and authorised transfer
into the supplied university template. The [Word draft](thesis-proposal-draft.docx)
now matches the six substantive sections of [proposal-draft.md](proposal-draft.md).
It supersedes the 10 October DOCX; its earlier QA record remains in Git history.
This is a review draft, not a signed, supervisor-approved or submitted document.

## Content and requirements

The transfer preserves all agreed substantive paragraphs, subheadings, table cells,
13 numbered references and their links. Markdown metadata and editorial process notes
are excluded from the university form. Main headings use the template's original
six bilingual labels; the actual methodology opens Section 3. Both improvement names
remain consistent. No scientific rewriting or experimental results were added.
The author's removal of the Chapter 5 deadline introduction is preserved.

Section 1 has approximately 1,300 English words excluding references, exceeding the
form's 1,000-word minimum. References remain at the end of Section 1 in first-citation
order. The native condition and schedule tables are editable; lists use Word numbering.
English body text uses Times New Roman 12 pt and 1.25 spacing. The supplied form,
rather than generic final-thesis formatting, governs the cover and bilingual elements.
Institutional sources and deadlines: [requirements](../requirements/README.md).

## Personal and administrative fields

The author confirmed Academic Master Student, Full-time and Self-proposed Project on
14 October. These are populated, including the selected native project-source checkbox.
Name, student ID, programme, school and supervisor follow the author/project record.

| Field | Current treatment | Remaining action |
|---|---|---|
| Defense venue | Blank; template's sample school removed | Enter the announced room or platform when known |
| Student signature | Blank | Author signs the approved version |
| Signing date | Blank; automatic DATE field removed | Enter actual signing date |
| Cover proposal date | 22 October 2026 | Uses the scheduled proposal-defense date, distinct from signing date |

Supervisor approval of this revised document remains outstanding. The September topic
approval concerned the earlier direction. The [email](supervisor-email-draft.md) is an
updated unsent draft. No email, signature or system upload has been performed.

## Visual and structural checks

The bundled document renderer produced **16 pages**: one cover, two unchanged
institutional instruction pages and 13 numbered report pages. Every page of the final
render was visually inspected. Chinese glyphs, English typography, cover title wrapping,
numbered lists, table borders and repeated schedule headers, bibliography, page numbers
and blank signature/date were checked. No clipping, overlap, broken row or empty overflow
page was observed. Original instruction pagination is retained, including its short
second page. The reference/final image comparison confirms both instruction pages
unchanged. Layout may vary with the Word installation and font substitutions.

The initial renderer lacked Chinese glyphs; QA was repeated with system Chinese fonts
and explicit Songti/Heiti fallback. This changes the QA environment, not template fonts.
The final package was not resaved by LibreOffice. PAGE fields are retained and
`updateFields=true` requests refresh when opened in Word; no native Word refresh is claimed.

The original template is byte-identical. Both section geometries (A4, template margins)
and all nine content controls are preserved. Control properties differ only in the
author-confirmed Self-proposed checkbox state; existing dropdown values are confirmed.
All original permission ranges, bookmarks, relationships, images, styles, headers and
footers survive. Existing numbering definitions are unchanged; appended definitions
provide independent lists with explicit restarts.

Only four package parts changed: `word/document.xml`, `word/settings.xml`,
`word/numbering.xml` and `word/_rels/document.xml.rels`. All other parts are byte-identical
to the template. Added relationships are external bibliography hyperlinks. Layout edits
shorten the empty cover spacer, permit expanding rows, prevent isolated lines/headings,
keep references together and repeat table headers. The automatic sample signing date
is deliberately removed. Structural, heading, field, image, style and control audits ran.
Accessibility audit found no high-severity issues; two generic header warnings apply
to the original identification/source form tables, which are not data tables. The two
new comparison/schedule tables have native repeating header rows.

Verified DOCX SHA-256: `cf669d6b3504f342956c5517180e3398dc7d5a2f72c5009d962a9194785a5f4f`.

Narrative source SHA-256: `71bd001d3d5e47f9f6341b625b40af800ff24dfa77906c23d7093dbb3f459fad`.

Unchanged template SHA-256: `07a5d42c83c3e0ffd61a800ffd38986a421172fe639ec0c540f3004d36e6b57c`.

## Literature and next review

This formatting task preserves the existing checked reference metadata and links;
it does not claim a new literature search or full-paper audit. Primary/version checks
and selected-reading limits remain in the [reading brief](../literature/reading-brief.md)
and [literature index](../literature/references.md). New narrative records still require
identifier reconciliation in Zotero and review of its generated export before submission.
No Zotero record, generated BibTeX, export setting or cloud synchronization was changed.

Next: review the formatted document with the supervisor, reconcile bibliography records,
fill the venue when announced and sign only the approved version. Model, spending cap,
sample size and evaluation freeze remain development decisions before paid experiments.
