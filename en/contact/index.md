---
layout: page
lang: en
nav_key: contact
translation_url: "/contato/"
title: "Contact"
description: "The confirmed public channel for following Jonathan Ribeiro's work and getting in touch."
eyebrow: "Conversation and collaboration"
intro: "A starting point for following the work, discussing tools, and opening possibilities for collaboration."
permalink: /en/contact/
---
{% assign locale = page.lang %}

<section class="section content-section" aria-labelledby="contact-channels">
  <div class="section-head">
    <div>
      <span class="section-label">Public channels</span>
      <h2 id="contact-channels">Where to find me</h2>
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
