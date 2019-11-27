
## Other Use Cases
The systems main application is to warn drivers during the turning process. However, other applications can be realized using the exact same setup, possibly running parallel to the exisiting live application (depending on the physical setup and the range of view the camera can identify certain elements with confidence).

### Use as monitoring device for passing cars @strategically sound points in the city (z.B Umweltplakete)
Currently there is no way for cities to monitor incoming traffic based on EURO 1-6 emissions standards for cars. Possibly, the camera can be trained to visually identify the EURO-Plakette indicating the emission standard of the incoming cars.  

Get your Nerd on and check how it is done in Berlin measuring air quality and calculating statisticaly values [here in German!](https://www.berlin.de/senuvk/umwelt/luftqualitaet/umweltzone/download/umweltzone_1jahr_bericht.pdf)

### Speed Monitoring 
It does not make sense to put speedometers everywhere in the city. However, many policies (f.e [Berlin Air Purity Plan](https://www.berlin.de/hauptstadtluft/en/improving-air-quality/air-purity-plan/) depend on monitoring to ensure that the policies in place are effective. Traffic and traffic speed play an important role here. Once a policy is in place, f.e. tempolimit 30km/h, the policy is only as good as the monitoring and the steps taken to improve the policy. Today, there is no way to actually monitor streets efficiently at low cost. 
Life_Cycle could take that part to monitor speedsters and count the total amount at places where it is installed anyway to save cyclists' lifes. 
Policies can then be adapted moving from a soft (f.e tempolimit) approach to harder approaches (f.e police control, speedometer, speedbumps, etc) if needed.

### Accident forensics & Video Material to train neural networks
Collected video material can be used to deal with questions arising after an accident has happened. Also the video material can be used to train neural networks dealing with predicting accidents. 
Currently, the video is not saved after being processed. However, in order to create new insights the network can be trained to identify when an accident has happened and keep a predetermined range of video material on a disk connected to the setup which otherwise will be deleted every x minutes. 

### Life observation of several intersections
The prototype currently works with one camera monitoring a certain area. However, with the power of the new Jetson XAVIER up to 16 CSI Cameras can be attached to the camera to monitor many different areas of one intersection creating a dense Network of monitoring and warning signals at minimum cost.

### Counting passing traffic participants at crossing (quantitativ analysis)
The initial setup [OpenDataCam](https://www.move-lab.com/project/opendatacam/) by Moovel has been inveneted for counting traffic on different levels. Participants who are ususally left out (bikes, pedestrians, scooters, skaters, etc.) in quantitative observations can now be quantified. For certain areas this data can lead to new insights why certain areas fluctuate in traffic. For more insights and further projects visit their website and watch their video below :point_down:

<a href="https://vimeo.com/346340651"><img src="https://www.move-lab.com/project/opendatacam/static/images/about-2.jpg" alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>
