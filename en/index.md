---
layout: home
lang: en
nav_key: home
translation_url: "/"
title: "Jonathan Ribeiro"
meta_title: "Bird bioacoustics and ecology"
description: "Bird research across passive acoustic monitoring, ecology, conservation, bioacoustics, and the development of tools in R and Python."
eyebrow: "A field notebook in sound"
hero_title: "I listen to landscapes to understand and conserve birds."
hero_intro: "I am Jonathan Ribeiro, a researcher in Recife. I bring passive acoustic monitoring, ecology, and code together to investigate birds and build research tools."
primary_cta:
  label: "Explore the research"
  url: "/en/research/"
secondary_cta:
  label: "View code on GitHub"
  url: "https://github.com/jrrribeiro"
permalink: /en/
---
{% assign locale = page.lang %}

<section class="section content-section" aria-labelledby="opening">
  <div class="section-head">
    <div>
      <span class="section-label">Opening note</span>
      <h2 id="opening">Between listening and evidence</h2>
    </div>
    <p>{{ site.data.profile.location_short[locale] }}</p>
  </div>
  <div class="prose lead-copy">
    <p>A recording preserves more than a sound: it holds traces of presence, rhythm, and change that may otherwise pass unnoticed in the field.</p>
    <p>My work begins where birds, soundscapes, and data meet. The aim is to frame useful ecological questions, organize evidence carefully, and build tools that make research clearer and more reproducible.</p>
  </div>
</section>

<section class="section content-section" aria-labelledby="research-lines">
  <div class="section-head">
    <div>
      <span class="section-label">01 · Research</span>
      <h2 id="research-lines">Intersecting lines of inquiry</h2>
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
  <p class="section-action"><a class="text-link" href="{{ '/en/research/' | relative_url }}">Explore the research overview <span aria-hidden="true">→</span></a></p>
</section>

<section class="section content-section" aria-labelledby="code-method">
  <div class="section-head">
    <div>
      <span class="section-label">02 · Code &amp; data</span>
      <h2 id="code-method">Code as part of the method</h2>
    </div>
    <p>R and Python support data organization, routine automation, and the development of research tools.</p>
  </div>
  <div class="resource-list">
    {% for repository in site.data.resources.repositories %}
      <article class="entry resource-entry">
        <div class="entry-heading">
          <p class="meta">{{ repository.type[locale] }}</p>
          <h3>{{ repository.name }}</h3>
        </div>
        <p>{{ repository.description[locale] }}</p>
        <a class="text-link" href="{{ repository.url }}" aria-label="Open {{ repository.name }} on GitHub">View repository <span aria-hidden="true">↗</span></a>
      </article>
    {% endfor %}
  </div>
  <p class="section-action"><a class="text-link" href="{{ '/en/resources/' | relative_url }}">Explore code and data <span aria-hidden="true">→</span></a></p>
</section>

<section class="section content-section" aria-labelledby="growing-archive">
  <div class="section-head">
    <div>
      <span class="section-label">03 · Archive</span>
      <h2 id="growing-archive">An archive taking shape</h2>
    </div>
    <p>The site will grow with verified records, keeping a clear distinction between what is available and what is still being organized.</p>
  </div>
  <nav class="index-list" aria-label="Academic sections being organized">
    <a class="index-entry" href="{{ '/en/projects/' | relative_url }}"><span>Projects</span><span aria-hidden="true">→</span></a>
    <a class="index-entry" href="{{ '/en/publications/' | relative_url }}"><span>Publications</span><span aria-hidden="true">→</span></a>
    <a class="index-entry" href="{{ '/en/teaching/' | relative_url }}"><span>Teaching and activities</span><span aria-hidden="true">→</span></a>
  </nav>
</section>

<section class="section cta-band" aria-labelledby="conversation">
  <div>
    <span class="section-label">Contact</span>
    <h2 id="conversation">Research also grows through conversation.</h2>
  </div>
  <a class="button-link" href="{{ '/en/contact/' | relative_url }}">Open contact channels <span aria-hidden="true">→</span></a>
</section>
