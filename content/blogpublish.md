Title: Publishing a blog with Pelican
Date: 2015-07-24 22:20
Category: Tech

I consider myself a practical kind of guy. So when I sought a way of publishing my personal space on the web, I searched for tools that did the job without much hassle, and that did offer some sort of customizations. Being a Python programmer by heart, I ran into this very nice static site generator called [Pelican](http://blog.getpelican.com/), and instantly fell with in love with it. So what would be a better first post than telling how I set this blog up! I'll be covering here the three main tools that I used: Pelican to generate the site, [GitHub Pages](https://pages.github.com/) to host it and [Travis](https://travis-ci.org/) to automate the deploy process.

### Create your own blog using Pelican

Pelican has a very handy [tutorial](http://docs.getpelican.com/en/latest/quickstart.html) explaining how to get your blog up and running quickly. Since it is already pretty detailed, I'll focus on what I did differently.

First off, you'll need to install Pelican through Pip. Even though you can install the package in your computer, I would advise installing it inside a [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/). That way all the required packages will be installed inside a separate folder that you can easily remove later.

``` bash
$ pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
```

These commands will install, create and activate a new virtualenv called `blog`. Now every Python package will be seamlessly installed inside this special folder until you deactivate it.
Now we can safely install Pelican packages so we can quickstart our blog.

``` bash
(venv) $ pip install pelican markdown
(venv) $ mkdir blog/ && cd blog/
(venv) $ pelican-quickstart
```



### Hosting it on GitHub Pages

### Automatically deploy it using Travis

