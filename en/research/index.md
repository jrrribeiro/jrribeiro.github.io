---
layout: page
lang: en
nav_key: research
translation_url: "/pesquisa/"
title: "Research"
description: "Jonathan Ribeiro's interests in passive acoustic monitoring, community and population ecology, conservation, and bird bioacoustics."
eyebrow: "Questions, signals, and scales"
intro: "Sound offers a way to observe birds and connect ecological patterns with questions about communities, populations, and conservation."
permalink: /en/research/
---
{% assign locale = page.lang %}
{% assign workflow = site.data.research.workflow[locale] %}

<section class="section content-section" aria-labelledby="research-overview">
  <div class="section-head">
    <div>
      <span class="section-label">Overview</span>
      <h2 id="research-overview">Birds as the common thread</h2>
    </div>
    <p>{{ site.data.research.intro[locale] }}</p>
  </div>
  <p class="lead-copy">The focus lies in the relationship between what can be heard, the ecological patterns under investigation, and the evidence needed to support conservation.</p>
</section>

<section class="section content-section" aria-labelledby="research-themes">
  <div class="section-head">
    <div>
      <span class="section-label">Themes</span>
      <h2 id="research-themes">Four connected perspectives</h2>
    </div>
  </div>
  <div class="topic-grid">
    {% for theme in site.data.research.themes %}
      <article class="entry topic-entry" id="{{ theme.key }}">
        <span class="entry-marker" aria-hidden="true">{{ theme.marker }}</span>
        <h3>{{ theme.title[locale] }}</h3>
        <p>{{ theme.description[locale] }}</p>
      </article>
    {% endfor %}
  </div>
</section>

<section class="section content-section" aria-labelledby="research-workflow">
  <div class="section-head">
    <div>
      <span class="section-label">Computational practice</span>
      <h2 id="research-workflow">{{ workflow.title }}</h2>
    </div>
    <p>{{ workflow.description }}</p>
  </div>
  <ol class="process-list">
    {% for step in workflow.steps %}
      <li><span aria-hidden="true">0{{ forloop.index }}</span>{{ step }}</li>
    {% endfor %}
  </ol>
  <p class="section-action"><a class="text-link" href="{{ '/en/resources/' | relative_url }}">View tools under development <span aria-hidden="true">→</span></a></p>
</section>
