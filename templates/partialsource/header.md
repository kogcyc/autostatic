<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <meta name="description" content="{{ desc }}">
    <meta name="description" content="{{ desc }}">
    <meta property="og:title" content="{{ title }}">
    <meta property="og:description" content="{{ desc }}">
    {% if image %}
    <meta property="og:image" content="{{ image }}">
    {% endif %}
    <link rel="stylesheet" href="/static/style.css">

    
    <!-- Open Graph / Social Meta -->
    <meta property="og:title" content="{{ title }}">
    <meta property="og:description" content="{{ desc }}">
    {% if image %}<meta property="og:image" content="{{ image }}">{% endif %}
  
</head>
