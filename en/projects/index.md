---
layout: page
lang: en
nav_key: projects
translation_url: "/projetos/"
title: "Projects"
description: "A space for Jonathan Ribeiro's research projects, with stages and descriptions published only after verification."
eyebrow: "Research in progress"
intro: "A notebook for following projects in development, their contexts, and the materials ready to be shared."
permalink: /en/projects/
---
{% assign locale = page.lang %}
{% assign projects = site.data.projects.items %}
{% assign empty_state = site.data.projects['empty'][locale] %}

<section class="section content-section" aria-labelledby="project-list">
  <div class="section-head">
    <div>
      <span class="section-label">Project notebook</span>
      <h2 id="project-list">Initiatives and collaborations</h2>
    </div>
    <p>A space for bringing questions, methods, progress, and outcomes together without losing the context of each initiative.</p>
  </div>

  {% if projects.size > 0 %}
    <div class="record-list">
      {% for project in projects %}
        <article class="entry record-entry">
          <p class="meta">{{ project.status[locale] }}{% if project.period %} · {{ project.period }}{% endif %}</p>
          <h3>{{ project.title[locale] }}</h3>
          <p>{{ project.summary[locale] }}</p>
          {% if project.url %}<a class="text-link" href="{{ project.url }}">Open project <span aria-hidden="true">↗</span></a>{% endif %}
        </article>
      {% endfor %}
    </div>
  {% else %}
    <div class="empty-state">
      <span class="empty-state-mark" aria-hidden="true">○</span>
      <div>
        <h3>{{ empty_state.title }}</h3>
        <p>{{ empty_state.description }}</p>
        <p class="muted">{{ empty_state.note }}</p>
        <a class="text-link" href="{{ empty_state.action_url | relative_url }}">{{ empty_state.action_label }} <span aria-hidden="true">→</span></a>
      </div>
    </div>
  {% endif %}
</section>

<section class="section content-section" aria-labelledby="project-structure">
  <div class="section-head">
    <div>
      <span class="section-label">Structure</span>
      <h2 id="project-structure">What each record will include</h2>
    </div>
  </div>
  <ul class="detail-list">
    <li><strong>Question and context</strong><span>The ecological problem and its motivation.</span></li>
    <li><strong>Methods and scope</strong><span>How acoustic, ecological, or computational data enter the work.</span></li>
    <li><strong>Progress</strong><span>The current stage and materials ready to be shared.</span></li>
    <li><strong>Related outputs</strong><span>Publications, code, and datasets when available.</span></li>
  </ul>
</section>
