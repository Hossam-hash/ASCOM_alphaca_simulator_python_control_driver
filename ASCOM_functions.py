import time

import requests



#########Dome connection
dome_base_url = 'http://localhost:32323/api/v1/dome'
dome_number = 0
# flag = True

def dome_connection_control(dome_base_url, dome_number, flag):
    """control the connection of dome flag=true make connection true and the oppsite is true """
    url = f"{dome_base_url}/{str(dome_number)}/connected"
    data = {'Connected': str(flag)}
    response = requests.put(url, data=data)
    status = requests.get(url)
    if status.json()['Value']==True:
        return 'Dome is connected'
    else:
        return 'Dome is Disconnected'

def dome_altitude_value_status(dome_base_url, dome_number):
    """known what is the value of dome altitude"""
    dome_altiude_url= f"{dome_base_url}/{str(dome_number)}/altitude"
    return requests.get(dome_altiude_url).json()['Value']





def dome_at_home_status(dome_base_url, dome_number):
    """known if the Dome at home or not if output True the Dome at home else the dome isnot"""
    dome_athome_url= f"{dome_base_url}/{str(dome_number)}/athome"
    return requests.get(dome_athome_url).json()['Value']


def dome_at_park_status(dome_base_url, dome_number):
    """known if the Dome at park or not if output True the Dome at park else the dome isnot"""
    dome_altiude_url= f"{dome_base_url}/{str(dome_number)}/atpark"
    return requests.get(dome_altiude_url).json()['Value']


def dome_azimuth_status(dome_base_url, dome_number):
    """Returns the dome azimuth (degrees, North zero and increasing clockwise, i.e., 90 East, 180 South, 270 West)"""
    dome_altiude_url= f"{dome_base_url}/{str(dome_number)}/azimuth"
    return requests.get(dome_altiude_url).json()['Value']


def dome_can_move_to_home(dome_base_url, dome_number):
    '''True if the dome can move to the home position'''
    dome_canfindhome= f"{dome_base_url}/{str(dome_number)}/canfindhome"
    return requests.get(dome_canfindhome).json()['Value']

def dome_can_park_or_not(dome_base_url, dome_number):
    '''True if the dome is capable of programmed parking (Park() method)'''
    dome_canPark= f"{dome_base_url}/{str(dome_number)}/canpark"
    return requests.get(dome_canPark).json()['Value']


def dome_can_set_altitude_or_not(dome_base_url, dome_number):
    '''True if driver is capable of setting the dome altitude.'''
    dome_cansetAltitude= f"{dome_base_url}/{str(dome_number)}/cansetaltitude?"
    return requests.get(dome_cansetAltitude).json()['Value']

def dome_can_set_azimuth_or_not(dome_base_url, dome_number):
    '''True if driver is capable of setting the dome azimuth.'''
    dome_cansetAzimuth= f"{dome_base_url}/{str(dome_number)}/cansetazimuth?"
    return requests.get(dome_cansetAzimuth).json()['Value']

def dome_park_can_de_set_or_not(dome_base_url, dome_number):
    '''True if driver is capable of setting the dome park position.'''
    dome_cansetpark= f"{dome_base_url}/{str(dome_number)}/cansetpark?"
    return requests.get(dome_cansetpark).json()['Value']


def dome_shutter_can_open_auto_or_not(dome_base_url, dome_number):
    '''True if driver is capable of automatically operating shutter can open or not'''
    dome_cansShutterOpen= f"{dome_base_url}/{str(dome_number)}/cansetshutter?"
    return requests.get(dome_cansShutterOpen).json()['Value']

def dome_slaving_telescope_or_not(dome_base_url, dome_number):
    '''True if driver is capable of slaving to a telescope the dome support slaving to telescope'''
    dome_cansslave= f"{dome_base_url}/{str(dome_number)}/canslave?"
    return requests.get(dome_cansslave).json()['Value']

