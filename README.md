# countryPopulationDensity
Population density by countries calculated from the population and land areas from the CIA World Factbook. Uses mostly 2015 estimates. Plots the population densites on a world map.

![World Population Density Estimated 2015 Data](/images/worldPopulationDensity2015_rainbow.png)

## About
I enjoy to browse through the [CIA World Factbook](https://www.cia.gov/library/publications/resources/the-world-factbook/rankorder/rankorderguide.html) from time to time. I've always found population density to be an interesting metric for comparision. Once I noticed that population density wasn't on the World Factbook, I decided to calculate it myself with a python script using the provided country populations and area estiamtes.   
## Data
I've saved the resulting pouplation densites as [data/countryPopDensity.csv](data/countryPopDensity.csv). Most of the data is from 2015 estimates. I'll try to update when the new estimates are available.

The country [population data](https://www.cia.gov/library/publications/resources/the-world-factbook/rankorder/2119rank.html) from the World Factbook pulled on March 28, 2016.

The country [area data](https://www.cia.gov/library/publications/resources/the-world-factbook/rankorder/2147rank.html) from the World Factbook pulled on March 28, 2016.
## Images
I couldn't stop with just the data, as the data would make for some very cool color map plots of the world. I've created a bunch of images showing the population density of the world with different matplotlib color maps. Images were saved as pdf (vector images) or png. 

Check out the [images](/images)!
## Links
- [CIA World Factbook](https://www.cia.gov/library/publications/resources/the-world-factbook/)
- [Cartopy](http://scitools.org.uk/cartopy/) 
- [Natural Earth Scale Downloads](http://www.naturalearthdata.com/downloads/) - contains country shapes - hindsight says I could have used this to calculate the population densites...
- [Stackexchange comment by Rutger Kassies](http://stackoverflow.com/questions/25505674/python-matplotlib-add-colorbar) - colorbar with world map
- [Blog post describing the process](http://jekel.me/2016/Population-Density-Plots/)
- [Complete imgur gallery](http://imgur.com/a/Pb1i6)

## License

Feel free to modify, use, and distribute as you like! I have uploaded it as a MIT License.

The MIT License (MIT)

Copyright (c) 2016 Charles Jekel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.