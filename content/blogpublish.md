Title: Publishing a blog with Pelican
Date: 2016-04-07 22:20
Category: Tech
Summary: Learn how to publish a blog using Pelican and GitHub Pages
Status: Published

I consider myself a practical kind of guy. So when I sought a way of publishing my personal space on the web, I searched for tools that did the job without much hassle, and that did offer some sort of customizations. Being a Python programmer by heart, I ran into this very nice static site generator called [Pelican](http://blog.getpelican.com/), and instantly fell with in love with it. So what would be a better first post than telling how I set this blog up! I'll be covering here the two main tools that I used: Pelican to generate the site and [GitHub Pages](https://pages.github.com/) to host it. Just so you know, I'll assume that you're using a Linux enviromnent here, doing the same in Windows might be considerably more complex.

### Create your own blog using Pelican

First off, you'll need to install Pelican through [Pip](https://pip.pypa.io/en/stable/). Even though you can install the package in your computer, I would advise installing it inside a [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/). That way all the required packages will be installed inside a separate folder that you can easily remove later, and also they won't mess with the ones you have already installed in your operating system.

``` bash
$ pip install virtualenv
$ mkdir blog/ && cd blog/
$ virtualenv devenv/blog
$ source devenv/blog/bin/activate
```

These commands will install, create and activate a new virtualenv called `blog`. Now every Python package will be seamlessly installed inside this special folder until you deactivate it.
Now we can safely install Pelican packages so we can quickstart our blog.

``` bash
(blog) $ pip install pelican markdown
(blog) $ pelican-quickstart
```

This will ask several questions about your blog. Answer with your personal data, use the default setting for the ones you are unsure of. When it asks you if you want to publish through GitHub Pages, answer as follows:

```bash
> Do you want to upload your website using GitHub Pages? (y/N) Y
> Is this your personal page (username.github.io)? (y/N) Y
```

This will create all necessary files to get your blog up and running. To test if everything is running smoothly, write a sample blog page using Markdown and check the resulting HTML.

``` bash
(blog) $ printf '%s\n%s\n\n%s\n' 'Title: My title' 'Date: 2010-12-03 10:20' \
'My content.' >> content/helloworld.md
(blog) $ make html serve
```

The first command will create a file in Markdown format with a sample blog post under the folder `content`. The second one will create the HTML and serve it under the default port (8000). Open up your web browser and go to the URL at `localhost:8000`, if everything is working correctly you should see your blog with the default theme of Pelican and the blog post that we created before. If you didn't like this theme, you can always check for some others at [Pelican Themes](http://www.pelicanthemes.com/).

### Hosting it on GitHub Pages

Now it is time to think how we are going to publish this code online. [GitHub Pages](https://pages.github.com/) is a fantastic tool where we can easily do that with a simple `git push` to a branch, so that is what we are going to use here.

* Create a GitHub pages repository 

Go to your GitHub account page and create a repository called `<username>.github.io`, where `<username>` is your GitHub username. This is where all your source and output files will be stored.

* Set up Git for your blog and upload some content
    
One thing to keep in mind here is that the `master` branch in your github.io repository is where the files which are going to be published will be stored. That is, all your HTML, CSS, images, etc. Since we are using another tool to generate these files, it makes sense to store our source code into another branch, and when it is time to publish we generate all the HTML and upload to the `master` branch. So here we are going to use the branch `content` to store all our source code as follows.

```bash
(blog) $ make clean
(blog) $ git init
(blog) $ git checkout -b content
(blog) $ git add .
(blog) $ git commit -m 'Initial commit'
(blog) $ git remote add origin https://github.com/<username>/<username>.github.io.git
(blog) $ git push origin content

```

Use here your GitHub username and password. Now our code is securely stored, but we still didn't publish it yet. For that to happen, we need to upload all files in the `output` folder (the one created after the `make html`) to the `master` branch in our GitHub Pages repository. To simplify this, I'll use a tool called `ghp-import` which allows us to do it pretty easily.

```bash
(blog) $ pip install ghp-import
(blog) $ make github
```

After pushing your code, wait some seconds and visit `http://<username>.github.io`, check how your blog is up and running! 

Yeah, but things are not that simple. You may have noticed that we ended in the `master` branch, but you really don't want to work directly on it. But since the `master` and the `content` branch are not really based on one another, changing back and forth between both can be a huge headache, one that I wouldn't want to have every time that I publish my blog. Automating this publishing process (using a tool like [Travis](https://travis-ci.org/), for example) is the answer for this, and that will be covered in another post. For now, disregard the `master` branch and pull the code again from GitHub before moving forward.

```bash
(blog) $ deactivate && cd .. && rm -fr blog/
$ git clone https://github.com/<username>/<username>.github.io.git blog
$ cd blog/ && virtualenv devenv/blog
$ source devenv/blog/bin/activate

```


### Setting up your code nicely

What if you want to write to your blog from another machine, or you wipe your hard drive, or *gasp* your PC is stolen? You don't want to set up all this again now, do you? Now we will delve into some good practices with Python that will help you to avoid some headaches in the future.

* Define the required packages of your project

When we are using Pip as a package manager, it is pretty standard to declare the list of depencies of a project in a file called `requirements.txt`. Everything that we manually installed through `pip install` (that is, the dependecies of our project so far) should be explicited listed in this file, so you (and someone else, if this a shared blog) will know what to install when creating content for the blog. Note that I excluded the package `virtualenv` because it is not REALLY a dependency of the project, think of it more like a tool that you will want to have installed in your machine for other Python apps that you might create.

```bash
(blog) $ printf '%s\n%s\n%s\n' 'pelican' 'markdown' \
'ghp-import' >> requirements.txt
(blog) $ pip install -r requirements.txt
```

Now everytime you want to recreate your virtualenv, a simple `pip install -r requirements.txt` will install in it all dependencies of the blog, so you can start coding again quickly.

* Avoid getting junk files into the repository

Some files in your repository directory shouldn't be on git, like the virtualenv that we just created, the files that we can generate from our source or some files that Pelican creates when you debug your code, for example. To avoid sending them to your remote repository, create a `.gitignore` file as follows:

```bash
(blog) $ printf '%s\n%s\n%s\n%s\n' 'devenv/' 'output/*' \
'cache' '*.pid' >> .gitignore
```

Finally, commit both these files and push to your repository.

```bash
(blog) $ git add .gitignore requirements.txt
(blog) $ git commit -m 'Adding gitignore and requirements'
(blog) $ git push origin content
```

And that's it for today! In another post I'll talk about how to automate the deploy process using Travis, stay tuned!

