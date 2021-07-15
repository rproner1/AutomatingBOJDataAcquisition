# AutomatingBOJDataAcquisition

The `scrapeTheBOJ` module contains the `scrapeTheBOJ()` function. The function retreives PPI data on information and communications equipment from the Bank of Japan and downloads it as a comma-separated value (csv) file. The function takes three parameters:

  fromYear: str. The lower limit of the date range (inclusive). Default="2016".
  toYear: str. The upper limit of the date range (inclusive). Default="2021".
  noHeader: bool. Whether or not to omit the header. Default=True. If noHeader=False, a simple header will be created. 
  
The function does not return a value. Rather, it downloads a csv directly.

# Examples

scrapeTheBOJ(fromYear="2016", toYear="2021", noHeader=True)
