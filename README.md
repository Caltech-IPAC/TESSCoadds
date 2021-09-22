# <font color="#880000"> Image Cutouts of Co-Added TESS Full Frame Images

## <font color="#880000">The TESS Sky Survey

The Transiting Exoplanet Sky Survey (TESS) is surveying the sky with four CCD cameras, each with a field of view of 24 degrees and pixel size 21 arcmin. These cameras are aligned to cover the sky in a combined instantaneous field of view of 24 x 96 degrees. The survey observing pattern consists of 26 of these sectors of sky, 13 in each hemisphere, centered near the ecliptic poles. The schematic illustrates the field of view and scan pattern (from Ricker et al. 2015, JATIS, 1, 014003). This has since been modified for Year 2 operations in the Northern hemisphere, to start some sectors at a higher latiutude.


<img src="TESS_mosaic.png" />


TESS acquires approximately 1200 observations ("full frame images, FFIs) of each sector over thirty 30 days  with an observing cadence of 30 minutes, and then moves to the adjacent sector. Thus over two years, TESS accumulates a survey of the sky in both hemispheres.


## <font color="#880000"> Low Surface Brightness Astronomy with TESS

The optical design of TESS makes it a potentially powerful tool for studying the low surface brightness Universe. Thus we have used the Montage image mosaic engine (http://montage.ipac.caltech.edu) to create co-added images of the observations in each sector, by exactly registering all the images in each sector and coadding them.  These coadded images can be accessed through this cut out service. The data set consists consists of 336 images derived from the 21 sectors of data that been released in Spring 2020.

## <font color="#880000">A Python Notebook for Creating Cutouts of TESS Coadded Images

This notebook demonstrates the use of a Python client library to discover the sky coverage of an object or position within the co-added images, and to create image cutouts at these positions. The library delivers cutouts from the co-added images, rather than from a mosaic of the co-added images, because a mosaic shows serious contamination from residual scattered light on spatial scales of as small as 5 degrees.


