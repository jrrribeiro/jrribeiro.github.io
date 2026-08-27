---
layout: home
lang: pt
nav_key: home
translation_url: "/en/"
title: "Jonathan Ribeiro"
meta_title: "Bioacústica e ecologia de aves"
description: "Pesquisa sobre aves na interface entre monitoramento acústico passivo, ecologia, conservação, bioacústica e desenvolvimento de ferramentas em R e Python."
eyebrow: "Caderno de campo sonoro"
hero_title: "Escuto paisagens para compreender e conservar aves."
hero_intro: "Sou Jonathan Ribeiro, pesquisador em Recife. Aproximo monitoramento acústico passivo, ecologia e código para investigar aves e construir ferramentas de pesquisa."
primary_cta:
  label: "Explorar pesquisa"
  url: "/pesquisa/"
secondary_cta:
  label: "Ver código no GitHub"
  url: "https://github.com/jrrribeiro"
permalink: /
---
{% assign locale = page.lang %}

<section class="section content-section" aria-labelledby="abertura">
  <div class="section-head">
    <div>
      <span class="section-label">Nota de abertura</span>
      <h2 id="abertura">Entre escuta e evidência</h2>
    </div>
    <p>{{ site.data.profile.location_short[locale] }}</p>
  </div>
  <div class="prose lead-copy">
    <p>Uma gravação preserva mais que um som: ela registra indícios de presença, ritmos e mudanças que podem passar despercebidos em campo.</p>
    <p>Meu trabalho parte desse encontro entre aves, paisagens sonoras e dados. O objetivo é formular perguntas ecológicas úteis, organizar evidências com cuidado e criar ferramentas que tornem a pesquisa mais clara e reprodutível.</p>
  </div>
</section>

<section class="section content-section" aria-labelledby="linhas-pesquisa">
  <div class="section-head">
    <div>
      <span class="section-label">01 · Pesquisa</span>
      <h2 id="linhas-pesquisa">Linhas que se cruzam</h2>
    </div>
    <p>{{ site.data.research.intro[locale] }}</p>
  </div>
  <div class="topic-grid">
    {% for theme in site.data.research.themes %}
      <article class="entry topic-entry">
        <span class="entry-marker" aria-hidden="true">{{ theme.marker }}</span>
        <h3>{{ theme.title[locale] }}</h3>
        <p>{{ theme.description[locale] }}</p>
      </article>
    {% endfor %}
  </div>
  <p class="section-action"><a class="text-link" href="{{ '/pesquisa/' | relative_url }}">Conheça o panorama de pesquisa <span aria-hidden="true">→</span></a></p>
</section>

<section class="section content-section" aria-labelledby="codigo-metodo">
  <div class="section-head">
    <div>
      <span class="section-label">02 · Código &amp; dados</span>
      <h2 id="codigo-metodo">Código como parte do método</h2>
    </div>
    <p>R e Python apoiam a organização de dados, a automação de rotinas e o desenvolvimento de ferramentas para pesquisa.</p>
  </div>
  <div class="resource-list">
    {% for repository in site.data.resources.repositories %}
      <article class="entry resource-entry">
        <div class="entry-heading">
          <p class="meta">{{ repository.type[locale] }}</p>
          <h3>{{ repository.name }}</h3>
        </div>
        <p>{{ repository.description[locale] }}</p>
        <a class="text-link" href="{{ repository.url }}" aria-label="Abrir {{ repository.name }} no GitHub">Ver repositório <span aria-hidden="true">↗</span></a>
      </article>
    {% endfor %}
  </div>
  <p class="section-action"><a class="text-link" href="{{ '/recursos/' | relative_url }}">Explorar código e dados <span aria-hidden="true">→</span></a></p>
</section>

<section class="section content-section" aria-labelledby="arquivo-formacao">
  <div class="section-head">
    <div>
      <span class="section-label">03 · Arquivo</span>
      <h2 id="arquivo-formacao">Um arquivo em formação</h2>
    </div>
    <p>O site crescerá com registros conferidos, mantendo claro o que já está disponível e o que ainda está sendo organizado.</p>
  </div>
  <nav class="index-list" aria-label="Seções acadêmicas em organização">
    <a class="index-entry" href="{{ '/projetos/' | relative_url }}"><span>Projetos</span><span aria-hidden="true">→</span></a>
    <a class="index-entry" href="{{ '/publicacoes/' | relative_url }}"><span>Publicações</span><span aria-hidden="true">→</span></a>
    <a class="index-entry" href="{{ '/ensino/' | relative_url }}"><span>Ensino e atividades</span><span aria-hidden="true">→</span></a>
  </nav>
</section>

<section class="section cta-band" aria-labelledby="conversa">
  <div>
    <span class="section-label">Contato</span>
    <h2 id="conversa">Pesquisa também se faz em conversa.</h2>
  </div>
  <a class="button-link" href="{{ '/contato/' | relative_url }}">Abrir canais de contato <span aria-hidden="true">→</span></a>
</section>
