---
layout: page
lang: pt
nav_key: research
translation_url: "/en/research/"
title: "Pesquisa"
description: "Interesses de Jonathan Ribeiro em monitoramento acústico passivo, ecologia de comunidades e populações, conservação e bioacústica de aves."
eyebrow: "Perguntas, sinais e escalas"
intro: "O som oferece uma forma de observar aves, investigar padrões ecológicos e responder a perguntas sobre comunidades, populações e conservação."
permalink: /pesquisa/
---
{% assign locale = page.lang %}
{% assign workflow = site.data.research.workflow[locale] %}

<section class="section content-section" aria-labelledby="panorama-pesquisa">
  <div class="section-head">
    <div>
      <span class="section-label">Panorama</span>
      <h2 id="panorama-pesquisa">Aves como fio condutor</h2>
    </div>
    <p>{{ site.data.research.intro[locale] }}</p>
  </div>
  <p class="lead-copy">O foco está nas relações entre o que se ouve, os padrões ecológicos que se deseja compreender e as evidências necessárias para apoiar a conservação.</p>
</section>

<section class="section content-section" aria-labelledby="eixos-pesquisa">
  <div class="section-head">
    <div>
      <span class="section-label">Eixos</span>
      <h2 id="eixos-pesquisa">Quatro perspectivas conectadas</h2>
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

<section class="section content-section" aria-labelledby="fluxo-pesquisa">
  <div class="section-head">
    <div>
      <span class="section-label">Prática computacional</span>
      <h2 id="fluxo-pesquisa">{{ workflow.title }}</h2>
    </div>
    <p>{{ workflow.description }}</p>
  </div>
  <ol class="process-list">
    {% for step in workflow.steps %}
      <li><span aria-hidden="true">0{{ forloop.index }}</span>{{ step }}</li>
    {% endfor %}
  </ol>
  <p class="section-action"><a class="text-link" href="{{ '/recursos/' | relative_url }}">Ver ferramentas em desenvolvimento <span aria-hidden="true">→</span></a></p>
</section>
