---
layout: page
lang: pt
nav_key: projects
translation_url: "/en/projects/"
title: "Projetos"
description: "Espaço para projetos de pesquisa de Jonathan Ribeiro, com estados e descrições publicados somente após conferência."
eyebrow: "Pesquisa em andamento"
intro: "Um caderno para acompanhar iniciativas em desenvolvimento, seus contextos e os materiais que puderem ser compartilhados."
permalink: /projetos/
---
{% assign locale = page.lang %}
{% assign projects = site.data.projects.items %}
{% assign empty_state = site.data.projects['empty'][locale] %}

<section class="section content-section" aria-labelledby="projetos-lista">
  <div class="section-head">
    <div>
      <span class="section-label">Caderno de projetos</span>
      <h2 id="projetos-lista">Iniciativas e colaborações</h2>
    </div>
    <p>Um espaço para reunir perguntas, métodos, andamento e resultados sem perder o contexto de cada iniciativa.</p>
  </div>

  {% if projects.size > 0 %}
    <div class="record-list">
      {% for project in projects %}
        <article class="entry record-entry">
          <p class="meta">{{ project.status[locale] }}{% if project.period %} · {{ project.period }}{% endif %}</p>
          <h3>{{ project.title[locale] }}</h3>
          <p>{{ project.summary[locale] }}</p>
          {% if project.url %}<a class="text-link" href="{{ project.url }}">Abrir projeto <span aria-hidden="true">↗</span></a>{% endif %}
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

<section class="section content-section" aria-labelledby="estrutura-projetos">
  <div class="section-head">
    <div>
      <span class="section-label">Estrutura</span>
      <h2 id="estrutura-projetos">O que cada registro reunirá</h2>
    </div>
  </div>
  <ul class="detail-list">
    <li><strong>Pergunta e contexto</strong><span>O problema ecológico e sua motivação.</span></li>
    <li><strong>Métodos e recorte</strong><span>Como dados acústicos, ecológicos ou computacionais entram no trabalho.</span></li>
    <li><strong>Andamento</strong><span>Etapa atual e materiais que já podem ser compartilhados.</span></li>
    <li><strong>Resultados relacionados</strong><span>Publicações, código e bases de dados quando existirem.</span></li>
  </ul>
</section>