def dome_azimuth_position_synced_or_not(dome_base_url, dome_number):
    '''True if driver is capable of synchronizing the dome azimuth position using the SyncToAzimuth(Double) method indicate whether the dome azimuth position can be synced'''
    dome_canAzmuthSyn= f"{dome_base_url}/{str(dome_number)}/cansyncazimuth?"
    return requests.get(dome_canAzmuthSyn).json()['Value']

def dome_shutter_status(dome_base_url, dome_number):
    '''Returns the status of the dome shutter or roll-off roof. 0 = Open, 1 = Closed, 2 = Opening, 3 = Closing, 4 = Shutter status error'''
    dome_shutterStatus= f"{dome_base_url}/{str(dome_number)}/shutterstatus?"
    return requests.get(dome_shutterStatus).json()['Value']

def dome_slave_status(dome_base_url, dome_number):
    '''True if the dome is slaved to the telescope in its hardware, else False.indicate whether the dome is slaved to telescope'''
    dome_slaveStatus= f"{dome_base_url}/{str(dome_number)}/slaved?"
    return requests.get(dome_slaveStatus).json()['Value']

def dome_set_slave_control(dome_base_url, dome_number, flag):
    """control the dome is slaved to the telescope"""
    url = f"{dome_base_url}/{str(dome_number)}/slaved"
    data = {'Slaved': str(flag)}
    response = requests.put(url, data=data)
    status = requests.get(url)
    #check if the driver has the applity to slave pr not
    if dome_slave_status(dome_base_url, dome_number)==True:
        if status.json()['Value']==True:
            return 'Dome is slaved '
        elif status.json()['Value']==False:
            return 'Dome is not slaved'
    else:
        return 'the driver hasnot the applity to slave'

def dome_slewing_status(dome_base_url, dome_number):
    '''True if any part of the dome is currently moving, False if all dome components are steady.indicate whether any part of dome is moving'''
    dome_slewing_Status= f"{dome_base_url}/{str(dome_number)}/slewing?"
    return requests.get(dome_slewing_Status).json()['Value']


def dome_slewing_control(dome_base_url, dome_number):
    '''Calling this method will immediately disable hardware slewing (Slaved will become False).immediately cancel current dome operations'''
    dome_slewing_Control= f"{dome_base_url}/{str(dome_number)}/abortslew?"
    if dome_slewing_status(dome_base_url, dome_number)==True:
        if requests.get(dome_slewing_Control).json()['Value']==True:
            return 'Dome is slaved '
        elif requests.get(dome_slewing_Control).json()['Value']==False:
            return 'Dome is not slaved'
    else:
        return 'the driver hasnot the applity to slave'


def dome_close_shutter_control(dome_base_url, dome_number):
    '''Close the shutter or otherwise shield telescope from the sky.'''
    dome_close_shutter = f"{dome_base_url}/{str(dome_number)}/closeshutter"
    if dome_shutter_can_open_auto_or_not(dome_base_url, dome_number) == True:
        if requests.put(dome_close_shutter).status_code==200:
            return 'shutter is closed successfully'
        else:
            return 'shutter erroe in close'
    else:
        return 'the driver hasnot the applity to close automatically'

def dome_find_home_control(dome_base_url, dome_number):
    '''After Home position is established initializes Azimuth to the default value and sets the AtHome flag.start operation to search for the dome home position '''
    dome_find_Home_Control = f"{dome_base_url}/{str(dome_number)}/findhome"

    if requests.put(dome_find_Home_Control).status_code==200:
        return 'the system sets the azimuth to a default value and updates the "AtHome" flag to indicate that it is currently in the home '
    else:
        return 'Error'

def dome_open_shutter_control(dome_base_url, dome_number):
    '''Open shutter or otherwise expose telescope to the sky.'''
    dome_open_shutter = f"{dome_base_url}/{str(dome_number)}/openshutter"
    if dome_shutter_can_open_auto_or_not(dome_base_url, dome_number) == True:
        if requests.put(dome_open_shutter).status_code==200:
            return 'shutter is opened successfully'
        else:
            return 'shutter erroe in open'
    else:
        return 'the driver hasnot the applity to open automatically'



