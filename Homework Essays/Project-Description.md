# Project Description

## Team Name: 
Metaverse Maintenance

## Team members:
- Cory Gish, Electrical Engineering -- gishcd@mail.uc.edu
- Ryan Logsdon, Computer Science -- logsdori@mail.uc.edu
    
## Project Topic Area: 
- Internet of Things (IOT)
- Virtual Reality
- Automotive

## Project Abstract:
This project is a data collection and analysist tool for consumer and commercial automotive vehicles. Users for this device include mechanics, fleet managers, data analysts, and conventional drivers.  The system will allow users to view, analyze, and improve vehicle performance through a multi-platform analysis tool including in-vehicle display, web application, and a virtual reality environment. 

## Inadequacy of Current Solutions: 
The current solution to this project can be seen through the Progressive Snapshot. This device reads OBDII data from your vehicle and reports your driving habits to the insurance company. The inadequacy of this solution is that users can never see the data being collected through the Snapshot device. Moreover, other solutions include handheld OBD diagnostic tools. These devices take a single reading of the diagnostic data and display it on the connected device. This solution does not provide real-time vehicle diagnostics while driving, or the ability to track this data over time.  

## Technical Background Applicable to Problem:
Both team members worked at ITE, a product development company in Cincinnati, Ohio. During their time at ITE, both team members were exposed to cloud based IOT tracking through Losant. This tool allows a set of assets to track, collect, monitor, and send live data from anywhere in the world. Losant offers the ability for this data to be modified and displayed through a variety of out-of-the-box dashboard development tools. Furthermore, Ryan's experience in virtual reality and software development provides a firm foundation in the capabilities of modern equipment to provide users with the best possible viewing experience. Cory's background in electrical engineering will allow him to contribute towards the optimization of hardware throughout the system, as well as provide understanding into how the asset can safely monitor the vehicles diagnostic data. 

## Approach:
Due to the complexity and multitude of functionality that is required of the system discussed above, the team has broken the system into three major categories. The first category is the automotive-device interface. This area of focus will include designing hardware components to gather real-time automotive data points to be analyzed throughout the system. A Raspberry Pi 3 Model B will collect data through a Bluetooth OBD diagnostic board. This data will be displayed through a human machine interface (HMI) that provides an operator with a dashboard of real-time attribute values. 

The second major category is internet of things (IOT) capability. For this system to provide an immersive cross-platform experience, it is necessary that automotive data can be accessed through a variety of interfaces. Well-designed IOT connectivity will limit the latency of data retrieval and provide a real-time experience across any platform. To incorporate these requirements within the system, the team will use a Blues Wireless Cellular Notecard to send live diagnostic data from the Raspberry Pi to Losant. From here, data will be collected and displayed on a real-time and historical dashboard.

The last category of focus for this project is user interfaces. The project team would like to implement a virtual reality (VR) experience to provide users with three-dimensional data visualization of automotive attributes. However, since VR could become a barrier to entry of an average user, the team will also provide a browser-based application to allow the system to be viewed on any network capable device. This application will provide users with the ability to create an account, register a vehicle, and display the vehicles real-time and historical device data. For the VR environment, Noda.io, a mind-mapping tool, will be used to integrate the dashboards in to a 3-D environment. This environment will include a model of a user's vehicle and appropriate sensors to represent the attribute data being collected from the vehicle. 
    
