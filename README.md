# CmyPlot  
**Data Visualisation Web App** 


![GitHub](https://img.shields.io/github/license/ShreeSub/CmyPlot)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5634725.svg)](https://doi.org/10.5281/zenodo.5634725)
![example event parameter](https://github.com/bradley-erickson/project1/actions/workflows/python-app.yml/badge.svg?event=push)
![Github](https://img.shields.io/badge/language-python-red.svg)
![GitHub issues](https://img.shields.io/github/issues-raw/ShreeSub/CmyPlot)
![Github closes issues](https://img.shields.io/github/issues-closed-raw/ShreeSub/CmyPlot)
![Github pull requests](https://img.shields.io/github/issues-pr/ShreeSub/CmyPlot)
![Github closed pull requests](https://img.shields.io/github/issues-pr-closed/ShreeSub/CmyPlot)
[![codecov](https://codecov.io/gh/ShreeSub/CmyPlot/branch/main/graph/badge.svg?token=R0VY8JQO96)](https://codecov.io/gh/ShreeSub/CmyPlot)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Why Data Visualization?

With enormous data in hand you would always want to visualize it for good understanding and better clarity with minimal efforts. 

As the famous saying goes - `"The greatest value of visualization is when it forces us to notice what we never expected to see"` - John W. Tukey

`CmyPlot` is a web app that provides interface for uploading a csv data file and convert it into Tables and interesting graphs with one click

- ## Built with

  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="40" height="40" />
  <img src="docs/images/custom_icons/plotly_icon.png" width="40" height="40"/>
  <img src = "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg" width="40" height="40"/>

- **Language used:** Python
- **Libraries used:** Flask, Plotly, Dash
- **Development/ Debug Server:** Flask
- **Production Server:** Waitress
- **Deployment Platform:** Heroku <br><br>
**Note:** The application has been deployed on Heroku (free platform service). The app's usage is limited to monthly pool of free dyno hours. Also, free apps sleep automatically after 30 mins of inactivity to conserve your dyno hours.
## Visual Walkthrough:
<p align="center"><img width="700" src="./docs/demo/phase2_cmyplotdemo.gif"></p>

## What's new?
[Phase 1 vs phase 2](https://github.com/ShreeSub/CmyPlot/blob/main/Phase%202%20docs/deltadocument.md)

## Docs
[Documentation](https://elric97.github.io/CmyPlot/)

## Quick look:
Give it a try yourself: https://cmyplot.herokuapp.com/ 

(Heroku server may take long to respond first time, if no traffic within last 30 minutes).
<table border="2" bordercolorlight="#b9dcff" bordercolordark="#006fdd">

  <tr style="background: #010203 ">
    <td valign="left"> 
      <p style="color: #FF7A59"> 1.This is the main Cmyplot web page 
      </p>
      <a href="./docs/images/home_page_updated.png"> 
        <img src="./docs/images/home_page_updated.png" >      
      </a>
    </td>
    <td valign="left"> 
      <p style="color: #FF7A59"> 2.You have an option to upload your csv file 
        by Drag and drop or click
      </p>
      <a href="./docs/images/pre_upload_updated.png">
        <img src="./docs/images/pre_upload_updated.png"> 
      </a>
    </td>
  </tr>
  
  <tr style="background: #010203;"> 
    <td valign="left">
      <p style="color: #FF7A59"> 3.Once the file is uploaded, you can choose
         to visualize using either table or graph
      </p>  
      <a href="./docs/images/post_upload_updated.png">
        <img src="./docs/images/post_upload_updated.png">    
      </a>
    </td>
    <td valign="left"> 
      <p style="color: #FF7A59"> 4.For table, you could use 
      filters to sort the data as you want and select number of entries you want to display
      </p>
      <a href="./docs/images/table_updated.png">
        <img src="./docs/images/table_updated.png">          
      </a>
    </td>

  </tr> 
  
  <tr style="background: #010203;"> 
    <td valign="left">
     <p style="color: #FF7A59"> 5.Table representation of the data
      </p>
     <a href="./docs/images/table_filtered_updated.png">
        <img src="./docs/images/table_filtered_updated.png"> 
      </a> 
    </td> 
    <td valign="left">
     <p style="color: #FF7A59"> 6.Graph representation of the data. Here you get options to chose among multiple graph types and a sharable link to share or download the graph.
      </p>
     <a href="./docs/images/graph_filled_updated.png">
        <img src="./docs/images/graph_filled_updated.png"> 
      </a> 
    </td> 
  </tr> 

  <!-- <tr style="background: #010203;"> 
    <td valign = "center">
      <a href="./docs/images/graph_filled.png">
        <img src="./docs/images/graph_filled.png"> 
      </a>
    </td>
    
  </tr>  -->
 </table>
   
## Getting started:

  - ### Prerequisite:
      - Download [Python3.x](https://www.python.org/downloads/) on your system.

   - ### Installation:
      E.g If you downloaded `Python 3.9.7` above, then

      **Steps to setup virtual environment**
     - Create a virtual environment:

        `python3.9 -m venv project1_env`
    
     - Activate the virtual environment: 

        `source project1_env/bin/activate`
    
     - Build the virtual environment:(must be present in project directory)

        `pip install -r requirements.txt`

  - ### Run Instructions

     **To run/test the site locally:**

     - Clone [this (CmyPlot) github repo](https://github.com/bradley-erickson/CmyPlot).

     - Navigate to [project directory](./).

     - Create a virtual environment:

        `python -m venv project1_env`
    
     - Activate the virtual environment: 

        `source project1_env/bin/activate`
    
     - Build the virtual environment:

        `pip install -r requirements.txt`
  
     - Run:
     
        `python src/plotting/index.py`

     - Site will be hosted at:
       `http://127.0.0.1:8085/`

## Future Scope 🐾
There are multiple dimensions to this project catering to the interests of
Various developers. Please check [CONTRIBUTING.md](./CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md) for contributing rules

* Resolve the existing issues.
* Add more functionality in Graph and Table visuals to give more flexibility to user to interact with data.
* Tables can be made editable to interact with data and visualize cause and effects for the given data.
* If you're an ML enthusiast, basic machine learning models can be implemented to identify patterns in the data.

## Roadmap
- [List of Roadmap and their corresponding open issues](https://github.com/ShreeSub/CmyPlot/issues)

## Team Members
[Aditi Bhagwat](https://github.com/aditi12200)

[Anumit Garg](https://github.com/anumitgarg)

[Palvit Garg](https://github.com/palvitgarg99)

[Rachit Sharma](https://github.com/elric97)

[Shree Ramasubramanian](https://github.com/ShreeSub)
