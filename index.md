---
title:
layout: splash
customjs:
 - assets/js/landingPage.js
 - assets/js/t.min.js
---

<h1>Welcome to my GitHub Page.</h1>

{% for js in page.customjs %}
<script async type="text/javascript" src="{{ js }}"></script>
{% endfor %}
