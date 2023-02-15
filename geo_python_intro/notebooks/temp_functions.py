""" 

"""


def fahr_to_celsius(temp_fahrenheit):
    """
    Function for converting temperature in Fahrenheit to celcius

    Parameters
    ----------
    temp_fahrenheit: <numerical>
        Temperature in fahrenheit
    
    Returns
    ---------
    <float>
        Converted temperature


    """
    temp_celcius = (temp_fahrenheit - 32)/1.8
    return temp_celcius


def temp_classifier(temp_celsius):
    """
    Function for classifying temperatures

    Parameters:
    ------------
    temp_celcius: <numerical>
        Temperature in celcius

    
    For loop: input temp_celcius
        Takes temp_celcius value and classifies the temperature class value according to the rules below:
    
        class value 0:  if temp_celsius is below -2 degrees Celsius
        class value 1:  if temp_celsius is equal or warmer than -2, but less than +2 degrees Celsius
        class value 2:  if temp_celsius is equal or warmer than +2, but less than +15 degrees Celsius
        class value 3:  if temp_celsius is equal or warmer than +15 degrees Celsius

    Return:
    ----------
    <integer>
    Reclassified temperature value


    """
    if temp_celsius < -2:
        class_value = 0
    elif (temp_celsius >= -2) and (temp_celsius < 2):
        class_value = 1
    elif (temp_celsius >= 2) and (temp_celsius < 15):
        class_value = 2
    else:
        class_value = 3
    return class_value