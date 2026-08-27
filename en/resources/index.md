---
layout: page
lang: en
nav_key: resources
translation_url: "/recursos/"
title: "Code & data"
description: "Code and tools developed by Jonathan Ribeiro, with space for future acoustic and ecological research datasets."
eyebrow: "Code, tools, and data"
intro: "Computational resources connecting acoustic data, validation, and reproducible research workflows."
permalink: /en/resources/
---
{% assign locale = page.lang %}

<section class="section content-section" aria-labelledby="repositories">
  <div class="section-head">
    <div>
      <span class="section-label">Public code</span>
      <h2 id="repositories">Featured repositories</h2>
    </div>
    <p>Tools connecting acoustic-data processing, human review, and the organization of scientific workflows.</p>
  </div>
  <div class="resource-list">
    {% for repository in site.data.resources.repositories %}
      <article class="entry resource-entry">
        <div class="entry-heading">
          <p class="meta">{{ repository.type[locale] }}</p>
          <h3>{{ repository.name }}</h3>
        </div>
        <p>{{ repository.description[locale] }}</p>
        <ul class="tag-list" aria-label="Technologies and topics">
          {% for tag in repository.tags %}<li>{{ tag[locale] }}</li>{% endfor %}
        </ul>
        <a class="text-link" href="{{ repository.url }}" aria-label="Open {{ repository.name }} on GitHub">Code and documentation <span aria-hidden="true">↗</span></a>
      </article>
    {% endfor %}
  </div>
</section>

<section class="section content-section" aria-labelledby="other-resources">
  <div class="section-head">
    <div>
      <span class="section-label">Catalog</span>
      <h2 id="other-resources">Packages and datasets</h2>
    </div>
    <p>New resources will appear only when documentation and a confirmed public address are available.</p>
  </div>
  <div class="empty-grid">
    <div class="empty-state compact">
      <span class="empty-state-mark" aria-hidden="true">○</span>
      <div><h3>Packages</h3><p>{{ site.data.resources['empty'].packages[locale] }}</p></div>
    </div>
    <div class="empty-state compact">
      <span class="empty-state-mark" aria-hidden="true">○</span>
      <div><h3>Datasets</h3><p>{{ site.data.resources['empty'].datasets[locale] }}</p></div>
    </div>
  </div>
  <p class="section-action"><a class="text-link" href="{{ site.data.profile.github }}">View all repositories on GitHub <span aria-hidden="true">↗</span></a></p>
</section>
