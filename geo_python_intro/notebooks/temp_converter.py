
def celcius_to_fahr(temp_celcius):
    return 9/5 * temp_celcius + 32


def kelvins_to_celcius(temp_kelvins):
    return temp_kelvins - 273.15


def kelvins_to_fahr(temp_kelvins):
    temp_celsius = kelvins_to_celsius(temp_kelvins)
    temp_fahr = celsius_to_fahr(temp_celsius)
    return temp_fahr


def temp_calcuulator(temp_k, convert_to):
    """
    Function to convert temp in Kelvin to C or F

    Parameters
    ----------
    temp_k: <numerical>
        Temperature in kelvins
    convert_to: <str>
        Target temp either in Celcius ('C') or Farenheit ('F')

    Returns
    --------
    <float> 
        Converted temperature
        
    """
    #check if user wants temp in Celcius
    if convert_to == "C":
        #convert value to celcius using imported script
        converted_temp = kelvins_to_celcius(temp_kelvins=temp_k)
    elif convert_to == "F":
        converted_temp = kelvins_to_fahr(temp_kelvins=temp_k)
    # return result
    return converted_temp