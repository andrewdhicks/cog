# ODC SOW

# To Do
- [//www.smartsheet.com/how-write-statement-work-any-industry](https://www.smartsheet.com/how-write-statement-work-any-industry)

# Introduction

- USGS/EROS fully supports the ODC Initiative
    - EROS values its partnership with GA on this initiative

> This document defines the joint research specifically between GA and USGS/EROS and benefits the larger science and ODC communities.

# Objectives/Purpose

## The Big WHY:

> In a nutshell scientists just want to do science!

The old model of:
- specifying new equipment; and waiting for it to be deployed
- purchasing or deploying scientific tools
- filtering and downloading data
- sub-setting and further filtering data

Has been disrupted/replaced by a cloud centric approach:
- Infrastructure is stood up from code (IaaS) (Infrastructure as Code)
- Data has been processed to standard scientific levels
- Data is at your fingertips
- Cloud tools (like ODC) are present and free to use
- Scientists focus on science


> Also; There is a goal of 20 by 20 Cubes in the larger ODC context.


# Scope of Work

- This document covers the technical scope of this work only. All political agreements are the responsibility of the governing bodies of each agency.

- The primary scope of this work is to create a Data Cube instance in the cloud that exploits s3 object stored ARD data.

The research for this task will involve the following disciplines at a minimum:
1. Project Management
2. System Administration
3. Cloud Engineering
4. Software Development/Engineering
5. Data Base Administration
6. Data Science

## Limiting the Target Use Case

> To be effective we recommend limiting the target use case to:
1. Hayden Island (Portland Oregon)  ## Spaghetti, 
2. US ARD Data
    - Specifically h03v03 ## 2350 scene/tiles
    - target bucket (as of this writing) ga-odc-eros-co3-west
        - still need to code a distributed 
3. AWS cloud provider
    - us-west-2 (Oregon) region # its all about the Oregon
    - ga-aws-usgs - account
    - 
4. Data Format Constraints
    - Cloud Optimized Geotiff - This is the **focus**.
        - Comparisons to tiff, geotiff and tarred geotiff may be documented
5. Data Base Constraint
    - PostgreSQL (SQLAlchemy)
    - Run on a small EC2 instance; for first demonstration
    - as with all factors in this project, this could scale up in many ways.
        - Should use Amazon Relational Database Service (RDS) – AWS in round 2/phase 2



## Expected Outcomes

## Deliverables

### Deadline Approaching

- This work needs to be completed by January 31, 2018 to be displayed on February 14, 2018.


1. Data Storage of one ARD tile (full temporal legacy)
2. Project and Task Plans
3. Data Cube Instances 
    - AWS us-west-2
    - private libvirt instances
4. Prototype code for indexing from ARD.xml[2350] to PostgreSQL
5. Demonstration of water though time over the Hayden Island area of Oregon
    - Highlights Landsat strengths
    - Highlights ODC strengths
    - Determination of s3/cloud viability for ODC and Landsat

## Constraints and Risks

### Constraints

1. Limited access to project sponsors
2. Limited access to experts at EROS
3. Limited size of AWS instances and mostly transient use
4. Large technology gamut and limited experience in certain technologies
5. So many ideas; so little time

### Mitigations

1. Limit the scope; phase the project
2. Follow project management rigor
3. Target communication to the reader; evaluate the effectiveness
4. Schedule monthly briefings
5. Allow for some autonomy an self directed teams
6. Build some contingency lighter weight demos - jupyter notebook - synthetic simutlatiions squared
7. Limit tools and embrace the cloud collaborative paradigm

# Roles and Responsibilities


# Related Work

1. Level1 Cloud Data Storage
    - Commercial use and exploitation of level1 data
    - Collection 1
    - Related white papers on cloud storage

