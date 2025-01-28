# Spotify-Dashboard
This repository contains the resources and instructions to create an advanced Spotify Dashboard using Power BI. The dashboard visualizes data on the most streamed Spotify songs , including charts, measures, and interactive features.
# Project Overview
The project leverages Power BI's capabilities to create an engaging dashboard that displays insights such as top songs, artist popularity, and trends over time. It utilizes the Spotify Developer API to enrich song data with album cover images, enhancing the visual appeal of the dashboard.
Getting Started
To get started with the Spotify Dashboard project, follow these steps:

# Prerequisites
Power BI Desktop installed on your machine.
Python (for fetching album cover URLs using the Spotify Developer API).
Spotify Developer account to obtain API credentials.
# Installation
Clone the repository to your local machine:

git clone https://github.com/Harshithvarma007/Spotify-Dashboard.git
Open the Power BI Desktop application and load the dashboard.pbix file.

# Setup Spotify Developer API
To fetch album cover URLs from the Spotify Developer API:

Create a Spotify Developer account and register a new application.
Obtain your Client ID and Client Secret.
Update the url.py script with your API credentials (client_id and client_secret).
Run the script to fetch album cover URLs and update the dataset (spotify-2023-urls.csv).
# Usage
Once the setup is complete, open dashboard.pbix in Power BI Desktop. Refresh the data to load the updated dataset with album cover URLs. Explore different visualizations, slicers, and data cards to interact with the dashboard.

# Dashboard Features
Charts and Visualizations
Top Songs by Streams: Visualize the top songs based on streaming counts.
Artist Popularity: Analyze artist popularity trends.
Trend Analysis: Track streaming trends over time using date-based slicers.
# Adding Background Image
To add the custom background image:

Copy the provided background image to your Power BI canvas.
Set the image properties to match the specified dimensions and alignment.
# Creating Measures
Measures are used for dynamic calculations in Power BI:

_max streams: Calculates the maximum number of streams for a song.
_Top Song streams: Compares individual song streams against the maximum streams.
_Average Stream per year: Computes the average streams per year.
_Top song vs AVG: Measures the deviation of top song streams from the average streams.
# Advanced Visualizations
HTML Content: Embed HTML content for custom visualizations or images.
Unit Chart: Display energy percentage using Vega visualization.
HeatMap: Use Vega-Lite to visualize streaming data across months and days of the week.
