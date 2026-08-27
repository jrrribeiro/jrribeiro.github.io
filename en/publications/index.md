---
layout: page
lang: en
nav_key: publications
translation_url: "/publicacoes/"
title: "Publications"
description: "A space reserved for Jonathan Ribeiro's scientific output, with references added after bibliographic verification."
eyebrow: "Scientific output"
intro: "An organized publication list for reading, citation, and access to materials connected with the research."
permalink: /en/publications/
---
{% assign locale = page.lang %}
{% assign publications = site.data.publications.items %}
{% assign empty = site.data.publications.empty[locale] %}

<section class="section content-section" aria-labelledby="bibliography">
  <div class="section-head">
    <div>
      <span class="section-label">Scientific output</span>
      <h2 id="bibliography">Verified references</h2>
    </div>
    <p>Papers, chapters, preprints, and other outputs will be presented with consistent metadata and canonical links.</p>
  </div>

  {% if publications.size > 0 %}
    <ol class="publication-list">
      {% for publication in publications %}
        <li class="entry publication-entry">
          <p class="meta">{{ publication.year }} · {{ publication.type }}</p>
          <h3>{{ publication.title }}</h3>
          <p>{{ publication.authors | join: ', ' }}</p>
          {% if publication.container_title %}<p class="muted"><em>{{ publication.container_title }}</em></p>{% endif %}
          {% if publication.doi %}<a class="text-link" href="https://doi.org/{{ publication.doi }}">DOI <span aria-hidden="true">↗</span></a>{% elsif publication.url %}<a class="text-link" href="{{ publication.url }}">Access <span aria-hidden="true">↗</span></a>{% endif %}
        </li>
      {% endfor %}
    </ol>
  {% else %}
    <div class="empty-state">
      <span class="empty-state-mark" aria-hidden="true">○</span>
      <div>
        <h3>{{ empty.title }}</h3>
        <p>{{ empty.description }}</p>
        <p class="muted">{{ empty.note }}</p>
      </div>
    </div>
  {% endif %}
</section>

<section class="section content-section" aria-labelledby="publication-standard">
  <div class="section-head">
    <div>
      <span class="section-label">Editorial standard</span>
      <h2 id="publication-standard">A list designed for reading and citation</h2>
    </div>
    <p>Each record may include authorship, year, venue, DOI or URL, open-access status, and related materials.</p>
  </div>
</section>
