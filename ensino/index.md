---
layout: page
lang: pt
nav_key: teaching
translation_url: "/en/teaching/"
title: "Ensino"
description: "Espaço para disciplinas, minicursos, palestras e materiais acadêmicos de Jonathan Ribeiro, sem atividades não confirmadas."
eyebrow: "Ensino e atividades acadêmicas"
intro: "Um espaço para reunir experiências de ensino, formação, palestras e materiais de apoio com seus devidos contextos."
permalink: /ensino/
---
{% assign locale = page.lang %}
{% assign activities = site.data.teaching.items %}
{% assign empty_state = site.data.teaching['empty'][locale] %}

<section class="section content-section" aria-labelledby="atividades-academicas">
  <div class="section-head">
    <div>
      <span class="section-label">Atividades</span>
      <h2 id="atividades-academicas">Ensino, formação e troca</h2>
    </div>
    <p>Uma área para reunir atividades acadêmicas com datas, contextos e materiais de apoio.</p>
  </div>

  {% if activities.size > 0 %}
    <div class="record-list">
      {% for activity in activities %}
        <article class="entry record-entry">
          <p class="meta">{{ activity.year }} · {{ activity.kind[locale] }}</p>
          <h3>{{ activity.title[locale] }}</h3>
          <p>{{ activity.summary[locale] }}</p>
          {% if activity.url %}<a class="text-link" href="{{ activity.url }}">Ver atividade <span aria-hidden="true">↗</span></a>{% endif %}
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
      </div>
    </div>
  {% endif %}
</section>
