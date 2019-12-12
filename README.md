# Flow-Plot

## Purpose:  To plot scatterplots and heatmaps of protein expression from individual cells from csv files generated from the FlowJo software
This is a quick program that will use python's seaborn data visualization library to plot scatterplots and heatmaps from csv files exported from the FlowJo software.  Each "event" generated from flow cytometry corresponds to 1 individual cell.

## Why not just use FlowJo to plot these graphs? 
The FlowJo software is a pain in the ass to use. :rage: :rage: :rage: It's buggy, laggy, and on top of all that it requires a $1000 USB license key in order to use it's full functionality.  It's graphics options are also very limited.  This project sets out to create a code that generates more versitile and customizable graphs for flow cytometry data.  And most importantly:  **IT'S FREE!!!**

## How to export csv files from FlowJo
1. Open your flow cytometry FCS files using FlowJo
2. Select and highlight the subgroup of events that you want to export.  Alternatively, you can just highlight and export all the events instead of exporting subgroups of cells.  
![Imgur](https://i.imgur.com/LIdrQV6.png)
3. Go to the upper left side of FlowJo and click: File > Export/Concatenate > Export / Concatenate Populations 
![Imgur](https://i.imgur.com/SJiRDd1.png)
4. In the pop-up menu that opens up, in the Format drop down menu, select "CSV - Scale values".  Then click the bubble to include both the header and stain.  Pick the destination folder that you want your csv file to be exported to.  Lastly, click Export.  
![Imgur](https://i.imgur.com/5ZBwXSG.png)

## How to use the program
1. Use the pandas "pd.read_csv" function to import your csv file using a local file path.  Replace the file path in the complete-code - that is specific to the PC I am currently on.  Feel free to use a sample csv file include in the github repo.  
2. Modify the styling and colors of the graphs.  The "x" and "y" correspond to columns on the csv file.  Name the columns using their headers wrapping in quotes.  Example: x='FSC-A', y='SSC-A'
3. Run the code :thumbsup: 

## Dependencies: 
1. seaborn 
2. matplotlib 
3. pandas 
4. numpy
5. csv 

## References: 
1. The [seaborn statistical data visualization website](https://seaborn.pydata.org/index.html) was incredibly useful for making the graphs.
2. The course on DataCamp on how to import files into python using pandas.
3. The [Python Testing 101](https://www.youtube.com/watch?v=etosV2IWBF0) was used for testing the code.

## Thanks:
Thanks to John Lee and Martin Skarzynski for teaching a whole crew of python noobs how to code in their BIOF309 class!!! :clap: 