def dome_park_position_control(dome_base_url, dome_number):
    '''After assuming programmed park position, sets AtPark flag.Rotate dome in azimuth to park position'''
    if dome_at_park_status(dome_base_url, dome_number)==False:
        if dome_park_can_de_set_or_not(dome_base_url, dome_number)==True:
            dome_park_control = f"{dome_base_url}/{str(dome_number)}/park"
            if requests.put(dome_park_control).status_code == 200:
                return 'Dome is park successfully'
        return 'the driver hasnot the applity to park automatically'
    else:
        return 'Dome is already parked'




def dome_set_current_park_position_control(dome_base_url, dome_number):
    '''Set the current azimuth, altitude position of dome to be the park position.'''
    dome_set_park_control = f"{dome_base_url}/{str(dome_number)}/setpark"

    if requests.put(dome_set_park_control).status_code == 200:
        return ' the current azimuth, altitude position of dome is set be the park position'
    else:
        return 'Error'


def control_dome_altitude_value_motion(dome_base_url, dome_number,altitude_value):
    '''Slew the dome to the given altitude position(control the altitude position)'''
    dome_altitude__value_control = f"{dome_base_url}/{str(dome_number)}/slewtoaltitude"
    data = {'Altitude': altitude_value}
    response = requests.put(dome_altitude__value_control, data=data)
    if response.status_code == 200:
        if 0<= altitude_value <= 90:
            added_startime=time.time()
            dome_altitude_value_status(dome_base_url, dome_number)
            add_end_time = time.time()
            start_time = time.time()
            while dome_altitude_value_status(dome_base_url, dome_number)!=altitude_value:
                time.sleep(0.001)
            end_time = time.time()
            taketime = (end_time - start_time)-(add_end_time-added_startime)
            if taketime<0:
                taketime=0
            return f"{'The new altitude angle = ' }{dome_altitude_value_status(dome_base_url,dome_number)}{' with taken time :'}{taketime}{' sec'}"
        else:
            return response.json()['ErrorMessage']
    else:
        return 'Error'

def control_dome_azimuth_value_motion(dome_base_url, dome_number,azimuth_value):
    '''Slew the dome to the given azimuth position (control the azimuth dome position)'''
    dome_azimuth_value_control = f"{dome_base_url}/{str(dome_number)}/slewtoazimuth"
    data = {'Azimuth': azimuth_value}
    response = requests.put(dome_azimuth_value_control, data=data)
    if response.status_code == 200:
        if 0<= azimuth_value <= 360:
            added_startime=time.time()
            dome_azimuth_status(dome_base_url, dome_number)
            add_end_time = time.time()
            start_time = time.time()
            while dome_azimuth_status(dome_base_url, dome_number)!=azimuth_value:
                time.sleep(0.001)
            end_time = time.time()
            taketime = (end_time - start_time)-(add_end_time-added_startime)
            if taketime<0:
                taketime=0
            return f"{'The new azimuth angle = ' }{dome_azimuth_status(dome_base_url, dome_number)}{' with taken time :'}{taketime}{' sec'}"
        else:
            return response.json()['ErrorMessage']
    else:
        return 'Error'

def dome_synchro_to_given_azimuth(dome_base_url, dome_number,azimuth_value):
    '''Synchronize the dome to the given azimuth position.means aligning or orienting the dome of an observatory to a specific azimuthal direction'''
    dome_azimuth_value_synch = f"{dome_base_url}/{str(dome_number)}/synctoazimuth"
    data = {'Azimuth': azimuth_value}
    response = requests.put(dome_azimuth_value_synch, data=data)
    if response.status_code == 200:
        if 0<= azimuth_value <= 360:
            return f"{'The new azimuth angle = '}{dome_azimuth_status(dome_base_url, dome_number)}"
        else:
            return response.json()['ErrorMessage']
    else:
        return 'Error'


