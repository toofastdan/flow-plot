# flow-plot: a free alternative to graph flow cytometry data

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

## 
The purpose of this project to the be able to plot protein expression data without a FlowJo USB license key (which costs over $1000).  The FlowJo sotfware has limited figure making options and will not allow you make make figures without hte USB license key.  However, FlowJo will allow people to export a raw csv file with all the data bundled in.  Seaborn will allow us to make customizable, publication-grade figures without having to rely on overly-expensive software with limited figure making ability.