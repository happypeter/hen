---
layout: default
title: hen
---

  <h1>Peter Blog Posts</h1>
  <ul class="posts">
    {% for post in site.posts %}
      <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="/hen{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