def unique_actions(dome_base_url, dome_number,action_name):
    '''Actions and SupportedActions are a standardised means for drivers to extend functionality beyond the built-in capabilities of the ASCOM device interfaces.
    The key advantage of using Actions is that drivers can expose any device specific functionality required. The downside is that, in order to use these unique features,
     every application author would need to create bespoke code to present or exploit them.'''
    dome_unique_action_url = f"{dome_base_url}/{str(dome_number)}/action"
    data = {'Action': action_name}
    response = requests.put(dome_unique_action_url, data=data)
    return response.json()

'''
Transmits an arbitrary string to the device and does not wait for a response. Optionally, protocol framing characters may be added to the string before transmission.that is not supported here
dome_unique_action_url = f"{dome_base_url}/{str(dome_number)}/commandblind"
    data = {
    'Command': anycommand,
    'Raw=false'
    }
#RAW : If set to true the string is transmitted 'as-is', if set to false then protocol framing characters may be added prior to transmission.
'''

'''
Transmits an arbitrary string to the device and waits for a boolean response. Optionally, protocol framing characters may be added to the string before transmission..that is not supported here
dome_unique_action_url = f"{dome_base_url}/{str(dome_number)}/commandbool"
    data = {
    'Command': anycommand,
    'Raw=false'
    }
#RAW : If set to true the string is transmitted 'as-is', if set to false then protocol framing characters may be added prior to transmission.
'''
'''
Transmits an arbitrary string to the device and waits for a string response. Optionally, protocol framing characters may be added to the string before transmission
.that is not supported here
dome_unique_action_url = f"{dome_base_url}/{str(dome_number)}/commandstring"
    data = {
    'Command': anycommand,
    'Raw=false'
    }
#RAW : If set to true the string is transmitted 'as-is', if set to false then protocol framing characters may be added prior to transmission.
'''



def connection_dome_status(dome_base_url, dome_number):
    '''Retrieves the connected state of the device if True : connected'''
    dome_connection_tatus_url = f"{dome_base_url}/{str(dome_number)}/connected?"
    return requests.get(dome_connection_tatus_url).json()['Value']

def device_dome_description(dome_base_url, dome_number):
    '''The description of the device'''
    dome_devcie_Des_url = f"{dome_base_url}/{str(dome_number)}/description?"
    return requests.get(dome_devcie_Des_url).json()['Value']

def driver_description(dome_base_url, dome_number):
    '''The description of the driver'''
    driver_Des_url = f"{dome_base_url}/{str(dome_number)}/driverinfo?"
    return requests.get(driver_Des_url).json()['Value']


def driver_version(dome_base_url, dome_number):
    '''A string containing only the major and minor version of the driver.'''
    driver_versio_url = f"{dome_base_url}/{str(dome_number)}/driverversion?"
    return requests.get(driver_versio_url).json()['Value']




def aSCOM_device_version(dome_base_url, dome_number):
    '''This method returns the version of the ASCOM device interface contract to which this device complies. Only one interface version is current at a moment in time and all new devices should be built to the latest interface version.
Applications can choose which device interface versions they support and it is in their interest to support previous versions as well as the current version to ensure they can use the largest number of devices.'''

    aSCOM_device_version_url = f"{dome_base_url}/{str(dome_number)}/interfaceversion?"
    return requests.get(aSCOM_device_version_url).json()['Value']

def device_name(dome_base_url, dome_number):
    '''The name of the device'''
    device_name_url = f"{dome_base_url}/{str(dome_number)}/name?"
    return requests.get(device_name_url).json()['Value']

def action_name_suportted(dome_base_url, dome_number):
    '''Returns the list of action names supported by this driver.'''
    action_name_suportted_url = f"{dome_base_url}/{str(dome_number)}/supportedactions?"
    return requests.get(action_name_suportted_url).json()['Value']