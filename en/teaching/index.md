---
layout: page
lang: en
nav_key: teaching
translation_url: "/ensino/"
title: "Teaching"
description: "A space for Jonathan Ribeiro's courses, workshops, talks, and academic materials."
eyebrow: "Teaching and academic activities"
intro: "A space for teaching, training, talks, and supporting materials presented in their proper contexts."
permalink: /en/teaching/
---
{% assign locale = page.lang %}
{% assign activities = site.data.teaching.items %}
{% assign empty = site.data.teaching.empty[locale] %}

<section class="section content-section" aria-labelledby="academic-activities">
  <div class="section-head">
    <div>
      <span class="section-label">Activities</span>
      <h2 id="academic-activities">Teaching, training, and exchange</h2>
    </div>
    <p>A space for academic activities presented with dates, context, and supporting materials.</p>
  </div>

  {% if activities.size > 0 %}
    <div class="record-list">
      {% for activity in activities %}
        <article class="entry record-entry">
          <p class="meta">{{ activity.year }} · {{ activity.kind[locale] }}</p>
          <h3>{{ activity.title[locale] }}</h3>
          <p>{{ activity.summary[locale] }}</p>
          {% if activity.url %}<a class="text-link" href="{{ activity.url }}">View activity <span aria-hidden="true">↗</span></a>{% endif %}
        </article>
      {% endfor %}
    </div>
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
