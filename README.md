# Langille Lab website

Source for [morganlangille.com](https://morganlangille.com), built with Jekyll and served by GitHub Pages.

Most updates are edits to one of three data files in `_data/`. You can make them on github.com: open the file, click the pencil icon, edit, and commit. The site rebuilds itself within a minute or two.

## Add a publication

Open `_data/publications.yml` and add an entry at the top with just the DOI:

```yaml
- doi: 10.1186/s40168-026-02529-z
```

When you commit, a GitHub Action looks up the title, authors, journal and year and fills them in, then the site rebuilds. You can watch it under the Actions tab. Papers without a DOI can be written out in full; copy the shape of any existing entry.

Optional fields on any entry:

* `featured: true` shows the paper under Selected publications on the homepage (up to four, newest first).
* `tags: [methods]` labels the paper for later grouping.

## Update people

Edit `_data/people.yml`.

* **Current members** are listed in the order shown on the page. Put a photo in `images/` and name it in `photo:`, or leave `photo:` out to show initials.
* **When someone leaves,** move them to `alumni:` with their group and the year they left. Add `now:` only if you know where they went.

## Update software

Edit `_data/software.yml`. `home: true` shows a tool on the homepage.

## Pages

| File | Page |
| --- | --- |
| `index.html` | Home |
| `research.html` | Research |
| `software.html` | Software |
| `members.html` | People |
| `pubs.html` | Publications |
| `positions.html` | Join us |
| `contact.html` | Contact |

Shared pieces live in `_layouts/default.html`, `_includes/` (header, footer, publication entry) and `assets/css/site.css`. Contact details and links used across the site are in `_config.yml`.
