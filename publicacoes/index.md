---
layout: page
lang: pt
nav_key: publications
translation_url: "/en/publications/"
title: "Publicações"
description: "Área reservada à produção científica de Jonathan Ribeiro, com referências adicionadas após conferência bibliográfica."
eyebrow: "Produção científica"
intro: "Uma lista de publicações organizada para leitura, citação e acesso aos materiais relacionados à pesquisa."
permalink: /publicacoes/
---
{% assign locale = page.lang %}
{% assign publications = site.data.publications.items %}
{% assign empty = site.data.publications.empty[locale] %}

<section class="section content-section" aria-labelledby="bibliografia">
  <div class="section-head">
    <div>
      <span class="section-label">Produção científica</span>
      <h2 id="bibliografia">Referências verificadas</h2>
    </div>
    <p>Artigos, capítulos, preprints e outros resultados serão apresentados com metadados consistentes e links canônicos.</p>
  </div>

  {% if publications.size > 0 %}
    <ol class="publication-list">
      {% for publication in publications %}
        <li class="entry publication-entry">
          <p class="meta">{{ publication.year }} · {{ publication.type }}</p>
          <h3>{{ publication.title }}</h3>
          <p>{{ publication.authors | join: ', ' }}</p>
          {% if publication.container_title %}<p class="muted"><em>{{ publication.container_title }}</em></p>{% endif %}
          {% if publication.doi %}<a class="text-link" href="https://doi.org/{{ publication.doi }}">DOI <span aria-hidden="true">↗</span></a>{% elsif publication.url %}<a class="text-link" href="{{ publication.url }}">Acessar <span aria-hidden="true">↗</span></a>{% endif %}
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

<section class="section content-section" aria-labelledby="criterio-publicacoes">
  <div class="section-head">
    <div>
      <span class="section-label">Critério editorial</span>
      <h2 id="criterio-publicacoes">Uma lista feita para leitura e citação</h2>
    </div>
    <p>Cada registro poderá reunir autoria, ano, veículo, DOI ou link permanente, disponibilidade de acesso e materiais relacionados.</p>
  </div>
</section>
