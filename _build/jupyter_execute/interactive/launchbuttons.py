#!/usr/bin/env python
# coding: utf-8

# # Launch into interactive computing interfaces
# 
# Because Jupyter Books are built with Jupyter notebooks, you can allow users to launch live Jupyter sessions in the cloud directly from your book.
# This lets readers quickly interact with your content in a traditional coding interface.
# They do so by clicking a **Launch Button** that takes them to an interactive environment.
# 
# There are numerous online notebook services - a good comparison is provided [in this article](https://www.dataschool.io/cloud-services-for-jupyter-notebook) - and the following sections describes the available integrations provided by Jupyter Book.
# 
# (launchbuttons/configuration)=
# ## Common launch button configuration
# 
# In the case of each interactive service, you'll need to tell Jupyter Book where your book content lives online.
# To do so, use this configuration in `_config.yml`:
# 
# ```yaml
# # Information about where the book exists on the web
# repository:
#   url                       : https://github.com/yourusername/yourbookrepo  # Online location of your book
#   path_to_book              : path/to/book  # Optional path to your book, relative to the repository root
#   branch                    : master  # Which branch of the repository should be used when creating links (optional)
# ```
# 
# A quick description of each option is below:
# 
# `url`:
#   A GitHub repository that includes your source files used to build the Jupyter Book.
#   These files can either be in the root of the repository, or in a sub-folder (in which case you should use `path_to_book`).
# 
# `path_to_book`:
#   A path, relative to your repository's root, to your book's source files.
#   Use this if your book is in a sub-folder of your repository (e.g. `docs/` or `book/`).
# 
# `branch`:
#   The branch where your book's **source files** are stored (not your book's _build files_, which generally exist in `gh-pages/` branch).

# ## Control the notebook interface that opens
# 
# Binder and JupyterHub sessions can be opened using either the "classic" Jupyter Notebook or the new JupyterLab interface backend (see [jupyter.org](https://jupyter.org) for more details).
# This is configured using:
# 
# ```yaml
# launch_buttons:
#   notebook_interface: "jupyterlab"  # or "classic"
# ```
# 
# One thing to take into account when choosing the interface is that notebooks written in the [MyST Markdown](../file-types/myst-notebooks.md) text-based format will not be opened as notebooks out-of-the-box.
#  If you wish for these files to be opened as notebooks then firstly you must ensure that [`jupytext>=0.16`](https://jupytext.readthedocs.io/en/latest/formats.html#myst-markdown) is installed in the Binder/JupyterHub environment for your book (no support for this feature exists in Google Colab).
# You then have two options:
# 
# - Use the "classic" interface, which will then immediately open these files as notebooks.
# - The "jupyterlab" interface (at the time of writing) has not yet implemented this behaviour, and so you will need to instruct readers to right-click the Markdown file and click "Open in notebook editor".

# (launchbuttons/binder)=
# ## Add a Launch on {term}`Binder` button
# 
# {term}`BinderHub` can be used to build the environment needed to run a repository, and provides
# a link that lets others interact with that repository. If your Jupyter Book is hosted online
# on GitHub, you can automatically insert buttons that link to the Jupyter Notebook running in a BinderHub.
# When a user clicks the button, they'll be taken to a live version of the page. If your code
# doesn't require a significant amount of CPU or RAM, you can use the free, public BinderHub running
# at https://mybinder.org.
# 
# To automatically include Binder link buttons in each page of your Jupyter Book, use the following
# configuration in `_config.yml`:
# 
# ```yaml
# launch_buttons:
#   binderhub_url: "https://mybinder.org"  # The URL for your BinderHub (e.g., https://mybinder.org)
# ```
# 
# By adding this configuration, along with the repository url configuration above, Jupyter Book
# will insert Binder links to any pages that were built from notebook content.
# 
# 

# ## Add a Launch on {term}`JupyterHub` button
# 
# JupyterHub lets you host an online service that gives users their own Jupyter servers with an environment that you specify for them.
# It allows you to give users access to resources and hardware that you provision in the cloud, and allows you to authenticate users in order to control who has access to your hardware.
# 
# Similar to Binder link buttons, you can also automatically include interact links that send your readers to a JupyterHub that is running a live, interactive version of your page.
# This is accomplished using the [nbgitpuller](https://github.com/jupyterhub/nbgitpuller) server extension.
# 
# You can configure the location of the JupyterHub (which you may set up on your own using a guide such as [zero to jupyterhub for kubernetes](https://z2jh.jupyter.org) or [the littlest jupyterhub](https://tljh.jupyter.org)) with the following configuration:
# 
# ```yaml
# launch_buttons:
#   jupyterhub_url: "your-hub-url"  # The URL for your JupyterHub. (e.g., https://datahub.berkeley.edu)
# ```
# 
# On your JupyterHub server, you need two dependencies installed:
# 1. To clone the notebook with the launch link, the server needs
# [`nbgitpuller`](https://jupyterhub.github.io/nbgitpuller/). 
# 
# 2. To open myst-markdown as notebooks, the server needs
# [`jupytext>=0.16`](https://jupytext.readthedocs.io/en/latest/formats.html#myst-markdown). 
# 
# You can add the following line to your `DockerFile`:
# ```
# RUN pip install jupytext nbgitpuller
# ```

# ## Add a Launch on {term}`Google Colab` button
# 
# If your Jupyter Book is hosted online on GitHub, you can automatically insert buttons that link to the Jupyter Notebook running on [Google Colab](https://colab.research.google.com/).
# When a user clicks the button, they'll be taken to a live version of the page.
# 
# Similar to Binder link buttons, you can automatically include Google Colab link buttons with the following configuration in `_config.yml`:
# 
# ```yaml
# launch_buttons:
#   colab_url: "https://colab.research.google.com"
# ```
# 
# ```{note}
# Google Colab links will only work for pages that have the `.ipynb` extension.
# ```
