# Interview with the Vampire transcript set: audit report

## Scope

This package contains speaker-attributed transcripts for all 22 supplied episodes: Season 1 (7), Season 2 (8), and Season 3 (7). Episode previews, companion promos, subtitle-site watermarks, and post-episode insider segments are excluded. Opening recaps remain included.

No episode audio or video was used. Timing and English subtitle wording come from the supplied SRT files. S01E01 uses the revised pilot teleplay, and S02E08 uses OCR alignment to the supplied production script. Explicit speaker labels in the supplied Season 2 subtitles are retained. Remaining turns use text and scene continuity recognition.

## Confidence states

| State | Meaning |
|---|---|
| `confirmed` | Explicit subtitle cue, production-script cue, or exact supplied teleplay support. |
| `high` | Strong script alignment, exact attributed-dialogue match, or close grammatical and temporal continuity. |
| `uncertain` | Best named candidate from text-only context. Review this state first. |

## Multilingual dialogue

The `dialogue` field holds spoken wording. `english_subtitle` holds the corresponding English subtitle or translation when the spoken wording differs. `language` identifies French or mixed dialogue where detected. Pilot French that the supplied English track omitted is restored from the teleplay when explicit. Where the teleplay specifies French but prints only English, the French is reconstructed and marked `uncertain` rather than represented as verbatim performance dialogue.

For `uncertain` rows, `speaker_candidates` records the next-best text-only candidates where available.

## Coverage

| Episode | Title | Turns | Confirmed | High | Uncertain | Named/descriptive speakers |
|---|---|---:|---:|---:|---:|---:|
| S01E01 | In Throes of Increasing Wonder... | 1143 | 903 | 234 | 6 | 31 |
| S01E02 | After the Phantoms of Your Former Self | 866 | 0 | 37 | 829 | 5 |
| S01E03 | Is My Very Nature That of a Devil | 762 | 0 | 32 | 730 | 5 |
| S01E04 | The Ruthless Pursuit of Blood with All a Child's Demanding | 716 | 1 | 21 | 694 | 7 |
| S01E05 | A Vile Hunger for Your Hammering Heart | 760 | 0 | 29 | 731 | 6 |
| S01E06 | Like Angels Put in Hell by God | 781 | 0 | 42 | 739 | 4 |
| S01E07 | The Thing Lay Still | 711 | 0 | 19 | 692 | 5 |
| S02E01 | What Can the Damned Really Say to the Damned | 690 | 0 | 22 | 668 | 4 |
| S02E02 | Do You Know What It Means to Be Loved by Death | 867 | 0 | 18 | 849 | 5 |
| S02E03 | No Pain | 772 | 86 | 13 | 673 | 17 |
| S02E04 | I Want You More Than Anything in the World | 902 | 69 | 14 | 819 | 18 |
| S02E05 | Don't Be Afraid, Just Start the Tape | 962 | 0 | 47 | 915 | 5 |
| S02E06 | Like the Light by Which God Made the World Before He Made Light | 741 | 0 | 27 | 714 | 8 |
| S02E07 | I Could Not Prevent It | 813 | 0 | 34 | 779 | 7 |
| S02E08 | And That's the End of It. There's Nothing Else | 897 | 521 | 93 | 283 | 14 |
| S03E01 | Detroit | 985 | 2 | 164 | 819 | 8 |
| S03E02 | Toledo | 957 | 2 | 74 | 881 | 8 |
| S03E03 | Toronto | 1025 | 4 | 133 | 888 | 6 |
| S03E04 | The Devil's Road | 1066 | 2 | 179 | 885 | 5 |
| S03E05 | New York | 1016 | 4 | 129 | 883 | 9 |
| S03E06 | Montreal | 1053 | 7 | 125 | 921 | 7 |
| S03E07 | The Failures | 1036 | 9 | 65 | 962 | 6 |

Total dialogue turns: **19,521**. Confirmed: **1,610**. High: **1,551**. Uncertain: **16,360**.

## Files

Each episode folder contains Markdown, CSV, and JSONL. The package root also contains series-wide CSV and JSONL files plus this report. CSV is the easiest format for filtering by `confidence`; Markdown is optimized for reading; JSONL is optimized for downstream processing.
