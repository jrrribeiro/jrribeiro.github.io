---
layout: page
lang: pt
nav_key: resources
translation_url: "/en/resources/"
title: "Código & dados"
description: "Código e ferramentas desenvolvidos por Jonathan Ribeiro, além de um espaço para futuros conjuntos de dados de pesquisa acústica e ecológica."
eyebrow: "Código, ferramentas e dados"
intro: "Recursos computacionais que aproximam dados acústicos, validação e fluxos de pesquisa reproduzíveis."
permalink: /recursos/
---
{% assign locale = page.lang %}

<section class="section content-section" aria-labelledby="repositorios">
  <div class="section-head">
    <div>
      <span class="section-label">Código público</span>
      <h2 id="repositorios">Repositórios em destaque</h2>
    </div>
    <p>Ferramentas que conectam processamento de dados acústicos, revisão humana e organização de fluxos científicos.</p>
  </div>
  <div class="resource-list">
    {% for repository in site.data.resources.repositories %}
      <article class="entry resource-entry">
        <div class="entry-heading">
          <p class="meta">{{ repository.type[locale] }}</p>
          <h3>{{ repository.name }}</h3>
        </div>
        <p>{{ repository.description[locale] }}</p>
        <ul class="tag-list" aria-label="Tecnologias e temas">
          {% for tag in repository.tags %}<li>{{ tag[locale] }}</li>{% endfor %}
        </ul>
        <a class="text-link" href="{{ repository.url }}" aria-label="Abrir {{ repository.name }} no GitHub">Código e documentação <span aria-hidden="true">↗</span></a>
      </article>
    {% endfor %}
  </div>
</section>

<section class="section content-section" aria-labelledby="outros-recursos">
  <div class="section-head">
    <div>
      <span class="section-label">Catálogo</span>
      <h2 id="outros-recursos">Pacotes e bases de dados</h2>
    </div>
    <p>Novos recursos só aparecem quando houver documentação e um endereço público confirmado.</p>
  </div>
  <div class="empty-grid">
    <div class="empty-state compact">
      <span class="empty-state-mark" aria-hidden="true">○</span>
      <div><h3>Pacotes</h3><p>{{ site.data.resources['empty'].packages[locale] }}</p></div>
    </div>
    <div class="empty-state compact">
      <span class="empty-state-mark" aria-hidden="true">○</span>
      <div><h3>Bases de dados</h3><p>{{ site.data.resources['empty'].datasets[locale] }}</p></div>
    </div>
  </div>
  <p class="section-action"><a class="text-link" href="{{ site.data.profile.github }}">Ver todos os repositórios no GitHub <span aria-hidden="true">↗</span></a></p>
</section>
