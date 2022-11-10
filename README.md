# HTMx-Dictionary

A small application to combine API requests with HTMx, a JavaScript library designed to extend the ability of HTML. Among other features, it allows POST/GET requests to be made without reloading the page, inserting the response directly in to any chosen element in the DOM.

Django combined with HTMx is considered a good combination as it compliments Django and its features. It allows for more maintainable front-end for small scale projects.

HTMx is a popular library with Django developers so this was a demonstration of implementing one of the features, offering AJAX requests without the need of large JavaScript front-end frameworks.

# Details

I came across HTMx while revising and learned that AJAX requests could be made using it without the need of heavy front-end frameworks. I set out to familiarise myself with its features and decided to create a simple application demonstrating a core feature.

HTMx is implemented by adding specific attributes to HTML elements, allowing any element to send POST or GET requests and inserting the response at any targeted element. These requests still require an endpoint so a URL, view and template was created for it.

In the case of this web-application, a free dictionary API was used so when a user submits a word, the request is sent and the response is then inserted in to the document almost immediately. This blends well with Django as it and allows me to create more dynamic content while still using the Django templating system.

A walking toon character is displayed to show that the page does not reload. I also wanted to create a playful design that is simple yet endearing.
