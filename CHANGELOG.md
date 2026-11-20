# Changelog

All notable changes to liaqat-gta6-clipper (Learn With Liaqat edition, based on gta6-clipper by NoCodeHack). Newest first.

## 1.0.13
### Added
- Light mode for low-memory laptops: under 12 GB of RAM the app makes 1 Short at a time, renders at 30 fps, uses the first hour of very long streams, deletes the downloaded audio after the transcript and checks free disk space before it starts.
### Changed
- Make, Schedule, Brand, Auto-post and Settings now follow the app language in all 8 languages.
### Testing
- Light mode on the same video and picks: peak memory 5.84 GB -> 1.85 GB, about 25% slower, both Shorts passed the quality check.
- All 8 languages walked in the browser with no untranslated labels and no errors.

## 1.0.12
### Changed
- Sharper video: the stretched 9:16 crops are scaled with a sharper method and lightly sharpened, the in-between steps no longer lose detail, and the final file keeps more of it.
### Testing
- Same moment rendered before and after: face/cam panel twice as sharp, game panel 15-25% sharper; render about 14% slower.

## 1.0.11
### Added
- What's new: Settings > Updates now lists every version with what changed and how it was tested, and shows what an update brings before you install it. After each update, a short "What's new" window appears once.
### Fixed
- Live hunt on Kick no longer stops after a few minutes. When a stream goes silent without closing, the recorder restarts it within 30 seconds.
- A face shown on an in-game TV or a video inside the stream now fills the Short, without the dark room above it.
- The Short screen (versions, Ask the AI, Look, post text, schedule) now follows the app language in all 8 languages.
### Testing
- Kick: a live channel recorded 11 minutes without a gap; a stream that goes silent was restarted every time.
- In-game TV Short: the dark band went from 5.6 s to none on the face shots.
- All 8 languages checked in the browser with no errors.

## 1.0.10
### Fixed
- "End 2 s earlier" and other trims in "Ask the AI to change it" now work. The renderer used to move the end back to the previous full sentence (sometimes 13 s earlier), so the AI refused. A trim you ask for now keeps your end, on the last whole word, and is never lengthened again.
### Testing
- "End 2 s earlier" clicked in the app on a real Short: new version in 3 minutes, ends 3.1 s earlier on a whole word, quality check passed.

## 1.0.9
### Fixed
- Shorts that came out too quiet now get their sound brought to the normal level (-14 LUFS) at the end of the render, so they pass the quality check.
- The new screens (Add your voice, Help, Disk space, AI tool test and costs, Video on my PC) now follow the app language: English, French, Spanish, Portuguese, German, Arabic, Italian and Turkish.
- After a run, the AI opens the app for you so you can review your Shorts and add your voice.
- "Video picked" shows the file name instead of the whole path on Windows.
### Testing
- A Short that measured -18.7 LUFS came out at -14.2 LUFS and passed the quality check.
- All 8 languages checked in the browser (no English left, no errors, Arabic right to left).

