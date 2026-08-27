---
layout: page
lang: pt
nav_key: contact
translation_url: "/en/contact/"
title: "Contato"
description: "Canal público confirmado para acompanhar o trabalho e entrar em contato com Jonathan Ribeiro."
eyebrow: "Conversa e colaboração"
intro: "Um ponto de partida para acompanhar o trabalho, conversar sobre ferramentas e abrir possibilidades de colaboração."
permalink: /contato/
---
{% assign locale = page.lang %}

<section class="section content-section" aria-labelledby="canais-contato">
  <div class="section-head">
    <div>
      <span class="section-label">Canais públicos</span>
      <h2 id="canais-contato">Onde me encontrar</h2>
    </div>
    <p>{{ site.data.contact.intro[locale] }}</p>
  </div>
  <div class="contact-list">
    {% for channel in site.data.contact.channels %}
      <article class="entry contact-entry">
        <h3>{{ channel.label }}</h3>
        <p>{{ channel.description[locale] }}</p>
        <a class="text-link" href="{{ channel.url }}">{{ channel.url | remove: 'https://' }} <span aria-hidden="true">↗</span></a>
      </article>
    {% endfor %}
  </div>
  <p class="muted availability-note">{{ site.data.contact.unavailable[locale] }}</p>
</section>
