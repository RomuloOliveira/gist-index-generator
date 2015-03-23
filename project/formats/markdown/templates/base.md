gist-files
==========

Index of  of my gist-files. Life is too short to access {{ url }}

{% for gist in gists %}
- [{{ gist.filename }}]({{ gist.url }})  
{%- if gist.description %}
  - {{ gist.description }}
{%- endif -%}
{% endfor %}