## 1.0.8
### Added
- More sources: links from TikTok, X, Instagram, Facebook, Rumble, Vimeo, Reddit and Dailymotion, besides YouTube, Twitch and Kick. **Make > Video on my PC** clips your own recordings. Short clips (from 8 s) work when you give the link.
- Add your voice in the app: open a Short, pause where you want to talk, record one sentence (or use a phone voice memo) and get a new version with the game sound lowered under you. The original stays.
- Help page (side menu and Settings): answers to the questions asked most.
- Settings > AI tool shows what each tool costs, and **Test this AI tool** checks it and says how to fix it if it doesn't answer.
- Settings > Disk space: see how much the downloaded videos take and delete them. Shorts and transcripts stay.
- **Show in folder** on every Short.
- Google Antigravity CLI as an AI tool.
### Fixed
- "Make a version with this look" made no new version when the app runs from another folder (transcript path). A render that makes nothing now reports a failure.
- Runs in Antigravity no longer stop after 30 minutes: the app downloads, transcribes and renders by itself and asks Antigravity only to pick the moments. When its free quota runs out, the app picks with No AI.
- Shorts no longer come out too short (9 to 12 s) after the silences are cut: the app widens the moment and renders it once more. No AI also skips moments that are mostly silence.
- When a site changes and downloads break (TikTok did), the skill updates its downloader to the newest build and tries again.
- Failed steps now show **How to fix** in plain words: credit balance too low, quota ran out, Codex sandbox without internet, not signed in, YouTube login, ffmpeg missing.
- Setup ends by opening the app.
- Live hunt says it watches from the moment you start, and where to find the hours before.
### Testing
- Claude Code, fresh install of this version: install + setup + 1 Short in 20 min, QC PASS.
- Codex 0.162 with full access: install + setup + 1 Short in 16.5 min, QC PASS.
- Antigravity CLI 1.5.11: install + setup 234 s; from the app 3 of 3 Shorts in 29 min; No AI fallback 1 of 1 when its quota ran out.
- TikTok link: downloader updated itself, 1 Short QC PASS. Video file from the PC (folder with spaces): 1 Short QC PASS.
- A Short that came out at 10.1 s re-rendered at 15.0 s. No AI: 3 of 3 at full length (before: 2 of 2 too short).
- Voice: recorded in the browser and from a file, new version made in about 10 s.

## 1.0.7
### Added
- OpenCode as an AI tool (Settings > AI tool). The install and setup sentences also work inside OpenCode, on its free models.
- Clip rules: each streamer shows Clipping allowed, Has clip tips, No clipping or Rules unknown, with the source. Live hunt and Make Shorts stop on "No clipping" unless you confirm you have permission. The list updates with the app.
### Testing
- OpenCode 1.19.6 on Windows, free model: install 80 s, setup 3.5 min, app AI test OK.

## 1.0.6
### Added
- Past streams: every streamer has a "Past streams" list (last 5 ended streams on Twitch, Kick and YouTube) with a "Make Shorts" button.
- "Paste a link" accepts a live stream, a past stream (VOD) or any video.
### Fixed
- Live hunts keep running and stay visible after the app restarts.
- "1 clip found" instead of "1 clips found", in all 8 languages.

## 1.0.5
### Added
- README with screenshots, a live-hunt gallery and an install-in-one-sentence section.
- Live hunt can watch up to 8 streams at once (Twitch, YouTube, Kick); each chat spike is rendered into a finished Short.
### Changed
- Spacing between blocks is applied globally, so cards no longer touch their buttons.

## 1.0.4
### Fixed
- Live clips that were mostly gameplay without speech are now kept whole instead of being cut to about one second.
- Live spikes are rendered into the same Library as the batch Shorts, one at a time.
### Changed
- Maximum Short length raised from 32 s to 60 s, because viral moments run 6 to 61 s.

## 1.0.3
### Changed
- AI cost labels now show a measured range as a share of a Claude Pro session (Smart about 8-25%, Deep about 30-90% per 10 Shorts) instead of a flat estimate.

## 1.0.2
### Added
- "Connect Blotato" dialog with four steps and the official Blotato MCP command.
### Changed
- The Blotato card is separated from the buttons below it; the side-menu Auto-post button opens the dialog.

## 1.0.1
### Added
- Visible Blotato auto-post card on Home, an Auto-post button in the side menu and a banner on the Approved page.
### Changed
- Moments are anchored on the chat spike and start with their setup; windows up to 60 s are allowed.

## 1.0.0
### Added
- Skill that finds GTA 6 videos and streams, transcribes on your PC, picks the best moments and renders finished 9:16 Shorts with face-tracked framing, word captions, hook title, cover and post text.
- Local web app: Home, Shorts by day, one-at-a-time review (approve or reject), Approved, scheduling, streamers, brand and settings.
- Live hunt: records a stream, watches chat speed and loudness and cuts a Short on a spike.
- Pick modes Free, Smart and Deep; Ask the AI to change a Short in plain words.
- Updates every 5 hours that keep your workspace, brand and clips.
