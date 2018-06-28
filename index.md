---
title:
layout: splash
customjs:
 - assets/js/t.min.js
 - assets/js/landingPage.js
---

<h1>Welcome to my personal GitHub Page.</h1>

{% for js in page.customjs %}
<script type="text/javascript" src="{{ js }}"></script>
{% endfor %}
